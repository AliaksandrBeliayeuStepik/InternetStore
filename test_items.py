from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_button(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
    assert button
