from flask import Flask, render_template, request, redirect
from flask import Blueprint

bookings_blueprint = Blueprint("bookings", __name__)