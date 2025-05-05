from flask import Flask

def create_app():  
    app = Flask(__name__)
    app.secret_key = '040601deiker'
    from .main.routers import app_main
    from .app_nivelbasico.routers import app_basico
    from .app_nivelinter.routers import app_intermedio
    from .app_nivelavanzado.routers import app_avanzado
    from .app_registros.routers import app_registrar

    app.register_blueprint(app_main, url_prefix =  "/")
    app.register_blueprint(app_basico, url_prefix = "/basico")
    app.register_blueprint(app_intermedio, url_prefix = "/intermedio")
    app.register_blueprint(app_avanzado, url_prefix = "/avanzado")
    app.register_blueprint(app_registrar, url_prefix = "/registro")

    
    
    return app