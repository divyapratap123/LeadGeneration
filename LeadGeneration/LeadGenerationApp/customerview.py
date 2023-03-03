from django.shortcuts import render
from django.http.response import JsonResponse
from django.db import connection
from .import tuple_to_dict
from django.views.decorators.clickjacking import xframe_options_exempt



from LeadGenerationApp.models import Cities
from LeadGenerationApp.models import States
from LeadGenerationApp.models import customer

from LeadGenerationApp.serializers import StateSerializer
from LeadGenerationApp.serializers import CitySerializer
from LeadGenerationApp.serializers import customerSerializer
from rest_framework.decorators import api_view
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def Customerinterface(request):
    return render(request,"customer.html")
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def State_List(request):
    if request.method=='GET':
        State_list=States.objects.all()
        State_Serializer=StateSerializer(State_list,many=True)
        return JsonResponse(State_Serializer.data,safe=False)
    return JsonResponse({},safe=False)
@xframe_options_exempt
def City_List(request):
    if request.method=='GET':
        City_List=Cities.objects.raw('select * from leadgenerationapp_cities where stateid={0}'.format(request.GET['stateid']))
        City_Searializer=CitySerializer(City_List,many=True)
        return JsonResponse(City_Searializer.data,safe=False)
    return JsonResponse({},safe=False)
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def Customer_submit(request):
    if request.method=='POST':
        customer_serializer=customerSerializer(data=request.data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return render(request,'customer.html',{'message':'Record Submitted Successfully'})
        return render(request,"customer.html",{'message':"Server Error : Fail to Submit Record"})

@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def Display_All_Customer(request):
    return render(request,'displayallcustomer.html')
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def Customer_List(request):
    if request.method=='GET':
        cursor=connection.cursor()
        q="select c.*,(select s.statename from leadgenerationapp_states s where s.stateid=c.state)as statename,(select a.cityname  from leadgenerationapp_cities a where a.cityid=c.city) as cityname from leadgenerationapp_customer c"
        cursor.execute(q)
        data=tuple_to_dict.ParseToDict(cursor)
        print(data)
        return JsonResponse(data,safe=False)
    return JsonResponse({},safe=False)
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def Customer_list_by_id(request):
  if request.method == 'GET':
    customerid=request.GET['customerid']
    cursor=connection.cursor()
    q="select c.* ,(select s.statename from leadgenerationapp_states s where s.stateid=c.state) as statename,(select a.cityname from leadgenerationapp_cities a where a.cityid=c.city) as cityname from leadgenerationapp_customer c where c.id={0}".format(customerid)
    cursor.execute(q)
    data=tuple_to_dict.ParseToOne(cursor)
    data['dob'] = str(data['dob'])
    return render(request, "customerById.html", {"record": data})
  return JsonResponse({}, safe=False)




