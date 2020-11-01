from flask import jsonify, request
from app import db
from app.models import Shelter
from app.api import bp


@bp.route('/shelters', methods=['GET'])
def get_shelters():
    """Get Shelters.
    ---
    responses:
        '200':
          description: return all shelters
        """
    return jsonify(Shelter.get_all_shelters())


@bp.route('/setShelters', methods=['POST'])
def set_shelters():
    """Set shelters to db.
    ---
    responses:
        '200':
          description: shelters added
        """
    data = request.get_json()
    Shelter.set_shelters(data)
    return Response("", 201, mimetype='application/json')
