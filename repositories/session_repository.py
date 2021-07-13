from db.run_sql import run_sql
from models.booking import Booking
from models.member import Member
from models.session import Session

def save(session):
    sql = "INSERT INTO sessions(session_name, instructor, weekday, time) VALUES (%s, %s, %s, %s) returning id"
    values = [session.session_name, session.instructor, session.weekday, session.time]
    results = run_sql(sql, values)
    session.id = results[0]['id']
    return session

def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM sessions WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def members(session):
    members = []
    sql = "SELECT members.* FROM members INNER JOIN bookings on bookings.member_id = members.id WHERE bookings.member_id = %s"
    values = [session.id]
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['first_name'],row['last_name'],row['age'])
        members.append(member)
    return members

def select_all():
    sessions = []

    sql = "SELECT * FROM sessions"
    results = run_sql(sql)
    for row in results:
        session = Session(row['session_name'], row['weekday'], row['instructor'], row['time'], row['id'])
        sessions.append(session)
    return sessions

def select(id):
    session = None
    sql = "SELECT * FROM sessions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        session = Session(result['session_name'], result['weekday'], result['instructor'], result['time'])
    return session