import os
from linkedin_scraper import Person, actions
from selenium import webdriver
# driver = webdriver.Chrome("./chromedriver")
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

email = os.getenv("UserEmail")
password = os.getenv("Password")
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
cyril_account = Person("https://www.linkedin.com/in/cyrilmichino/", driver=driver)

for position in cyril_account.experiences:
    print(cyril_account.name + " has worked for " + position.institution_name + " and the company link: " + position.linkedin_url)

