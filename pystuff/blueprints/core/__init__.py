import datetime

from flask.ext import login
from flask import views
import flask

from pystuff import models
from pystuff.extensions import db


class PostList(views.MethodView):
    def get(self):
        return flask.render_template(
            'post_list.html',
            object_list=models.Post.query.filter_by(
                draft=False).order_by('-created_at'),
        )


class PostDetail(views.MethodView):
    def get(self, pk, slug):
        obj = models.Post.query.get_or_404(pk)
        resp = flask.render_template(
            'post_detail.html',
            obj=obj
        )

        cookie_key = 'post_%s' % pk
        resp = flask.make_response(resp)
        request = flask.request
        if not request.cookies.get(cookie_key):
            resp.set_cookie(
                cookie_key,
                datetime.datetime.utcnow().strftime('%Y/%B/%d %H:%M:%S'),
            )
            obj.views = models.Post.views + 1
            db.session.add(obj)
            db.session.commit()

        return resp


class PostCreate(views.MethodView):
    decorators = [login.login_required]
    template_name = 'add_post.html'

    def get(self):
        return flask.render_template(
            self.template_name,
        )

    def post(self):
        return flask.render_template(
            self.template_name,
        )


blueprint = flask.Blueprint('core', __name__, template_folder='templates')
blueprint.add_url_rule('', view_func=PostList.as_view('post_list'))
blueprint.add_url_rule(
    '<int:pk>/<slug>/', view_func=PostDetail.as_view('post_detail'))
#blueprint.add_url_rule('', view_func=PostCreate.as_view('post_create'))
#blueprint.add_url_rule(
#    '<int:pk>/', view_func=PostCreate.as_view('post_create'))
