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

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def sessions(member):
    sessions = []
    sql = "SELECT sessions.* FROM sessions INNER JOIN bookings on bookings.session_id = sessions.id WHERE bookings.member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    for row in results:
        session = Session(row['session_name'], row['weekday'],['instructor'],['time'],['id'])
        sessions.append(session)
    return sessions

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row['first_name'], row['last_name'], row['age'], row['id'])
        members.append(member)
    return members

def select(id):
    member = None
    sql = "SELECT * FROM members where id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        member = Member(result['first_name'], result['last_name'],result['age'], result['id'])
    return member

def update(member):
    sql = "UPDATE members SET (first_name, last_name, age) = (%s,%s,%s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.age, member.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)