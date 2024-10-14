import unittest
from practice2 import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee(emp_id=1, name="Jane Doe", salary=50000)

    def test_get_salary(self):
        self.assertEqual(self.employee.salary, 50000)

    def test_set_salary(self):
        self.employee.salary = 60000
        self.assertEqual(self.employee.salary, 60000)

    def test_work_logging(self):
        # Set up a logging handler to capture the log output
        with self.assertLogs('root', level='INFO') as log:
            self.employee._work()
        self.assertIn('動きます', log.output[0])

if __name__ == '__main__':
    unittest.main()