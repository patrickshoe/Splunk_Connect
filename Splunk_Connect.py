import sys
import splunklib.client as client
import getpass

HOST = input('Enter your hostname or ip address:')
PORT = 8089
USERNAME = input('Enter your username:')
print("Welcome",USERNAME)
PASSWORD = getpass.getpass('Enter your password:')

#create a service and log in
service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD,
    scheme = 'https')

#Print installed apps to the console to verify login for app in service.apps:
for app in service.apps:
    print(app.name)

jobs=service.jobs
users=service.users
inputs=service.inputs
indexes=service.indexes
savedsearches=service.saved_searches 

print("There are", len(jobs), "jobs available for", USERNAME,".")
print("\nSearch IDs:\n " + "\n ".join([job.sid for job in jobs]))

kwargs={"sort_key":"realname", "sort_dir":"asc"}
users=service.users.list(count=-1,**kwargs)

print ("Users:")
for user in users:
    print("%s (%s)" % (user.realname, user.name))
    for role in user.role_entities:
        print(" - ", role.name)
        
for index in indexes:
    count = index["totalEventCount"]
    print("%s (events: %s)" % (index.name, count))
    
for savedsearch in savedsearches:
    print(" " + savedsearch.name)
    print("    Query: " + savedsearch["search"])

#viewing inputs is currently not working                
#for item in inputs:
#    print("%s (%s)" % (item.name,item.kind))
