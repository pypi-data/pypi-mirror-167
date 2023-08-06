# coding=utf-8
from typing import Literal
from acfunsdk.source import apis

__author__ = 'dolacmeo'


class AcRank:
    date_ranges = ['DAY', 'THREE_DAYS', 'WEEK']
    rank_data = None

    def __init__(self, acer,
                 cid: [int, None] = None,
                 sub_cid: [int, None] = None,
                 limit: int = 50,
                 date_range: (Literal['DAY', 'THREE_DAYS', 'WEEK'], None) = None):
        self.acer = acer
        self.cid = cid if isinstance(cid, int) else ""
        self.sub_cid = sub_cid if isinstance(sub_cid, int) else ""
        self.limit = limit
        self.date_range = date_range if date_range in self.date_ranges else self.date_ranges[0]
        self.get_data()

    def get_data(self):
        param = {
            "channelId": self.cid,
            "subChannelId": self.sub_cid,
            "rankLimit": self.limit,
            "rankPeriod": self.date_range
        }
        api_req = self.acer.client.get(apis['rank_list'], params=param)
        if api_req.json().get('result') == 0:
            self.rank_data = api_req.json().get('rankList')

    def contents(self):
        if self.rank_data is None:
            return None
        data_list = list()
        for content in self.rank_data:
            if content['contentType'] == 2:
                data_list.append(self.acer.AcVideo(content['dougaId'], content))
            elif content['contentType'] == 3:
                data_list.append(self.acer.AcArticle(content['resourceId'], content))
        return data_list

    def ups(self):
        if self.rank_data is None:
            return None
        data_list = list()
        for content in self.rank_data:
            data_list.append(self.acer.AcUp({"userId": content['userId'], "name": content['userName']}))
        return data_list
