from django.shortcuts import render
from django.db import connection
from .import tuple_to_dict
from django.shortcuts import redirect
from .import tuple_to_dict
from  django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from LeadGenerationApp.models import feedback
from LeadGenerationApp.serializers import FeedbackSerializer

from rest_framework.decorators import api_view
@api_view(['GET','POST','DELETE'])
def LoginInterface(request):
    return render(request,"Login.html")
def AdminDashBoard(request):
    try:
     admin=request.session['ADMIN']
     return render(request,"AdminDashboard.html",{"admin":admin})
    except:
        return render(request,"Login.html",{})
def ManagerDashBoard(request):
    try:
     manager=request.session['MANAGER']

     return render(request,'ManagerDashboard.html',{"manager":manager})
    except:
        return render(request,"Login.html")
def EmployeeDashBoard(request):
    try:
        employee= request.session['EMPLOYEE']

        return render(request, 'EmployeeDashboard.html', {"employee": employee})
    except:
        return render(request, "Login.html")
@api_view(['GET','POST','DELETE'])
def Check_Admin_Login(request):
    if request.method=='GET':
       cursor=connection.cursor()
       q="select * from leadgenerationapp_administrator where mobileno='{0}' and password='{1}'".format(request.GET['mobileno'],request.GET['password'])
       cursor.execute(q)
       data=tuple_to_dict.ParseToDict(cursor)
       if(len(data)==1):
        request.session['ADMIN']=data

        return JsonResponse({"data":data,"status":True},safe=False)
       else:
           return JsonResponse({"data":{}, "status": False}, safe=False)

    return JsonResponse({},safe=False)
@api_view(['GET','POST','DELETE'])
def Check_Manager_Login(request):
    if request.method=='GET':
       cursor=connection.cursor()
       q="select * from leadgenerationapp_manager where mobileno='{0}' and password='{1}'".format(request.GET['mobileno'],request.GET['password'])
       cursor.execute(q)
       data=tuple_to_dict.ParseToDict(cursor)
       for i in data:
           i['dob']=str(i['dob'])
       if(len(data)==1):

        request.session['MANAGER']=data
        print( request.session['MANAGER'])
        return JsonResponse({"data":data,"status":True},safe=False)
       else:
           return JsonResponse({"data":{}, "status": False}, safe=False)

    return JsonResponse({},safe=False)
@api_view(['GET','POST','DELETE'])
def Check_Employee_Login(request):
    if request.method=='GET':
       cursor=connection.cursor()
       q="select * from leadgenerationapp_employee where mobileno='{0}' and password='{1}'".format(request.GET['mobileno'],request.GET['password'])
       cursor.execute(q)
       data=tuple_to_dict.ParseToDict(cursor)
       for i in data:
           i['dob']=str(i['dob'])
       if(len(data)==1):
        request.session['EMPLOYEE']=data
        return JsonResponse({"data":data,"status":True},safe=False)
       else:
           return JsonResponse({"data":{}, "status": False}, safe=False)

    return JsonResponse({},safe=False)
@api_view(['GET','POST','DELETE'])
def LogoutAdmin(request):
    del request.session["ADMIN"]
    return render(request,"Login.html")
@api_view(['GET','POST','DELETE'])
def LogoutManager(request):
    del request.session["MANAGER"]
    return render(request,"Login.html")
@api_view(['GET','POST','DELETE'])
def LogoutEmployee(request):
    del request.session["EMPLOYEE"]
    return render(request,"Login.html")



