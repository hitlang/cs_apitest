""" failure type exceptions
    these exceptions will mark test as failure
"""


class MyBaseFailure(Exception):
    pass


class ParseTestsFailure(MyBaseFailure):
    pass


class ValidationFailure(MyBaseFailure):
    pass


class ExtractFailure(MyBaseFailure):
    pass


class MyBaseError(Exception):
    pass


class FileFormatError(MyBaseError):
    pass


class TestCaseFormatError(FileFormatError):
    pass


class TestSuiteFormatError(FileFormatError):
    pass


class ParamsError(MyBaseError):
    pass


class NotFoundError(MyBaseError):
    pass


class FileNotFound(FileNotFoundError, NotFoundError):
    pass



class ApiNotFound(NotFoundError):
    pass


class TestcaseNotFound(NotFoundError):
    pass


