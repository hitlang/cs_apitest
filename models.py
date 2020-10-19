# -*-coding:utf-8 -*-
# !/usr/bin/python3
# @Author:liulang
from enum import Enum
from typing import Any
from typing import Dict, Text, Union, Callable
from typing import List
from pydantic import BaseModel, Field
Name = Text
Url = Text
Headers = Dict[Text, Text]
Cookies = Dict[Text, Text]

class MethodEnum(Text, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"
    PATCH = "PATCH"

class TRequest(BaseModel):
    """requests.Request model"""
    method: MethodEnum
    url: Url
    params: Dict[Text, Text] = {}
    headers: Headers = {}
    req_json: Union[Dict, List, Text] = Field(None, alias="json")
    data: Union[Text, Dict[Text, Any]] = None

class TStep(BaseModel):
    name: Name
    request: Union[TRequest, None] = None
    testcase: Union[Text, Callable, None] = None

class TestCase(BaseModel):
    teststeps: List[TStep]

class TestsMapping(BaseModel):
    testcases: List[TestCase]

class RequestData(BaseModel):
    method: MethodEnum = MethodEnum.GET
    url: Url
    headers: Headers = {}
    body: Union[Text, bytes, Dict, List, None] = {}








