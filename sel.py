from time import sleep
from selenium import webdriver


def up(name, ema, pas):

    browser = webdriver.Firefox("H:\\CS\\studies\\python\\selenium")
    # connect to site
    browser.get("http://www.udemy.com")#, wait_on_page=3, wait_for_page_body=True)
    # find link button
    reg_el = browser.find_element_by_link_text("Sign up")
    # click
    reg_el.click()
    # enter full name
    full_name = browser.find_element_by_id("id_fullname")
    full_name.send_keys(name)
    # enter email
    email_el = browser.find_element_by_id("email--1")
    email_el.send_keys(ema)
    # enter password
    pass_el = browser.find_element_by_id("password")
    pass_el.send_keys(pas)
    # check if check box
    browser.execute_script("window.scrollTo(0,100)")
    browser.execute_script('document.getElementById("id_subscribe_to_emails").checked = false')
    # find submit link
    sub_el = browser.find_element_by_id('submit-id-submit')
    # click submit
    sub_el.click()
    # check if success
    if '=1' in browser.current_url:
        browser.close()
        return True

def other_page(link):
    browser = webdriver.Firefox("H:\\CS\\studies\\python\\selenium")
    # connect to site
    browser.get(link)
    sleep(3)
    # check for el
    try:
        el = browser.find_element_by_class_name("styles--btn--express-checkout--28jN4")
        if el.text == 'Enroll now':
            expired = 'False'
        elif el.text == 'Buy now':
            expired = 'True'
    except:
        expired = 'True'
    
    link = browser.current_url
    title = browser.find_element_by_class_name("clp-lead__title--small").text

    browser.close()

    return link, title, expired

