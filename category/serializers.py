# package
from rest_framework import serializers
# models
from category.models import CategoryModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('code', 'name')

    def update(self, instance, validated_data):
        now_requester = self.context['request'].user
        instance.code = validated_data['code']
        instance.name = validated_data['name']
        instance.updated_user = now_requester
        instance.save()
        return instance


class GetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ('id', 'code', 'name')


class CreateCategorySerializer(serializers.ModelSerializer):
    category_list = serializers.ListField(write_only=True, child=CategorySerializer(), label='類型列表')

    class Meta:
        model = CategoryModel
        fields = ('category_list',)

    def create(self, validated_data):
        now_requester = self.context['request'].user
        for category_data in validated_data['category_list']:
            CategoryModel.objects.create(
                code=category_data['code'],
                name=category_data['name'],
                create_user=now_requester,
                updated_user=now_requester
            )
        return validated_data
