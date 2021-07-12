from db.run_sql import run_sql
from models.booking import Booking
from models.session import Session
from models.member import Member

def save(booking):
    sql = "INSERT INTO bookings (member_id, session_id) VALUES (%s,%s) RETURNING id"
    values = [booking.member.id, booking.session.id ]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking

def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)