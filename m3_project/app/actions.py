from objectpack.actions import *

from app.controller import observer as obs
from app.ui import *
from app.models import *

class ContentTypePack(ObjectPack):

    model = ContentType
    add_to_menu = True

    edit_window = add_window = ModelEditWindow.fabricate(model)


class UserPack(ObjectPack):

    model = User
    add_to_menu = True

    add_window = UserAddWindow
    edit_window = ModelEditWindow.fabricate(model)


class GroupPack(ObjectPack):

    model = Group
    add_to_menu = True

    edit_window = add_window = ModelEditWindow.fabricate(model)


class PermissionPack(ObjectPack):

    model = Permission
    add_to_menu = True

    edit_window = add_window = ModelEditWindow.fabricate(
        model,
        model_register=obs,
    )
