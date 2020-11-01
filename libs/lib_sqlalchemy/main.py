from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base


engine = sqlalchemy.create_engine('sqlite:///site.db', echo=True)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)


Base.metadata.create_all(bind=engine)

ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')

Session = sessionmaker(bind=engine)
session = Session()

# session.add(ed_user)

our_user = session.query(User).filter_by(name='ed').first()
print(our_user)

# session.add_all([
#     User(name='wendy', fullname='Wendy Williams', nickname='windy'),
#     User(name='mary', fullname='Mary Contrary', nickname='mary'),
#     User(name='fred', fullname='Fred Flintstone', nickname='freddy')])


print(session.dirty)
