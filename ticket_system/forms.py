from django import forms
from django.conf import settings
from django.core.mail import send_mail

from .models import Agent
from django.core.validators import EmailValidator

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['email', 'mobile', 'firstname', 'lastname', 'role', 'profile_pic', 'status']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Add custom email validation logic if needed
        if not EmailValidator()(email):
            raise forms.ValidationError("Invalid email format")
        return email

def send_email(receiver_email, username, password):
    subject = "Credentials for Agent/Subadmin"
    message = f"Dear Agent/Subadmin,\n\nYour username is: {username}\nYour password is: {password}\n\nPlease keep this information secure."
    sender_email = settings.EMAIL_HOST_USER

    send_mail(subject, message, sender_email, [receiver_email])





from django import forms
from .models import Users, TicketItem
from django.utils.timezone import now

class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['email', 'mobile', 'firstname', 'lastname', 'role', 'profile_pic', 'status']


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100, required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)


class TicketForm(forms.ModelForm):
    class Meta:
        model = TicketItem
        fields = ['user', 'assets', 'priority', 'serial_no', 'model_no', 'ticket_status']



class TicketFilterForm(forms.Form):
    STATUS_CHOICES = [
        ('', 'All'),  # Adding an empty option to select all statuses
        ('Open', 'Open'),
        ('Closed', 'Closed'),
        ('Pending', 'Pending'),
        # Add more status options if needed
    ]
    PRIORITY_CHOICES = [
        ('', 'All'),  # Adding an empty option to select all priorities
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        # Add more priority options if needed
    ]

    start_date = forms.DateTimeField(label='Start Date', initial=now().replace(hour=0, minute=0, second=0, microsecond=0))
    end_date = forms.DateTimeField(label='End Date', initial=now().replace(hour=23, minute=59, second=59, microsecond=999))
    status = forms.ChoiceField(choices=STATUS_CHOICES, label='Status', required=False)
    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, label='Priority', required=False)
