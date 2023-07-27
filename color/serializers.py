# package
from rest_framework import serializers
# models
from color.models import ColorModel


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorModel
        fields = ('code', 'name')

    def update(self, instance, validated_data):
        now_requester = self.context['request'].user
        instance.code = validated_data['code']
        instance.name = validated_data['name']
        instance.updated_user = now_requester
        instance.save()
        return instance


class GetColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorModel
        fields = ('id', 'code', 'name')


class CreateColorSerializer(serializers.ModelSerializer):
    color_list = serializers.ListField(write_only=True, child=ColorSerializer(), label='顏色列表')

    class Meta:
        model = ColorModel
        fields = ('color_list',)

    def create(self, validated_data):
        now_requester = self.context['request'].user
        for color_data in validated_data['color_list']:
            ColorModel.objects.create(
                code=color_data['code'],
                name=color_data['name'],
                create_user=now_requester,
                updated_user=now_requester
            )
        return validated_data
