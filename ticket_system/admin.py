from django.contrib import admin
# from django.contrib.admin import AdminSite

from .models import Agent

class AgentAdmin(admin.ModelAdmin):
    list_display = ('email', 'firstname', 'lastname', 'mobile', 'role', 'status')
    list_filter = ('role', 'status')
    search_fields = ('email', 'firstname', 'lastname', 'mobile')

admin.site.register(Agent, AgentAdmin)




from django.contrib import admin


from .models import Users, TicketItem, Issue, Tickets


# Register your models here.

@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'mobile', 'firstname', 'lastname', 'role', 'status')
    list_filter = ('role', 'status')
    search_fields = ('email', 'mobile', 'firstname', 'lastname')
    # Add more customization as needed


class TicketAdmin(admin.ModelAdmin):
    list_display = ('user', 'assets', 'priority', 'serial_no', 'model_no', 'ticket_status')
    list_filter = ('priority', 'ticket_status')
    search_fields = ('user__username', 'user__email', 'assets', 'serial_no', 'model_no')


admin.site.register(TicketItem, TicketAdmin)


class CustomIssueAdmin(admin.ModelAdmin):
    list_display = ('ticket_status', 'priority', 'created_at')
    list_filter = ('ticket_status', 'priority')
    search_fields = ('ticket_status', 'priority')  # Add any other fields you want to search by

admin.site.register(Issue, CustomIssueAdmin)


admin.site.register(Tickets)


# class MyAdminSite(AdminSite):
#     site_header = 'Asset Tracker System Admin'  # Set your custom admin name here
#
#
# # Instantiate your custom admin site
# admin_site = MyAdminSite(name='myadmin')
#
#
#
#
#
# admin_site.register(Asset, AssetAdmin)