from . import headerParser
from . import formParser


def ParserRequestFactory(data):
    request = {}
    headers = data[data.index(b"\n")+1:data.index(b"\r\n\r\n")+4]
    method, path, version = data[:data.index(
        b"\n")].decode().strip().split(" ")
    body = data[data.index(b"\r\n\r\n")+4:]
    headers = headerParser.HTTPHeaders.parse(headers)
    if "content_type" in headers:
        request["formData"] = formParser.Parse(headers, body)
    if "cookie" in headers:
        request["cookie"] = {i.split("=")[0].strip(): i.split(
            "=")[1].strip() for i in headers["cookie"].split(";")}
    request["method"] = method
    request["path"] = path
    request["version"] = version
    return request
