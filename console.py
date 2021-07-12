import pdb
from models.member import Member
from models.session import Session
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.session_repository as session_repository
import repositories.booking_repository as booking_repository

booking_repository.delete_all()
member_repository.delete_all()
session_repository.delete_all()

member1 = Member("Fred", "Jones",72)
member_repository.save(member1)

member2 = Member("Ashley","Evans", 32)
member_repository.save(member2)

member3 = Member("Edward","Fletcher", 21)
member_repository.save(member3)

session1 = Session("Spin", "Thursday","John", "13:00")
session_repository.save(session1)

session2 = Session("Crossfit", "Monday", "Zsolt", "18:00")
session_repository.save(session2)

session3 = Session("Zumba","Tuesday", "Juan", "10:00")
session_repository.save(session3)

booking1 = Booking(member1, session1)
booking_repository.save(booking1)

booking2 = Booking(member2, session2)
booking_repository.save(booking2)

booking3 = Booking(member3, session3)
booking_repository.save(booking3)

booking4 = Booking(member1, session2)
booking_repository.save(booking4)

booking5 = Booking(member2,session3)
booking_repository.save(booking5)

booking6 = Booking(member3, session1)
booking_repository.save(booking6)

pdb.set_trace()