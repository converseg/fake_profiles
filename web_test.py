import selenium
from selenium import webdriver
import time
import random
import numpy as np
import json

# capabilities = {
#   'browserName': 'firefox',
#   'browserVersion': '68.0',
#   'platformName': 'Windows 10',
#   'sauce:options': {}
# }

# testing profile: vw829vbs.default-release on FF87
# profile 1: nstcxnhb.default-release-4 on FF81

binary_path = 'C:/Program Files/Mozilla Firefox87/firefox.exe' # my testing installation
ff_binary = webdriver.firefox.firefox_binary.FirefoxBinary(firefox_path=binary_path)
profile_path = 'C:\\Users\\conve_000\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\vw829vbs.default-release'
ff_profile = webdriver.firefox.firefox_profile.FirefoxProfile(profile_directory=profile_path)

print('ff_profile path: ' + ff_profile.path)


browser = webdriver.Firefox(firefox_binary=ff_binary, firefox_profile=ff_profile) #browser_profile=None
# this isn't actually getting me the FF profile or any browsing history

# things that could be useful
#function browser.add_cookie(cookie_dict) # do I need to save all cookies, then add them?
#function browser.get_cookies() -- returns a set of dictionaries
#function browser.delete_all_cookies()
#function find_element(by='id') 

print('set profile path: ' + profile_path)
print('temp profile path: ' + browser.firefox_profile.path)

#search for a product then click on something
browser.get('https://youtube.com')
yt_search = browser.find_elements_by_name('search_query')[0]
yt_search.send_keys('tennis')
yt_search.submit()
time.sleep(30)
videos = browser.find_elements_by_id('video-title')
videos[random.randrange(5)].click()
time.sleep(3)
# c1 = browser.get_cookies()
# print("First YT visit cookies:")
# print(c1)
# print('\n')
# #go to a specific channel and click on a random video or two
# browser.get('https://www.google.com/search?q=pizza')
# browser.get('https://amazon.com')
# # set up an email address for them and visit it or send an email
# time.sleep(2)
# browser.get('https://youtube.com')
# yt_search = browser.find_elements_by_name('search_query')[0]
# yt_search.send_keys('pizza')
# yt_search.submit()
# time.sleep(3)
# videos = browser.find_elements_by_id('video-title')
# videos[random.randrange(5)].click()
# time.sleep(3)
# c2 = browser.get_cookies()
# print("second YT visit cookies:")
# print(c2)

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
#browser.quit() 
browser.close()


# Ideas for different profiles:
# - sports profile
# - video game profile
# - artist profile
# - musician profile
# - online shopping profile
# - news articles (left-leaning) - interests in Race - Black Panther, Judas & Black Messiah, Kendrick Lamar, Ibram X Kendi, etc
# - fox news and alt-right
# - one person only looks up info about housing / mortgage loans (control profile 1)
# - one profile doesn't have any browsing history (control profile 2)
# - do stereotype reinforcements cause an ethical issue?


