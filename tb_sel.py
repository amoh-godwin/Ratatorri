from  time import sleep
from tbselenium.tbdriver import TorBrowserDriver
import tbselenium.common as cm
from tbselenium.utils import launch_tbb_tor_with_stem

"""

FIX evelynkendrickh12@yahoo.com, liarm
IN WHO are many eenroll but we have set to empty to make

"""

tbb_dir = "C:\\Program Files (x86)\\Tor Browser"
launch_tbb_tor_with_stem(tbb_dir) # I think you can remove this, but maybe some future usages need that 

def nroll_other(browser, link):
    browser.maximize_window()
    browser.load_url(link,
    wait_on_page=5, wait_for_page_body=True)

    try:
        el = browser.find_element_by_class_name("styles--btn--express-checkout--28jN4")

    except:
        print('Except')
        sleep(15)
        try:
            el = browser.find_element_by_class_name("styles--btn--express-checkout--28jN4")
        except:
            print('Deep Except')
            return False
        print('after Except')

    if el.text == 'Enroll now':
        sleep(2)
        try:
            el.click()
        except:
            # probably obscured
            browser.execute_script("window.scrollBy(0,100)")
            el.click()

        print('enroll')
        sleep(12)
        if 'checkout' in browser.current_url:
            print('chec')
            try:
                sub_els = browser.find_elements_by_class_name("btn-lg")
            except:
                # Wait
                sleep(15)

            # Continue even after exception
            sub_el = sub_els[1]
            sub_el.click()
            sleep(5)
            if 'success' not in browser.current_url or 'subscribe' not in browser.current_url:
                print('aah')
                sleep(8)
                try:
                    _ = browser.find_element_by_id("billingAddressSecondaryInput")
                except:
                    print('has no second')
                    sleep(12)
                    if 'success' in browser.current_url:
                        print('except handler')
                        return True
                    sub_el.click()
                    sleep(12)
                    if 'success' in browser.current_url:
                        print('except handler')
                        return True
                else:
                    print('bac')
                    try:
                        sel_el = browser.find_element_by_id("billingAddressCountry")
                    except:
                        # Wait
                        sleep(15)

                    sel_el.click()
                    opts = browser.find_elements_by_tag_name("option")
                    opts[232].click()
                    sleep(7)
                    sub_el.click()
                    return True
                    
            elif 'success' in browser.current_url:
                # Success
                print('success')
                return True
            else:
                print('else statement')
                browser.close()
                return True

        elif 'subscribe' in browser.current_url:
            print('has')
            return True

        else:
            print('suspect good choice suscribe should have handled this')
            # has suscribe
            sleep(10)
            return True

    elif el.text == 'Buy now':
        print('by now')
        return False

    elif el.text == 'Go to course':
        print('has already neroll')
        return True

    else:
        print('Dont know what is going on')
        sleep(10)
        return False


def loggin(ema, pas):
    try:
        browser = TorBrowserDriver(tbb_dir, tor_cfg=cm.USE_STEM)
    except:
        # selenium.common.exceptions.WebDriverException: Message: Access is denied. (os error 5)
        # mozilla is updating
        print('probably updating sleep 30')
        sleep(30)
        browser = TorBrowserDriver(tbb_dir, tor_cfg=cm.USE_STEM)
    # connect to site
    try:
        browser.load_url("https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F",
    wait_on_page=5, wait_for_page_body=True)

    except:
        # selenium.common.exceptions.NoSuchWindowException: Message: Browsing context has been discarded
        try:
            browser = TorBrowserDriver(tbb_dir, tor_cfg=cm.USE_STEM)
        except:
            # selenium.common.exceptions.WebDriverException: Message: Access is denied. (os error 5)
            # mozilla is updating
            print('probably updating sleep 30')
            sleep(30)
            browser = TorBrowserDriver(tbb_dir, tor_cfg=cm.USE_STEM)
        
        browser.load_url("https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F",
    wait_on_page=5, wait_for_page_body=True)

    # reg_el.click()
    # maximise
    browser.maximize_window()
    # Scroll
    browser.execute_script("window.scrollTo(0,100)")
    try:
        email_el = browser.find_element_by_id("email--1")
    except:
        sleep(10)
        try:
            email_el = browser.find_element_by_id("email--1")
        except:
            return False
    email_el.send_keys(ema)
    # enter password
    pass_el = browser.find_element_by_id("id_password")
    pass_el.send_keys(pas)
    # find submit link
    sub_el = browser.find_element_by_id('submit-id-submit')
    # click submit
    sub_el.click()
    sleep(2)
    # check
    try:
        avatar = browser.find_element_by_id('u711-popover-trigger--18')
    except:
        avatar = None

    if avatar:
        return browser
    elif 'udemy.com' in browser.current_url:
        return browser
    else:
        return None

def pop(browser):
    try:
        dvi = browser.find_element_by_class_name("progress--progress-container--RxDGm")
    except:
        sleep(12)
        try:
            dvi = browser.find_element_by_class_name("progress--progress-container--RxDGm")
        except:
            print('Something really wrong')
            sleep(30)
            try:
                dvi = browser.find_element_by_class_name("progress--progress-container--RxDGm")
            except:
                return False
    
    dvi.click()
    sleep(1)
    po = browser.find_element_by_class_name("progress-popover-content--progress-text--1COmZ")
    txs = po.text.split(" ")
    # close
    cl = browser.find_element_by_class_name("popover--close--3mACo")
    cl.click()
    return txs

def acther(browser, co, per):

    browser.maximize_window()
    # goto co
    link = "https://www.udemy.com/home/my-courses/"
    browser.load_url(link,
    wait_on_page=5, wait_for_page_body=True)
    sleep(12)
    print('home')
    # goto link

    try:
        browser.load_url(co,
    wait_on_page=5, wait_for_page_body=True)
    except:
        # not nroll
        print('not nroll')
        return False
    """
    try:
        ddcs = browser.find_elements_by_class_name("card--learning")
        strs = browser.find_elements_by_class_name("details__name")
    except:
        sleep(12)
        try:
            ddcs = browser.find_elements_by_class_name("card--learning")
            strs = browser.find_elements_by_class_name("details__name")
        except:
            print('something really wrong')
            sleep(12)
            ddcs = browser.find_elements_by_class_name("card--learning")
            strs = browser.find_elements_by_class_name("details__name")

    ddc = None
    for x in range(len(strs)):
        if co == strs[x].text:
            ddc = ddcs[x]
    if not ddc:
        return False
    ddc.click()
    """
    sleep(12)
    print('this is')
    # check if reall
    try:
        el = browser.find_element_by_class_name("styles--btn--express-checkout--28jN4")
        if el.text == 'Buy now':
            return False
    except:
        pass

    # moal
    try:
        _ = browser.find_element_by_class_name('modal-content')
        cl = browser.find_elements_by_class_name("close")
        cl[1].click()
    except:
        sleep(5)
        pass

    try:
        _ = browser.find_element_by_class_name("course-content--loading--17QD6")
        print('Tortoise')
        sleep(60)
    except:
        pass

    print('step 1')
    # check
    txs = pop(browser)
    if not txs:
        return False

    total = int((int(txs[2]) / 100) * per)
    count = 0
    print('step 2')
    # sections
    secs = browser.find_elements_by_class_name("section--section-heading--2k6aW")
    for x in range(len(secs)):
        if count <= total:
            # do nothting
            pass
        else:
            print('step break out')
            break

        if x == 0:
            # its already opens
            pass
        else:
            # click to open
            secs[x].click()
        sps = browser.find_elements_by_class_name("curriculum-item-link--title--zI5QT")
        las = browser.find_elements_by_class_name("curriculum-item-link--progress-toggle--1CMcg")
        print(f'labls {sps} \n\n {las}')
        for y in range(len(las)):
            count += 1
            
            if count <= int(txs[0]):
                print('go forward')
                pass
            elif count <= total:
                if 'Quiz' in sps[y].text:
                    pass
                else:
                    las[y].click()
                    browser.execute_script("window.scrollBy(0,32)")
            else:
                break
        # click to close
        secs[x].click()
    sleep(15)
    txs = pop(browser)
    pere = int((int(txs[0]) / int(txs[2])) * 100)
    return pere


def up(name, ema, pas):

    browser = TorBrowserDriver(tbb_dir, tor_cfg=cm.USE_STEM)
    # connect to site
    browser.load_url("https://www.udemy.com/join/signup-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F", wait_on_page=5, wait_for_page_body=True)
    # find link button
    #reg_el = browser.find_element_by_link_text("Sign up")
    # https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F
    # click
    # reg_el.click()
    # enter full name
    full_name = browser.find_element_by_id("id_fullname")
    full_name.send_keys(name)
    # enter email
    email_el = browser.find_element_by_id("email--1")
    email_el.send_keys(ema)
    # enter password
    pass_el = browser.find_element_by_id("password")
    pass_el.send_keys(pas)
    # Scroll
    browser.execute_script("window.scrollTo(0,100)")
    browser.execute_script('document.getElementById("id_subscribe_to_emails").checked = false')

    # find submit link
    sub_el = browser.find_element_by_id('submit-id-submit')
    # click submit
    sub_el.click()
    sleep(1)
    # check
    if '=1' in browser.current_url:
        browser.close()
        return True

