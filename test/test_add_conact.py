
from model.contact import Contact

def test_add_contact(app):
    app.contact.create_contact(Contact("Leon", "asds","asdasd", "xzcsad", "qwewqe", "dasd", "sdasd", "774234234", "qweqw@sad.ru"))

def test_add_empty_contact(app):
    app.contact.create_contact(Contact("", "","", "", "", "", "", "", ""))
