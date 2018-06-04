import falcon


class SunScreenerResource:
    def on_get(eslf, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = ()
