from rest_framework import serializers


class ExtendedModelSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True


class ExtendedSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True