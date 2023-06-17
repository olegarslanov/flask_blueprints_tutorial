from flask import Blueprint

example_blueprint = Blueprint('example_blueprint', __name__)
ENDPOINT_NAME = "/user"

@example_blueprint.route(f'{ENDPOINT_NAME}/')
def get_all_users():
    return {1:"Vytautas", 2: "Jonas"}

@example_blueprint.route(f'{ENDPOINT_NAME}/greet_user/<user>')
def index(user: str):
    return {"greet": f"Hello {user}"}