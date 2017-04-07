import web


# post /book/add
def add_book(name, author, press) -> {
    '成功': {'code!': 0, 'id': 42,}
}:
    """新增图书"""
    pass


# post /book/add
def update_book(id:int, name=None, author=None, press=None) -> {
    '成功': {'code!': 0},
    '未找到ID': {'code!': 1, 'message!': '该书已被删除',}
}:
    """修改图书信息"""
    web.header('Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE, OPTIONS')
    pass


# get /book/(?<id>\d+)
def detail_book(id:int) -> {
    '成功': {
        'code!': 0,
        'detail': {
            'name': '深入理解计算机系统',
            'author': "[美国] Randal E·Bryant / David O'Hallaron",
            'press': '中国电力出版社',
        }
    },
    '未找到ID': {'code!': 1, 'message!': '该书已被删除',}
}:
    """查询图书详情"""
    pass


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
    """查询图书列表"""
    pass


# delete /book/(?<id>\d+)
def delete_book(id:int) -> {
    '成功': {'code!': 0}
}:
    """删除图书"""
    pass


