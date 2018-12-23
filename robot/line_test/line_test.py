from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import requests
import json

def nowTime():
  hr = int(time.strftime("%H", time.localtime()))
  mi = int(time.strftime("%M", time.localtime()))
  am_pm = "AM"
  if hr >= 12 :
    am_pm = "PM"
    if hr > 12 : hr = hr - 12
  return "%d:%02d %s" %(hr, mi, am_pm)

def verifyAhfargoIsFine(driver):
  is_fine = str()
  for index in range(0,3):
    if driver.find_element_by_xpath('//*[@id="_chat_room_msg_list"]').get_attribute('innerHTML').count(nowTime()) < 3:
      is_fine = 'no'
    else:
      is_fine = 'yes'
    time.sleep(3)
    print(is_fine)
  return is_fine

def sendMessage(message):
  headers={
    'authorization': 'Bearer 91GhAd0IeyItMXs6e+Dl1sqYplxhXLMDj8ZzbnK57uqfgurw6IQ5TyjHoDd3S8XhPWVXWG9vKVtOBgGxYdRO8OhQpTbV93WakQi+uYnDgA4XroAAH/K5+FODaBAaTWG6VbDkrtgsVWnGgQBhBYmPNwdB04t89/1O/w1cDnyilFU=',
    'content-type': 'application/json'
  }
  payload={
      "to": "C9eb08306f28fd68ea5254ce123977be9",
      "messages":[
          {
              "type":"text",
              "text":message
          }
      ]
  }
  res=requests.post("https://api.line.me/v2/bot/message/push",headers=headers,data=json.dumps(payload))
class NewDriver():
  driver = None
  orignal_method = None
  def __find_element_by_xpath(self, xpath):
    return WebDriverWait(self.driver, 180).until(EC.element_to_be_clickable((By.XPATH, xpath)))
  @staticmethod
  def patch(driver):
    NewDriver(driver)
    return driver
  def __init__(self, driver):
    self.driver = driver
    self.orignal_method = driver.find_element_by_xpath
    driver.find_element_by_xpath = self.__find_element_by_xpath

def lineTest():
  options = webdriver.chrome.options.Options()
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-setuid-sandbox")
  options.add_extension('%sLINE_v2.1.5.crx' %FileRoute)
  options.add_argument("user-data-dir=./")
  options.add_argument('--profile-directory=test')

  oriDriver = webdriver.Chrome(chrome_options=options)
  driver = NewDriver.patch(oriDriver)

  print('Go to index')
  driver.get("chrome-extension://ophjlpahpchlmihnnnihgmmeilfjmjjc/index.html")
  print('Typing email and password')
  driver.find_element_by_xpath('//*[@id="line_login_email"]').clear()
  driver.find_element_by_xpath('//*[@id="line_login_email"]').send_keys(LINE_USER)
  driver.find_element_by_xpath('//*[@id="line_login_pwd"]').send_keys(LINE_PASSWORD)
  driver.find_element_by_xpath('//*[@id="login_btn"]').click()
  print("Password is %s" %driver.find_element_by_xpath('//*[@id="login_content"]/div/section/div').get_attribute('innerHTML'))
  sendMessage(driver.find_element_by_xpath('//*[@id="login_content"]/div/section/div').get_attribute('innerHTML'))
  print('Select line bot')
  driver.find_element_by_xpath('//*[@id="_search_input"]').send_keys("Go")
  time.sleep(3)
  print('Typing to line bot')
  driver.find_element_by_xpath('//*[@id="_chat_list_body"]/li').click()
  time.sleep(3)
  while True:
    sendMessage('Ahfar Go test is begin')
    fail = 0
    for item in range(0, 60*60*24):
      driver.find_element_by_xpath('//*[@id="_chat_room_input"]').send_keys("55", Keys.ENTER)
      print('Verify')
      print(driver.find_element_by_xpath('//*[@id="_chat_room_msg_list"]').get_attribute('innerHTML').count(nowTime()))
      print(nowTime())
      if verifyAhfargoIsFine(driver) == 'yes' :
        print('fine')
        fail = 0
      else :
        print('fail + 1')
        fail += 0
      if fail == 3 :
        sendMessage('Ahfar Go is crash')
        fail = 0
      time.sleep(60)
  driver.close()

if __name__ == "__main__":
  FileRoute='%s/' %os.path.dirname(os.path.abspath(__file__))
  LINE_USER = ""
  LINE_PASSWORD = ""
  
  lineTest()