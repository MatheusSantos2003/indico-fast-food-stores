from apps.stores.stores_controllers import stores_bp as stores_api


def register_routes(app):
    """

    Aqui você faria o registro de novas rotas na aplicação

    """

    app.register_blueprint(stores_api, url_prefix='/stores')
    # app.register_blueprint(users_api, url_prefix='/stores')
    

