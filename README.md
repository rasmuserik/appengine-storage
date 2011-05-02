# Simple storage engine that runs on google appengine

Sample usage:
    
Retrieve an element from a database:
    https://example.com/database-name/key

Create a new element in the database (only works if it doesn''t exists):
    https://example.com/database-name/key?put=value

Update an element in the database:
    https://example.com/database-name/key?put=new_value&prev=previous_value

Wrap the result in javascript padding:
    https://example.com/database-name/key?callback=js_func

Retrieve list of changed elements since a given timestamp (ie. 1234567890 seconds after 1970):
    https://example.com/database-name/since?1234567890

Notice: access control is not a part of the storage engine, and should be handled elsewhere.
