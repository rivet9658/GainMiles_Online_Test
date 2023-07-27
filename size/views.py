# package
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
# models
from size.models import SizeModel
# serializers
from size.serializers import SizeSerializer, GetSizeSerializer, CreateSizeSerializer
# permission
from size.permission import SizePermission


class SizeView(viewsets.ModelViewSet):
    queryset = SizeModel.objects.all()

    def get_permissions(self):
        permission_class = (IsAuthenticated, SizePermission)
        return [permission() for permission in permission_class]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return GetSizeSerializer
        elif self.action in ['create']:
            return CreateSizeSerializer
        elif self.action in ['update', 'partial_update']:
            return SizeSerializer
        else:
            return GetSizeSerializer

    @swagger_auto_schema(
        operation_summary='尺寸-獲取尺寸列表',
        operation_description='請求尺寸列表，過濾參數不輸入則那項不加入過濾',
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
            queryset = SizeModel.objects.filter(code__contains=filter_code)
        else:
            queryset = SizeModel.objects.all()
        if len(filter_name) > 0:
            queryset = queryset.filter(name__contains=filter_name)
        serializer = self.get_serializer(queryset, many=True)
        return Response({'msg': '獲得尺寸列表成功', 'data': serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='尺寸-獲取單一尺寸',
        operation_description='請求單一尺寸',
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="JWT Token", type=openapi.TYPE_STRING),
        ]
    )
    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = SizeModel.objects.all()
        filter_queryset = get_object_or_404(queryset, id=pk)
        serializer = self.get_serializer(filter_queryset)
        return Response({'msg': '獲得單一尺寸成功', 'data': serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='尺寸-新增尺寸',
        operation_description='新增尺寸',
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="JWT Token", type=openapi.TYPE_STRING),
        ]
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({'msg': '尺寸新增失敗', 'data': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'msg': '尺寸新增成功', 'data': request.data}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary='尺寸-更新尺寸',
        operation_description='更新指定尺寸',
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="JWT Token", type=openapi.TYPE_STRING),
        ]
    )
    def update(self, request, pk=None, *args, **kwargs):
        size_queryset = SizeModel.objects.filter(id=pk)
        if not size_queryset.exists():
            return Response({'msg': '查無更新目標資料', 'data': {}},
                            status=status.HTTP_400_BAD_REQUEST)
        size_data = size_queryset.first()
        serializer = self.get_serializer(size_data, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({'msg': '尺寸更新失敗', 'data': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'msg': '尺寸更新成功', 'data': request.data},
                        status=status.HTTP_201_CREATED)

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
        operation_summary='尺寸-刪除尺寸',
        operation_description='刪除尺寸',
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="JWT Token", type=openapi.TYPE_STRING),
        ]
    )
    def destroy(self, request, pk=None, *args, **kwargs):
        size_queryset = SizeModel.objects.filter(id=pk)
        if not size_queryset.exists():
            return Response({'msg': '查無刪除目標資料', 'data': {}},
                            status=status.HTTP_400_BAD_REQUEST)
        size_data = size_queryset.first()
        size_data.delete()
        return Response({'msg': '尺寸刪除成功', 'data': {'id': pk}},
                        status=status.HTTP_200_OK)
