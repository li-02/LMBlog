from app.config import BaseConfig


class DevConfig(BaseConfig):
    # 设置为开发环境
    ENV = 'development'
    """sqlalchemy的相关配置"""
    MYSQL_USER = 'root'  # 数据库用户名
    MYSQL_PASSWORD = 'mysqlmima0210'  # 数据库密码
    MYSQL_HOST = '127.0.0.1'  # ip or host
    MYSQL_PORT = 3306  # 数据库端口
    MYSQL_DATABASE = 'flask'  # 数据库名称
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8". \
        format(username=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOST,
               port=MYSQL_PORT, db=MYSQL_DATABASE)
