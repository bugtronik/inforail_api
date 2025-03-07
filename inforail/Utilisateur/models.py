from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthUsers(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50)  # Field name made lowercase.
    createdutc = models.DateTimeField(db_column='CreatedUtc')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifiedutc = models.DateTimeField(db_column='ModifiedUtc', blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.
    username = models.CharField(db_column='UserName', unique=True, max_length=255)  # Field name made lowercase.
    profileid = models.ForeignKey('AuthProfiles', models.DO_NOTHING, db_column='ProfileId', blank=True, null=True)  # Field name made lowercase.
    lastlogonutc = models.DateTimeField(db_column='LastLogonUtc', blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auth_users'


class AuthProfiles(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50)  # Field name made lowercase.
    createdutc = models.DateTimeField(db_column='CreatedUtc')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=50, blank=True, null=True)  # Field name made lowercase.
    modifiedutc = models.DateTimeField(db_column='ModifiedUtc', blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auth_profiles'
        
    def __str__(self)-> str:
        return self.name
