from flask import Blueprint, jsonify, request
from src.view.http_types.http_request import HttpRequest
from src.view.tag_creator_view import TagCreatorView
from src.erros.error_handler import handle_erros

tag_routes_bp = Blueprint('tag_routes', __name__)

@tag_routes_bp.route('/create_tag', methods=["POST"])
def create_tags():
    response = None
    try:
        # tag_creator_validator(request)
        tag_creator_view = TagCreatorView()

        http_request = HttpRequest(body=request.json)
        response = tag_creator_view.validate_and_create(http_request)
    except Exception as exception:
        response = handle_erros(exception)
        

    return jsonify(response.body), response.status_code