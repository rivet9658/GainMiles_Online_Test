# package
from rest_framework import permissions

view_category_model = 'category.view_categorymodel'
add_category_model = 'category.add_categorymodel'
change_category_model = 'category.change_categorymodel'
delete_category_model = 'category.delete_categorymodel'


class CategoryPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            permission_list = [view_category_model]
        elif view.action in ['create']:
            permission_list = [add_category_model]
        elif view.action in ['update', 'partial_update']:
            permission_list = [change_category_model]
        elif view.action in ['destroy']:
            permission_list = [delete_category_model]
        else:
            permission_list = []
        count = 0
        user = request.user
        for permission in permission_list:
            if user.has_perm(permission):
                count += 1
        return count >= len(permission_list)
