from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class guviInsta:
    #initialise a class to take in the url
    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)

    #create a function to load the url and maximise the window
    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    #create a function to get the no of followers using xpath
    def numberOfFollowers(self):
        xpath = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button/span/span"
        return self.driver.find_element(By.XPATH, xpath).text

    #create a function to get the no of people following
    def numberFollowing(self):
        xpath = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button/span/span"
        return self.driver.find_element(By.XPATH, xpath).text

    #create a funciton to exit
    def quit(self):
        self.quit()


url = "https://www.instagram.com/guviofficial//"
obj = guviInsta(url)
obj.boot()
obj.numberOfFollowers()
obj.numberFollowing()
obj.quit()