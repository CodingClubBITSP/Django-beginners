# please ensure that you have the following:
# selenium library.. v3.60
# time library which should be there by default
# download chromedriver_win32.zip from http://chromedriver.storage.googleapis.com/index.html..
# get anything above v2.23.. I got v2.24
# and yes, please be patient while the hints load, especially for question 2 and 4..
# please enter your email and password in the quotes marked with *****
# the chrome browser will open automatically and you can minimize it


from selenium import webdriver
import time


# This is the number of questions input
i = int(input('Enter the number of questions for which you would like to check the hint'))


# making a variable for the location of the chromedriver file...
# please change this according to your own file location for the code to work!!
chromedriver = 'C:\\Users\sangeeta karajgi\Downloads\chromedriver_win32\chromedriver.exe'
browser = webdriver.Chrome(chromedriver)


# You can resize the window by using the single line of code below..
# browser.set_window_size(1000, 1000)

# Trying to minimize the chrome window.. did not work for me..
'''chrome_options = Options()
    chrome_options.add_argument("--start-minimized")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    
    driver.window().setPosition(new Point(-2000, 0))'''


# getting the url for the required google login for Qrious
browser.get('http://nikskhandelwal98.pythonanywhere.com/accounts/google/login/?process=login')
time.sleep(5)


# specifying the location for the email box
email = browser.find_element_by_xpath('//*[@id="identifierId"]')
email.send_keys('')                                                 # ******
# your email id has been entered


# clicking on the next button to take us to the password page
next1 = browser.find_element_by_xpath('//*[@id="identifierNext"]')
next1.click()
time.sleep(5)

# specifying the location of the password box
password = browser.find_element_by_css_selector('#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
password.send_keys('')                                              # ******
# your password has been entered


# clicking on the next button to take me to the main Qrious site
next2 = browser.find_element_by_xpath('//*[@id="passwordNext"]')
next2.click()
print('ready')
time.sleep(10)


a = 1

# while loop to load each page and print the hint....
while a <= i:

    url = ('http://nikskhandelwal98.pythonanywhere.com/accounts/profile/' + str(a) + '/#')

    a += 1
    browser.get(url)

    # the main problem I encountered was that both the question and the hint had the same xpath.
    # Hence, I got both the elements as a list and then printed out the second element, i.e. the hint

    phrases = browser.find_elements_by_id("ele1")
    hint = phrases[1]
    words = list(hint.text.split())
    words.remove("Hint")
    words.remove(":")

    print(" ".join(words))


# the xpaths
''' line number of hint is 89 in source code.
# //*[@id="ele1"]/text()[2]
# //*[@id="ele1"]/text()[1]
# //*[@id="ele1"]/text()[1]
# //*[@id="ele1"]/text()[2]
'''
