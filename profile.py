import time
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Profile():
    def __init__(self, profile_num, params={}):
        self.params = params
        self.profile_num = profile_num
        if profile_num == 0:
            profile_directory = 'C:\\Users\\gconverse\\Desktop\\privacy_law\\project\\fake_profiles\\ff_profiles\\test_profile'
        else:
            #profile_directory = 'C:\\Users\\gconverse\\Desktop\\privacy_law\\project\\fake_profiles\\ff_profiles\\ff_profile_'+str(self.profile_num) #TODO: uncomment this line
            # for now, just always use the test profile so I don't screw up browsing histories
            profile_directory = 'C:\\Users\\gconverse\\Desktop\\privacy_law\\project\\fake_profiles\\ff_profiles\\test_profile' #TODO: remove this line
        self.ff_profile_dir = profile_directory

        # personality also indicates the tab to click on at trackthis.link
        
        if profile_num == 1:
            self.ff_version = 81
            self.personality = 'hypebeast'
        elif profile_num == 2:
            self.ff_version = 83
            self.personality = 'rich'
        elif profile_num == 3:
            self.ff_version = 84
            self.personality = 'doomsday'
        elif profile_num == 4:
            self.ff_version = 85
            self.personality = 'influencer'
        elif profile_num == 5:
            self.ff_version = 86
            self.personality = 'None'
        else:
            self.ff_version = 87  # used for dev purposes
            self.personality = 'rich'
        #comment this out later -- for development purposes only
        self.ff_version = 87 # always use FF 87 in development TODO: remove this
        self.ff_bin_path = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe' #TODO: remove this
        #self.ff_bin_path = 'C:\\Program Files\\Mozilla Firefox'+self.ff_version+'\\firefox.exe' #TODO: uncomment this line
        self.ff_binary = webdriver.firefox.firefox_binary.FirefoxBinary(firefox_path=self.ff_bin_path)
        # TODO: is it best to make the driver an attribute, or pass it into functions?
        self.driver = None
        

    def start_browser(self):
        self.ff_profile = webdriver.firefox.firefox_profile.FirefoxProfile(self.ff_profile_dir) # it needs to make a new temp file each time I start it
        self.driver = webdriver.Firefox(firefox_profile=self.ff_profile, firefox_binary=self.ff_binary)


    def visit_sites(self):
        if self.driver is None:
            self.start_browser()
        #driver = webdriver.Firefox(firefox_profile=self.ff_profile, firefox_binary=self.ff_binary)
        if self.profile_num < 5: # profile 5 doesn't build up that browsing history
            self.visit_trackthis()
            time.sleep(5)
        self.visit_loan_sites()
        time.sleep(15)
        self.save_browsing_history()
        time.sleep(5)
        self.end_session()

    def visit_trackthis(self):
        print('go to trackthis.link and open tabs')
        self.driver.get('https://trackthis.link')
        personality_tab = self.driver.find_element_by_class_name('tab.tab-slanted.' + self.personality)
        personality_tab.click()
        button = self.driver.find_element_by_class_name('c2a.button-slanted.md-trigger')
        button.click() # goes to a warning page first
        my_buttons = self.driver.find_elements_by_class_name('c2a.button-slanted')
        open_tabs_button = my_buttons[-1]
        open_tabs_button.click()
        # it would be better to open these in tabs, not windows
        #ActionChains(self.driver) \
        #        .key_down(Keys.CONTROL) \
        #        .click(open_tabs_button) \
        #        .key_up(Keys.CONTROL) \
        #        .perform()
        print('I have opened a bunch of tabs related to: ' + self.personality)

    def visit_loan_sites(self):
        print('search about loans etc')
        self.driver.get('https://www.bankrate.com/calculators/mortgages/mortgage-calculator.aspx') # bankrate might be a good fintech lender to look at too

    def save_browsing_history(self):
        print('*********')
        print('save the browsing history for Profile ' + str(self.profile_num) + ': '+ self.personality)
        print('*********')
        self.driver.get('about:support')
        box = self.driver.find_element_by_id('profile-dir-box')
        temp_profile_path = box.text
        print('copy contents from temp to saved profile')
        print('saving profile ' + temp_profile_path + ' to ' + self.ff_profile_dir)
        os.system('xcopy ' + temp_profile_path + ' ' + self.ff_profile_dir + ' /Y /G /K /R /E /S /C /H /Q')
        print('browsing history copied to permanent location')


    def end_session(self):
        self.driver.quit()
        self.driver = None #TODO: is this a good idea?


