from . import headerParser
from . import formParser
def ParserRequestFactory(data):
    headers = data[data.index(b"\n")+1:data.index(b"\r\n\r\n")+4]
    body = data[data.index(b"\r\n\r\n")+4:]
    headers = headerParser.HTTPHeaders.parse(headers)
    if "content_type" in headers:
        formData = formParser.Parse(headers["content_type"],body)
    if "cookie" in headers:
        headers["cookie"] = {i.split("=")[0].strip():i.split("=")[1].strip() for i in headers["cookie"].split(";")}
        print(headers["cookie"])

class Request:
    def __init__(self):
        self
