# package
from rest_framework import permissions

view_size_model = 'size.view_sizemodel'
add_size_model = 'size.add_sizemodel'
change_size_model = 'size.change_sizemodel'
delete_size_model = 'size.delete_sizemodel'


class SizePermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            permission_list = [view_size_model]
        elif view.action in ['create']:
            permission_list = [add_size_model]
        elif view.action in ['update', 'partial_update']:
            permission_list = [change_size_model]
        elif view.action in ['destroy']:
            permission_list = [delete_size_model]
        else:
            permission_list = []
        count = 0
        user = request.user
        for permission in permission_list:
            if user.has_perm(permission):
                count += 1
        return count >= len(permission_list)
