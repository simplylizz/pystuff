import flask


def create_app():
    app = flask.Flask(__name__)
    app.config.from_envvar('PYSTUFF_APP_CONFIG')

    # all blueprints are lives here
    from blueprints import accounts
    from blueprints import core

    app.register_blueprint(accounts.blueprint, url_prefix='/accounts/')
    app.register_blueprint(core.blueprint, url_prefix='/stuff/')
    app.add_url_rule('/', view_func=core.PostList.as_view('main'))

    # end blueprints

    # extensions
    import models
    import extensions

    from flask.ext.security import datastore as security_datastore
    from flask.ext.social import datastore as social_datastore

    db = extensions.db
    db.init_app(app)

    datastore = security_datastore.SQLAlchemyUserDatastore(
        db, models.User, models.Role)
    extensions.security.init_app(app, datastore)

    datastore = social_datastore.SQLAlchemyConnectionDatastore(
        db, models.Connection)
    extensions.social.init_app(app, datastore)

    admin = extensions.admin
    admin.init_app(app)
    for model in (models.User, models.Post):
        admin.add_view(extensions.AuthModelView(model, db.session))

    # end extensions

    return app
