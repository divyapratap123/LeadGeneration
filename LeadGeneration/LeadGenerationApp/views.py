from django.shortcuts import render
from django.db import connection
from .import tuple_to_dict
from django.shortcuts import redirect
from django.views.decorators.clickjacking import xframe_options_exempt


# Create your views here.
from  django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from LeadGenerationApp.models import Employee
from LeadGenerationApp.models import Cities
from LeadGenerationApp.models import States


from LeadGenerationApp.serializers import EmployeeSerializer
from LeadGenerationApp.serializers import StateSerializer
from LeadGenerationApp.serializers import CitySerializer
from LeadGenerationApp.serializers import ManagerSerializer


from rest_framework.decorators import api_view
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def EmployeeInterface(request):
    return render(request,"employee.html")
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def EmployeeSubmit(request):
    if request.method == 'POST':
       # employee_data = request.GET.dict()
        employee_serializer = EmployeeSerializer(data=request.data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return render(request, "employee.html",{"message":"Record Submitted Successfully"})

        return render(request,"employee.html",{"message":"Server error:Fail to SubmitteRecord"})

@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def State_List(request):
    if request.method=='GET':
        State_List=States.objects.all()
        State_Serializer=StateSerializer(State_List,many=True)
        return JsonResponse(State_Serializer.data,safe=False)
    return JsonResponse({},safe=False)
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def City_List(request):
    if request.method=='GET':
        City_List=States.objects.raw('select * from leadgenerationapp_cities where stateid={0}'.format(request.GET['stateid']))
        City_Serializer=CitySerializer(City_List,many=True)
        return JsonResponse(City_Serializer.data,safe=False)
    return JsonResponse({},safe=False)
'''
@api_view(['GET','POST','DELETE'])
def Employee_list(request):
    if request.method=='GET':

        employee_list=Employee.objects.all()
        employee_serializer=EmployeeSerializer(employee_list,many=True)

        return JsonResponse(employee_serializer.data,safe=False)
    return JsonResponse({},safe=False)
'''
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def Employee_list(request):
    if request.method=='GET':
        cursor=connection.cursor()
        q="select e.*,(select s.statename from leadgenerationapp_states s where s.stateid=e.state) as statename,(select c.cityname from leadgenerationapp_cities c where c.cityid=e.city) as cityname,(select m.managername from leadgenerationapp_manager m where m.id=e.managerid) as managername from leadgenerationapp_employee e"
        cursor.execute(q)
        data=tuple_to_dict.ParseToDict(cursor)

        return JsonResponse(data, safe=False)
    return JsonResponse({}, safe=False)
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def Employee_list_By_Id(request):
    if request.method=='GET':
        employeeid=request.GET['employeeid']
        cursor=connection.cursor()
        q="select e.*,(select s.statename from leadgenerationapp_states s where s.stateid=e.state) as statename,(select c.cityname from leadgenerationapp_cities c where c.cityid=e.city) as cityname,(select m.managername from leadgenerationapp_manager m where m.id=e.managerid) as managername from leadgenerationapp_employee e where e.id={0}".format(employeeid)
        cursor.execute(q)
        data=tuple_to_dict.ParseToOne(cursor)
        data['dob']=str(data['dob'])
        if(data['gender']=='Male'):mg=True
        else:mg=False
        if(data['gender']=='Female'):fg=True
        else:fg=False
        return render(request, "employeeById.html",{"record":data ,'mgender':mg,'fgender':fg})

    return JsonResponse({}, safe=False)
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def Employee_update_delete(request):
    if request.method=='GET':
        btn=request.GET['btn']
        if(btn=='Edit'):
            employee=Employee.objects.get(pk=request.GET['id'])
            employee.firstname=request.GET['firstname']
            employee.lastname=request.GET['lastname']
            employee.dob=request.GET['dob']
            employee.gender=request.GET['gender']
            employee.emailid=request.GET['emailid']
            employee.address=request.GET['address']
            employee.state=request.GET['state']
            employee.city=request.GET['city']
            employee.designation=request.GET['designation']
            employee.managerid=request.GET['managerid']
            employee.save()
        else:
            employee=Employee.objects.get(pk=request.GET['id'])
            employee.delete()
    return redirect('/api/displayallemployee')
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def Employee_display_picture(request):
    if request.method=='GET':
        return render(request,'EmployeePicture.html',{'id':request.GET['employeeid'],"employeename":request.GET['employeename'],"picture":request.GET['picture']})
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def UpdateEmployeeImage(request):
    if request.method=='POST':
        employee=Employee.objects.get(pk=request.POST['id'])
        employee.photograph=request.FILES['photograph']
        employee.save()
    return redirect('/api/displayallemployee')


@xframe_options_exempt
def Displayallemployee(request):
    return render(request,"displayallemployee.html")



