#!/usr/bin/env python
# coding: utf-8

import os

from flask.ext.script import Manager

import pystuff
from pystuff.extensions import db
from pystuff import models


app = pystuff.create_app()
manager = Manager(app)
project_root_path = os.path.join(os.path.dirname(app.root_path))


@manager.command
def run():
    """Run local server."""
    app.run()


@manager.command
def initdb():
    """Reset and init database."""

    db.drop_all()
    db.create_all()

    user = models.User(
        username=u'admin',
        email=u'admin@example.com',
        password=u'password',
    )

    # First post from my sandbox.
    post = models.Post(
        author=user,
        title=u'5 минут, полёт нормальный',
        slug='pystuff-go-go-go',
        body=u"""<p>Привет, мир!</p>\n<p>Запустился очередной сайт ("портал" звучало бы слишком пафосно) на питоне о питоне - pystuff.</p>\n<p>На самом деле я хочу изучить Flask. За одно заставить себя читать больше инфы о python, т.к. я выбрал его как основной скилл. Ну ещё хочется совсем чуть-чуть экспериментов по (ой!) SEO и маркетингу.</p>\n<p>За сим прощаюсь, всем спасибо за внимание, до новых встреч.</p>\n<p>P.S. Поехали!</p>""",
    )

    db.session.add(user)
    db.session.add(post)
    db.session.commit()


manager.add_option('-c', '--config',
                   dest="config",
                   required=False,
                   help="config file")


if __name__ == "__main__":
    manager.run()
