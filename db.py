from peewee import *

# By passing "None" to the database class we're able to dynamically reference it later on
# thus we can pass configurations to it in the main file (see aswcp_webserver.py).
database = PostgresqlDatabase(None)

# Sublcass to reference the above "database" variable
class BaseModel(Model):
	class Meta:
		database = database

class Users(BaseModel):
	id = PrimaryKeyField()
	username = CharField(max_length=20)
	pw = CharField(max_length=256)
	email = CharField(max_length=100)

class Servers(BaseModel):
	id = PrimaryKeyField()
	user = ForeignKeyField(Users, cascade=True)
	ipv4 = CharField(max_length=17)
	ipv6 = CharField(max_length=45)
	hostname = CharField(max_length=256)
	added = IntegerField()

class Api(BaseModel):
	id = PrimaryKeyField()
	private = CharField(max_length=212)
	public = CharField(max_length=86)
	server = ForeignKeyField(Servers, cascade=True)

users = Users
servers = Servers
api = Api