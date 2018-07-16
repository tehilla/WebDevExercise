from tornado.web import Application, RequestHandler
import tornado.ioloop
import calculator
import json


class MainHandler(RequestHandler):
    def post(self):
        try:
            body = self.request.body
            json_body = json.loads(body)
            input_data = json_body['input'] if 'input' in json_body and json_body['input'] else ''
            json_state = json_body['calculatorState'] if 'calculatorState' in json_body and json_body['calculatorState'] else '{}'
            res = calculator.calculateNextState(json.dumps(json_state), input_data)
        except Exception as e:
            if str(e) == 'Invalid input':
                res = json.dumps({'display': str(e)})
            else:
                res = json.dumps({'display': 'Error'})
        self.write(res)


def make_app():
    return Application([
        (r"/calculate", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(3000)
    tornado.ioloop.IOLoop.current().start()
