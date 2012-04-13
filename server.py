import tornado.ioloop
import tornado.web
from model import User, Message, get_session
from datetime import datetime

# Tornadail Configuration
server_port = 2626                       # Default: 26
db_address = "sqlite:///tornadail.db"    # DB of you choice


session = get_session(db_address)


class ServerHandler(tornado.web.RequestHandler):
    def get(self):
        details = {
                    'server': 'Tornadail',
                    'version': '0.1',
                    'protocol': '0.1'}
        self.write(details)
        self.set_status(200)


class UserHandler(tornado.web.RequestHandler):
    def get(self, username):
        messages = []
        for message in session.query(Message).all():
            m = {
                'sender': message.sender,
                'recipient': message.recipient,
                'time': str(message.time),
                'title': message.title,
                'content': message.content,
                'read': message.read,
                'id': message.id
                }
            messages.append(m)
        listing = {
                    'order': '-date',
                    'limit': 10,
                    'messages': messages
                    }
        self.write(listing)
        self.set_status(200)

    def post(self, username):
        try:
            user = session.query(User).filter_by(name=username).one()
        except:
            user = User(name=username)
            session.add(user)
            session.commit()
        message = Message(user=user,
                            sender=self.get_argument('sender'),
                            recipient=self.get_argument('recipient'),
                            time=datetime.now(),
                            title=self.get_argument('title'),
                            content=self.get_argument('content'),
                            read=False)
        session.add(message)
        session.commit()
        self.set_status(201)


class MessageHandler(tornado.web.RequestHandler):
    def get(self, username, message_id):
        try:
            message = session.query(Message).filter_by(id=message_id).one()
        except:
            self.set_status(404)
            return
        data = {'recipient': message.recipient,
                    'sender': message.sender,
                    'read': message.read,
                    'title': message.title,
                    'date': str(message.time),
                    'content': message.content}
        self.write(data)
        self.set_status(200)

    def delete(self, username, message_id):
        try:
            message = session.query(Message).filter_by(id=message_id).one()
        except:
            self.set_status(404)
            return
        session.delete(message)
        session.commit()

    def put(self, username, message_id):
        try:
            message = session.query(Message).filter_by(id=message_id).one()
        except:
            self.set_status(404)
            return
        for key in self.request.arguments:
            value = self.get_argument(key)
            if value == "True":
                value = True
            elif value == "False":
                value = False
            message.__setattr__(key, value)
        session.commit()


application = tornado.web.Application([
    (r"/", ServerHandler),
    (r"/([a-z]+)/", UserHandler),
    (r"/([a-z]+)/([0-9]+)", MessageHandler),
])

if __name__ == "__main__":
    application.listen(server_port)
    application.debug = True
    print("Tornadail H-Mail Server is running on port %s" % server_port)
    tornado.ioloop.IOLoop.instance().start()
