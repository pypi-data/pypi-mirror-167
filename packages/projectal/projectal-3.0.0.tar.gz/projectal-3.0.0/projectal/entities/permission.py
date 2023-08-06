from projectal.entity import Entity
from projectal.linkers import *


class Permission(Entity, UserLinker, AccessPolicyLinker):
    """
    Implementation of the [Permission](https://projectal.com/docs/latest/#tag/Permission) API.
    """
    _path = 'permission'
    _name = 'permission'
    _links_reverse = [UserLinker, AccessPolicyLinker]