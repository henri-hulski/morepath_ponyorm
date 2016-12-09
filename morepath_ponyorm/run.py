import morepath

from .app import App
from .model import db


def run():   # pragma: no cover
    db.bind('sqlite', 'morepath_ponyorm.db', create_db=True)
    db.generate_mapping(create_tables=True)

    morepath.autoscan()
    morepath.run(App())
