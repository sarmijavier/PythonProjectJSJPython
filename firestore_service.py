import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


if not firebase_admin._apps:
    credential = credentials.Certificate('./key_firestores.json')
    firebase_admin.initialize_app(credential)


db = firestore.client()

def get_user(user_id):
    return db.collection(u'users').document(user_id).get()


def create_user(user_data):
    user_ref = db.collection(u'users').document(user_data.email)
    user_ref.set({
        'name': user_data.name,
        'password': user_data.password
    })