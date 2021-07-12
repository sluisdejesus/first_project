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
    values = session.id
    results = run_sql(sql, values)

    for row in results:
        member = Member(row['first_name'],row['last_name'],row['age'])
        members.append(member)
    return members