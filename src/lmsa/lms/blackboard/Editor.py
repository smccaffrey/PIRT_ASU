from lmsa.lms.blackboard import BlackBoard
from bs4 import BeautifulSoup
import time

class Editor(BlackBoard):

    DUE_DATE_VALUE = 'dp_dueDate_date'
    DUE_DATE_TIME = 'tp_dueDate_time'
    CANCEL =
    SUBMIT =

    def __init__(self, driver):
        #need to check to see if this passes our driver in
        super(Editor, self).__init__(driver)

    def due_date(self, date, wait = None):
        try:
            self.driver.find_element_by_xpath(Editor.DUE_DATE_VALUE).clear()
            self.driver.find_element_by_xpath(Editor.DUE_DATE_VALUE).send_keys(date)
            time.sleep(wait)
        except Exception as e:
            return False
        return True

    def due_date_time(self, time, wait = None):
        try:
            driver.find_element_by_xpath(Editor.DUE_DATE_TIME).clear()
            driver.find_element_by_xpath(Editor.DUE_DATE_TIME).send_keys(time)
            time.sleep(wait)
        except Exception as e:
            return False
        return True

    def cancel(self, wait = None):
        try:
            self.driver.find_element_by_name(Editor.CANCEL).click()
            time.sleep(wait)
        except Exception as e:
            pass

    def submit(self, wait = None):
        try:
            self.driver.find_element_by_name(Editor.SUBMIT).click()
            time.sleep(wait)
        except Exception as e:
            pass


class TestOptions(Editor):

    EDIT_TEST_OPTIONS = '//a[@title="Edit the Test Options"]'
    START_RESTRICT_CHECK = '//*[@id="start_restrict"]'
    START_RESTRICT_DATE = '//*[@id="dp_restrict_start_date"]'
    START_RESTRICT_TIME = '//*[@id="tp_restrict_start_time"]'
    END_RESTRICT_CHECK = '//*[@id="end_restrict"]'
    END_RESTRICT_DATE = '//*[@id="dp_restrict_end_date"]'
    END_RESTRICT_TIME = '//*[@id="tp_restrict_end_time"]'
    DUE_DATE_CHECK = '//*[@id="_dueDate"]'
    DUE_DATE_DATE = ''
    LATE_SUBMISSION_CHECK = '//*[@id="doNotAllowLateSubmission"]'


    def __init__(self):
        return

    def nav_assignments(self, element, wait = None):
        try:
            self.driver.find_element_by_xpath('//a[@title=' + "\"" + element + " item options" + "\"" ']').click()
            time.sleep(wait)
        except Exception as e:
            return False
        return True

    def edit_test_options(self, wait = None):
        """
        Clicks the 'Edit Test Options Button' for entering the edit options menu.

        :Args:
        -   wait: Specifies time to wait after action.
            If None, does nothing.
        """
        try:
            self.driver.find_element_by_xpath(TestOptions.EDIT_TEST_OPTIONS).click()
            time.sleep(wait)
        except Exception as e:
            return False
        return True

    def start_restrict_check(self, state, wait = None):
        try:
            if state:
               self.driver.find_element_by_xpath('//*[@id="start_restrict"]').click()
               time.sleep(wait)
            else:
               #if not state need to assure that box is NOT checked
        except Exception as e:
            return False
        return True

    def end_restrict_check(self, state, wait = None):
        try:
            if state:
                self.driver.find_element_by_xpath('//*[@id="end_restrict"]').clear()
                self.driver.find_element_by_xpath('//*[@id="end_restrict"]').click()
                time.sleep(wait)
            else:
                self.driver.find_element_by_xpath('//*[@id="end_restrict"]').clear()
                time.sleep(wait)
        except Exception as e:
            return False
        return True

        def due_date_in_use(self, state, wait = None):
            #Add if statement for checkbox logic
            try:
                self.driver.find_element_by_xpath('//*[@id="_dueDate"]"]')
            except Exception as e:
                return False
            return True

    def late_submission_check(self, state, wait = None):
        try:
            if state:
                self.driver.find_element_by_xpath('//*[@id="doNotAllowLateSubmission"]').click()
                time.sleep(wait)
            else:
               #if not state need to assure that box is NOT checked
        except Exception as e:
            return False
        return True







class AssignmentOptions(Editor):

    POINTS_POSSIBLE = '//*[@id="possible"]'
    MAKE_ASSIGNMENT_AVAILABLE = '//*[@id="isAvailable"]'
    START_LIMIT_AVAILABILITY = '//*[@id="start_limitAvailability"]'
    END_LIMIT_AVAILABILITY = '//*[@id="end_limitAvailability"]'
    TRACK_NUMBER_OF_VIEWS = '//*[@id="isTracked"]'

    def __init__(self):
        return

    def nav_tests(self, element, wait = None):
        try:
            self.driver.find_element_by_xpath('//a[@title=' + "\"" + element + " item options" + "\"" ']').click()
            time.sleep(wait)
        except Exception as e:
            return False
        return True

    def due_date_in_use(self, state, wait = None):
        #Add if statement for checkbox logic
        try:
            self.driver.find_element_by_xpath('//*[@id="due_date_in_use"]')
        except Exception as e:
            return False
        return True
