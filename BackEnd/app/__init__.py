from flask import Flask
from app.tools.mysql import db
import os
from flask_cors import CORS

if os.getenv('FLASK_ENV') == 'development' or os.getenv('FLASK_ENV') is None:
    from app.config.DevConfig import DevConfig
if os.getenv('FLASK_ENV') == 'production':
    from app.config.ProdConfig import ProdConfig
config_choice = DevConfig if 'DevConfig' in locals() else ProdConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(config_choice)
    db.init_app(app)
    db.app = app
    app.app_context().push()
    # 利用flask_cors解决跨域问题
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
    # 跨域初始化
    cors.init_app(app)
    from app.router import test
    app.register_blueprint(test.bp)
    return app


app = create_app()
