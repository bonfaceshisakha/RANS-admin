from flask import Blueprint

mod_api = Blueprint('api', __name__,)

@mod_api.route('/getstuff')
def getStuff():
    return '{"greetings" : "Hello user"}'