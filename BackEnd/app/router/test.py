from flask import Blueprint

bp = Blueprint('test', __name__, url_prefix='/api/test')


@bp.route('/1', methods=['GET', 'POST'])
def test1():
    """/api/test/1"""
    return 'test1'
