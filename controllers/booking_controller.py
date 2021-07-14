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
    return render_template('/bookings/index.html', bookings = bookings)

@bookings_blueprint.route('/bookings/<id>')
def show_booking(id):
    booking = booking_repository.select(id)
    return render_template('bookings/show.html', booking = booking, session = session, member = member)

@bookings_blueprint.route('/bookings', methods = ['POST'])
def make_booking():
    member_id = request.form['member.id']
    session_id = request.form['session.id']
    booking = Booking(session_id, member_id, id)
    booking_repository.save(booking)
    return "Booking made"