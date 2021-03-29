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
        print('Using profile at ' + self.ff_profile_dir)
        print('Assuming personality ' + self.personality)
        print('**************')
        

    def start_browser(self):
        self.ff_profile = webdriver.firefox.firefox_profile.FirefoxProfile(self.ff_profile_dir) # it needs to make a new temp file each time I start it
        self.driver = webdriver.Firefox(firefox_profile=self.ff_profile, firefox_binary=self.ff_binary)


    def visit_sites(self, save_history=True):
        if self.driver is None:
            self.start_browser()
        if self.profile_num < 5: # profile 5 doesn't build up that browsing history
            self.visit_trackthis()
            time.sleep(5)
        self.visit_loan_sites()
        time.sleep(5)
        if save_history:
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
        time.sleep(20)
        window_handles = self.driver.window_handles
        print('**number of windows open: ' + str(len(window_handles)))

    def visit_loan_sites(self):
        # TODO: probably faster to do all this in new windows so don't have to wait for page to load???
        print('search about loans etc')
        # visit the site for each financialy institution and navigate to home mortgage
        # Wells Fargo
        self.driver.get('https://wellsfargo.com')
        self.driver.get('https://www.wellsfargo.com/home-mortgage')
        self.driver.get('https://www.wellsfargo.com/mortgage/rates')

        # JP Morgan Chase
        self.driver.get('https://www.chase.com')
        self.driver.get('https://www.chase.com/personal/mortgage')
        self.driver.get('https://www.chase.com/personal/mortgage/mortgage-rates')

        # Bank of America
        self.driver.get('https://www.bankofamerica.com')
        self.driver.get('https://www.bankofamerica.com/mortgage/first-time-home-buyer')
        self.driver.get('https://www.bankofamerica.com/mortgage/home-mortgage')

        # QuickenLoans
        self.driver.get('https://quickenloans.com') # do I need to do any sort of time.sleep on each page?
        self.driver.get('https://www.quickenloans.com/mortgage-rates?qlsource=nav')
        self.driver.get('https://rocketmortgage.com')
        self.driver.get('https://www.rocketmortgage.com/l2/bamv2/step/1?LoanPurpose=purchase&qls=RBA_rocketme.0000000018') # is going to the URL the same as clicking the link?

        # LoanDepot
        self.driver.get('https://www.loandepot.com')
        self.driver.get('https://www.loandepot.com/buying-a-house')
        self.driver.get('https://www.loandepot.com/buying-a-house/home-loan-rates')

        # United Shore
        # I'm still not convinced that this is 'Fintech' - also UWM.com is for lenders, not lendees
        self.driver.get('https://www.uwm.com/')
        self.driver.get('https://www.uwm.com/price-a-loan/uwm-rates')
        self.driver.get('https://www.uwm.com/price-a-loan/exclusives/home-value-estimator')

        # go to zillow and look at homes
        self.driver.get('https://zillow.com')
        search_bar = self.driver.find_element_by_class_name('react-autosuggest__container.num-rows-5')
        #search_bar.send_keys('52246') # TODO: find out a good zipcode to use
        #search_bar.submit() # it asks another question (rent/buy)
        self.driver.get('https://www.zillow.com/homes/52246_rb/')
        # should I click on a home?
        self.driver.get('https://www.zillow.com/home-loans')
        self.driver.get('https://www.zillow.com/mortgage-calculator')
        self.driver.get('https://google.com')
        # do google search
        self.driver.get('https://www.bankrate.com/calculators/mortgages/mortgage-calculator.aspx') # bankrate might be a good fintech lender to look at too
        self.driver.get('https://www.nerdwallet.com/best/mortgages/mortgage-lenders')
        self.driver.get('https://loans.usnews.com/mortgage-lenders')

        # Search on youtube and google for mortgage loan stuff

        print('Done searching loan stuff')


    def save_browsing_history(self):
        print('save the browsing history for Profile ' + str(self.profile_num) + ': '+ self.personality)
        print('*********')
        self.driver.get('about:support')
        box = self.driver.find_element_by_id('profile-dir-box')
        temp_profile_path = box.text
        print('saving profile ' + temp_profile_path + ' to ' + self.ff_profile_dir)
        os.system('xcopy ' + temp_profile_path + ' ' + self.ff_profile_dir + ' /Y /G /K /R /E /S /C /H /Q')
        print('browsing history copied to permanent location')


    def end_session(self):
        print('Ending browsing session')
        self.driver.quit()
        self.driver = None #TODO: is this a good idea?


