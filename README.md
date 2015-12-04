Simon Fraser University CMPT 470 GROUP 12 
Scheduler Application README

TABLE OF CONTENTS		
-=================		
-1. General Function Descriptions		
-2. How to use Scheduling Application		
-3. List of Bugs		
-4. Test Usernames		
-5. Member of team

1. General Function Descriptions
--------------------------------
We have designed an application that will assist in employee managing for a general workplace. 
It features a scheduling application, messaging board, and an employee database for users to manipulate. 
Our project is running on Django 1.8.3. and Python 3.4.0.  Our user interface is implemented with Bootstrap,  
which uses a combination of JQuery, HTML, CSS and Javascript. 

Login page:
The login screen is implemented using Bootstrap. We have implemented CSRF 
tokens through Django to ensure CSRF security in our login process.

Main Page: 
The main page  features a navigation bar that display different links depending 
on whether a user is a manager or employee. It also features a mobile compact view.
The main page greets the user with a welcome message and easily accessible navigation. 
Users are able to logout as well. 

Scheduling:
Managers selects dates on interactive calendar as open for availibility to work. 
Once employees are logged in, they are able to select time slots from the dates
that managers have enabled for them. Their selection is then displayed to the manager and he/she can
select the employee they want to work that particular day and employees are now scheduled for that certain time.
The order that the employees are displayed to the manager are done so in terms of how many hours that employee has
worked in total as a recommendation to the manager to reward employees who work more. 

Messaging Board:
Any user is able to see the messaging board, as well as write a message to post on it 
for everyone to see in order to inform other employees of any issues that need to be dealt with in the business.


Employee Display/Personal Details Display:
Managers are able to see the list of employees in the database, users are able to 
see their own personal details.

Django Website Administration:
Admins are able to create and edit staff, grant or reject permissions through the built in Django admin app.


2. How to use Scheduling Application
------------------------------------
Admin View:
After logging in, you will be at the main page.
	From the Navigation Bar: 
	TO SEE PERSONAL DETAILS
		>>Select Personal Details
	TO SEE EMPLOYEE LIST AND CREATE EMPLOYEES
		>> Select All Employee Information
		>> Click Add an New Employee
		>> Complete form.
	TO OPEN DAYS FOR FOR AVAILIBILITY FOR EMPLOYEES
		>> Select open availibility
	TO ASSIGN EMPLOYEES TO SCHEDULE
		>> Select MAnage Schedule
	TO SEE WHICH EMPLOYEE IS WORKING ON A PARTICULAR DAY
		>> Select view assigned schedule
		>> Select date through drop down 
	TO SEE AND WRITE MESSAGES
		>> Select Message Board

In order to edit employee accounts, the admin must use the built in Django admin app by going to cmpt470.csil.sfu.ca/Scheduler/admin
From there, only the admin or any designated staff accounts can log in to here.

	TO ADD/EDIT USERNAMES AND PASSWORDS:
		>>Select Users
		>>Select user you want to edit or select Add
		>>Edit the appropriate fields then click one of the save options
		>>Adding staff or superuser status can be done here as well

	TO EDIT OTHER USER ACCOUNT DETAILS OR ADD USER DETAILS TO NEWLY CREATED USERS:
	(*adding details to a user like this is only required when a user account is created through this admin portal*)
		>>Select User Profiles
		>>Select user you want to edit or select Add
		>>Edit the appropriate fields then click one of the save options
	

Employee View:
 After logging in, you will be at the main page.
	From the Navigation Bar: 
	TO SEE PERSONAL DETAILS
		>>Select Personal Details
	TO CHOOSE TIMESLOTS
		>>Select manage schedule
	TO SEE YOUR SCHEDULED SHIFTS
		>> Select View Availibilty 
	TO SEE AND WRITE MESSAGES
		>> Select Message Board


3. List of Bugs
---------------
- Can’t see employee detail in employee list
- There are currently no confirmation screens  for selecting date in open availabililty.
- No confirmation screen after selecting time slot.
- View availbilty will display boolean instead of "Pending" or "Accepted" in Firefox.
- UI with the open availability page stops is not implemented due to conflicts
-FIREFOX

4. Test Usernames
-----------------
Employee View
Username: employee1
Password: pwdpwd

Username: employee2
Password: pwdpwd

Username: employee3
Password: pwdpwd

Admin/Manager View
Username: admin
Password: pwdpwd


5. Member of team
ÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑÑ
Yu-Chun(May) Lin
Yuan(Kimi) Li
Zoya Zou
Emily Chen
Andrew Wong
Sam Li

