from unittest import TestCase
from unittest.mock import patch
class TestHelper(TestCase):
    @patch('src.db_helper.DbHelper')
    def test_max_salary_is_greater_than_min_salary(self,MockDbHelper):
        db_helper=MockDbHelper()
        db_helper.get_maximum_salary.return_value=158220
        db_helper.get_minimum_salary.return_value=38623
        actualMax = db_helper.get_maximum_salary()
        actualMin = db_helper.get_minimum_salary()
        self.assertGreater(actualMax,actualMin)



