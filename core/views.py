from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .forms import ClientForm, ProgramForm
from .models import Client, Enrollment, Program
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ClientSerializer
from rest_framework.permissions import IsAuthenticated


# Register view for authentication
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


# Home view (requires login)
@login_required
def home(request):
    return render(request, 'home.html')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        messages.success(self.request, 'You have successfully logged in.')
        return super().form_valid(form)

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')

# Registering a new client
@login_required
def register_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client registered successfully!')
            return redirect('client_list')
    else:
        form = ClientForm()

    return render(request, 'register_client.html', {'form': form})

# Viewing the client list
@login_required
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

# Viewing the client's profile through a primary key
@login_required
def client_profile(request, pk):
    client = Client.objects.get(pk=pk)
    enrolled_programs = Enrollment.objects.filter(client=client)
    return render(request, 'client_profile.html', {
        'client': client,
        'enrolled_programs': enrolled_programs
    })

# Edit Client
@login_required
def edit_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client updated successfully!')
            return redirect('client_profile', pk=client.pk)
    else:
        form = ClientForm(instance=client)
    return render(request, 'edit_client.html', {'form': form})


# Delete Client
@login_required
def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return redirect('client_profile', pk=pk)

# Enroll a Client into a program
@login_required
def enroll_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    all_programs = Program.objects.all()
    enrolled_programs = client.enrollments.values_list('program_id', flat=True)
    available_programs = all_programs.exclude(id__in=enrolled_programs)

    if not available_programs.exists():
        messages.info(request, "This client is already enrolled in all available programs.")
        return redirect('client_profile', pk=pk)

    if request.method == 'POST':
        program_id = request.POST.get('program')
        program = get_object_or_404(Program, id=program_id)
        Enrollment.objects.create(client=client, program=program)
        messages.success(request, f"Client enrolled in {program.name} successfully!")
        return redirect('client_profile', pk=pk)

    return render(request, 'enroll_client.html', {
        'client': client,
        'available_programs': available_programs
    })

# View to handle program creation
@login_required
def create_program(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Program created successfully!')
            return redirect('program_list')  # Redirect to program list after creation
    else:
        form = ProgramForm()
    return render(request, 'create_program.html', {'form': form})

# View to display all programs
@login_required
def program_list(request):
    programs = Program.objects.all()
    return render(request, 'program_list.html', {'programs': programs})

# Edit Program View
def edit_program(request, pk):
    program = get_object_or_404(Program, pk=pk)

    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            messages.success(request, 'Program updated successfully!')
            return redirect('program_list')
    else:
        form = ProgramForm(instance=program)

    return render(request, 'edit_program.html', {'form': form, 'program': program})

# Delete Program View
def delete_program(request, pk):
    program = get_object_or_404(Program, pk=pk)

    if request.method == 'POST':
        program.delete()
        messages.success(request, 'Program deleted successfully!')
        return redirect('program_list')

    return render(request, 'confirm_delete_program.html', {'program': program})

# API View
class ClientProfileAPIView(APIView):

    def get(self, request, pk, format=None):
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return Response({"detail": "Client not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ClientSerializer(client)
        return Response(serializer.data)






