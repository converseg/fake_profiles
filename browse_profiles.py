import selenium
from selenium import webdriver
import time
import random
import numpy as np
import os
import json
import pickle

### This file is no longer in use -- could delete later

# search loan, home, mortgage info
def search_loans(browser):
    browser.get('https://zillow.com')
    # search zipcode, click on a house
    browser.get('https://google.com')
    #search = browser.find_elements_by_name('q')
    #search.send_keys('best mortgage lenders')
    #search.submit()
    #links = browser.find_elements_by_class_name(' ') # need to make sure not to click on an ad
    #links[random.randrange(3)].click()
    browser.get('https://youtube.com')
    yt_search = browser.find_elements_by_name('search_query')[0]
    yt_search.send_keys('how to get a mortgage loan')
    yt_search.submit()
    videos = browser.find_elements_by_id('video-title')
    videos[random.randrange(5)].click()
    return browser

#def load_cookies(browser, profile_num):
#    cookie_dir = 'cookies_'+str(profile_num)+'/'
#    print("Browser:")
#    print(browser) #what if I just save this WebDriver object
#    for filename in os.listdir(cookie_dir):
#        f = open(cookie_dir+filename,'r')
#        cookie = json.load(f)
#        print(cookie)
#        browser.add_cookie(cookie) # can only add a cookie from example.com after going there (browser.get(example.com))
#    return browser

def save_cookies(cookie_list, domain_list, c_dir):
    print("Try to save cookies")
    list_of_cookie_lists = []
    domain_order_dict = {}
    for i in range(len(domain_list)):
        list_of_cookie_lists.append([])
        domain_order_dict[domain_list[i]] = i

    print('domain order dict: ')
    print(domain_order_dict)
    counter = len(domain_list)
    for cookie in cookie_list: # all cookies
        domain = cookie.get('domain') # returns None if domain doesn't exist
        if domain[1:] in domain_list:
            ind = domain_order_dict[domain[1:]]
        else:
            print('cookie found for a new domain')
            domain_list.append(domain[1:])
            list_of_cookie_lists.append([])
            domain_order_dict[domain[1:]] = counter
            ind = counter
            counter = counter + 1
        list_of_cookie_lists[ind].append(cookie)
    
    print("List of cookie lists:")
    print(list_of_cookie_lists)
    print("write pickle files")
    for i in range(len(list_of_cookie_lists)):
        cookie_list = list_of_cookie_lists[i]
        domain = domain_list[i]
        filename =  c_dir+domain+'.pkl'
        print('writing file ' + filename)
        pickle.dump(cookie_list, open(filename, 'wb'))

# Profile 1: Sports
def profile1_visit():
    ff_path = 'C:/Program Files/Mozilla Firefox/firefox.exe'
    #ff_profile = webdriver.FirefoxProfile(profile_directory='./p1')
    #browser = webdriver.Firefox(firefox_profile=ff_profile, firefox_binary=ff_path) # find out how to specify installation/version
    ff_profile = webdriver.firefox.firefox_profile.FirefoxProfile(profile_directory='./p1')
    print(ff_profile.path)
    browser = webdriver.firefox.webdriver.WebDriver(firefox_profile=ff_profile, firefox_binary=ff_path)
    #browser = load_cookies(browser, 1) # need to visit a site, then add the cookies corresponding to that domain

    c_dir = 'cookies_1/'

    # include housing/loan sites here
    domain_list =['youtube.com'] # ['zillow.com', 'youtube.com', 'google.com', 'espn.com']
    #pickle_list = ['zillow.com.pkl', 'youtube.com.pkl', 'google.com.pkl', 'espn.com.pkl'] # same as domains, but for pickle files
    list_of_cookie_lists = []

    print("Load in cookies:")
    # First, go to each domain and add the associated cookies
    for i in range(len(domain_list)):
        print('load cookies: ' + domain_list[i]) 
        try:
            cookies = pickle.load(open(c_dir+domain_list[i]+'.pkl', 'rb'))
        except:
            print('there are no previously saved cookies')
            cookies = []
        list_of_cookie_lists.append(cookies)
        print('visit site and add cookies:')
        browser.get('https://'+domain_list[i])
        for j in range(len(cookies)): # add each cookie
            browser.add_cookie(cookies[j])

    print('number of cookies pre-browse:')
    print(len(browser.get_cookies()))
    print(browser.get_cookies())
    # build browsing history
    browser.get('https://youtube.com')
    #browser.get('https://google.com')
    #browser.get('https://espn.com')
    #browser.get('https://amazon.com')

    # workflow:
    # brwoser.get('example.com')
    # add cookies related to example.com
    # browser.get('example.com')
    # do things on example.com

    print("after visiting youtube:")
    print(len(browser.get_cookies())) # get_cookies only gets the cookies from the CURRENT domain
    print(browser.get_cookies())
 

    # search homes, loans, financial stuff
    browser = search_loans(browser)

    # save cookies
    all_cookies = browser.get_cookies()
    print('number of cookies after browsing housing loans:')
    print(len(all_cookies))
    print(all_cookies)
    save_cookies(all_cookies, domain_list, c_dir)
    print('just saved cookies:')

def profile2_visit():
    browser = webdriver.Firefox()
    browser = webdriver.Firefox() # find out how to specify installation/version
    browser = load_cookies(browser, 2) # load cookies
    # save cookies
    save_cookies(browser, 2)


def profile3_visit():
    browser = webdriver.Firefox()
    browser = webdriver.Firefox() # find out how to specify installation/version
    browser = load_cookies(browser, 3) # load cookies
    # save cookies
    save_cookies(browser, 3)


def profile4_visit():
    browser = webdriver.Firefox()
    browser = webdriver.Firefox() # find out how to specify installation/version
    browser = load_cookies(browser, 4) # load cookies
    # save cookies
    save_cookies(browser, 4)


def profile5_visit():
    browser = webdriver.Firefox()
    browser = webdriver.Firefox() # find out how to specify installation/version
    browser = load_cookies(browser, 5) # load cookies
    # save cookies
    save_cookies(browser, 5)


def profile6_visit():
    browser = webdriver.Firefox()
    browser = webdriver.Firefox() # find out how to specify installation/version
    browser = load_cookies(browser, 6) # load cookies
    # save cookies
    save_cookies(browser, 6)



#### ----- script ----- ####
def main():
    profiles = [profile1_visit] #, profile2_visit, profile3_visit, profile4_visit, profile5_visit, profile6_visit] 
    
    # run this each day for a week
    for profile in profiles:
        profile()


if __name__ == '__main__':
    main()
