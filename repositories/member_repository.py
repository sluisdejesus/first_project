from db.run_sql import run_sql
from models.booking import Booking
from models.session import Session
from models.member import Member

def save(member):
    sql = "INSERT INTO members (first_name, last_name, age) VALUES (%s, %s, %s) returning id"
    values = [member.first_name, member.last_name, member.age]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def sessions(member):
    sessions = []
    sql = "SELECT sessions.* FROM sessions INNER JOIN bookings on bookings.session_id = sessions.id WHERE bookings.member_id = %s"
    values = member.id
    results = run_sql(sql, values)

    for row in results:
        session = Session(row['session_name'], row['weekday'],['instructor'],['time'],['id'])
        sessions.append(session)
    return sessions