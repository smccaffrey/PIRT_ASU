from lmsa.lms.blackboard import BlackBoard
from bs4 import BeautifulSoup
import time

class Editor(BlackBoard):

    def __init__(self, driver):
        #need to check to see if this passes our driver in
        super(Editor, self).__init__(driver)

    def due_date(self, date, wait = None):
        try:
            self.driver.find_element_by_id('dp_dueDate_date').clear()
            self.driver.find_element_by_id('dp_dueDate_date').send_keys(date)
            time.sleep(wait)
        except Exception as e:
            return False
        return True

    def due_date_time(self, time, wait = None):
        try:
            driver.find_element_by_id('tp_dueDate_time').clear()
            driver.find_element_by_id('tp_dueDate_time').send_keys(time)
            time.sleep(wait)
        except Exception as e:
            return False
        return True

    def cancel(self, wait = None):
        try:
            self.driver.find_element_by_name('bottom_Cancel').click()
            time.sleep(wait)
        except Exception as e:
            pass

    def submit(self, wait = None):
        try:
            self.driver.find_element_by_name('bottom_submit').click()
            time.sleep(wait)
        except Exception as e:
            pass


class TestOptions(Editor):

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
            self.driver.find_element_by_xpath('//a[@title="Edit the Test Options"]').click()
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

    XPATHS = {
        'POINTS_POSSIBLE':'//*[@id="possible"]'
        'MAKE_ASSIGNMENT_AVAILABLE':'//*[@id="isAvailable"]',
        'START_LIMIT_AVAILABILITY':'//*[@id="start_limitAvailability"]',
        'END_LIMIT_AVAILABILITY':'//*[@id="end_limitAvailability"]',
        'TRACK_NUMBER_OF_VIEWS':'//*[@id="isTracked"]'}

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
