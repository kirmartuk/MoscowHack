import os
import io
import docx

from datetime import date
from app.api import bp
from flask import Flask, request, abort, jsonify, send_file
from flask import send_from_directory, render_template
from app import app
from flasgger import Swagger
from app.models import *

UPLOAD_DIRECTORY = os.getcwd() + "/src/"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

swagger = Swagger(app)


@bp.route("/files")
def list_files():
    """list files on the server
    ---
    responses:
        '200':
          description: return all files in directory
        """
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)


@bp.route("/files/<path:path>")
def get_file(path):
    """Download a file.
    ---
    parameters:
         - in: path
           name: filename
           type: string
           required: true
    responses:
        '200':
          description: file downloaded
        """
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


@bp.route("/files/<filename>", methods=["POST"])
def post_file(filename):
    """Upload a file
     ---
    parameters:
         - in: path
           name: filename
           type: string
           required: true
    responses:
         200:
           description: return file
        """

    if "/" in filename:
        # Return 400 BAD REQUEST
        abort(400, "no subdirectories allowed")

    with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
        fp.write(request.data)

    # Return 201 CREATED
    return "", 201


@bp.route("/report/<animal_id>", methods=["GET"])
def get_report(animal_id):
    """Get report of animal
     ---
    parameters:
         - in: path
           name: id
           type: int
           required: true
    responses:
         200:
           description: return file
        """

    animal = Animal.get_by_id(animal_id)
    document = docx.Document("/home/kirill/hackaton/src/output.docx")
    for paragraph in document.paragraphs:
        paragraph.text = paragraph.text.replace('[date]', date.today().strftime("%d /%m / %Y год"))
        paragraph.text = paragraph.text.replace('[idcard]', str(animal.idcard))
        paragraph.text = paragraph.text.replace('[address]', str(Shelter.get_by_id(animal.shelter).address))
        paragraph.text = paragraph.text.replace('[daddy]', str(Shelter.get_by_id(animal.shelter).name))

        if animal.animal_type == 1:
            paragraph.text = paragraph.text.replace('[dog]', 'нет')
            paragraph.text = paragraph.text.replace('[cat]', 'да')
        else:
            paragraph.text = paragraph.text.replace('[dog]', 'да')
            paragraph.text = paragraph.text.replace('[cat]', 'нет')

        paragraph.text = paragraph.text.replace('[age]', str(animal.age))
        paragraph.text = paragraph.text.replace('[cell]', str(animal.cell))
        paragraph.text = paragraph.text.replace('[weight]', str(animal.weight))
        paragraph.text = paragraph.text.replace('[nickname]', animal.nickname)
        if animal.male == 1:
            paragraph.text = paragraph.text.replace('[sex]', "М")
        else:
            paragraph.text = paragraph.text.replace('[sex]', "Ж")
        # get breed
        paragraph.text = paragraph.text.replace('[breed]', str(animal.animal_breed))
        paragraph.text = paragraph.text.replace('[color]', str(animal.color))
        paragraph.text = paragraph.text.replace('[fur]', str(animal.fur))
        paragraph.text = paragraph.text.replace('[ear]', str(animal.ears))
        paragraph.text = paragraph.text.replace('[tail]', str(animal.tail))
        paragraph.text = paragraph.text.replace('[size]', str(animal.size))
        paragraph.text = paragraph.text.replace('[specials]', str(animal.special_signs))
        paragraph.text = paragraph.text.replace('[character]', str(animal.character))
        paragraph.text = paragraph.text.replace('[character]', str(animal.character))
        paragraph.text = paragraph.text.replace('[idmark]', str(animal.idmark))
        if animal.ready == 0:
            paragraph.text = paragraph.text.replace('[ready]', 'Нет')
        else:
            paragraph.text = paragraph.text.replace('[ready]', 'Да')
        paragraph.text = paragraph.text.replace('[sterilized]', str(animal.sterilized))
        paragraph.text = paragraph.text.replace('[veterinarian]', str(animal.veterinarian))

    document.save(UPLOAD_DIRECTORY + '/reports' + str(animal.id) + '.docx')
    return send_file(UPLOAD_DIRECTORY + '/reports' + str(animal.id) + '.docx',
                     mimetype='application/vnd.openxmlformats-officedocument.wordprocessing',
                     as_attachment=True)
