from django.shortcuts import render
from django.db import connection
from .import tuple_to_dict
from django.shortcuts import redirect
from django.views.decorators.clickjacking import xframe_options_exempt
# Create your views here.
from  django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from LeadGenerationApp.models import manager
from LeadGenerationApp.models import Cities
from LeadGenerationApp.models import States




from LeadGenerationApp.serializers import ManagerSerializer
from LeadGenerationApp.serializers import StateSerializer
from LeadGenerationApp.serializers import CitySerializer

from rest_framework.decorators import api_view
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def Managerinterface(request):
    return render(request,"manager.html")

@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def ManagerSubmit(request):
    if request.method == 'POST':
       # manager_data = request.GET.dict()
        manager_serializer = ManagerSerializer(data=request.data)
        if manager_serializer.is_valid():
            manager_serializer.save()
            print(manager_serializer)
            return render(request,"manager.html",{"message":"Record Submitted Successfully"})

        return render(request,"manager.html",{"message":"Server error:Fail to SubmitteRecord"})

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
def Manager_List(request):
    if request.method=='GET':
        Manager_List=manager.objects.all()
        manager_serializer=ManagerSerializer(Manager_List,many=True)
        return JsonResponse(manager_serializer.data,safe=False)
    return JsonResponse({},safe=False)
'''
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def Manager_List(request):
    if request.method=='GET':
        cursor=connection.cursor()
        q="select m.*,(select s.statename from leadgenerationapp_states s where s.stateid=m.state) as statename,(select c.cityname from leadgenerationapp_cities c where c.cityid=m.city) as cityname from leadgenerationapp_manager m"
        cursor.execute(q)
        employeerecords=cursor.fetchall()

        description=cursor.description
        columnnames=[]
        for des in description:
            columnnames.append(des[0])
        data=[]
        for row in employeerecords:
            data.append(dict(zip(columnnames,list(row))))

        return JsonResponse(data, safe=False)
    return JsonResponse({}, safe=False)
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def Manager_List_by_id(request):
    if request.method=='GET':
        managerid=request.GET['managerid']

        cursor=connection.cursor()
        q="select m.*,(select s.statename from leadgenerationapp_states s where s.stateid=m.state) as statename,(select c.cityname from leadgenerationapp_cities c where c.cityid=m.city) as cityname from leadgenerationapp_manager m where m.id={0}".format(managerid)
        cursor.execute(q)
        data=tuple_to_dict.ParseToOne(cursor)
        data['dob']=str(data['dob'])
        if(data['gender']=='Male'):mg=True
        else:mg=False
        if(data['gender']=='Female'):fg=True
        else:fg=False

        return render(request,"managerById.html",{'record':data,'mgender':mg,'fgender':fg})
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def Manager_update_delete(request):
    if request.method=='GET':
        btn=request.GET['btn']
        if(btn=='Edit'):
            Manager= manager.objects.get(pk=request.GET['id'])
            Manager.managerid=request.GET['managerid']
            Manager.managername=request.GET['managername']
            Manager.dob=request.GET['dob']
            Manager.gender=request.GET['gender']
            Manager.addres=request.GET['address']
            Manager.city=request.GET['city']
            Manager.state=request.GET['state']
            Manager.emailid=request.GET['emailid']
            Manager.mobileno=request.GET['mobileno']
            Manager.save()
        else:
            Manager=manager.objects.get(pk=request.GET['id'])
            Manager.delete()
    return redirect('/api/displayallmanager')
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def Manager_Display_picture(request):
    if request.method=='GET':
        return render(request,"ManagerPicture.html",{'id':request.GET['mid'],"managername":request.GET['managername'],"picture":request.GET['picture']})
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def UpdateManagerImage(request):
    if request.method=='POST':
        Manager=manager.objects.get(pk=request.POST['id'])
        Manager.photograph=request.FILES['photograph']
        Manager.save()
    return redirect('/api/displayallmanager')



@xframe_options_exempt
def DisplayallManager(request):
    return render(request,"displayallmanager.html")