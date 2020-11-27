from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

chromeOptions = Options()
chromeOptions.headless = True
watchlist = ["CSE 535", "CSE 539", "CSE 574", "CSE 575"]
courseCatalogURL = "https://webapp4.asu.edu/catalog/classlist?t=2211&s=CSE&n=5**&hon=F&promod=F&e=all&page=1"
chromedriverFullPath = "" #Enter path to your chromedriver (Add to PATH, and have chrome binary installed)

browser = webdriver.Chrome(executable_path=chromedriverFullPath, options=chromeOptions)
browser.get()
try:
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "td.titleColumnValue"))
    )
    classList = browser.find_elements_by_css_selector('td.titleColumnValue')
    courseNumberList = browser.find_elements_by_css_selector('td.subjectNumberColumnValue.nowrap')
    availableSeatList = browser.find_elements_by_css_selector('td.availableSeatsColumnValue')
    for courseNumber, class_, availableSeat in zip(courseNumberList, classList, availableSeatList):
        if (courseNumber.text in watchlist):
            print("{}: {}\n{}\n".format(courseNumber.text, class_.text, availableSeat.text))
finally:
    browser.quit()
