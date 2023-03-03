from django.db import models

# Create your models here.
class Employee(models.Model):
    firstname = models.CharField(max_length=45, blank=False, default='')
    lastname= models.CharField(max_length=45,blank=False, default='')
    dob= models.DateField(blank=False, default='')
    gender=models.CharField(max_length=6,blank=False, default='')
    emailid=models.CharField(max_length=45,blank=False, default='')
    mobileno=models.CharField(max_length=12,blank=False, default='')
    address=models.CharField(max_length=200,blank=False, default='')
    state=models.CharField(max_length=45,blank=False, default='')
    city=models.CharField(max_length=45,blank=False, default='')
    designation=models.CharField(max_length=45,blank=False, default='')
    managerid=models.IntegerField(blank=False)
    photograph=models.ImageField(upload_to='static/')
    password = models.CharField(max_length=45, blank=False, default='')
class States(models.Model):
    stateid=models.IntegerField(blank=False)
    statename=models.CharField(max_length=45,blank=False,default='')
class Cities(models.Model):
    stateid=models.IntegerField(blank=False)
    cityid=models.IntegerField(blank=False)
    cityname=models.CharField(max_length=45,blank=False,default='')
class manager(models.Model):
    managerid=models.IntegerField(blank=False)
    managername=models.CharField(max_length=45,blank=False,default='')
    dob=models.DateField(blank=False, default='')
    gender=models.CharField(max_length=6,blank=False, default='')
    address=models.CharField(max_length=200,blank=False, default='')
    state = models.CharField(max_length=45, blank=False, default='')
    city = models.CharField(max_length=45, blank=False, default='')
    mobileno= models.CharField(max_length=12, blank=False, default='')
    emailid= models.CharField(max_length=45, blank=False, default='')
    password=models.CharField(max_length=45,blank=False,default='')
    photograph=models.ImageField(upload_to='static/')
class customer(models.Model):
    firstname=models.CharField(max_length=45,blank=False,default='')
    lastname=models.CharField(max_length=45,blank=False,default='')
    dob=models.DateField(blank=False,default='')
    emailid=models.CharField(max_length=45,blank=False,default='')
    mobileno=models.CharField(max_length=10,blank=False,default='')
    alternateno=models.CharField(max_length=45,default='',blank=False)
    orgname=models.CharField(max_length=45,blank=False,default='')
    address=models.CharField(max_length=200,blank=False,default='')
    state=models.CharField(max_length=45,blank=False,default='')
    city=models.CharField(max_length=45,blank=False,default='')
    photograph=models.ImageField(upload_to='static/')

class administrator(models.Model):
    mobileno=models.CharField(max_length=45,blank=False,default='')
    adminname=models.CharField(max_length=45,blank=False,default='')
    password=models.CharField(max_length=45,blank=False,default='')
class feedback(models.Model):
    customerid=models.CharField(max_length=15,blank=False,default='')
    customername=models.CharField(max_length=15,blank=False,default='')
    callerid=models.CharField(max_length=15,blank=False,default='')
    status=models.CharField(max_length=15,blank=False,default='')
    callername=models.CharField(max_length=15,blank=False,default='')
    currentdate=models.DateField(blank=False,default='')
    phonestatus=models.CharField(max_length=15,blank=False,default='')
    conversation=models.CharField(max_length=100,blank=False,default='')
    leadstatus=models.CharField(max_length=15,blank=False,default='')




















