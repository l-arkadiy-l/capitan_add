from data import db_session
from data.users import User


def add_user(surname, name, age, position, speciality, address, email):
    user = User()
    user.surname = surname
    user.name = name
    user.age = age
    user.position = position
    user.speciality = speciality
    user.address = address
    user.email = email

    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


def fill_base():
    temp_users = [("Scott", "Ridley", "45", "captain", "team leader", "module_1", "scott@mars.com"),
                  ("Andrey", "Constant", "23", "no capitan", "human", "module_2", "andrey@mars.com"),
                  ("Max", "Second", "34", "no capitan", "human", "module_3", "MrDLon@mars.com"),
                  ("Honor", "McGregor", "98", "no capitan", "human", "module_4", "greror@mars.com")]
    for user in temp_users:
        add_user(*user)


if __name__ == "__main__":
    db_session.global_init("db/mars.db")
    fill_base()

