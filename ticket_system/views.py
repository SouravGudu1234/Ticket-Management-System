from django.core.mail import send_mail
from django.db import IntegrityError
from django.db.models.functions import datetime
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from .forms import AgentForm, UserForm, LoginForm, TicketForm
from .models import TicketItem, Agent, Tickets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .utils import create_user_with_password  # Assuming you have this utility function


from django.core.mail import send_mail
from django.conf import settings

def send_email(receiver_email, username, password):
    subject = "Credentials for Agent/Subadmin"
    message = f"Dear Agent/Subadmin,\n\nYour username is: {username}\nYour password is: {password}\n\nPlease keep this information secure."
    sender_email = settings.EMAIL_HOST_USER

    send_mail(subject, message, sender_email, [receiver_email])


def create_agent(request):
    if request.method == 'POST':
        form = AgentForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                agent = form.save()

                username = agent.email
                agent_password = "password123"  # Use your preferred method to generate a password
                create_user_with_password(username, agent.email, agent.firstname)

                send_email(agent.email, username, agent_password)

                return redirect('agent_created')
            except IntegrityError:
                error_message = "An account with this email already exists."
                return render(request, 'create_agent.html', {'form': form, 'error_message': error_message})
    else:
        form = AgentForm()
    return render(request, 'create_agent.html', {'form': form})


def agent_created(request):
    return render(request, 'agent_created.html')


def index(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                error_message = "Invalid email or password. Please try again."
                return render(request, 'login.html', {'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


class LoginView(View):
    @method_decorator(csrf_protect)
    def get(self, request):
        return render(request, 'login.html')

    @method_decorator(csrf_protect)
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        elif username == "Admin" and password == "Kusha@1234":
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
        messages.error(request, 'Invalid username or password.')
        return render(request, 'login.html')



def dashboard_view(request):
    today = datetime.now().date()
    one_week_ago = today - timedelta(days=7)

    active_tickets_count = TicketItem.objects.filter(created_at__gte=one_week_ago).count()
    resolved_tickets_count = TicketItem.objects.filter(resolved_at__gte=one_week_ago).count()
    closed_tickets_count = TicketItem.objects.filter(closed_at__gte=one_week_ago).count()
    active_agents_count = Agent.objects.count()

    context = {
        'active_tickets_count': active_tickets_count,
        'resolved_tickets_count': resolved_tickets_count,
        'closed_tickets_count': closed_tickets_count,
        'active_agents_count': active_agents_count,
    }

    return render(request, 'dashboard.html', context)


def email_template(request):
    context = {
        'username': 'example_user',
        'password': 'example_password'
    }
    return render(request, 'email_template.html', context)


def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            return redirect('registration_success')
    else:
        form = UserForm()
    return render(request, 'register_user.html', {'form': form})


def registration_success(request):
    return render(request, 'registration_success.html')


def ticket_form(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket_success')
    else:
        form = TicketForm()
    return render(request, 'ticket_form.html', {'form': form})


def get_mobile(request):
    user = request.GET.get('user')
    mobile = '7008878869'  # Example mobile number
    data = {'mobile': mobile}
    return JsonResponse(data)


def ticket_reports(request):
    if request.method == 'POST':
        startdate_str = request.POST.get('startdate')
        enddate_str = request.POST.get('enddate')
        ticketstatus = request.POST.get('ticketstatus')
        priority = request.POST.get('priority')

        tickets = Tickets.objects.all()

        if startdate_str:
            startdate = datetime.strptime(startdate_str, '%Y-%m-%d')
            tickets = tickets.filter(created_at__gte=startdate)
        if enddate_str:
            enddate = datetime.strptime(enddate_str, '%Y-%m-%d')
            tickets = tickets.filter(created_at__lte=enddate)
        if ticketstatus:
            tickets = tickets.filter(ticket_status=ticketstatus)
        if priority:
            tickets = tickets.filter(priority=priority)
    else:
        tickets = Tickets.objects.all()

    return render(request, 'ticket_reports.html', {'tickets': tickets})


@login_required
def ticket_listing(request):
    if request.user.is_authenticated:
        user = request.user
        tickets = Tickets.objects.filter(assigned_agent=user)
    return render(request, 'ticket_listing.html', {'tickets': tickets})


def update_ticket_status(request, ticket_id):
    ticket = get_object_or_404(Tickets, pk=ticket_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')
        ticket.status = new_status
        ticket.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})


def ticket_success(request):
    return render(request, 'ticket_form.html')
