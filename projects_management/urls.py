from django.conf.urls import url
from . import views

urlpatterns = [
    # /projects/
    url(r'^$', views.index, name='index'),
    # ex: /projects/5/
    url(r'^(?P<project_id>[0-9]+)/$', views.project_detail, name='project_detail'),
    url(r'^delete_all/$', views.delete_all_projects, name='delete_all_projects'),
    url(r'^new/$', views.new_project, name='new_project'),
    url(r'^new_employee/$', views.new_employee, name='new_employee'),
    url(r'^all_employee/$', views.all_employee, name='all_employee'),
    # ex: /projects/view_employee/5/
    url(r'^view_employee/(?P<employee_id>[0-9]+)/$', views.employee_detail, name='employee_detail'),
    url(r'^delete_project/(?P<project_id>[0-9]+)/$', views.delete_project, name='delete_project'),
    url(r'^delete_employee/(?P<employee_id>[0-9]+)/$', views.delete_employee, name='delete_employee'),
    url(r'^add_emps_to_project/(?P<project_id>[0-9]+)/$', views.add_emps_to_project, name='add_emps_to_project'),
]
