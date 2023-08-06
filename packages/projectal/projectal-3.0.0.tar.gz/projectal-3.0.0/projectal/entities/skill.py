from projectal.entity import Entity
from projectal.linkers import *


class Skill(Entity, StaffLinker, TaskLinker, TaskTemplateLinker):
    """
    Implementation of the [Skill](https://projectal.com/docs/latest/#tag/Skill) API.
    """
    _path = 'skill'
    _name = 'skill'
    _links_reverse = [StaffLinker, TaskLinker, TaskTemplateLinker]
