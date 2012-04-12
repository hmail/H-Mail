import tornado.ioloop
import tornado.web
from datetime import datetime

db_name = "tornadail"
db_username = "tornadail"
db_password = "tornadail"


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
        self.set_status(200)


class UserHandler(tornado.web.RequestHandler):
    def get(self, username):
        listing = {
                    'order': '-date',
                    'limit': 10,
                    'messages': [
                        {'from': 'yoav#service.com',
                        'id': 1,
                        'to': '%s#service.com' % username,
                        'title': 'here is the title',
                        'read': True,
                        'date': str(datetime.now())
                        },
                        {'from': 'yoav#service.com',
                        'id': 2,
                        'to': '%s#service.com' % username,
                        'title': 'here is the title',
                        'read': False,
                        'date': str(datetime.now())
                        }
                        ]
                    }
        self.write(listing)
        self.set_status(200)

    def post(self):
        self.set_status(201)


class MessageHandler(tornado.web.RequestHandler):
    def get(self, username, message_id):
        message = {'from': 'yoav#service.com',
                    'to': '%s#service.com' % username,
                    'id': message_id,
                    'read': True,
                    'title': 'here is the title',
                    'date': str(datetime.now()),
                    'content': 'hey man!'}
        self.write(message)
        self.set_status(200)


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/([a-z]+)/", UserHandler),
    (r"/([a-z]+)/([0-9]+)", MessageHandler),

])

if __name__ == "__main__":
    application.listen(2626)
    application.debug = True
    print("Tornadail H-Mail Server is running on port 2626")
    tornado.ioloop.IOLoop.instance().start()
