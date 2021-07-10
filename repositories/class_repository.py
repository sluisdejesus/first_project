from db.run_sql import run_sql
from models.booking import Booking
from models.class import Class
from models.member import Member

def save(class):
    sql = "INSERT INTO classes(class_name, instructor, weekday, time) VALUES (%s, %s, %s, %s) returning id"
    values = [class.class_name, class.instructor, class.weekday, class.time]
    results = run_sql(sql, values)
    class.id = results[0]['id']
    return results