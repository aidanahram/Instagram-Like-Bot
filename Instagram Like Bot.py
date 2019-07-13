#!/usr/bin/env python
import selenium 
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys as keys
import time
import random

class insta_bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()
        
    def login(self):
        bot = self.bot
        url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
        bot.get(url)
        #wait for the page to load
        time.sleep(3)
        user = bot.find_element_by_name('username')
        user.send_keys(self.username)
        passw = bot.find_element_by_name('password')
        passw.send_keys(self.password)
        #sometimes the login button changes xpaths so it'll try both
        try:
            login = bot.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[6]/button/div')
        except: 
            try: 
                login = bot.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
            except:
                pass
        login.click()
        time.sleep(3)
        #sometimes asks to enable notifications, If it does appear it clicks not now
        try:
            notnow = bot.find_element_by_class_name('HoLwm')
            notnow.click()
        except:
            pass
    
    def search(self, hastag):
        bot = self.bot
        search = bot.find_element_by_class_name('x3qfX')
        search.clear()
        search.send_keys(hastag)
        search.click()
        time.sleep(0.5)
        for x in range(3):
            search.click()
            search.send_keys(keys.ENTER)
            time.sleep(random.random())
    
    def give_likes(self):
        bot = self.bot
        #first post 
        post = bot.find_element_by_class_name('_9AhH0')
        post.click()
        #sleep so the bot doesn't get detected
        while 1:
            time.sleep(random.uniform(1.0, 3.0))
            try:
                #try to see if the post is already liked, if yes go to net one
                liked = bot.find_element_by_class_name('glyphsSpriteHeart__filled__24__red_5')
                nextpost = bot.find_element_by_class_name('coreSpriteRightPaginationArrow')
                nextpost.click()
            except:
                #instagram likes switching up the like button a lot 
                try:
                    like = bot.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span')
                    like.click()
                except:
                    try:
                        like = bot.find_element_by_class_name('glyphsSpriteHeart__outline__24__grey_9')
                        like.click()
                    except:
                        try:
                            like = bot.find_element_by_class_name('u-__7')
                            like.click()
                        except:   
                            try:
                                like = bot.find_element_by_class_name('dCJp8')
                                like.click()
                            except:   
                                try:
                                    like = bot.find_element_by_class_name('afkep')
                                    like.click()
                                except:   
                                    try: 
                                        like = bot.find_element_by_class_name('_0mzm-') 
                                        like.click()
                                    except:
                                        #if all else fails lets just click move onto next post
                                        nextpost = bot.find_element_by_class_name('coreSpriteRightPaginationArrow')
                                        nextpost.click()
                                        time.sleep(random.uniform(1.0, 3.0))
            #sleep so the bot doesn't get detected
            time.sleep(random.uniform(1.0, 3.0))
            nextpost = bot.find_element_by_class_name('coreSpriteRightPaginationArrow')
            nextpost.click()
            
    #if you got the page open alreadly loaded up to a post you can you this to keep it going
    def start_from_here(self):
         while 1:
            time.sleep(random.uniform(1.0, 3.0))
            try:
                #try to see if the post is already liked, if yes go to net one
                liked = bot.find_element_by_class_name('glyphsSpriteHeart__filled__24__red_5')
                nextpost = bot.find_element_by_class_name('coreSpriteRightPaginationArrow')
                nextpost.click()
            except:
                #instagram likes switching up the like button a lot 
                try:
                    like = bot.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span')
                    like.click()
                except:
                    try:
                        like = bot.find_element_by_class_name('glyphsSpriteHeart__outline__24__grey_9')
                        like.click()
                    except:
                        try:
                            like = bot.find_element_by_class_name('u-__7')
                            like.click()
                        except:   
                            try:
                                like = bot.find_element_by_class_name('dCJp8')
                                like.click()
                            except:   
                                try:
                                    like = bot.find_element_by_class_name('afkep')
                                    like.click()
                                except:   
                                    try: 
                                        like = bot.find_element_by_class_name('_0mzm-') 
                                        like.click()
                                    except:
                                        #if all else fails lets just click move onto next post
                                        nextpost = bot.find_element_by_class_name('coreSpriteRightPaginationArrow')
                                        nextpost.click()
                                        time.sleep(random.uniform(1.0, 3.0))
            #sleep so the bot doesn't get detected
            time.sleep(random.uniform(1.0, 3.0))
            nextpost = bot.find_element_by_class_name('coreSpriteRightPaginationArrow')
            nextpost.click()


machine = insta_bot('YOUR USERNAME', 'YOUR PASSWORD')
machine.login()
time.sleep(2)
#make sure to include the hastag symbol in the search function
machine.search('#YOUR HASTAG')
time.sleep(3)
machine.give_likes()







