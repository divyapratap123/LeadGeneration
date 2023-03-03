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
from django.views.decorators.clickjacking import xframe_options_exempt


from rest_framework.decorators import api_view
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def Feedback(request):
    return render(request,"feedback.html",{})
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def Feedback_Submit(request):

    if request.method=='POST':
       # employee_data = request.GET.dict()
        feedback_serializer=FeedbackSerializer(data=request.data)
        print(feedback_serializer)
        if feedback_serializer.is_valid():
           feedback_serializer.save()

           return render(request,"feedback.html",{"message":"Record Submitted Successfully"})

        return render(request,"feedback.html",{"message":"Server error:Fail to Submit Record"})
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
    keys=list(request.session.keys())
    user={'caller':keys[0]}
    if("ADMIN" in keys):
        user['id']=request.session['ADMIN'][0]["id"]
        user['name']=request.session['ADMIN'][0]['adminname']
    elif("MANAGER" in keys):
        user['id'] = request.session['MANAGER'][0]["id"]
        user['name'] = request.session['MANAGER'][0]['firstname']+""+ request.session['MANAGER'][0]['lastname']
    elif ("EMPLOYEE" in keys):
        user['id'] = request.session['EMPLOYEE'][0]["id"]
        user['name'] = request.session['EMPLOYEE'][0]['firstname']+""+request.session['EMPLOYEE'][0]['lastname']
    return render(request, "feedback.html", {"record": data,'user':user})
  return JsonResponse({}, safe=False)
