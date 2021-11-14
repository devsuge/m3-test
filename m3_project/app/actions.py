from objectpack.actions import *
from objectpack.slave_object_pack.actions import SlavePack
from objectpack.ui import ModelEditWindow

from app.models import *
from app.ui import *


class ContentTypePack(ObjectPack):

    model = ContentType

    add_window = ModelEditWindow.fabricate(model=ContentType)
    edit_window = ModelEditWindow.fabricate(model=ContentType)
    add_to_menu = True


class UserPack(ObjectPack):

    model = User

    add_window = UserAddWindow
    edit_window = ModelEditWindow.fabricate(model=User)
    add_to_menu = True


class GroupPack(ObjectPack):

    model = Group

    add_window = ModelEditWindow.fabricate(model=Group)
    edit_window = ModelEditWindow.fabricate(model=Group)
    add_to_menu = True


class PermissionPack(ObjectPack):
    # чинить
    model = Permission
    add_window = PermissionAddWindow#ModelEditWindow.fabricate(model=Permission)

    edit_window = ModelEditWindow.fabricate(model=Permission)
    add_to_menu = True