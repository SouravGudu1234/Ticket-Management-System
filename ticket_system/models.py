from django.core.mail import send_mail
from django.db import models, IntegrityError
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.models import User as DjangoUser



class Agent(models.Model):
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    ROLE_CHOICES = (
        ('Agent', 'Agent'),
        ('Subadmin', 'Subadmin'),

    )
    role = models.CharField(max_length=8, choices=ROLE_CHOICES)
    profile_pic = models.ImageField(upload_to='profile_pic', max_length=100, null=True, blank=True)
    status = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # If object is being created for the first time
            password = None
            if self.role == 'Agent' or self.role == 'Subadmin':
                password = self.firstname.lower() + '@1234'  # Password format for agents/subadmins
            elif self.role == 'User':
                password = 'User@1234'  # Constant password for users
            if password:
                try:
                    # Create a corresponding User object with the generated password
                    user = DjangoUser.objects.create_user(username=self.email, email=self.email, password=password)
                except IntegrityError:
                    # Handle IntegrityError (email address already exists)
                    raise IntegrityError("An account with this email already exists.")

                # Send email to the agent/subadmin
                subject = 'Your Account Details'
                context = {'username': self.email, 'password': password}
                html_message = render_to_string('email_template.html', context)
                plain_message = strip_tags(html_message)
                from_email = 'souravsahuoffical@gmail.com'  # Change this to your email address
                to_email = self.email
                send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)
        super().save(*args, **kwargs)


class Ticket(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    closed_at = models.DateTimeField(null=True, blank=True)




from django.db import models

class Users(models.Model):
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    ROLE_CHOICES = (
        ('User', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    profile_pic = models.ImageField(upload_to='profile_pics', max_length=255)
    status = models.BooleanField(default=True)


class TicketItem(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Emergency', 'Emergency'),
    ]
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Ready to Dispatch', 'Ready to Dispatch'),
        ('Dispatched', 'Dispatched'),
        ('Closed', 'Closed'),
    ]
    ASSETS_CHOICES = [
        ('Dekstop', 'Dekstop'),
        ('Keyboard', 'Keyboard'),
        ('Mouse', 'Mouse'),
        ('CPU', 'CPU'),
        # Add more choices as needed
    ]

    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)
    assets = models.CharField(max_length=50, choices=ASSETS_CHOICES)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    serial_no = models.CharField(max_length=15)
    model_no = models.CharField(max_length=15)
    ticket_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    closed_at = models.DateTimeField(null=True, blank=True)



class Issue(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Ready to Dispatch', 'Ready to Dispatch'),
        ('Dispatched', 'Dispatched'),
        ('Closed', 'Closed'),
    ]
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Emergency', 'Emergency'),
    ]
    ticket_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)



class Tickets(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('Open', 'Open'), ('Closed', 'Closed'), ('Pending', 'Pending')])
    assigned_agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
