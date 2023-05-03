from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from datetime import date


def create_driver():
    service = Service(executable_path="./chromedriver.exe")
    options = ChromeOptions()
    # Optional: Maintains the window opened
    # options.add_experimental_option("detach", True)
    return webdriver.Chrome(service=service, options=options)


def get_weekday():
    today = date.today()
    weekday_num = today.weekday()
    weekday_names = ["Monday", "Tuesday", "Wednesday",
                     "Thursday", "Friday", "Saturday", "Sunday"]
    return weekday_names[weekday_num]


def select_weekday_web(driver, weekday):
    driver.get("http://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
    elem_select = Select(driver.find_element(By.ID, "select-demo"))
    elem_select.select_by_visible_text(weekday)


def return_web_response(driver):
    elem_day_selected = driver.find_element(By.CLASS_NAME, "selected-value")
    return elem_day_selected.text


def main():
    driver = create_driver()
    weekday = get_weekday()
    select_weekday_web(driver, weekday)
    print(return_web_response(driver))
    driver.close()


main()
