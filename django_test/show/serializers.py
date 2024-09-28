from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import (
    Category,
    MasterUnit,
    OtherUnit,
    Show,
    ShowInfo,
    SourceWeb,
    SubUnit,
    SupportUnit,
)


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class MasterUnitSerializer(ModelSerializer):
    class Meta:
        model = MasterUnit
        fields = "__all__"


class OtherUnitSerializer(ModelSerializer):
    class Meta:
        model = OtherUnit
        fields = "__all__"


class ShowSerializer(ModelSerializer):
    class Meta:
        model = Show
        fields = "__all__"


class ShowInfoSerializer(ModelSerializer):
    class Meta:
        model = ShowInfo
        fields = "__all__"


class SourceWebSerializer(ModelSerializer):
    class Meta:
        model = SourceWeb
        fields = "__all__"


class SubUnitSerializer(ModelSerializer):
    class Meta:
        model = SubUnit
        fields = "__all__"


class SupportUnitSerializer(ModelSerializer):
    class Meta:
        model = SupportUnit
        fields = "__all__"
