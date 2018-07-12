import tornado.ioloop
import tornado.web
import calculator
import json
import logging


class MainHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            body = self.request.body
            jsonBody = json.loads(body)
            jsonState = jsonBody.get('calculatorState', '{}')
            input = jsonBody.get('input', '')
            res = calculator.calculateNextState(json.dumps(jsonState), input)
        except Exception as ex:
            print(str(ex))
            res = json.dumps({'display': ''})
        self.write(res)


def make_app():
    return tornado.web.Application([
        (r"/calculate", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
