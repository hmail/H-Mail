from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.types import String, Integer, Boolean, DateTime, Text
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    messages = relationship("Message", backref="user")


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    sender = Column(String(50))
    recipient = Column(String(50))
    read = Column(Boolean)
    time = Column(DateTime)
    title = Column(String(1024))
    content = Column(Text)


class Setting(Base):
    __tablename__ = 'settings'

    # id = Column(Integer, primary_key=True)
    key = Column(String(50), primary_key=True)
    value = Column(String(255))


def get_session(db_address):
    engine = create_engine(db_address, echo=False)
    # Base.metadata.drop_all(engine)         # Uncommit to erase DB
    Base.metadata.create_all(engine)
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return Session()
