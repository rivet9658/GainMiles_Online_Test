# package
from rest_framework import permissions

view_commodity_model = 'commodity.view_commoditymodel'
add_commodity_model = 'commodity.add_commoditymodel'
change_commodity_model = 'commodity.change_commoditymodel'
delete_commodity_model = 'commodity.delete_commoditymodel'


class CommodityPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if view.action in ['list', 'retrieve']:
            permission_list = [view_commodity_model]
        elif view.action in ['create']:
            permission_list = [add_commodity_model]
        elif view.action in ['update', 'partial_update']:
            permission_list = [change_commodity_model]
        elif view.action in ['destroy']:
            permission_list = [delete_commodity_model]
        else:
            permission_list = []
        count = 0
        user = request.user
        for permission in permission_list:
            if user.has_perm(permission):
                count += 1
        return count >= len(permission_list)
