#!/usr/bin/env python

# Developed by Michael Orozco
# iBit IT
# Start dev: 10/16/2015 11:38pm
# End dev: 10/17/2015 1:45am

import argparse, os
import time

from selenium import webdriver

import yaml

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.common.keys import Keys

# from pyvirtualdisplay import Display


class craigslistBot:
    def debug(self, inString):
        print(" [LOG] {BOT} - %s" % inString.encode('utf-8').strip())

    def __init__(self, loginEmail="", loginPass="", contactNumber="", contactName="", postTitle="", postCode="",
                 postContentFile="", price="", waitTime=10):
        # self.display = ""

        # if not os.name == 'nt':
        #     self.display = Display(visible=0, size=(800, 600))
        #     self.display.start()
        #
        # self.client = webdriver.Firefox()
        with open('config.yaml') as fp:
            data = yaml.load(fp)
        self.waitTime = 1
        self.client = webdriver.Chrome()
        self.isLoggedIn = False
        self.loginEmail = data['clistLoginEmail']
        self.loginPass = data['clistLoginPassword']
        self.contactNumber = data['contactNumber']
        self.contactName = data['contactName']
        self.postTitle = data['postTitle']
        self.postCode = data['postCode']
        self.postContent = data['postContent']
        self.price = data['price']
        self.odometer = data['odometer']
        self.vin = data['vin']
        self.condition = data['condition']
        self.cylinders = data['cylinders']
        self.fuel = data['fuel']
        self.drive = data['drive']
        self.paintColor = data['color']
        self.size = data['size']
        self.transmission = data['transmission']
        self.titleStatus = data['titleStatus']
        self.type = data['carType']
        self.modelYear = data['modelYear']
        self.makeAndModel = data['makeAndModel']

        self.chains = webdriver.ActionChains(self.client)

    def login(self):
        self.debug("Navigating to craigslist login")
        self.client.get("https://accounts.craigslist.org/login")
        self.debug("Logging in")
        self.client.find_element_by_css_selector("#inputEmailHandle").send_keys(self.loginEmail)
        self.client.find_element_by_css_selector("#inputPassword").send_keys(self.loginPass)
        # self.client.find_element_by_css_selector("form[name='login'] .accountform-btn button").click()
        self.client.find_element_by_class_name("accountform-btn").click()

        try:
            self.client.find_element_by_class_name('account-header')
        except NoSuchElementException:
            self.debug("Not logged in")
            return
        self.debug("Logged in")
        self.isLoggedIn = True

    def dropdown(self, menu, keys):
        self.chains.click(menu).send_keys(keys).send_keys(Keys.ENTER).perform()
        self.chains.reset_actions()
        time.sleep(self.waitTime)

    def createPost(self):
        # if not self.isLoggedIn:
        #     return 0

        self.debug("Navigating to post page")
        self.client.get("http://post.craigslist.org/c/ral")
        self.debug("Selecting 'For Sale By Owner'")
        self.client.find_element_by_xpath("//input[@value='fso']").click()
        time.sleep(self.waitTime)
        self.debug("Selecting 'Cars & Trucks - By Owner'")
        self.client.find_element_by_xpath("//input[@value='145']").click()
        time.sleep(self.waitTime)

        self.debug("Trying to fill in email")
        try:
            self.client.find_element_by_css_selector('#FromEMail').send_keys(self.loginEmail)
        except NoSuchElementException:
            self.debug("Not avaliable")
        try:
            self.client.find_element_by_css_selector('#FromEMail').send_keys(self.loginEmail)
        except NoSuchElementException:
            self.debug("Not avaliable")

        self.client.find_element_by_css_selector("#PostingTitle").send_keys(self.postTitle)
        time.sleep(self.waitTime)
        self.client.find_element_by_xpath("//input[@name='price']").send_keys(self.price)
        time.sleep(self.waitTime)
        self.client.find_element_by_css_selector("#postal_code").send_keys(self.postCode)
        time.sleep(self.waitTime)
        self.debug("Setting options")
        if self.vin is not None:
            self.client.find_element_by_xpath("//input[@name='auto_vin']").send_keys(self.vin)
            time.sleep(self.waitTime)
        if self.odometer is not None:
            self.client.find_element_by_xpath("//input[@name='auto_miles']").send_keys(self.odometer)
            time.sleep(self.waitTime)
        self.client.find_element_by_xpath("//input[@name='auto_make_model']").send_keys(self.makeAndModel)
        time.sleep(self.waitTime)
        if self.condition is not None:
            menu = self.client.find_element_by_xpath("//label[contains(@class, 'condition')]")
            if self.condition == "like new":
                self.dropdown(menu, 'like')
            else:
                self.dropdown(menu, self.condition)
        if self.cylinders is not None:
            menu = self.client.find_element_by_xpath("//label[contains(@class, 'cylinders')]")
            self.dropdown(menu, self.cylinders)

        if self.drive is not None:
            menu = self.client.find_element_by_xpath("//label[contains(@class, 'drive')]")
            self.dropdown(menu, self.drive)
        # Set Fuel -- Required
        menu = self.client.find_element_by_xpath("//label[contains(@class, 'fuel')]")
        self.dropdown(menu, self.fuel)
        if self.paintColor is not None:
            menu = self.client.find_element_by_xpath("//label[contains(@class, 'paint')]")
            self.dropdown(menu, self.paintColor)
        if self.size is not None:
            menu = self.client.find_element_by_xpath("//label[contains(@class, 'size')]")
            self.dropdown(menu, self.size)
        # Set Title Status -- Required
        menu = self.client.find_element_by_xpath("//label[contains(@class, 'auto_title_status')]")
        self.dropdown(menu, self.titleStatus)
        # Set Transmission type -- Required
        menu = self.client.find_element_by_xpath("//label[contains(@class, 'transmission')]")
        self.dropdown(menu, self.transmission)
        if self.type is not None:
            menu = self.client.find_element_by_xpath("//label[contains(@class, 'auto_bodytype')]")
            self.dropdown(menu, self.type)
        # Set Model Year -- Required
        menu = self.client.find_element_by_xpath("//label[contains(@class, 'year')]")
        self.dropdown(menu, self.modelYear)
        self.client.find_element_by_css_selector("#PostingBody").send_keys(self.postContent)
        self.debug("Checking 'Okay to contact by phone'")
        self.client.find_element_by_xpath("//input[contains(@name, 'contact_phone_ok')]").click()
        time.sleep(self.waitTime)
        self.debug("Checking 'Okay to contact by text'")
        self.client.find_element_by_xpath("//input[contains(@name, 'contact_text_ok')]").click()
        time.sleep(self.waitTime)
        self.debug("Filling in contact phone number")
        self.client.find_element_by_xpath("//input[@name='contact_phone']").send_keys(self.contactNumber)
        time.sleep(self.waitTime)
        self.debug("Filling in contact name")
        self.client.find_element_by_xpath("//input[contains(@name, 'contact_name')]").send_keys(self.contactName)
        time.sleep(self.waitTime)

        self.debug("Clicking continue")
        self.client.find_element_by_css_selector('button[value="continue"]').click()
        self.debug("Clicking continue after map")
        self.client.find_element_by_xpath("//button[contains(@class, 'continue')]").click()
        self.debug("Upload Images from directory")

        cwd = os.getcwd()
        for i in os.listdir('photos'):
            path = cwd + "/photos/" + i
            self.client.find_element_by_xpath("//input[@type='file']").send_keys(path)

        time.sleep(20)



def main():
    startExecTime = time.time()

    clBot = craigslistBot()
    clBot.login()
    clBot.createPost()
    endExecTime = time.time()
    clBot.debug("Execution time: %s seconds" % int(endExecTime - startExecTime))

    print("Finished")

    return 0


main()
