from flask import request, Flask
import atexit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="chromedriver")
driver.implicitly_wait(30)
randomApp = Flask(__name__)

@randomApp.route('/')
def hello_world():
	return "Hello!"
	
@atexit.register
def exit():
	driver.quit()