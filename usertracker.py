import main
import time
backend = main.Backend()


def resolver(request, params):
    with open("records.txt", "a") as file:
        file.write(params["name"])
    return


def logger(request):
    with open("logs.txt", "a") as file:
        file.write(str(time.time()))
    return


backend.routes["/add/<str:name>"] = resolver
backend.middlewares.append(logger)

backend.run()
