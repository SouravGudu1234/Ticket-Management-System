Introduction
TICKET MANAGEMENT SYSTEM

Description :

Ticket Management System is a support application developed for clients (computer hardware shop) wherein they raise tickets for customers(users) and resolve the issues by the respective agents and notify users about the resolution and report generation of respective sections.

There will be four roles as Admin,Subadmin,Agent and User.

1. Admin          - Responsible for creating agents and subadmin

2. Subadmin   - Responsible for creating users,tickets and assigning tickets  to agents and generating reports.

3. Agent          - Responsible for resolving the tickets of users

Modules :

•       Dashboard :

            Landing page of the application which contains all main content  that gives us an overview of the ticket status and accessible for all roles.All details on dashboard will be per day basis

•       Active tickets count (How many tickets had been generated today)

•       Resolved tickets count (How many tickets had been resolved today)

•       Closed tickets count (How many tickets had been closed today)

•       Active Agents count (How many agents are working on the tickets today)

 

 

•       Login Form:

            Admin,sub admin and agents can login to the application

            For now,User should not be able to login to the application.

            Fields Required :

1.     username          ---- (text field) ---- (required / email format)

2.     password           ---- (pwdtext field)  ---- (required / validate the pattern)

 

•       Register User  Form:

            Admin can create agents/subadmin

Subadmin can create users

            Once agent/subadmin is created,an email should be sent to the agent/subadmin with respective username and password
            Fields Required :

1.     username          ---- (text field) ----(required / email format /  )

2.     mobile                ---- (text field) ---- (required / mobile number validated)

3.     firstname            ---- (text field) ---- (required / minimum 5 characters maximum 15 charatcers) 

4.     lastname            ---- (text field) ----  (minimum 5 characters maximum 15 characters) 

5.     role                    ---- (dropdown field) ---- required (Agent/Subadmin/User)

6.     profile_pic          ---- (upload field) --- max upload size of 20kb/image format supported(jpg,png,gif)

7.     status                 ---- (toggle button) ----active/inactive --- by default should be active

8.     password should be autosaved from backend with specific condition based on roles
Password Format:
For User => User@1234(constant)

                     For Agent/Subadmin => firstnameofagent@1234 with firstletter capital

 

•       Ticket Generation Form:

            For now,users should not be allowed to generate tickets.

            All tickets coming from user will be reported to subadmin and only Subadmin can create tickets and   assign tickets to agents.

           

            Fields Required:

1.       user                 ---- (dropdown field) ---- required

2.       mobile             ---- autofilled based on user

3.       assets             ---- (text field) ---- required (ex:desktop,laptop,keyborad,etc...hardware submitted by user which has an issue)

4.       priority                         ---- (dropdown field) ---- required (Low/Medium/High/Emergency)

5.       serialNo                       ---- (text field) ---- required / minimum 5 characters maximum 15 characters 

6.       ModelNo         ---- (text field) ---- required / minimum 5 characters maximum 15 characters 

7.       ticketStatus     ---- by default on creation it should be pending (Pending/Approved/Ready to Dispatch/Dispatched/Closed)

 

•       Tickets Listing for Agents:

            Agents can view all the tickets assigned to them and then accordingly update the                         ticketStatus as per the progress.

            Can Display the required fields for listing

            Action - Update Status i.e.agent should be able to update the ticket status

 

•       Report generation for tickets generated:

            Subadmin should be able to view the ticket reports based on following filters:

            startdate          ---- (datepicker field) ---- block past dates

            enddate           ---- (datepicker field) ---- greater than startdate

            ticketstatus        ---- (dropdown field)

            priority            ---- (dropdown field)

 

Definition:

            Ticket Status:

            1.Pending -Initial state when ticket is generated

            2.Approved - If the issue is valid then agent approves the ticket

            3.Ready to Dispatch - Once the issue is resolved the product is ready to dispatch

            4.Dispatched - Once the product is delivered then dispatched

            5.Closed - Once the user acknowledges after collecting,then ticket is closed.

 

Note:

1.     All  the forms should be csrf, xss protected.

2.      The application should be developed with any bootstrap theme (preferably adminlte theme).

3.     Pep8 and should follow repository pattern

4.     Try to use models and relationships for fetching data

5.     Tables should be created using migrations only

6.     Can use seeders or custom configuration file for any dropdown rather than hardcoding ex:ticketpriority,ticketStatus

7.     Try to use datatables for pagination and sorting while listing data

8.     Need to use custom configuration file for any hardcoded values

 

Technology Specification:

            Python framework / MySQL / HTML / CSS / JavaScript / Jquery

Delivery 

Technology Stack
The Technology Stack as Follows.
Python - Backend
