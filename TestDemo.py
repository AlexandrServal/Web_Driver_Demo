from selene import be, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as match
from webdriver_manager.chrome import ChromeDriverManager

"""
def by(css_selector: str):
    return By.CSS_SELECTOR, css_selector


def element(selector) -> WebElement:
    return wait.until(match.visibility_of_element_located(by(selector)))


def assert_text(locator, value):
    wait.until()



driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
wait = WebDriverWait(driver, 4)
"""
browser.open('https://duckduckgo.com/')

browser.element('[name=q]').should(be.blank).type('yashaka selene python').press_enter()
browser.all('.result').should(have.size_greater_than(5))\
    .first.should(have.text('User-oriented Web UI browser tests'))
browser.all('.result').first.element('a').click()
browser.should(have.title_containing('yashaka/selene'))
