#!/usr/bin/python3

import xmlrpc.client
import datetime

###Vars
username = 'mahesh'
password = 'foo'
db = 'xmlrpc'
url='http://localhost:8082'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

chk_out = {
    'employee_id':6,
    'check_out':datetime.datetime.now()
}
print(type(chk_out))
print(chk_out)

models.execute_kw(db, uid, password, 'hr.employee','attendance_manual',[[uid],['hr_attendance.hr_attendance_action_my_attendances']])


# models.execute_kw(db, uid, password, 'hr.attendance', 'write',[[4],{
#     'check_out':datetime.datetime.now()}])
#print(foo)


# common.execute_kw(db, uid, password, 'res.partner', 'check_access_rights',['read'])

# partner = {
#     'name': 'GG name1',
#     'lang': 'en_US',
#     'mobile':'985324524',
# }
# partner_id = sock.execute(dbname, uid, password, 'res.partner', 'create', partner)

# atten = {
#     'employee_id':6,
#     'check_in': datetime.datetime.now()
# }
#
# chk_out = {
#     'employee_id':6,
#     'check_out':datetime.datetime.now()
# }
# common.execute_kw(db, uid, password, 'res.partner', 'write', [[id], {
#     'name': "Newer partner"
# }])
# common.execute_kw(db, uid, password, 'res.partner', 'name_get', [[id]])
# common.execute_kw(db, uid, password, 'hr.attendance', 'write', chk_out)
#
#

#checkin = sock.execute(db, uid, password, 'hr.attendance', 'write', chk_out)

#if checkin:
#    print("Successfully checked out for: ", atten['employee_id'])
