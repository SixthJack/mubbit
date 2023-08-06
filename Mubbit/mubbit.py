from Parser import Parser
from Router import Router


def mubbit(routes, middlewares, data):
    request = Parser.ParserRequestFactory(data)
    for middleware in middlewares:
        middleware(request)
    for route in routes:
        if (params := Router.matcher(route, request["path"])) != None:
            routes[route](request, params)

    return "\r\n\r\n"
