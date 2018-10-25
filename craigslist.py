#!/usr/bin/env python

# Developed by Michael Orozco
# iBit IT
# Start dev: 10/16/2015 11:38pm
# End dev: 10/17/2015 1:45am

import argparse, os
import time

from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common import action_chains, keys


from pyvirtualdisplay import Display



class craigslistBot:
    def debug(self, inString):
        print(" [LOG] {BOT} - %s" % inString.encode('utf-8').strip())

    def __init__(self, loginEmail="", loginPass="", contactNumber="", contactName="", postTitle="", postCode="",
                 postContentFile="", price="", waitTime=10):
        self.display = ""

        if not os.name == 'nt':
            self.display = Display(visible=0, size=(800, 600))
            self.display.start()

        # self.client = webdriver.Firefox()
        self.client = webdriver.Chrome()
        self.isLoggedIn = False
        self.loginEmail = loginEmail
        self.loginPass = loginPass
        self.contactNumber = contactNumber
        self.contactName = contactName
        self.postTitle = postTitle
        self.postCode = postCode
        self.postContent = postContentFile
        self.waitTime = waitTime
        self.price = price
        self.odometer = odometer
        self.vin = vin
        self.condition = condition
        self.cylinders = cylinders
        self.fuel = fuel
        self.drive = drive
        self.paintColor = color
        self.size = size
        self.transmission = transmission
        self.type = carType
        self.modelYear = modelYear
        self.makeAndModel = makeAndModel


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

    def createPost(self):
        if not self.isLoggedIn:
            return 0

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
        if self.vin is not None:
            self.client.find_element_by_xpath("//input[@name='auto_vin']").send_keys(self.vin)
            time.sleep(self.waitTime)
        if self.odometer is not None:
            self.client.find_element_by_xpath("//input[@name='auto_miles']").send_keys(self.odometer)
            time.sleep(self.waitTime)
        self.client.find_element_by_xpath("//input[@name='auto_make_model']").send_keys(self.makeAndModel)
        time.sleep(self.waitTime)
        if self.condition is not None:
            self.client.find_element_by_xpath("//label[contains(@class, 'condition')]//option['like new']").click()
            select = Select(self.client.find_element_by_xpath("//select[contains(@id, 'ui-id-3')]"))
            WebDriverWait(self.client, timeout=10).until(EC.element_to_be_clickable((By.XPATH, "//select['contains(@name=condition')]//option['like new']")))
            select.select_by_visible_text(self.condition)

            select.selec
        # self.debug("Checking 'Okay to contact by phone'")
        # self.client.find_element_by_css_selector("#contact_phone_ok").click()
        # time.sleep(self.waitTime)
        # self.debug("Checking 'Okay to contact by text'")
        # self.client.find_element_by_css_selector("#contact_text_ok").click()
        # time.sleep(self.waitTime)
        # self.debug("Filling in contact phone number")
        # self.client.find_element_by_css_selector("#contact_phone").send_keys(self.contactNumber)
        # time.sleep(self.waitTime)
        # self.debug("Filling in contact name")
        # self.client.find_element_by_css_selector("#contact_name").send_keys(self.contactName)
        # time.sleep(self.waitTime)
        # self.debug("Filling in post title")
    #     self.client.find_element_by_css_selector("#PostingTitle").send_keys(spintax.parse(self.postTitle))
    #     time.sleep(self.waitTime)
    #     self.debug("Filling in zip code")
    #     self.client.find_element_by_css_selector("#postal_code").send_keys(self.postCode)
    #     time.sleep(self.waitTime)
    #
    #     self.debug("Getting post content")
    #     f = open(self.postContent, "rb")
    #     content = f.read()
    #     f.close()
    #
    #     self.debug("Spinning content")
    #     spinContent = spintax.parse(content)
    #
    #     self.debug("Filling in post content")
    #     self.client.find_element_by_css_selector("#PostingBody").send_keys(spinContent)
    #     time.sleep(self.waitTime)
    #     self.debug("Checking 'Okay to contact for other offers'")
    #     self.client.find_element_by_css_selector("#oc").click()
    #     time.sleep(self.waitTime)
    #     self.debug("Unchecking 'Want a map' if checked")
    #     try:
    #         self.client.find_element_by_css_selector("#wantamap:checked")
    #     except NoSuchElementException:
    #         self.debug("Not checked")
    #     finally:
    #         self.client.find_element_by_css_selector("#wantamap:checked").click()
    #     time.sleep(self.waitTime)
    #     self.debug("Clicking continue")
    #     self.client.find_element_by_css_selector('button[value="Continue"]').click()
    #     time.sleep(self.waitTime)
    #     if "editimage" in self.client.current_url:
    #         self.debug("Clicking continue")
    #         self.client.find_element_by_css_selector('button.done').click()
    #     time.sleep(self.waitTime)
    #     self.debug("Clicking publish")
    #     self.client.find_element_by_css_selector('.draft_warning button[value="Continue"]').click()
    #     time.sleep(10)


def main(loginEmail, loginPass, contactNumber, contactName, postTitle, postCode, postContentFile, waitTime):
    startExecTime = time.time()

    clBot = craigslistBot(loginEmail, loginPass, contactNumber, contactName, postTitle, postCode, postContentFile,
                          waitTime)
    clBot.login()
    # clBot.createPost()
    endExecTime = time.time()
    clBot.debug("Execution time: %s seconds" % int(endExecTime - startExecTime))

    print("Finished")

    return 0


parser = argparse.ArgumentParser(description="Craigslist Poster Script")
parser.add_argument('loginEmail', metavar='LOGINEMAIL', type=str, help='Email to use for login')
parser.add_argument('loginPass', metavar='LOGINPASS', type=str, help='Password to use for login')
parser.add_argument('contactNumber', metavar='CONTACTNUM', type=str, help='Contact number for post')
parser.add_argument('contactName', metavar='CONTACTNAME', type=str, help='Contact name for post')
parser.add_argument('postTitle', metavar='POSTTITLE', type=str, help='Title of the post to be made')
parser.add_argument('postCode', metavar='POSTCODE', type=str, help='Zip code for post')
parser.add_argument('postContent', metavar='POSTCONTENT', type=str, help='Path to file for post content')
parser.add_argument('waitTime', metavar='WAITTIME', type=int, help='Time to wait in between actions (Recommend 3)')
args = parser.parse_args()
main(args.loginEmail, args.loginPass, args.contactNumber, args.contactName, args.postTitle, args.postCode,
     args.postContent, args.waitTime)
