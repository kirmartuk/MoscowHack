from flask import jsonify, request, Response
from app import db
from app.models import Animal, AnimalBreed
from app.api import bp


@bp.route('/animals', methods=['GET'])
def get_animals():
    """Get all animals
     ---
    responses:
         200:
           description: return all animal
        """
    try:
        limit = int(request.args['limit'])
        offset = int(request.args['offset'])
        return jsonify(Animal.filter(limit, offset, request.args))
    except Exception as e:
        return Response(e, 400, mimetype='application/json')


@bp.route('/breeds', methods=['GET'])
def get_breed():
    """Get all breeds
     ---
    responses:
         200:
           description: return all breeds
        """
    return jsonify(AnimalBreed.get_all_breeds())


@bp.route('/animals/<int:id>', methods=['GET'])
def get_animal(id):
    """Download a file.
    ---
    parameters:
         - in: path
           name: id
           type: int
           required: true
    responses:
        '200':
          description: return animal
        """
    return jsonify(Animal.get_by_id(id))


@bp.route('/socialized', methods=['GET'])
def get_socialized():
    """Get animals for users.
    ---
    responses:
        '200':
          description: return animals
        """
    try:
        limit = int(request.args['limit'])
        offset = int(request.args['offset'])
        return jsonify(Animal.get_socialized(limit, offset, request.args))
    except Exception as e:
        return Response(e, 400, mimetype='application/json')


@bp.route('/animals', methods=['POST'])
def add_animal():
    """Add animal.
    ---
    responses:
        '200':
          description: animal added
        """
    data = request.get_json()
    Animal.add_json(data)
    return Response("", 201, mimetype='application/json')


@bp.route('/animals', methods=['PUT'])
def update_animal():
    """Update animal.
    ---
    responses:
        '200':
          description: animal updated
        """
    data = request.get_json()
    Animal.update_json(data)
    return Response("", 201, mimetype='application/json')
