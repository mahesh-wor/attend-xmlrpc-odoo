import xmlrpc.client
import datetime

username = 'foo'
password = 'foo'
dbname = 'foo'
sock_common = xmlrpc.client.ServerProxy('http://localhost:8081/xmlrpc/common')
uid = sock_common.login(dbname, username, password)
print(uid)
sock = xmlrpc.client.ServerProxy('http://localhost:8081/xmlrpc/object')

# partner = {
#     'name': 'GG name1',
#     'lang': 'en_US',
#     'mobile':'985324524',
# }
# partner_id = sock.execute(dbname, uid, password, 'res.partner', 'create', partner)

atten = {
    'employee_id':10,
    'check_in': datetime.datetime.now(),
}

chk_out = {
    'employee_id':1,
    'check_out':datetime.datetime.now(),
}

checkin = sock.execute(dbname, uid, password, 'hr.attendance', 'write', chk_out)

if checkin:
    print("Successfully checked out for: ", atten['employee_id'])

