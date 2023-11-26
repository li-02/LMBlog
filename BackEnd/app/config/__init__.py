import os
from datetime import timedelta


# for origin
class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'LET_KEY_THAT_HARD_TO_GUESS'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False  # 每次请求结束后自动提交数据库的更改
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 动态追踪修改设置

    JWT_ALGORITHM = 'HS256'
    JWT_LEEWAY = timedelta(seconds=300)
    JWT_VERIFY_CLAIMS = ['signature', 'exp', 'nbf', 'iat']
    JWT_NOT_BEFORE_DELTA = timedelta(seconds=0)
    JWT_REQUIRED_CLAIMS = ['exp', 'iat', 'nbf']
    JWT_AUTH_HEADER_PREFIX = 'bearer'
    JWT_ACCESS_TOKEN_EXPIRES = os.environ.get('JWT_ACCESS_TOKEN_EXPIRES') or timedelta(seconds=3600 * 24 * 3)
    PROPAGATE_EXCEPTIONS = True
    JWT_COOKIE_CSRF_PROTECT = True
    JWT_CSRF_CHECK_FORM = True
    JWT_SECRET_KEY = 'super-secret'

    # 服务器公网ip和端口
    IP_PORT = '127.0.0.1:5000'

    # 这个根目录可以自动获取文件的根目录，在创建dao的时候用这个就不用挪cur了
    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    SWAGGER_HOST = "127.0.0.1:5000" if os.getenv('FLASK_ENV') == 'development' else "39.106.43.122:5000"
    # swagger api 文档管理工具
    SWAGGER_TEMPLATE = {
        "swagger": "2.0",
        "info": {
            "title": "LMBlog",
            "description": "LMBlogAPI管理文档",
            "contact": {
                "responsibleDeveloper": "LML",
                "email": "lml2272944319@gmail.com",
                # "url": "www.me.com",
            },
            # 服务条款
            # "termsOfService": "http://me.com/terms",
            "version": "2.0-dev"
        },
        "host": SWAGGER_HOST,  # overrides localhost:5000
        # "basePath": "/api",  # base bash for blueprint registration
        "schemes": [
            "http",
            # "https"
        ],
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "in": "header",
                "name": "Authorization"
            }
        },
        "operationId": "getmyData"
    }
