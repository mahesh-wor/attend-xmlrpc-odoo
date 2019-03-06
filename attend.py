#!/usr/bin/python2
############################################################################
### Some Casual Imports
import xmlrpc.client
import datetime
import sys
import os

############################################################################
###Credentials Administrator or one with manager access of Attendance module.
username = 'your-user-name-here'
password = 'your-password-here'
db = 'your-database-name-here' #database name
url='your-odooserver-url-here' #odooserver url

############################################################################
###Help Usuage Printing.
def attend_help():
    print("""
Usage: attend <username> checkin/checkout
Good Luck !!
    """)

if len(sys.argv)==1:
    print("""
Roses are red, Violets are blue
without any arguments master,
what am i going to do. """)
    attend_help()
    exit()
############################################################################
###Try-except to prevent Error raises
try:
    emp_name = sys.argv[1]
except IndexError as indexerrname:
    print("You sure that employee exists?")
    attend_help()
    exit()

############################################################################
###Try-except to prevent Error raises
try:
    chkinout = sys.argv[2]
except IndexError as indexerrio:
    print("Makeup your mind. It's easy either checkin or checkout.")
    attend_help()
    exit()

############################################################################
### xmlrpc objects
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

############################################################################
###Get UserID of the employee authenticated with above usernmae.
uid = common.authenticate(db, username, password, {})

############################################################################
###Get all the employees name & id . Later use it to extract needed ones.
emp_list = models.execute_kw(db, uid, password,'hr.employee', 'search_read',[],{'fields': ['name']})

############################################################################
###Try-except to prevent Error raises if the employee index don't exist
try:
    usr_emp_id=list(filter(lambda person: person['name'] == emp_name, emp_list))[0]['id']
except IndexError as indexerrempid:
    print("You sure that employee exists?")
    attend_help()
    exit()

############################################################################
### Get attendance state of the user.
attend_data=models.execute_kw(db, uid, password, 'hr.employee','search_read',[],{'fields':['attendance_state','name']})
attend_state=list(filter(lambda person: person['name'] == emp_name, attend_data))[0]['attendance_state']

############################################################################
### Noobish conditions and checking statements
if attend_state == 'checked_out' and chkinout == 'checkin':
    print('Checking in ...')
    result=models.execute_kw(db, uid, password, 'hr.employee','attendance_manual',[[usr_emp_id],['hr_attendance.hr_attendance_action_my_attendances']])
    check_in= result['action']['attendance']['check_in']
    check_out= result['action']['attendance']['check_out']
    print('Checked In/out at',check_in,check_out)
elif (attend_state == 'checked_in' and chkinout == 'checkout'):
    print('Checking out ...')
    result = models.execute_kw(db, uid, password, 'hr.employee','attendance_manual',[[usr_emp_id],['hr_attendance.hr_attendance_action_my_attendances']])
    check_in = result['action']['attendance']['check_in']
    check_out = result['action']['attendance']['check_out']
    print('Checked In/out at',check_in,check_out)
elif (attend_state == 'checked_in' and chkinout == 'checkin'):
    print('You are already checked in at:')
    print("Please checkout first.")
    attend_help()
elif (attend_state == 'checked_out' and chkinout == 'checkout'):
    print("You have already checked out at :",)
    print("Please checkin first.")
else:
    print("Makeup your mind. It's easy either checkin or checkout.")
    attend_help()
exit()
############################################################################
### End of Script lol
