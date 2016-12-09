from pony.orm import count
from .model import Document

MAX_LIMIT = 20


class DocumentCollection(object):
    def __init__(self, offset, limit):
        self.offset = offset
        self.limit = min(limit, MAX_LIMIT)

    def query(self):
        return Document.select().limit(self.limit, offset=self.offset)

    def add(self, title, content):
        document = Document(title=title, content=content)
        document.flush()
        return document

    def previous(self):
        if self.offset == 0:
            return None
        new_offset = max(self.offset - self.limit, 0)
        return DocumentCollection(new_offset, self.limit)

    def next(self):
        doc_count = count(d for d in Document)
        new_offset = self.offset + self.limit
        if new_offset >= doc_count:
            return None
        return DocumentCollection(new_offset, self.limit)
