import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException


URL = "https://wisdomquotes.com/inspirational-quotes/"

chrome_path = os.path.abspath("chromedriver.exe")
driver = webdriver.Chrome(chrome_path)

def clean_quotes(quotes):
    for index in range(len(quotes)):
        if "click to tweet" in quotes[index].lower(): # perhaps have the click to tweet text separate
            quotes[index] = quotes[index].replace("Click to tweet", "")
            quotes[index] = quotes[index].replace("click to tweet", "")
        quotes[index] = quotes[index].strip()
    return quotes

def wait_for_element(driver, tag):
    max_wait_time_in_sec = 5
    try:
        wait = WebDriverWait(driver, max_wait_time_in_sec)
        wait.until(ec.visibility_of_element_located((By.TAG_NAME, tag)))
    except TimeoutException:
        driver.close()
        raise TimeoutException("ERROR: Element not visible within given search time")

def get_quotes(driver,tag):
    wait_for_element(driver,tag)
    quotes = [quote.text for quote in driver.find_elements_by_tag_name(tag)]
    return quotes

def write_to_file(path, data):
    with open(path, "w") as file:
        for item in data:
            file.write(item + "\n")


if __name__ == "__main__":
    driver.get(URL)
    quotes = get_quotes(driver, "blockquote")     
    quotes = clean_quotes(quotes)
    driver.close()
    write_to_file("quotes_lib.txt", quotes)