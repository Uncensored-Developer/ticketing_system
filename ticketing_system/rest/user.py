import json
import uuid
from flask import Blueprint, Response
from ticketing_system.factories.user import create_user_list_use_case, create_user_json_encoder


blueprint = Blueprint('user', __name__)

users = [
            {
                'token': uuid.uuid4().hex,
                'email': 'adssghh@hshkj.com',
                'user_type': 'staff',
                'name': 'ken Ten'
            },
            {
                'token': uuid.uuid4().hex,
                'email': 'adssghh@hshkj.com',
                'user_type': 'staff',
                'name': 'ken Ten'
            },
            {
                'token': uuid.uuid4().hex,
                'email': 'adssghh@hshkj.com',
                'user_type': 'staff',
                'name': 'ken Ten'
            }
        ]


@blueprint.route('/users', methods=['GET'])
def user():
    result = create_user_list_use_case(users).execute()
    return Response(
        json.dumps(result, cls=create_user_json_encoder()),
        mimetype='application/json', status=200
    )
