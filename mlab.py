import mongoengine
# mongodb://<dbuser>:<dbpassword>@ds035683.mlab.com:35683/a7-server-apihost = "ds121980.mlab.com"
host = "@ds035683.mlab.com"
port = 35683
db_name = "a7-server-api"
username = "tranhanhieu"
password = "tranhanhieu"
def connect():
    mongoengine.connect(db_name, host=host, port=port, username=username, password=password)
def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]
def item2json(item):
    import json
    return json.loads(item.to_json())