import falcon
import redis


def transform(req):
    zipcode = req.get_param('zip', required=True)
    date = req.get_param('date', required=True)
    hour = req.get_param('hour', required=True)

    return f'{zipcode}.{date}:{hour}'


class SunScreenerResource:
    def on_get(self, req, resp):
        key = transform(req)
        resp.status = falcon.HTTP_200
        resp.body = (r.get(key))

r = redis.from_url(os.environ.get("REDIS_URL"))
r.set('78701.20180608:0600', '0')

app = falcon.API()
sunscreener = SunScreenerResource()

app.add_route('/', sunscreener)
# ?zip=78701&date=20180608&hour=0600
