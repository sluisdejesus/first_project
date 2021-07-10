from flask import Flask

from controllers.member_controller import members_blueprint
from controllers.class_controller import classes_blueprint
from controllers.booking_controller import bookings_blueprint

app = Flask(__name__)

app.register_blueprint(members_blueprint)
app.register_blueprint(classes_blueprint)
app.register_blueprint(bookings_blueprint)

@app.route('/')
def home():
    return "hello this is the beginning"


if __name__ == '__main__':
    app.run(debug=True)