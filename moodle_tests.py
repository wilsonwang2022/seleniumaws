import unittest
import moodle_methods as methods
import moodle_locators as locators


class MoodlePositiveTestCases(unittest.TestCase):

    @staticmethod # signal to Unittest framework that this is a function inside the class (vs. @classmethod)
    def test_create_new_user(): # test_ in the name is mandatory
        methods.setUp()
        methods.log_in(locators.moodle_username, locators.moodle_password)
        methods.create_new_user()
        methods.search_user()
        methods.log_out()
        methods.log_in(locators.new_username, locators.new_password)
        methods.check_we_logged_in_with_new_cred()
        methods.log_out()
        methods.log_in(locators.moodle_username, locators.moodle_password)
        methods.delete_user()
        methods.log_out()
        methods.tearDown()