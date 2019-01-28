"""Test assignment status queryable.
"""
import unittest

from app.queryables.assignment_status_queryable import AssistantStatusQueryable


class TestAssignmentStatusQueryable(unittest.TestCase):
    def test_returns_list(self):
        '''Test returns list.
        '''

        queryable = AssistantStatusQueryable()
        result = queryable.to_list()
        self.assertIsInstance(result, list)


if __name__ == '__main__':
    unittest.main()
