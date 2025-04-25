
from model.contact import Contact

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact("Leon", "asds","asdasd", "xzcsad", "qwewqe", "dasd", "sdasd", "774234234", "qweqw@sad.ru"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact("", "","", "", "", "", "", "", ""))
    app.session.logout()
