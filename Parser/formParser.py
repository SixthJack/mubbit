import cgi
def parseEncodeForm(raw):
    raw = raw.decode()
    return {data.split("=")[0]:data.split("=")[1] for data in raw.split("&")}
def parse_multipart_form_data(data, boundary):
    """
    Yes To Be Implemented
    """
    pass
def Parse(content_type,body):
    if "x-www-form-urlencoded" in content_type:
        return parseEncodeForm(body)
    if "multipart" in content_type:
        print("Multipart is yet to be implemented")
        bondary = content_type.split(";")[1].strip().split("=")[1]
        parse_multipart_form_data(body.decode(),bondary)
