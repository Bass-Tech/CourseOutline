from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from App.database import db
from App.models import document
from App.maker import *
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app, send_from_directory, send_file, jsonify, current_app
from flask_login import current_user, login_user, logout_user


form_views = Blueprint('form_views', __name__, template_folder='../templates')
@form_views.route('/CompiledForm', methods=['GET'])
def generatreCourseOutline():
    return render_template("templates/CompiledForm.html")
