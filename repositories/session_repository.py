from db.run_sql import run_sql
from models.booking import Booking
from models.member import Member
from models.session import Session

def save(session):
    sql = "INSERT INTO session(session_name, instructor, weekday, time VALUES (%s, %s, %s, %s) returning id"
    values = [session.first_name, session.instructor, session.weekday, session.time]
    results = run_sql(sql, values)
    session.id = results[0]['id']
    return session