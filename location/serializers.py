from rest_framework import serializers
from . import models


class ProfileTypeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = models.ProfileType
        fields = '__all__'


class SiteProfileSerializer(serializers.ModelSerializer):
    uuid = serializers.ReadOnlyField()

    class Meta:
        model = models.SiteProfile
        exclude = ['id']

    def validate_profiletype(self, value):
        if (self.initial_data['organization_uuid'] !=
                str(value.organization_uuid)):
            raise serializers.ValidationError(
                'Invalid ProfileType. It should belong to your organization')
        return value
