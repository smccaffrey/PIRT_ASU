from lmsa.lms.blackboard import BlackBoard
from bs4 import BeautifulSoup
import time

class Editor(BlackBoard):

    def __init__(self, driver):
        self.driver = driver
        #need to check to see if this passes our driver in
        #super(Editor, self).__init__(driver)
        #edit_test_options()

    EDIT_TEST_OPTIONS = '//a[@title="Edit the Test Options"]'

    #edit_assignment_options()
    EDIT_ASSIGNMENT_OPTIONS = '//a[@title="Edit"]'

    CANCEL = '//*[@id="bottom_submitButtonRow"]/input[1]'
    SUBMIT = '//*[@id="bottom_submitButtonRow"]/input[2]'



    def form_selector(self, element):
        try:
            self.driver.find_element_by_xpath('//a[@title=' + "\"" + element + " item options" + "\"" ']').click()
            time.sleep(wait)
        except Exception as e:
            return False
        return True

    def edit_test_options(self, wait = None):
        try:
            self.driver.find_element_by_xpath(Editor.EDIT_TEST_OPTIONS).click()
            time.sleep(wait)
        except Exception as e:
            return False
        return True

    def edit_assignment_options(self, wait = None):
        try:
            self.driver.find_element_by_xpath(Editor.EDIT_ASSIGNMENT_OPTIONS).click()
            time.sleep(wait)
        except Exception as e:
            return False
        return True

    def check_state(self, xpath):
        x = self.driver.find_element_by_xpath(xpath)
        if x.is_selected() == True:
            return True
        return False

    def toggle_state(self, xpath):
        if self.check_state() != DESIRED_STATE:
            self.driver.find_element_by_xpath(xpath).click()
            return True
        return False

    def cancel(self, wait = None):
        try:
            self.driver.find_element_by_xpath(Editor.CANCEL).click()
            time.sleep(wait)
        except Exception as e:
            return False
        return True

    def submit(self, wait = None):
        try:
            self.driver.find_element_by_xpath(Editor.SUBMIT).click()
            time.sleep(wait)
        except Exception as e:
            return False
        return True


class TestOptions(Editor):
    """
    All options for editing 'Tests' on BlackBoard Learn.
    Time.sleep() doesn't need to be called during these functions as all options
    will be executed on a single form each time.
    """
    #open_test_new_window()
    OPEN_TEST_IN_NEW_WINDOW_YES = '//*[@id="yesRadio"]'
    OPEN_TEST_IN_NEW_WINDOW_NO = '//*[@id="noRadio"]'

    #make_link_available()
    MAKE_LINK_AVAILABLE_YES = '//*[@id="fIsLinkVisible1"]'
    MAKE_LINK_AVAILABLE_NO = '//*[@id="fIsLinkVisible2"]'

    #create_announcment
    CREATE_ANNOUNCEMENT_YES = '//*[@id="fCreateAnnouncement1"]'
    CREATE_ANNOUNCEMENT_NO = '//*[@id="fCreateAnnouncement2"]'

    #multiple_attempts
    MULTIPLE_ATTEMPTS_CHECK = '//*[@id="fIsMultipleAttempts"]'
    ALLOW_UNLIMITED_ATTEMPTS = '//*[@id="fIsUnlimitedAttempts"]'
    NUMBER_OF_ATTEMPTS = '//*[@id="fNumMultipleAttempts"]'
    NUMBER_OF_ATTEMPTS_VALUE = '//*[@id="attemptCount"]'

    #force_completion
    FORCE_COMPLETION_CHECK = '//*[@id="fIsForceComplete"]'

    #start_restrict
    START_RESTRICT_CHECK = '//*[@id="start_restrict"]'
    START_RESTRICT_DATE = '//*[@id="dp_restrict_start_date"]'
    START_RESTRICT_TIME = '//*[@id="tp_restrict_start_time"]'

    #end_restrict
    END_RESTRICT_CHECK = '//*[@id="end_restrict"]'
    END_RESTRICT_DATE = '//*[@id="dp_restrict_end_date"]'
    END_RESTRICT_TIME = '//*[@id="tp_restrict_end_time"]'

    #due_date
    DUE_DATE_CHECK = '//*[@id="_dueDate"]'
    DUE_DATE_DATE = '//*[@id="dp_dueDate_date"]'
    DUE_DATE_TIME = '//*[@id="tp_dueDate_time"]'

    #late_submission
    LATE_SUBMISSION_CHECK = '//*[@id="doNotAllowLateSubmission"]'

    def open_test_new_window(self, state):
        if state:
            self.driver.find_element_by_xpath(TestOptions.OPEN_TEST_IN_NEW_WINDOW_YES)
            return True
        self.driver.find_element_by_xpath(TestOptions.OPEN_TEST_IN_NEW_WINDOW_NO)
        return False

    def make_link_available(self, state):
        if state:
            self.driver.find_element_by_xpath(TestOptions.MAKE_LINK_AVAILABLE_YES)
            return True
        self.driver.find_element_by_xpath(TestOptions.MAKE_LINK_AVAILABLE_NO)
        return False

    def create_announcment(self, state):
        if state:
            self.driver.find_element_by_xpath(TestOptions.CREATE_ANNOUNCEMENT_YES)
            return True
        self.driver.find_element_by_xpath(TestOptions.CREATE_ANNOUNCEMENT_NO)
        return False

    def multiple_attempts(self):
        return

    def force_completion(self):
        return

    def start_restrict(self):
        return

    def end_restrict(self):
        return

    def due_date(self, state, date, time):
        current_state = self.check_state(TestOptions.DUE_DATE_CHECK)
        if state != current_state:
            self.toggle_state(TestOptions.DUE_DATE_CHECK)
        if current_state:
            self.driver.find_element_by_xpath(TestOptions.DUE_DATE_VALUE).send_keys(date)
            self.driver.find_element_by_xpath(TestOptions.DUE_DATE_TIME).send_keys(time)

    def late_submission(self):
        return


class AssignmentOptions(Editor):

    def __init__(self):
        return
    #due_date()
    DUE_DATE_CHECK = '//*[@id="due_date_in_use"]'
    DUE_DATE_VALUE = '//*[@id="dp_dueDate_date"]'
    DUE_DATE_TIME = '//*[@id="tp_dueDate_time"]'

    #points_possible()
    POINTS_POSSIBLE = '//*[@id="possible"]'

    #make_assignment_available()
    MAKE_ASSIGNMENT_AVAILABLE = '//*[@id="isAvailable"]'

    #Need to map 'Submission Details' section
    #Need to map 'Grading Options' section
    #Need to map 'Display of Grades' section

    #start_limit_availability()
    START_LIMIT_AVAILABILITY = '//*[@id="start_limitAvailability"]'
    START_LIMIT_AVAILABILITY_DATE = '//*[@id="dp_limitAvailability_start_date"]'
    START_LIMIT_AVAILABILITY_TIME = '//*[@id="tp_limitAvailability_start_time"]'

    #end_limit_availability()
    END_LIMIT_AVAILABILITY = '//*[@id="end_limitAvailability"]'
    END_LIMIT_AVAILABILITY_DATE = '//*[@id="dp_limitAvailability_end_date"]'
    END_LIMIT_AVAILABILITY_TIME = '//*[@id="tp_limitAvailability_end_time"]'

    #track_number_of_views()
    TRACK_NUMBER_OF_VIEWS_CHECK = '//*[@id="isTracked"]'

    def due_date(self):
        return

    def points_possible(self):
        return

    def make_assignment_available(self):
        return

    def start_limit_availability(self):
        return

    def end_limit_availability(self):
        return

    def track_number_of_views(self):
        return
