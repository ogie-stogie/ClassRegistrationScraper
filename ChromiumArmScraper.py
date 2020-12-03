from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from shutil import which

#ARM Architecture version

#sudo apt-get install chromium-chromedriver
#automated with crontab for every minute

chromiumOptions = Options()
chromiumOptions.binary = which("chromium")
chromiumOptions.add_argument("--headless")

watchlist = ["CSE 535", "CSE 539", "CSE 574", "CSE 575"]
courseCatalogURL = "https://webapp4.asu.edu/catalog/classlist?t=2211&s=CSE&n=5**&hon=F&promod=F&e=all&page=1"
newDataPath = open(r"enter/path/to/local/file", "w+")
browser = webdriver.Chrome(options=chromiumOptions)

browser.get(courseCatalogURL)
try:
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "td.titleColumnValue"))
    )
    classList = browser.find_elements_by_css_selector('td.titleColumnValue')
    courseNumberList = browser.find_elements_by_css_selector('td.subjectNumberColumnValue.nowrap')
    availableSeatList = browser.find_elements_by_css_selector('td.availableSeatsColumnValue')
    for courseNumber, class_, availableSeat in zip(courseNumberList, classList, availableSeatList):
        if (courseNumber.text in watchlist):
            newDataPath.write("{}: {}\n{}\n".format(courseNumber.text, class_.text, availableSeat.text))
except Exception as e:
    print(e)
finally:
    browser.quit()
newDataPath.close()
