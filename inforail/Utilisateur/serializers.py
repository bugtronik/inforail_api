from rest_framework import serializers
from .models import AuthUsers, AuthProfiles


class AuthProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthProfiles
        fields = ['id', 'createdby', 'createdutc', 'modifiedby', 'modifiedutc', 'active', 'name']
class AuthUsersSerializer(serializers.ModelSerializer):
    #profileid = serializers.StringRelatedField()
    profileid = AuthProfilesSerializer()
    class Meta:
        model = AuthUsers
        fields = ['id', 'createdby', 'createdutc', 'modifiedby', 'active', 'username', 'profileid', 'lastlogonutc']
        