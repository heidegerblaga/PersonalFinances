import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred_obj = firebase_admin.credentials.Certificate("personal-finanse-firebase-adminsdk-qzfyc-8e364f9beb.json")
default_app = firebase_admin.initialize_app(cred_obj)


db = firestore.client()

obj1 = {
	"Name": 'Mike',
	"Age": 100,
	"Net worth": 1000000
}

obj2 = {
	"Name": 'Tony',
	"Age": 23,
	"Net worth": 200000
}

data = [obj1,obj2]

for record in data:
	doc_ref = db.collection(u'User').document(record['Name'])
	doc_ref.set(record)
