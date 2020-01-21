import json
from flask import Blueprint, Response, request
from ticketing_system.responses.response_objects import ResponseSuccess, ResponseFailure
from ticketing_system.requests.list_tickets_request_object import ListTicketsRequestObject
from ticketing_system.requests.create_ticket_request_object import CreateTicketRequestObject
from ticketing_system.requests.get_and_update_ticket_request_object import GetAndUpdateTicketRequestObject
from ticketing_system.factories.ticket import (
    create_ticket_json_encoder, create_ticket_list_use_case,
    create_ticket_use_case, create_get_ticket_use_case,
    create_update_ticket_use_case
)


blueprint = Blueprint('ticket', __name__)

STATUS_CODES = {
    ResponseSuccess.SUCCESS: 200,
    ResponseFailure.RESOURCE_ERROR: 404,
    ResponseFailure.PARAMETERS_ERROR: 400,
    ResponseFailure.SYSTEM_ERROR: 500
}


@blueprint.route('/tickets', methods=['GET', 'POST'])
def tickets():
    user_token = request.headers.get('Authorization', None)
    if user_token:
        user_token = user_token.split()[1]
    if request.method == 'GET':
        query_params = {
            'filters': {},
        }
        for arg, values in request.args.items():
            query_params['filters'][arg] = values
        request_object = ListTicketsRequestObject.from_dict(query_params, user=user_token)
        response = create_ticket_list_use_case().execute(request_object)
    elif request.method == 'POST':
        request_object = CreateTicketRequestObject.from_dict(request.json, user=user_token)
        response = create_ticket_use_case().execute(request_object)
    return Response(json.dumps(response.value, cls=create_ticket_json_encoder()),
                    mimetype='application/json',
                    status=STATUS_CODES[response.type])


@blueprint.route('/tickets/<code>', methods=['GET', 'PATCH'])
def ticket(code):
    user_token = request.headers.get('Authorization', None)
    if user_token:
        user_token = user_token.split()[1]
    if request.method == 'GET':
        request_object = GetAndUpdateTicketRequestObject.from_dict({'code': code}, user=user_token)
        response = create_get_ticket_use_case().execute(request_object)
    if request.method == 'PATCH':
        import copy
        data = copy.deepcopy(request.json)
        data.update({'code': code})
        request_object = GetAndUpdateTicketRequestObject.from_dict(data, user=user_token)
        response = create_update_ticket_use_case().execute(request_object)
    return Response(json.dumps(response.value, cls=create_ticket_json_encoder()),
                    mimetype='application/json',
                    status=STATUS_CODES[response.type])
