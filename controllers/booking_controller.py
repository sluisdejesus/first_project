from models import session
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route('/bookings')
def bookings():
    bookings = booking_repository.select_all()
    members = member_repository.select_all()
    sessions = session_repository.select_all()
    return render_template('/bookings/index.html', bookings = bookings, sessions = sessions, members = members)

@bookings_blueprint.route('/bookings/<id>')
def show_booking(id):
    booking = booking_repository.select(id)
    member = member_repository.select(id)
    session = session_repository(id)
    return render_template('bookings/show.html', booking = booking, session = session, member = member)