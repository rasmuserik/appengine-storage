from google.appengine.ext import db
import cgi
import os
import time


class TimeLogEntry(db.Model):
    action = db.StringProperty(required=True)
    time = db.IntegerProperty(required=True)

form = cgi.FieldStorage()
print "Content-Type: text/javascript\n"


if "time" in form:
    time = int(form["time"].value)
else:
    time = int(time.time())

if "action" in form:
    entry = TimeLogEntry(
        time = time,
        action = form["action"].value,
        key_name = str(time)
        )
    entry.put()
    result = [entry]
else:
    result = db.GqlQuery("SELECT * FROM TimeLogEntry WHERE time <= :1 AND time > :2", time, time - 7*24*60*60)

result = ['{time:%d,action:"%s"}' % (x.time, x.action) for x in result]
result = "[" + ",".join(result) + "]"

if "callback" in form:
    print form["callback"].value + "(" + result + ");"
else:
    print result

"""
key = os.environ["PATH_INFO"]
name = key.split("/")[-1]
realm = key[1:-len(name)-1]
now = int(time.time())


print key
today = int( time.time() /60/60/24)


if "create" in form:
    result = "false"
    if not entry or "prev" in form and entry.value == form["prev"].value:
        Entry(realm =  realm,
            name = name,
            value = form["put"].value, 
            date = now,
            key_name = key).put()
    
        result = "true"
    else:
        result = "{error:'not a valid prev-value',current:" + entry.value + "}"

elif "since" in form:
    since = float(form["since"].value)
    keys = db.GqlQuery("SELECT __key__ FROM Entry WHERE realm = :1 AND date > :2",
                                realm, since)
    
    result = "[" + ",".join(["'" + elem.name()[len(realm):] + "'" for elem in keys]) + "]"

    result = "{keys:" + result + ",now:"+str(now)+"'}"

else:
    if entry:
        result = entry.value
    else:
        result = "undefined"

if "callback" in form:
    result = form["callback"].value + "(" + result + ");"

print result
"""
