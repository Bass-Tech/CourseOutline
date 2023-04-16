from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from App.database import db
from App.models import document
from App.maker import *
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, send_from_directory, send_file, jsonify, current_app
from flask_login import current_user, login_user, logout_user
from werkzeug.utils import secure_filename

form_views = Blueprint('form_views', __name__, template_folder='../templates')
@form_views.route('/CompiledForm', methods=['GET'])
def generatreCourseOutline():
    return render_template("/CompiledForm.html")

@form_views.route("/CompiledForm", methods=["POST"])
def compiled_form_action():
    json_data = request.json
    filename = writeDoc(json_data)
    return jsonify({
        'filename': filename
    })

@form_views.route("/CompiledForm/download/<filename>", methods=["GET"])
def LecturerDownloadFile(filename):
    return send_from_directory(directory=current_app.instance_path, path=filename, as_attachment=True)
