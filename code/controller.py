from datetime import datetime
from web import ctx
from model import Book


# post /book/add
def add_book(name, author, press) -> {
    '成功': {'code!': 0, 'id': 42,}
}:
    """新增图书
    :param name: 书名
    :param author: 作者
    :param press: 出版社
    :return id: 新增的书的ID
    """
    book = Book(name=name, author=author, press=press, create_at=datetime.now())
    ctx.db.add(book)
    ctx.db.commit()
    return '成功', {'id': book.id}


# post /book/add
def update_book(id:int, name=None, author=None, press=None) -> {
    '成功': {'code!': 0},
    '未找到ID': {'code!': 1, 'message!': '该书已被删除',}
}:
    """
    修改图书信息
    :param id: 图书ID
    :param name: 书名
    :param author: 作者
    :param press: 出版社
    :return: message: 错误信息
    """
    query = ctx.db.query(Book)
    book = query.filter(Book.id == id).first()
    if not book: return '未找到ID', {}
    if name is not None: book.name = name
    if author is not None: book.author = author
    if press is not None: book.press = press
    return '成功', {}


# get /book/(?<id>\d+)
def detail_book(id:int) -> {
    '成功': {
        'code!': 0,
        'detail': {
            'name': '深入理解计算机系统',
            'author': "[美国] Randal E·Bryant / David O'Hallaron",
            'press': '中国电力出版社',
            'create_at': '2017-04-07 12:01:02',
        }
    },
    '未找到ID': {'code!': 1, 'message!': '该书已被删除',}
}:
    """
    查询图书详情
    :param id: 图书ID
    :return: detail: 图书详情
    :return: name: 书名
    :return: author: 作者
    :return: press: 出版社
    :return: create_at: 创建时间
    """
    query = ctx.db.query(Book)
    book = query.filter(Book.id == id).first()
    if not book: return '未找到ID', {}
    return '成功', {'detail': book}


# get /book/list
def list_book() -> {
    '成功': {
        'code!': 0,
        'list': [
            {
                'id': 42,
                'name': '深入理解计算机系统',
                'author': "[美国] Randal E·Bryant / David O'Hallaron",
                'press': '中国电力出版社',
            },
            {
                'id': 43,
                'name': '编程珠玑',
                'author': "Jon Bentley",
                'press': '人民邮电出版社',
            },
        ]
    }
}:
    """
    查询图书列表
    :return: list: 图书列表
    :return: id: 图书ID
    :return: name: 书名
    :return: author: 作者
    :return: press: 出版社
    """
    return '成功', {'list': ctx.db.query(Book).all()}


# delete /book/(?<id>\d+)
def delete_book(id:int) -> {
    '成功': {'code!': 0}
}:
    """
    删除图书
    :param id: 图书ID
    """
    query = ctx.db.query(Book)
    book = query.filter(Book.id == id).first()
    if book:
        ctx.db.delete(book)
    return '成功', {}
