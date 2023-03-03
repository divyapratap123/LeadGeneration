from rest_framework import serializers
from LeadGenerationApp.models import Employee
from LeadGenerationApp.models import States
from LeadGenerationApp.models import Cities
from LeadGenerationApp.models import manager
from LeadGenerationApp.models import customer
from LeadGenerationApp.models import administrator
from LeadGenerationApp.models import feedback



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'firstname','lastname', 'dob', 'gender', 'emailid', 'mobileno', 'address', 'state', 'city', 'designation', 'managerid', 'photograph','password')
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = ('id', 'stateid','statename')
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ('id', 'stateid','cityid','cityname')
class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model =manager
        fields = ('id','managerid','managername','dob','gender','address','state','city','mobileno','emailid','password','photograph')
class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model= customer
        fields=('id','firstname','lastname','dob','emailid','address','alternateno','orgname','state','city','mobileno','emailid','photograph')
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model= administrator
        fields=('id','mobileno','adminname','password')
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model= feedback
        fields=('id','customerid','customername','callerid','status','callername','currentdate','phonestatus','conversation','leadstatus')
