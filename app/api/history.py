from flask import jsonify, request, Response
from app import db
from app.models import History
from app.api import bp


@bp.route('/history/<int:id>', methods=['GET'])
def get_events_for_animal(id):
    """Get animal's history.
    ---
    parameters:
         - in: path
           name: id
           type: int
           required: true
    responses:
        '200':
          description: return animal's history
        """
    try:
        return jsonify(History.get_events_for(id))
    except:
        e = {}
        return jsonify(e)


@bp.route('/history', methods=['POST'])
def add_event():
    """Add history to animal.
    ---
    responses:
        '200':
          description: history added
        """
    data = request.get_json()
    History.add(data)
    return Response("", 201, mimetype='application/json')
