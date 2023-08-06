# coding=utf-8
import json
import time
from bs4 import BeautifulSoup as Bs
from acfunsdk.source import routes, apis
from acfunsdk.page.utils import match1

__author__ = 'dolacmeo'


class BlockContent:
    content_data = None

    def __init__(self, acer, content_data: dict):
        self.acer = acer
        self.content_data = content_data

    def __repr__(self):
        if self.name:
            key = f"[{self.keyname}]" if self.keyname else ""
            return f"AcContent({self.name}{key})"
        return f"AcContent(#{self.blockId} Σ{self.contentCount})"

    @property
    def blockId(self):
        return self.content_data.get('blockId')

    @property
    def name(self):
        return self.content_data.get('name')

    @property
    def keyname(self):
        return self.content_data.get('interfaceParameter', '').strip()

    @property
    def contentCount(self):
        return self.content_data.get('contentCount')

    def list(self):
        data_list = list()
        for v in self.content_data.get('webContents'):
            if v['mediaType'] == 0:
                data_list.append(self.acer.AcVideo(v['mediaId'], v))
            elif v['mediaType'] == 1:
                data_list.append(self.acer.AcArticle(v['mediaId'], v))
            elif v['mediaType'] == 4:
                data_list.append(self.acer.AcUp(v))
            elif v['mediaType'] == 8:
                data_list.append(self.acer.AcImage(v['image'], v['link'], v['title'], self))
        return data_list


class ChannelBlock:
    block_data = None

    def __init__(self, acer, block_data: dict):
        self.acer = acer
        self.block_data = block_data

    def __repr__(self):
        return f"AcBlock(#{self.blockType} {self.name})"

    @property
    def name(self):
        return self.block_data.get('name', '').strip()

    @property
    def blockType(self):
        return self.block_data.get('blockType')

    def contents(self):
        return [BlockContent(self.acer, content) for content in self.block_data.get('content', [])]


class AcChannel:
    nav_data = dict()
    channel_obj = None
    channel_data = None
    is_main = False
    parent_data = None
    sub_data = None
    is_404 = False

    def __init__(self, acer, cid, nav_info: dict):
        self.acer = acer
        self.cid = str(cid)
        self.info = nav_info
        self.link = f"/v/list{self.cid}/index.htm"
        self._get_channel_info()

    @property
    def _main_channels(self):
        return {x["channelId"]: x for x in self.acer.channel_data}

    def _get_channel_info(self):
        for channel in self.acer.channel_data:
            if self.cid == channel['channelId']:
                self.parent_data = channel
                self.info = self.parent_data
                break
            for sub in channel['children']:
                if self.cid == sub['channelId']:
                    self.parent_data = channel
                    self.sub_data = sub
                    self.info = self.sub_data
                    break
        self.is_main = self.sub_data is None
        if self.parent_data is None:
            self.is_404 = True

    def __repr__(self):
        if self.is_404 is True:
            return f"AcChannel(#{self.cid} 404)"
        return f"AcChannel(#{self.cid} {self.info['name']})"

    def loading(self):
        if not self.is_main:
            print("Is sub channels, just use videos.")
            return False
        page_req = self.acer.client.get(f"{routes['index']}{self.link}")
        self.channel_obj = Bs(page_req.text, 'lxml')
        json_text = match1(page_req.text, r"(?s)__INITIAL_STATE__\s*=\s*(\{.*?\});")
        if json_text is None:
            self.is_404 = True
            return False
        self.channel_data = json.loads(json_text)

    def hot_words(self):
        if not self.is_main:
            return None
        if self.channel_data is None:
            self.loading()
        return self.channel_data['channel']['hotWordList']

    def blocks(self):
        if not self.is_main:
            return None
        if self.channel_data is None:
            self.loading()
        if self.cid == '63':
            return [ChannelBlock(self.acer, data) for data in self.channel_data['article']['blockList']]
        return [ChannelBlock(self.acer, data) for data in self.channel_data['channel']['blockList']]

    def ranks(self, limit: int = 50, date_range: str = None):
        if self.is_main:
            cid = int(self.cid)
            sub_cid = None
        else:
            cid = int(self.parent_data['channelId'])
            sub_cid = int(self.cid)
        return self.acer.AcRank(cid, sub_cid, limit, date_range=date_range)

    def videos(self,
               page: int = 1,
               sortby: [str, None] = None,
               duration: [str, None] = None,
               datein: [str, None] = None,
               obj: bool = True):
        if self.is_main or self.cid == '63':
            return None
        sortby_list = {
            "rankScore": "综合",
            "createTime": "最新投稿",
            "viewCount": "播放最多",
            "commentCount": "评论最多",
            "bananaCount": "投蕉最多",
            "danmakuCount": "弹幕最多"
        }
        assert sortby in sortby_list or sortby is None
        duration_list = {
            "all": "全部",
            "0,5": "5分钟以下",
            "5,30": "5-30分钟",
            "30,60": "30-60分钟",
            "60,": "60分钟以上"
        }
        assert duration in duration_list or duration is None
        datein_list = {
            "default": "近三个月",
            "20200101,20210101": "2020",
            "20190101,20200101": "2019",
            "20180101,20190101": "2018",
            "20170101,20180101": "2017",
            "20160101,20170101": "2016",
            "20150101,20160101": "2015",
            "20100101,20150101": "2014-2010",
            ",20100101": "更早",
        }
        assert datein in datein_list or datein is None
        api_req = self.acer.client.get(f"{routes['index']}{self.link}", params={
            "sortField": "rankScore" if sortby is None else sortby,
            "duration": "all" if duration is None else duration,
            "date": "default" if datein is None else datein,
            "page": page,
            "quickViewId": "listwrapper",
            "reqID": 0,
            "ajaxpipe": 1,
            "t": str(time.time_ns())[:13]
        })
        assert api_req.text.endswith("/*<!-- fetch-stream -->*/")
        api_data = json.loads(api_req.text[:-25])
        api_obj = Bs(api_data.get('html', ''), 'lxml')
        v_datas = list()
        for item in api_obj.select('.list-content-item'):
            item_data = {
                'ac_num': item.select_one('.list-content-top').attrs['href'][5:],
                'title': item.select_one('.list-content-title').a.attrs['title'],
                'duration': item.select_one('.danmaku-mask .video-time').text,
                'commentCountShow': item.select_one('.list-content-data .commentCount').text,
                'viewCountShow': item.select_one('.list-content-data .viewCount').text,
                'coverUrl': item.select_one('.list-content-cover').attrs['src'],
                'user': {
                    'id': item.select_one('.list-content-uplink').attrs['data-uid'],
                    'name': item.select_one('.list-content-uplink').attrs['title'],
                }
            }
            if obj is True:
                v_datas.append(self.acer.AcVideo(item_data['ac_num'], item_data))
            else:
                v_datas.append(item_data)
        return v_datas


class AcWen:
    realmIds = None
    cursor = "first_page"
    sortType = "createTime"
    onlyOriginal = False
    timeRange = "all"
    limit = 10
    article_data = list()

    def __init__(self, acer,
                 realmIds: [list, None] = None,
                 sortType: str = "createTime",
                 timeRange: str = "all",
                 onlyOriginal: bool = False,
                 limit: int = 10):
        self.acer = acer
        self.realmIds = realmIds
        assert sortType in ['createTime', 'lastCommentTime', 'hotScore']
        self.sortType = sortType
        assert timeRange in ['all', 'oneDay', 'threeDay', 'oneWeek', 'oneMonth']
        self.timeRange = timeRange
        self.onlyOriginal = onlyOriginal
        self.limit = limit

    def feed(self, obj: bool = True):
        if self.cursor == 'no_more':
            return None
        form_data = {
            "cursor": self.cursor,
            "sortType": self.sortType,
            "onlyOriginal": self.onlyOriginal,
            "timeRange": self.timeRange,
            "limit": self.limit,
        }
        if isinstance(self.realmIds, list):
            form_data['realmId'] = self.realmIds
        api_req = self.acer.client.post(apis['article_feed'], data=form_data)
        api_data = api_req.json()
        if api_data.get('result') == 0:
            self.cursor = api_data.get('cursor')
            new_data = api_data.get('data', [])
            self.article_data.extend(new_data)
            if obj is True:
                return [self.acer.AcArticle(x['articleId'], x) for x in new_data]
            return new_data
        return None

    def clean_cache(self):
        self.article_data = list()
        return True




