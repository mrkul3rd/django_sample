import os
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader
from django.contrib import messages
from .models import Project, Employee
from . import django_csv
from .forms import ProjectForm, EmployeeForm

# Create your views here.
def index(request):
    # reload_projects()
    # reload_employees()
    project_list = Project.objects.order_by('id')
    context = {
        'project_list': project_list,
    }
    return render(request, 'projects_management/index.html', context)

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    employees = Employee.objects.filter(project_id=project_id)
    other_employees = Employee.objects.exclude(project_id=project_id)

    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        # Save the new project to the database
        form.save(commit=True)
        messages.success(request, 'Project detail updated.')

        # Now call the index() view
        # return index(request)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        # The supplied form contained errors - just print them to the terminal
        print form.errors

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'projects_management/detail.html', {'form': form, 'project': project, 'employees': employees, 'other_employees': other_employees,})

def new_project(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = ProjectForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new project to the database
            form.save(commit=True)

            # Now call the index() view
            return HttpResponseRedirect(reverse('index'))
        else:
            # The supplied form contained errors - just print them to the terminal
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = ProjectForm

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'projects_management/new.html', {'form': form})

def delete_project(request, project_id):
    prj = Project.objects.get(id=project_id)
    prj.delete()
    return HttpResponseRedirect(reverse('index'))

def all_employee(request):
    employee_list = Employee.objects.order_by('id')
    context = {
        'employee_list': employee_list,
    }
    return render(request, 'projects_management/all_emp.html', context)

def new_employee(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            # return all_employee(request)
            return HttpResponseRedirect(reverse('all_employee'))
        else:
            print form.errors
    else:
        form = EmployeeForm

    return render(request, 'projects_management/new_emp.html', {'form': form})

def delete_employee(request, employee_id):
    emp = Employee.objects.get(id=employee_id)
    emp.delete()
    return HttpResponseRedirect(reverse('all_employee'))

def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        # Save the new employee to the database
        form.save(commit=True)
        messages.success(request, 'Employee detail updated.')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print form.errors

    return render(request, 'projects_management/emp_detail.html', {'form': form, 'employee': employee,})

def add_emps_to_project(request, project_id):
    employee_ids = request.GET.getlist('employee_ids[]')
    project = get_object_or_404(Project, id=project_id)

    if employee_ids:
        employees = Employee.objects.filter(id__in=employee_ids).update(project=project)

    emps_in_project = Employee.objects.filter(project_id=project_id)
    other_employees = Employee.objects.exclude(project_id=project_id)

    return render(request, 'projects_management/emps_in_project.html', {'project': project, 'employees': emps_in_project, 'other_employees': other_employees,})

def reload_projects():
    file_path = os.path.join(os.path.dirname(__file__), 'datas/projects.csv')
    csv_utils = django_csv.CSVUtilities(file_path)
    count = csv_utils.read_csv_into_model(Project, 
        {'id': 0, 'project_name': 1}
    )
    print '{} records imported.'.format(count)

def reload_employees():
    file_path_emp = os.path.join(os.path.dirname(__file__), 'datas/employees.csv')
    csv_utils_emp = django_csv.CSVUtilities(file_path_emp)
    csv_utils_emp.read_csv_into_model(Employee, 
        {'id': 0, 'emp_name': 1, 'project_id': 2}
    )

def delete_all_projects(request):
    Project.objects.all().delete()
    return HttpResponse('Delete all project successfully.')
