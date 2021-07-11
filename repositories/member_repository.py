from db.run_sql import run_sql
from models.booking import Booking
from models.class import Class
from models.member import Member

def save(member):
    sql = "INSERT INTO members(first_name, last_name, age VALUES (%s, %s, %s) returning id"
    values = [member.first_name, member.last_name, member.age]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)
