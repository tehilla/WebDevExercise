import tornado.ioloop
import tornado.web
import calculator
import json


class MainHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            body = self.request.body
            json_body = json.loads(body)
            input_data = json_body['input'] if 'input' in json_body else ''
            json_state = json_body['calculatorState'] if 'calculatorState' in json_body else '{}'
            res = calculator.calculateNextState(json.dumps(json_state), input_data)
        except:
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
