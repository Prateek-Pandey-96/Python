from userBuilder import UserBuilder
from user import User

builder = UserBuilder().get_builder()

user = builder.with_name("Prateek").with_age(27).with_address("some random address").build()

user.print_user()