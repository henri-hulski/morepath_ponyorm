import logging

from pony.orm import Database, PrimaryKey, Optional

db = Database()


class Root(object):
    pass


class Document(db.Entity):
    _table_ = 'document'

    id = PrimaryKey(int, auto=True)
    title = Optional(str)
    content = Optional(str)

    def before_insert(self):
        logging.warning('Here is the before_insert hook of the model.')

    def after_insert(self):
        logging.warning('Here is the after_insert hook of the model.')
