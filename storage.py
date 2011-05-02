from google.appengine.ext import db
import cgi
import os
import time


class Entry(db.Model):
    realm = db.StringProperty(required=True)
    name = db.StringProperty(required=True)
    value = db.StringProperty(required=True)
    date = db.FloatProperty(required=True)

form = cgi.FieldStorage()
key = os.environ["PATH_INFO"]
name = key.split("/")[-1]
realm = key[1:-len(name)-1]
now = float(time.time())

print "Content-Type: text/javascript\n"

entry = Entry.get_by_key_name(key)

if "put" in form:
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
