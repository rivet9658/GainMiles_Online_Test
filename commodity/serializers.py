# package
from rest_framework import serializers
# models
from commodity.models import CommodityModel, CommodityHaveCategoryModel, \
    CommodityHaveColorModel, CommodityHaveSizeModel
from category.models import CategoryModel
from color.models import ColorModel
from size.models import SizeModel
# serializers
from category.serializers import CategorySerializer
from color.serializers import ColorSerializer
from size.serializers import SizeSerializer


class GetCommoditySerializer(serializers.ModelSerializer):
    have_category = serializers.SerializerMethodField('get_commodity_have_category', label='')
    have_color = serializers.SerializerMethodField('get_commodity_have_color', label='')
    have_size = serializers.SerializerMethodField('get_commodity_have_size', label='')

    class Meta:
        model = CommodityModel
        fields = ('id', 'code', 'name', 'price', 'inventory', 'have_category', 'have_color', 'have_size')

    def get_commodity_have_category(self, obj):
        commodity_have_category = CommodityHaveCategoryModel.objects.filter(belong_commodity=obj)
        return [category.belong_category.name for category in commodity_have_category]

    def get_commodity_have_color(self, obj):
        commodity_have_color = CommodityHaveColorModel.objects.filter(belong_commodity=obj)
        return [color.belong_color.name for color in commodity_have_color]

    def get_commodity_have_size(self, obj):
        commodity_have_size = CommodityHaveSizeModel.objects.filter(belong_commodity=obj)
        return [size.belong_size.name for size in commodity_have_size]


class EditCommoditySerializer(serializers.ModelSerializer):
    category_list = serializers.ListField(write_only=True, child=CategorySerializer(), label='類別列表')
    color_list = serializers.ListField(write_only=True, child=ColorSerializer(), label='顏色列表')
    size_list = serializers.ListField(write_only=True, child=SizeSerializer(), label='尺寸列表')

    class Meta:
        model = CommodityModel
        fields = ('code', 'name', 'price', 'inventory', 'category_list', 'color_list', 'size_list')

    def create(self, validated_data):
        now_requester = self.context['request'].user
        commodity = CommodityModel.objects.create(
            code=validated_data['code'],
            name=validated_data['name'],
            price=validated_data['price'],
            inventory=validated_data['inventory'],
            create_user=now_requester,
            updated_user=now_requester
        )
        self.have_category_handle(commodity, validated_data['category_list'], now_requester)
        self.have_color_handle(commodity, validated_data['color_list'], now_requester)
        self.have_size_handle(commodity, validated_data['size_list'], now_requester)
        return validated_data

    def update(self, instance, validated_data):
        now_requester = self.context['request'].user
        instance.code = validated_data['code']
        instance.name = validated_data['name']
        instance.price = validated_data['price']
        instance.inventory = validated_data['inventory']
        instance.updated_user = now_requester
        instance.save()
        CommodityHaveCategoryModel.objects.filter(belong_commodity=instance).delete()
        CommodityHaveColorModel.objects.filter(belong_commodity=instance).delete()
        CommodityHaveSizeModel.objects.filter(belong_commodity=instance).delete()
        self.have_category_handle(instance, validated_data['category_list'], now_requester)
        self.have_color_handle(instance, validated_data['color_list'], now_requester)
        self.have_size_handle(instance, validated_data['size_list'], now_requester)
        return instance

    def have_category_handle(self, commodity, category_list, now_requester):
        for category in category_list:
            now_category = CategoryModel.objects.get_or_create(
                code=category['code'],
                name=category['name'],
                create_user=now_requester,
                updated_user=now_requester
            )
            CommodityHaveCategoryModel.objects.create(
                belong_commodity=commodity,
                belong_category=now_category,
                create_user=now_requester,
                updated_user=now_requester
            )

    def have_color_handle(self, commodity, color_list, now_requester):
        for color in color_list:
            now_color = ColorModel.objects.get_or_create(
                code=color['code'],
                name=color['name'],
                create_user=now_requester,
                updated_user=now_requester
            )
            CommodityHaveColorModel.objects.create(
                belong_commodity=commodity,
                belong_color=now_color,
                create_user=now_requester,
                updated_user=now_requester
            )

    def have_size_handle(self, commodity, size_list, now_requester):
        for size in size_list:
            now_size = SizeModel.objects.get_or_create(
                code=size['code'],
                name=size['name'],
                create_user=now_requester,
                updated_user=now_requester
            )
            CommodityHaveSizeModel.objects.create(
                belong_commodity=commodity,
                belong_size=now_size,
                create_user=now_requester,
                updated_user=now_requester
            )
