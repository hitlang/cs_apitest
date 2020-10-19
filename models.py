import os
from enum import Enum
from typing import Any
from typing import Dict, Text, Union, Callable
from typing import List

from pydantic import BaseModel, Field
from pydantic import HttpUrl

Name = Text
Url = Text
BaseUrl = Union[HttpUrl, Text]
VariablesMapping = Dict[Text, Any]
FunctionsMapping = Dict[Text, Callable]
Headers = Dict[Text, Text]
Cookies = Dict[Text, Text]
Verify = bool
Hooks = List[Union[Text, Dict[Text, Text]]]
Export = List[Text]
Validators = List[Dict]
Env = Dict[Text, Any]


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
    # used to extract request's response field
    extract: VariablesMapping = {}
    # used to export session variables from referenced testcase


class TestCase(BaseModel):
    teststeps: List[TStep]

#
# class ProjectMeta(BaseModel):
#     debugtalk_py: Text = ""  # debugtalk.py file content
#     debugtalk_path: Text = ""  # debugtalk.py file path
#     dot_env_path: Text = ""  # .env file path
#     functions: FunctionsMapping = {}  # functions defined in debugtalk.py
#     env: Env = {}
#     RootDir: Text = os.getcwd()  # project root directory (ensure absolute), the path debugtalk.py located


class TestsMapping(BaseModel):
    # project_meta: ProjectMeta
    testcases: List[TestCase]


# class TestCaseTime(BaseModel):
#     start_at: float = 0
#     start_at_iso_format: Text = ""
#     duration: float = 0


# class TestCaseInOut(BaseModel):
#     config_vars: VariablesMapping = {}
#     export_vars: Dict = {}

#
# class RequestStat(BaseModel):
#     content_size: float = 0
#     response_time_ms: float = 0
#     elapsed_ms: float = 0


# class AddressData(BaseModel):
#     client_ip: Text = "N/A"
#     client_port: int = 0
#     server_ip: Text = "N/A"
#     server_port: int = 0


class RequestData(BaseModel):
    method: MethodEnum = MethodEnum.GET
    url: Url
    headers: Headers = {}
    body: Union[Text, bytes, Dict, List, None] = {}


class ResponseData(BaseModel):
    status_code: int
    headers: Dict
    cookies: Cookies
    encoding: Union[Text, None] = None
    content_type: Text
    body: Union[Text, bytes, Dict]


class ReqRespData(BaseModel):
    request: RequestData
    response: ResponseData







