import json
from flask import Blueprint, Response, request
from ticketing_system.requests.create_reply_request_object import CreateReplyRequestObject
from ticketing_system.requests.list_replies_request_object import ListRepliesRequestObject
from ticketing_system.factories.reply import (
    create_reply_use_case, create_reply_json_serializer,
    create_list_replies_use_case
)
from .ticket import STATUS_CODES


blueprint = Blueprint('reply', __name__)


@blueprint.route('/replies', methods=['GET', 'POST'])
def replies():
    user_token = request.headers.get('Authorization', None)
    if user_token:
        user_token = user_token.split()[1]
    if request.method == 'GET':
        query_params = {
            'filters': {},
        }
        for arg, values in request.args.items():
            query_params['filters'][arg] = values
        request_object = ListRepliesRequestObject.from_dict(query_params, user=user_token)
        response = create_list_replies_use_case().execute(request_object)
    elif request.method == 'POST':
        request_object = CreateReplyRequestObject.from_dict(request.json, user=user_token)
        response = create_reply_use_case().execute(request_object)
    return Response(json.dumps(response.value, cls=create_reply_json_serializer()),
                    mimetype='application/json',
                    status=STATUS_CODES[response.type])
