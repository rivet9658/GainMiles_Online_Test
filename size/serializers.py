# package
from rest_framework import serializers
# models
from size.models import SizeModel


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeModel
        fields = ('code', 'name')

    def update(self, instance, validated_data):
        now_requester = self.context['request'].user
        instance.code = validated_data['code']
        instance.name = validated_data['name']
        instance.updated_user = now_requester
        instance.save()
        return instance


class GetSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeModel
        fields = ('id', 'code', 'name')


class CreateSizeSerializer(serializers.ModelSerializer):
    size_list = serializers.ListField(write_only=True, child=SizeSerializer(), label='尺寸列表')

    class Meta:
        model = SizeModel
        fields = ('size_list',)

    def create(self, validated_data):
        now_requester = self.context['request'].user
        for size_data in validated_data['size_list']:
            SizeModel.objects.create(
                code=size_data['code'],
                name=size_data['name'],
                create_user=now_requester,
                updated_user=now_requester
            )
        return validated_data
