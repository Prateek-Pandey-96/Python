from sqlalchemy.orm import sessionmaker
from models import User, engine

Session = sessionmaker(bind=engine)
session = Session()

# Create
# user = User(name="Prateek", age=28)
# user2 = User(name="Prateek1", age=29)
# user3 = User(name="Prateek2", age=30)
# user4 = User(name="Prateek3", age=31)

# session.add(user)
# session.add_all([user2, user3, user4])

# session.commit()

# Read
users = session.query(User).filter_by(id=1).all()
for user in users:
    print(f"user_id {user.id}, user_name {user.name}, age {user.age}")

# Delete
# session.delete(user)

# Update
# user.name = "a different name"
# user.commit