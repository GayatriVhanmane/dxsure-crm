from django.shortcuts import render, redirect, get_object_or_404
from .models import Client,Employee
from .forms import ClientForm, EmployeeForm
from django.db.models import Sum

def dashboard(request):
    # 1.Fetch counts from the database
    client_count = Client.objects.count()
    employee_count = Employee.objects.count()
    
    # 2. Calculate Totals (If there are no records, default to 0 to avoid errors)
    total_revenue = Client.objects.aggregate(Sum('revenue'))['revenue__sum'] or 0
    total_salary = Employee.objects.aggregate(Sum('salary'))['salary__sum'] or 0
    
    # 3. Calculate Profit or Loss
    profit_or_loss = total_revenue - total_salary

    context = {
        'client_count': client_count,
        'employee_count': employee_count,
        'total_revenue': total_revenue,
        'total_salary': total_salary,
        'profit_or_loss': profit_or_loss,
    }
    return render(request, 'crm_core/dashboard.html', context)

def client_list(request):
    clients = Client.objects.all() # Fetch all clients from MySQL
    return render(request, 'crm_core/client_list.html', {'clients': clients})

def add_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save() # Saves directly to your XAMPP MySQL
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'crm_core/add_client.html', {'form': form})

# 4. Edit Client View
def edit_client(request, pk):
    client = get_object_or_404(Client, pk=pk) # Fetch the specific client
    if request.method == "POST":
        # Pass the existing client 'instance' to the form so it knows what to update
        form = ClientForm(request.POST, instance=client) 
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client) # Pre-fill the form with existing data
        
    return render(request, 'crm_core/edit_client.html', {'form': form, 'client': client})

# 5. Delete Client View
def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        client.delete() # Removes it permanently from XAMPP MySQL
        return redirect('client_list')
    return render(request, 'crm_core/delete_client.html', {'client': client})

# List Employees
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'crm_core/employee_list.html', {'employees': employees})

# Add Employee
def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
        else:
            # THIS IS THE NEW LINE: It will print the exact reason to your terminal
            print("FORM ERRORS:", form.errors)
    else:
        form = EmployeeForm()
    return render(request, 'crm_core/add_employee.html', {'form': form})

# Edit Employee View
def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'crm_core/edit_employee.html', {'form': form, 'employee': employee})

# Delete Employee View
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('employee_list')
    return render(request, 'crm_core/delete_employee.html', {'employee': employee})