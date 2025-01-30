from rest_framework import serializers
from .models import AuthUsers, AuthProfiles

class AuthUsersSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    createdutc = serializers.DateTimeField()
    modifiedby = serializers.CharField()
    active = serializers.IntegerField()
    username = serializers.CharField()
    profileid = serializers.PrimaryKeyRelatedField(queryset=AuthProfiles.objects.all())
    lastlogonutc = serializers.DateTimeField()
    
    class Meta:
        model = AuthUsers
        fields = '__all__' 
        

class AuthProfilesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    createdby = serializers.CharField(max_length=100)
    createdutc = serializers.DateTimeField()
    modifiedby = serializers.CharField(max_length=100)
    modifiedutc = serializers.DateTimeField()
    active = serializers.BooleanField()
    name = serializers.CharField(max_length=100)
    
    class Meta:
        model = AuthProfiles