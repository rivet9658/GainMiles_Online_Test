# package
from rest_framework import permissions

view_color_model = 'color.view_colormodel'
add_color_model = 'color.add_colormodel'
change_color_model = 'color.change_colormodel'
delete_color_model = 'color.delete_colormodel'


class ColorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            permission_list = [view_color_model]
        elif view.action in ['create']:
            permission_list = [add_color_model]
        elif view.action in ['update', 'partial_update']:
            permission_list = [change_color_model]
        elif view.action in ['destroy']:
            permission_list = [delete_color_model]
        else:
            permission_list = []
        count = 0
        user = request.user
        for permission in permission_list:
            if user.has_perm(permission):
                count += 1
        return count >= len(permission_list)
