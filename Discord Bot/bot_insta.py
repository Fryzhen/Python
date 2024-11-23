from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def instagram(pseudo, message):
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://instagram.com/')
    time.sleep(4)

    login(browser)
    notification(browser)
    newmessage(pseudo, browser)
    sendmessage(message, browser)


# Automating the login
def login(browser):  # /html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input
    Username = browser.find_element(By.XPATH,
                                    "/html/body/div[2]/div/div/div/div/div/div/div/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")
    Username.send_keys("kappi_penguin")
    time.sleep(3)
    password = browser.find_element(By.XPATH,
                                    "/html/body/div[2]/div/div/div/div/div/div/div/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")
    password.send_keys("MonBot0!")
    time.sleep(3)
    password.submit()
    time.sleep(10)


# Automate the notifications


def notification(browser):
    time.sleep(4)
    msgclick = browser.find_element(By.CLASS_NAME, 'x1n2onr6')
    msgclick.click()
    time.sleep(4)
    Notnow = browser.find_element(By.XPATH,
                                  "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
    Notnow.click()
    time.sleep(4)
    browser.get("https://www.instagram.com/direct/inbox/")
    time.sleep(10)


# click the message


def firstmessage(browser):
    listmessage = browser.find_element(By.CLASS_NAME, "_abyk")

    firstmessage = listmessage.find_element(By.XPATH, "div/div[1]/a")
    firstmessage.click()
    time.sleep(9)


def newmessage(nick, browser):
    newmsg = browser.find_element(By.CLASS_NAME, "_abm0")
    newmsg.click()
    time.sleep(5)

    popup = browser.find_element(By.XPATH,
                                 "html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div")
    # dialogue + 1
    popup2 = popup.find_element(By.XPATH, "div[2]/div[1]")
    popup3 = popup2.find_element(By.XPATH, "div/div[2]/input")
    popup3.send_keys(nick)
    time.sleep(5)

    first = popup.find_element(By.XPATH, "div[2]/div[2]/div[1]")
    first.click()
    time.sleep(5)

    popup.find_element(By.XPATH, "div[1]/div/div[3]/div/button").click()
    time.sleep(10)


def sendmessage(message, browser):
    messagebar = browser.find_element(By.CLASS_NAME, "_acrb")

    messageinput = messagebar.find_element(By.XPATH, "div[2]/textarea")
    messageinput.send_keys(message)
    time.sleep(5)

    messagesend = messagebar.find_element(By.XPATH, "div[3]/div")
    messagesend.click()
    time.sleep(5)
