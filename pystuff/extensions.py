from flask.ext import admin as admin_ext
from flask.ext import login as login_ext
from flask.ext import security as security_ext
from flask.ext import social as social_ext
from flask.ext import sqlalchemy as sqlalchemy_ext
from flask.ext.admin.contrib import sqlamodel


db = sqlalchemy_ext.SQLAlchemy()
security = security_ext.Security()
social = social_ext.Social()
admin = admin_ext.Admin()


class AuthModelView(sqlamodel.ModelView):
    def is_accessible(self):
        return (
            login_ext.current_user.is_authenticated() and
            super(AuthModelView, self).is_accessible()
        )
