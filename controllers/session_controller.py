from flask import Flask, render_template, request,redirect
from flask import Blueprint
from models.session import Session
import repositories.session_repository as session_repository


sessions_blueprint = Blueprint("sessions", __name__)

@sessions_blueprint.route('/sessions')
def sessions():
    sessions = session_repository.select_all()
    return render_template('/sessions/index.html', sessions = sessions)

@sessions_blueprint.route('/sessions/new')
def new_session():
    sessions = session_repository.select_all()
    return render_template('/sessions/new.html', sessions = sessions)

@sessions_blueprint.route('/sessions', methods = ['POST'])
def create_session():
    session_name = request.form['session_name']
    weekday = request.form['weekday']
    instructor = request.form['instructor']
    time = request.form['time']
    new_session = Session(session_name, weekday, instructor, time)
    session_repository.save(new_session)
    return redirect ('/sessions')