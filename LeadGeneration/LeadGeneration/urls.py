"""LeadGeneration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from LeadGenerationApp import views
from LeadGenerationApp import managerview
from LeadGenerationApp import customerview
from LeadGenerationApp import Login
from LeadGenerationApp import feedback

from django.urls import re_path as url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/employeeinterface',views.EmployeeInterface),
    url(r'^api/employeesubmit',views.EmployeeSubmit),
    url(r'^api/statelist',views.State_List),
    url(r'^api/citylist', views.City_List),
    url(r'^api/employeelist', views.Employee_list),
    url(r'^api/displayallemployee', views.Displayallemployee),
    url(r'^api/employeebyid', views.Employee_list_By_Id),
    url(r'^api/employeeupdatedelete', views.Employee_update_delete),
    url(r'^api/display_employee_picture',views.Employee_display_picture),
    url(r'^api/update_employee_image',views.UpdateEmployeeImage),

    url(r'^api/managerinterface',managerview.Managerinterface),
    url(r'^api/managersubmit',managerview.ManagerSubmit),
    url(r'^api/managerstatelist', managerview.State_List),
    url(r'^api/managercitylist', managerview.City_List),
    url(r'^api/displaymanager',managerview.Manager_List),
    url(r'^api/displayallmanager',managerview.DisplayallManager),
    url(r'^api/managerbyid', managerview.Manager_List_by_id),
    url(r'^api/managerupdatedelete',managerview.Manager_update_delete),
    url(r'^api/display_manager_picture',managerview.Manager_Display_picture),
    url(r'^api/update_manager_image',managerview.UpdateManagerImage),



    url(r'^api/customerinterface', customerview.Customerinterface),
    url(r'^api/customerstatelist',customerview.State_List),
    url(r'^api/customercitylist',customerview.City_List),
    url(r'^api/Customer_Submit',customerview.Customer_submit),
    url(r'^api/displayallcustomer',customerview.Display_All_Customer),
    url(r'^api/displaycustomer',customerview.Customer_List),
    url(r'^api/customerbyid',customerview.Customer_list_by_id),




    url(r'^api/login',Login.LoginInterface),
    url(r'^api/admindashboard',Login.AdminDashBoard),
    url(r'^api/managerdashboard',Login.ManagerDashBoard),
    url(r'^api/employeedashboard',Login.EmployeeDashBoard),
    url(r'^api/checkadminlogin', Login.Check_Admin_Login),
    url(r'^api/checkmanagerlogin',Login.Check_Manager_Login),
    url(r'^api/checkemployeelogin',Login.Check_Employee_Login),
    url(r'^api/logoutadmin', Login.LogoutAdmin),
    url(r'^api/logoutmanager', Login.LogoutManager),
    url(r'^api/logoutemployee',Login.LogoutEmployee),


    url(r'^api/feedback',feedback.Feedback),
    url(r'^api/calldetailsubmit',feedback.Feedback_Submit),
    url(r'^api/callcustomerbyid',feedback.Customer_list_by_id),

]
