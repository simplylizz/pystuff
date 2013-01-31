import datetime

from flask.ext import security

import extensions


db = extensions.db


class DatesMixin(object):
    """Mixing with additional field to store date of creation and last
    modification.
    """
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.datetime.utcnow)


roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')),
)


class Role(db.Model, security.RoleMixin, DatesMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=False)


class User(db.Model, security.UserMixin, DatesMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    email = db.Column(db.String(256), nullable=False)
    avatar = db.Column(db.String(256))

    # Flask-Security stuff:
    password = db.Column(db.String, nullable=True)
    confirmed_at = db.Column(db.DateTime, nullable=True)
    last_login_at = db.Column(db.DateTime, nullable=True)
    current_login_at = db.Column(db.DateTime, nullable=True)
    last_login_ip = db.Column(db.String(46), default='')
    current_login_ip = db.Column(db.String(46), default='')
    login_count = db.Column(db.Integer, default=0)
    #roles = db.ListField(db.ReferenceField(Role), default=[])
    roles = []

    posts = db.relationship('Post', backref='author')

    def __unicode__(self):
        return u'#%s - %s' % (self.id, self.username)

    def is_active(self):
        return True


class Connection(db.Model, DatesMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    provider_id = db.Column(db.String(255))
    provider_user_id = db.Column(db.String(255))
    access_token = db.Column(db.String(255))
    secret = db.Column(db.String(255))
    display_name = db.Column(db.String(255))
    profile_url = db.Column(db.String(512))
    image_url = db.Column(db.String(512))
    rank = db.Column(db.Integer)


class Post(db.Model, DatesMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    slug = db.Column(db.String(255))
    body = db.Column(db.Text)
    original_url = db.Column(db.String(512), default='')
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    views = db.Column(db.Integer, default=0)

    def __unicode__(self):
        return u'#%s - %s' % (self.id, self.title)
