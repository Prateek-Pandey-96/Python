from django.shortcuts import render, redirect
from .models import *

def employee(request):
    if request.method == "POST":
        name = request.POST['name']
        designation = request.POST['designation']
        address = request.POST['address']
        
        Employee.objects.create(
            name = name,
            designation = designation,
            address = address
        )
        return redirect("/employee")
    queryset = Employee.objects.all()
    context = {'employees': queryset}
    return render(request, "employee.html", context)

def delete_employee(request, id):
    queryset = Employee.objects.get(id = id)
    queryset.delete()
    return redirect("/employee")

def update_employee(request, id):
    employee = Employee.objects.get(id=id)
    if(request.method == "POST"):
        employee.name = request.POST['name']
        employee.designation = request.POST['designation']
        employee.address = request.POST['address']

        employee.save()
        return redirect("/employee")
    context = {'employee': employee}
    return render(request, "update_employee.html", context)