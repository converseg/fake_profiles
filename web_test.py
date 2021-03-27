import selenium
from selenium import webdriver
import time
import random
import numpy as np
import json
import os

#capabilities = {
#  'browserName': 'firefox',
#  'browserVersion': '68.0',
#  'platformName': 'Windows 10',
#  'sauce:options': {}
#}

#use FF 87
bin_path = 'C:/Program Files/Mozilla Firefox/firefox.exe'
ff_binary = webdriver.firefox.firefox_binary.FirefoxBinary(firefox_path=bin_path)
#use test_profile
profile_path = './ff_profiles//test_profile'
ff_profile = webdriver.firefox.firefox_profile.FirefoxProfile(profile_directory=profile_path)

driver = webdriver.Firefox(firefox_profile=ff_profile, firefox_binary=ff_binary) #browser_profile=None

# things that could be useful
#function find_element(by='id') 

driver.get('https://gmail.com')
time.sleep(30)

# need to find temp profile after browsing and copy contents over to the saved FF profile in 'ff_profiles/test_profile'

# temp_profile_path = driver.firefox_profile.path #apparently this doesn't actually work?
print('what does it tell me the FF temp profile is?')
print(driver.firefox_profile.path)
print('Go find the actual FF temp profile path')
driver.get('about:support')
box = driver.find_element_by_id('profile-dir-box')
temp_profile_path = box.text
print('FF temp profile path: ', temp_profile_path)

print('now copy contents to save browsing history')
cwd = os.getcwd()
original_profile = cwd+'\\ff_profiles\\test_profile'
print('saving profile ' + temp_profile_path + ' to ' + original_profile)
os.system('xcopy ' + temp_profile_path + ' ' + original_profile + '/Y /G /K /R /E /S /C /H /Q')
print('files should be copied')

time.sleep(5)

driver.quit() 

#search for a product then click on something
#driver.get('https://youtube.com')
#yt_search = browser.find_elements_by_name('search_query')[0]
#yt_search.send_keys('tennis')
#yt_search.submit()
#time.sleep(3)
#videos = browser.find_elements_by_id('video-title')
#videos[random.randrange(5)].click()
#print("second YT visit cookies:")
#print(c2)

# all profiles visit zillow or show interest in purchasing a home, getting a loan

##dicts = browser.get_cookies()
##for d in dicts:
##    print(d)
##    
##cookie_dir = './cookies_0/'
##for i in range(len(dicts)):
##    with open(cookie_dir+'c'+str(i)+'.json', 'w') as fout:
##        json.dump(dicts[i], fout)
##
##print('dicts dumped')

# I could save the list of cookie dictionaries, then load them each time I start up
# do I still need different versions / installations of Firefox to protect against stateless tracking?
# won't my ip adress still be the same for each fake profile?



