from app import App
import logging
from models.User import get_all_users


class User_handler(App):
    @App.route("/users", methods=['GET'])
    def get_users(request):
        users_list = get_all_users()
        return request.Response(json=users_list)
