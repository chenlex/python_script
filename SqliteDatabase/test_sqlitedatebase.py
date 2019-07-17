import peewee
from playhouse.shortcuts import model_to_dict

db = peewee.SqliteDatabase("test.db")

class BaseModel(peewee.Model):
    class Meta:
        database = db
    def to_dict(self):
        return model_to_dict(self)

class New_Update(BaseModel):
    mac = peewee.CharField(primary_key=True)
    version = peewee.CharField()
    machine_id = peewee.CharField()
    hostname = peewee.CharField()
    disk = peewee.CharField()
    class Meta:
        db_table = 'New_Update'


#db.create_tables([Update,test], safe=True)  # ???
New_Update.create_table()

# test the query
query = New_Update.replace(mac='18:66:da:28:24:e2', version=30000, machine_id='d87475dffb662363093f506900000005', \
             hostname='host', disk='/dev/sda')
# ???create ???????? "UNIQUE constraint failed"
#query.save()

# get query
q = New_Update.select().where(New_Update.mac == '18:66:da:28:24:e2')
print(q[0].mac, q[0].version, q[0].machine_id, q[0].hostname, q[0].disk)
# get all
a = New_Update.select()
print(a[0].mac, a[0].version, a[0].machine_id, a[0].hostname, a[0].disk)

db.close()


