from projectal.entity import Entity
from projectal.linkers import *


class Customer(Entity, LocationLinker, ContactLinker, FileLinker, ProjectLinker, NoteLinker):
    """
    Implementation of the [Customer](https://projectal.com/docs/latest/#tag/Customer) API.
    """
    _path = 'customer'
    _name = 'customer'
    _links = [LocationLinker, ContactLinker, FileLinker, NoteLinker]
    _links_reverse = [ProjectLinker]
