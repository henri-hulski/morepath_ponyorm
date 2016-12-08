from pony.orm import Database, PrimaryKey, Optional

db = Database()


class Root(object):
    pass


class Document(db.Entity):
    _table_ = 'document'

    id = PrimaryKey(int, auto=True)
    title = Optional(str)
    content = Optional(str)
