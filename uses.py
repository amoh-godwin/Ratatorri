from selenium import webdriver
h3=1
dd=9
dd=11

with open('unsardine.txt', 'w') as t:
    t.write('')

def do():
    browser = webdriver.Firefox("H:\\CS\\studies\\python\\selenium")
    # connect to site
    browser.get("http://www.fakenamegenerator.com/gen-random-uk-uk.php")
    # find link button
    na_els = browser.find_elements_by_tag_name("h3")
    # click
    na_el = na_els[0]
    # enter full name
    em_els = browser.find_elements_by_tag_name("dd")
    em_te = em_els[8].text.split('\n')[0]
    paker = em_els[10]
    text = ':::'.join([na_el.text, em_te, paker.text])
    browser.quit()
    with open('unsardine.txt', 'a') as a:
        a.write(text + '\n')

while True:
    do()
