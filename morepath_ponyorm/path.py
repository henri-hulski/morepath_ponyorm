from .app import App
from .collection import DocumentCollection
from .model import Document, Root


@App.path(model=Root, path='/')
def get_root():
    return Root()


@App.path(model=Document, path='documents/{id}',
          converters={'id': int})
def get_document(request, id):
    return Document[id]


@App.path(model=DocumentCollection, path='documents')
def get_document_collection(request, offset=0, limit=10):
    return DocumentCollection(offset, limit)
