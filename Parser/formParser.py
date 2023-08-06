import cgi
import io


def parseEncodeForm(raw):
    raw = raw.decode()
    return {data.split("=")[0]: data.split("=")[1] for data in raw.split("&")}


def parse_multipart_form_data(data, headers):
    """
    Yes To Be Implemented
    """
    pass


def Parse(headers, body):
    if "x-www-form-urlencoded" in headers["content_type"]:
        return parseEncodeForm(body)
    if "multipart" in headers["content_type"]:
        print("Multipart is yet to be implemented")
        bondary = headers["content_type"].split(";")[1].strip().split("=")[1]
        return parse_multipart_form_data(body.decode(), headers)
