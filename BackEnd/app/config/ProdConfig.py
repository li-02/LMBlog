from app.config import BaseConfig


class ProdConfig(BaseConfig):
    ENV = 'production'
    MYSQL_USER = 'root'  # 数据库用户名
    MYSQL_PASSWORD = 'mysqlmima0210'  # 数据库密码
    MYSQL_HOST = '127.0.0.1'  # ip or host
    MYSQL_PORT = 3306  # 数据库端口
    MYSQL_DATABASE = 'flask'  # 数据库名称
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8". \
        format(username=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOST,
               port=MYSQL_PORT, db=MYSQL_DATABASE)
    SQLALCHEMY_POOL_SIZE = 100  # 数据库连接池大小
    SQLALCHEMY_POOL_RECYCLE = 3600  # 自动回收连接1h
    REDIS_HOST = '39.106.43.122'
    REDIS_PORT = 6379
    REDIS_DB = 1
    REDIS_PASSWORD = 'beon2.0_redis'
    # 私钥地址
    KEY_FILENAME = '/home/ssh/id_rsa_my_key'
    # 原始数据数据下载生成文件地址
    # ToDo 原始数据下载 先直接拿1.0的文件下载。2.0的定时任务需要修改一下aqi表的字段名。
    DATA_DOWNLOAD_PATH = r'/beon_v1/flux/data_download/'
    QC_DATA_DOWNLOAD_PATH = r'/beon_v1/flux/qc_data_download/'
    # 图片路径
    PIC_DIR = r'/beon_v1/image/'
    # 物候路径
    PHENO_PATH = r'/beon_v1/flux/phenology'
    # 红外路径
    CAMERA_PATH = r'/beon_v1/camera'
    # 红外照片筛选结果路径
    CAMERA_DETECTION_PATH = r'/beon_v1/camera_result'

    # 站点图片文件资源路径
    SITE_PIC_DIR = os.path.join(PIC_DIR, 'sites')
    RAW_SITE_PIC_DIR = os.path.join(SITE_PIC_DIR, 'raw')
    COMPRESS_SITE_PIC_DIR = os.path.join(SITE_PIC_DIR, 'compress')

    # 设备的图片的目录（压缩和原图）
    DEVICE_PIC_DIR = os.path.join(PIC_DIR, 'devices')
    RAW_DEVICE_PIC_DIR = os.path.join(DEVICE_PIC_DIR, 'raw')
    COMPRESS_DEVICE_PIC_DIR = os.path.join(DEVICE_PIC_DIR, 'compress')

    # 维修的图片的目录（压缩和原图）
    REPAIR_PIC_DIR = os.path.join(PIC_DIR, 'repair')
    VIDEO_REPAIR_PIC_DIR = os.path.join(REPAIR_PIC_DIR, 'video')
    RAW_REPAIR_PIC_DIR = os.path.join(REPAIR_PIC_DIR, 'raw')
    COMPRESS_REPAIR_PIC_DIR = os.path.join(REPAIR_PIC_DIR, 'compress')

    # 维护的图片的目录(压缩和原图)
    MAINTENANCE_PIC_DIR = os.path.join(PIC_DIR, 'maintenance')
    VIDEO_MAINTENANCE_PIC_DIR = os.path.join(MAINTENANCE_PIC_DIR, 'video')
    RAW_MAINTENANCE_PIC_DIR = os.path.join(MAINTENANCE_PIC_DIR, 'raw')
    COMPRESS_MAINTENANCE_PIC_DIR = os.path.join(
        MAINTENANCE_PIC_DIR, 'compress')

    # 这个根目录可以自动获取文件的根目录，在创建dao的时候用这个就不用挪cur了
    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
