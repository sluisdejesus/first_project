from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route('/bookings')
def bookings():
    bookings = booking_repository.select_all()
    return render_template('/bookings/index.html', bookings = bookings)

@bookings_blueprint.route('/bookings/<id>')
def show_booking(id):
    booking = booking_repository.select(id)
    return render_template('bookings/show.html', booking = booking)