# _*_ coding: utf-8 _*_

from model.group import Group

def test_add_group(app):
    app.group.create(Group("First", "first_group", "group_footer"))


def test_add_empty_group(app):
    app.group.create(Group("", "", ""))

