import os
from enum import Enum
from typing import Any
from typing import Dict, Text, Union, Callable
from typing import List
Name = Text
Url = Text
Headers = Dict[Text, Text]


class MethodEnum(Text, Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"
    PATCH = "PATCH"

class TRequest():
    """requests.Request model"""
    method: MethodEnum
    url: Url
    params: Dict[Text, Text] = {}
    headers: Headers = {}
    req_json: Union[Dict, List, Text]
    data: Union[Text, Dict[Text, Any]] = None

class TStep():
    name: Name
    request: Union[TRequest, None] = None
    testcase: Union[Text, Callable, None] = None

class TestCase():
    teststeps: List[TStep]

class TestCaseTime():
    start_at: float = 0
    start_at_iso_format: Text = ""
    duration: float = 0

class RequestData():
    method: MethodEnum = MethodEnum.GET
    url: Url
    headers: Headers = {}
    body: Union[Text, bytes, Dict, List, None] = {}




