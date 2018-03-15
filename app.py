from japronto import Application

app = Application()


class App():
    def route(url, methods=['GET', 'POST', 'DELETE', 'UPDATE'], *args, **kwargs):
        def decorator(fn):
            for method in methods:
                app.router.add_route(
                    url, fn, method=method.upper(), *args, **kwargs)
            return fn
        return decorator

    @route("/")
    def handleRoot(request):
        return request.Response(text="pyBanca")
