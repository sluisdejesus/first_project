from flask import Flask, render_template, request,redirect
from flask import Blueprint
from models.session import Session
import repositories.session_repository as session_repository


sessions_blueprint = Blueprint("sessions", __name__)

@sessions_blueprint.route('/sessions')
def sessions():
    sessions = session_repository.select_all()
    return render_template('/sessions/index.html', sessions = sessions)

@sessions_blueprint.route('/sessions/<id>')
def show_session(id):
    session = session_repository.select(id)
    return render_template('/sessions/show.html', session = session)

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

@sessions_blueprint.route('/sessions/<id>/edit')
def edit_session(id):
    session = session_repository.select(id)
    return render_template('sessions/edit.html', session = session)

@sessions_blueprint.route('/sessions/<id>', methods = ['POST'])
def update_session(id):
    session_name = request.form['session_name']
    weekday = request.form['weekday']
    instructor = request.form['instructor']
    time = request.form['time']
    session = Session(session_name, weekday, instructor, time, id)
    session_repository.update(session)
    return redirect ('/sessions/'+id)

@sessions_blueprint.route('/sessions/<id>/delete', methods = ['POST'])
def session_delete(id):
    session_repository.delete(id)
    return redirect ('/sessions')