from flask import views
from flask.ext import login
from flask.ext import social
from flask.ext.security import forms, utils
from flask.ext.security import views as security_views
import flask


class Login(views.View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        form = forms.LoginForm()

        if form.validate_on_submit():
            utils.login_user(form.user, remember=form.remember.data)
            flask.after_this_request(security_views._commit)

            return flask.redirect(utils.get_post_login_redirect())

        form.next.data = (
            utils.get_url(flask.request.args.get('next')) or
            utils.get_url(flask.request.form.get('next')) or
            ''
        )

        return flask.render_template('login.html', form=form)


class Profile(views.MethodView):
    decorators = [login.login_required]

    def get(self):
        return flask.render_template(
            'profile.html',
            twitter_conn=social.twitter.get_connection(),
            facebook_conn=social.facebook.get_connection(),
        )


blueprint = flask.Blueprint('accounts', __name__, template_folder='templates')

blueprint.add_url_rule('login/', view_func=Login.as_view('login'))
#blueprint.add_url_rule('profile/', view_func=Profile.as_view('profile'))
