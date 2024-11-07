from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#podsstawowa klasa dla modeli
Base = declarative_base()

#definicja modelu tabeli
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

#silnik baz danych SQLITE
engine = create_engine('sqlite:///osoba.db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#nowy użzytkownik
new_user = User(name='Ala',age=25)
session.add(new_user)
session.commit()

users = session.query(User).all()
for user in users:
    print(f"ID: {user.id}, name: {user.name}, age: {user.age}")
session.close()
