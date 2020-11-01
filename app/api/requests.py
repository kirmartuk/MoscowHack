from flask import jsonify, request, Response
from app import db
from app.models import PetRequest
from app.api import bp


@bp.route('/requests', methods=['GET'])
def get_requests():
    """Get requests.
    ---
    responses:
        '200':
          description: return all requests
        """
    return jsonify(PetRequest.get_all_requests())


@bp.route('/requests/<int:id>', methods=['GET'])
def get_request(id):
    """Get request.
    ---
    parameters:
         - in: path
           name: id
           type: int
           required: true
    responses:
        '200':
          description: return request
        """
    return jsonify(PetRequest.get_request(id))


@bp.route('/requests', methods=['POST'])
def add_request():
    """Add request
    ---
    responses:
        '200':
          description: request added
        """
    data = request.get_json()
    PetRequest.add_json(data)
    return Response("", 201, mimetype='application/json')
