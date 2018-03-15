from Database import engine, Base, Session
from models import User

Base.metadata.create_all(engine)

session = Session()

session.commit()
session.close()
