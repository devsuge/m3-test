from objectpack.ui import *
from m3_ext.ui import all_components as ext



class UserAddWindow(BaseEditWindow):

    def _init_components(self):
        super(UserAddWindow, self)._init_components()

        self.field__password = ext.ExtStringField(
            label='password',
            name='password',
            allow_blank=False,
            anchor='100%')

        self.field__last_login = ext.ExtDateField(
            label='last login',
            name='last_login',
            format='d.m.Y',
            allow_blank=False,
            anchor='100%')

        self.field__superuser = ext.ExtCheckBox(
            label='superuser status',
            name='is_superuser',
            allow_blank=False,
            anchor='100%')

        self.field__username = ext.ExtStringField(
            label='username',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__firstname = ext.ExtStringField(
            label='first name',
            name='first_name',
            allow_blank=False,
            anchor='100%')

        self.field__lastname = ext.ExtStringField(
            label='last name',
            name='last_name',
            allow_blank=False,
            anchor='100%')

        self.field__email = ext.ExtStringField(
            label='email address',
            name='email',
            allow_blank=False,
            anchor='100%')

        self.field__staff = ext.ExtCheckBox(
            label='staff status',
            name='is_staff',
            allow_blank=False,
            anchor='100%')

        self.field__active = ext.ExtCheckBox(
            label='active',
            name='is_active',
            allow_blank=False,
            anchor='100%')

        self.field__date_join = ext.ExtDateField(
            label='date joined',
            name='date_joined',
            format='d.m.Y',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__password,
            self.field__last_login,
            self.field__superuser,
            self.field__username,
            self.field__firstname,
            self.field__lastname,
            self.field__email,
            self.field__staff,
            self.field__active,
            self.field__date_join,
        ))

    def set_params(self, params):
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'
