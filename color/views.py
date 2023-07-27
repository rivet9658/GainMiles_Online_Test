# package
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
# models
from color.models import ColorModel
# serializers
from color.serializers import ColorSerializer, GetColorSerializer, CreateColorSerializer
# permission
from color.permission import ColorPermission


class ColorView(viewsets.ModelViewSet):
    queryset = ColorModel.objects.all()

    def get_permissions(self):
        permission_class = (IsAuthenticated, ColorPermission)
        return [permission() for permission in permission_class]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return GetColorSerializer
        elif self.action in ['create']:
            return CreateColorSerializer
        elif self.action in ['update', 'partial_update']:
            return ColorSerializer
        else:
            return GetColorSerializer

    @swagger_auto_schema(
        operation_summary='顏色-獲取顏色列表',
        operation_description='請求顏色列表，過濾參數不輸入則那項不加入過濾',
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
            queryset = ColorModel.objects.filter(code__contains=filter_code)
        else:
            queryset = ColorModel.objects.all()
        if len(filter_name) > 0:
            queryset = queryset.filter(name__contains=filter_name)
        serializer = self.get_serializer(queryset, many=True)
        return Response({'msg': '獲得顏色列表成功', 'data': serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='顏色-獲取單一顏色',
        operation_description='請求單一顏色',
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="JWT Token", type=openapi.TYPE_STRING),
        ]
    )
    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = ColorModel.objects.all()
        filter_queryset = get_object_or_404(queryset, id=pk)
        serializer = self.get_serializer(filter_queryset)
        return Response({'msg': '獲得單一顏色成功', 'data': serializer.data}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary='顏色-新增顏色',
        operation_description='新增顏色',
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="JWT Token", type=openapi.TYPE_STRING),
        ]
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({'msg': '顏色新增失敗', 'data': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'msg': '顏色新增成功', 'data': request.data}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary='顏色-更新顏色',
        operation_description='更新指定顏色',
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="JWT Token", type=openapi.TYPE_STRING),
        ]
    )
    def update(self, request, pk=None, *args, **kwargs):
        color_queryset = ColorModel.objects.filter(id=pk)
        if not color_queryset.exists():
            return Response({'msg': '查無更新目標資料', 'data': {}},
                            status=status.HTTP_400_BAD_REQUEST)
        color_data = color_queryset.first()
        serializer = self.get_serializer(color_data, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({'msg': '顏色更新失敗', 'data': serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'msg': '顏色更新成功', 'data': request.data},
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
        operation_summary='顏色-刪除顏色',
        operation_description='刪除顏色',
        manual_parameters=[
            openapi.Parameter('Authorization', openapi.IN_HEADER, description="JWT Token", type=openapi.TYPE_STRING),
        ]
    )
    def destroy(self, request, pk=None, *args, **kwargs):
        color_queryset = ColorModel.objects.filter(id=pk)
        if not color_queryset.exists():
            return Response({'msg': '查無刪除目標資料', 'data': {}},
                            status=status.HTTP_400_BAD_REQUEST)
        color_data = color_queryset.first()
        color_data.delete()
        return Response({'msg': '顏色刪除成功', 'data': {'id': pk}},
                        status=status.HTTP_200_OK)
