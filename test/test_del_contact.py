from model.contact import Contact

def test_del_first_contact(app):
    app.contact.delete_first_contact()
