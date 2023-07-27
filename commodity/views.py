# package
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
# models
from commodity.models import CommodityModel
# serializers
from commodity.serializers import GetCommoditySerializer, EditCommoditySerializer
# permission
from commodity.permission import CommodityPermission


class CommodityView(viewsets.ModelViewSet):
    queryset = CommodityModel.objects.all()

    def get_permissions(self):
        permission_class = (IsAuthenticated, CommodityPermission)
        return [permission() for permission in permission_class]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return GetCommoditySerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return EditCommoditySerializer
        else:
            return GetCommoditySerializer

    @swagger_auto_schema(
        operation_summary='商品-獲取商品列表',
        operation_description='請求商品列表，過濾參數不輸入則那項不加入過濾',
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="JWT Token", type=openapi.TYPE_STRING),
            openapi.Parameter('code', openapi.IN_QUERY, description="代號",
                              type=openapi.TYPE_STRING),
            openapi.Parameter('name', openapi.IN_QUERY, description="名稱",
                              type=openapi.TYPE_STRING),
        ]
    )
    def list(self, request, *args, **kwargs):
        filter_code = request.GET.get('code', '')
        filter_name = request.GET.get('name', '')
        if len(filter_code) > 0:
            queryset = CommodityModel.objects.filter(code__contains=filter_code)
        else:
            queryset = CommodityModel.objects.all()
        if len(filter_name) > 0:
            queryset = queryset.filter(name__contains=filter_name)
        serializer = self.get_serializer(queryset, many=True)
        return Response({'msg': '獲得商品列表成功', 'data': serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='商品-獲取單一商品',
        operation_description='請求單一商品',
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="JWT Token", type=openapi.TYPE_STRING),
        ]
    )
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'msg': '獲得單一商品成功', 'data': serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='商品-新增商品',
        operation_description='新增商品',
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="JWT Token", type=openapi.TYPE_STRING),
        ]
    )
    def create(self, request, *args, **kwargs):
        try:
            print(request.data['category_list'])
            print(request.data['color_list'])
            print(request.data['size_list'])
        except KeyError:
            return Response({'msg': '請求參數有誤，請檢查參數', 'data': {}},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({'msg': '商品新增失敗', 'data': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'msg': '商品新增成功', 'data': request.data},
                        status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary='商品-更新商品',
        operation_description='更新商品',
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="JWT Token", type=openapi.TYPE_STRING),
        ]
    )
    def update(self, request, pk=None, *args, **kwargs):
        try:
            print(request.data['category_list'])
            print(request.data['color_list'])
            print(request.data['size_list'])
        except KeyError:
            return Response({'msg': '請求參數有誤，請檢查參數', 'data': {}},
                            status=status.HTTP_400_BAD_REQUEST)
        commodity_queryset = CommodityModel.objects.filter(id=pk)
        if not commodity_queryset.exists():
            return Response({'msg': '查無更新目標資料', 'data': {}},
                            status=status.HTTP_400_BAD_REQUEST)
        commodity_data = commodity_queryset.first()
        serializer = self.get_serializer(commodity_data, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({'msg': '商品更新失敗', 'data': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'msg': '商品更新成功', 'data': request.data},
                        status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='不支援此操作',
        operation_description='不支援此操作',
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="JWT Token", type=openapi.TYPE_STRING),
        ]
    )
    def partial_update(self, request, pk=None, *args, **kwargs):
        return Response({'msg': '不支援此操作', 'data': {}},
                        status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @swagger_auto_schema(
        operation_summary='商品-刪除商品',
        operation_description='刪除商品',
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="JWT Token", type=openapi.TYPE_STRING),
        ]
    )
    def destroy(self, request, pk=None, *args, **kwargs):
        commodity_queryset = CommodityModel.objects.filter(id=pk)
        if not commodity_queryset.exists():
            return Response({'msg': '查無刪除目標資料', 'data': {}},
                            status=status.HTTP_400_BAD_REQUEST)
        commodity_data = commodity_queryset.first()
        commodity_data.delete()
        return Response({'msg': '商品刪除成功', 'data': {'id': pk}},
                        status=status.HTTP_200_OK)
