from __future__ import annotations
from typing import Iterator, List
import requests
import json
from .data import series_data
from collections import namedtuple

from .protocols import  series_list,series_id
class __base_lookup:
    @property
    def series_info(self)-> Iterator:
        for data in self._lookup_table:
            series_id=data.get("Series Id:", None)
            area=data.get("Area:", None)
            area_type=data.get("Area Type:",None)
            region=data.get("State/Region/Division:")
            yield series_id,area,area_type,region

    @property
    def series_id_list(self) -> series_list:
        series=[id_val[0] for id_val in self.series_info]

        return series_list(series=series)

    def series_exist_check(self,id:series_id):
        id=series_id(id=id).id
        if id in self.series_id_list.series:
            return True
        else:
            raise TypeError(f"No Existing Id In {self.__class__.__name__}")
    def get_seriesId_info(self,id:series_id):
        id=series_id(id=id).id
        for id_,area,area_type,region in self.series_info:
            if id == id_:
                return area,area_type,region

class _api_config:
    endpoint="https://api.bls.gov/publicAPI/v2/timeseries/data/"
    headers = {'Content-type': 'application/json'}
class series_object:
    def __new__(cls, id:series_id) ->series_object:
        obj=object.__new__(cls)
        obj.id=series_id(id=id).id
        obj._data=None
        obj._from_value=None
        obj._to_value=None
        return obj
    @property
    def _from(self):
        return self._from_value
    @_from.setter
    def _from(self,value:int):
        if not isinstance(value,int):
            raise TypeError("Must be type of int")
        self._from_value=value
        return self._from

    @property
    def _to(self):
        return self._to_value

    @_to.setter
    def _to(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Must be type of int")
        self._to_value = value
        return self._to


    @property
    def get_data(self) ->Iterator:
        if self._from==None or self._to==None:
            raise TypeError("Please specify _from and _to")
        if self._from > self._to:
            raise TypeError(" _from cannot be greater than 2")
        if self._data != None:
            return self._data
        else:
            ### call the api
            self.id=[self.id]
            data_requests=json.dumps({"seriesid":self.id,"startyear":str(self._from),"endyear":str(self._to), "registrationkey":self.token})
            response=requests.post(_api_config.endpoint,data=data_requests,headers=_api_config.headers)
            self._data=json.loads(response.text)

            return self._data

class _base:
    def __setattr__(self, attr, value) -> None:
        object.__setattr__(self, attr, value)
    # def __getattr__(self, item):
    #     raise TypeError( f"object not found {item}")
    def __getattribute__(self, item):
        return object.__getattribute__(self, item)


    @property
    def __getseriesobject__(self) -> Iterator:
        for attri in self.__dict__:
            attri_val=self.__getattribute__(attri)
            if isinstance(attri_val,series_object):
                yield attri_val
class __add_series(_base):


    def add_custom_series(self,series: series_list) ->object:
        obj=self._new()
        series=series_list(series=series).series
        if isinstance(series, List):
            for id in series:
                if self.series_exist_check(id):
                    ### creating another instance
                    area,area_type,region=self.get_seriesId_info(id)

                    obj.__setattr__(id,series_object(id))
                    series_obj = obj.__getattribute__(id)
                    series_obj.area = area
                    series_obj.area_type = area_type
                    series_obj.region = region
                    series_obj.token = self.token
        return obj
    def add_all_series(self):
        obj=self._new()
        for series_id,area,area_type,region in self.series_info:
            if series_id != None:
                obj.__setattr__(series_id,series_object(series_id))
                series_obj=obj.__getattribute__(series_id)
                series_obj.area=area
                series_obj.area_type=area_type
                series_obj.region=region
                series_obj.token=self.token
        return obj
class labor_force(__base_lookup,__add_series):
    def __init__(self):
        self._from_value = None
        self._to_value = None
        self._token=None

    @property
    def token(self):
        return self._token
    @token.setter
    def token(self,value):
        self._token=value
        return self.token



    @classmethod
    def _new(cls):
        return cls()

    @property
    def _from(self):
        return self._from_value

    @_from.setter
    def _from(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Must be type of int")
        self._from_value = value
        return self._from

    @property
    def _to(self):
        return self._to_value

    @_to.setter
    def _to(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Must be type of int")
        self._to_value = value
        return self._to

    _lookup_table=series_data

    def __iter__(self) -> Iterator:
        for series_node in self.__getseriesobject__:
            series_node._from=self._from
            series_node._to=self._to
            for sub_ in series_node.get_data["Results"]["series"]:
                seriesID = sub_["seriesID"]
                sub_sub_data = sub_["data"]
                for value in sub_sub_data:
                    year = value["year"]
                    period = value["period"]
                    periodName = value["periodName"]
                    val = value["value"]
                    tuple_name=namedtuple(f"response_data","seriesID year period periodName value area area_type region ")
                    data_return=tuple_name(seriesID,year,period,periodName,val, series_node.area,series_node.area_type,series_node.region)
                    data_return=data_return._asdict()
                    yield dict(data_return)







