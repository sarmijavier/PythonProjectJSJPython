from flask_login import UserMixin
from firestore_service import get_user


class UserData:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password


class UserModel(UserMixin):
    def __init__(self, user_data):
        """
        :params user_data: UserData
        """
        self.id = user_data.email
        self.name = user_data.name
        self.password = user_data.password
    

    @staticmethod
    def query(user_id):
        user_doc = get_user(user_id)
        #import pdb; pdb.set_trace()
        user_data = UserData(
            email = user_doc.id,
            name = user_doc.to_dict()['name'],
            password = user_doc.to_dict()['password']
        )

        return UserModel(user_data)