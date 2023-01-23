import unittest
from model import *
import datetime as dt

class ModelMethods(unittest.TestCase):

    def test_join_before_leave(self):
        start = dt.datetime.now()
        end = start + dt.timedelta(seconds=3.5)
        event = Event("123", start, end)
        attendance = EventAttendance.generate(event)
        print(attendance)
        self.assertTrue(attendance.leave > attendance.join)

if __name__ == '__main__':
    unittest.main()