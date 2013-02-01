#!/usr/bin/env python
# coding: utf-8

import os

from flask.ext import script
from flask.ext.security import utils

import pystuff
from pystuff.extensions import db
from pystuff import models


app = pystuff.create_app()
manager = script.Manager(app)
project_root_path = os.path.join(os.path.dirname(app.root_path))


@manager.command
def initdb():
    """Reset and init database."""

    db.drop_all()
    db.create_all()

    user_defaults = {
        'username': 'admin',
        'email': 'admin@example.com',
        'password': 'admin',
    }
    input_msg = 'Enter %s [%s]: '
    for key, value in user_defaults.iteritems():
        user_defaults[key] = raw_input(input_msg % (key, value)) or value

    user_defaults['password'] = utils.encrypt_password(
        user_defaults['password'])

    user = models.User(**user_defaults)

    db.session.add(user)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
