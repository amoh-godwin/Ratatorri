from time import sleep, time
from json import loads
import string
import secrets
from random import randrange
from tb_sel import up, loggin, nroll_other, acther
import model
from misc import rand_num, gen_pq, gen_clas, convert_two_to_json

print('this page run')


def add_users():
    with open('unsardined.txt', 'r') as un:
        lines = un.readlines()
        for line in lines:
            n, e, p = line.split(':::')
            print(p.strip())
            model.strip(p.strip(), e.lower())
            #model.insert_user(n, e, p.strip())


def start():
    all = model.see_unr()
    count = -1
    for x in all:
        count += 1
        if count >= 13 and count < 23:
            print(x)
            print('Sleeping...')
            sleep(1)
            if True:#up(x[0], x[1], x[2]):
                #
                model.register_user(x[1])
                print(f'done {x}')
                print('sleeping...', '\n')
        else:
            print(count)
            #sreturn


def nroll_cou(co, linker, signal_nroll, signal_status):
    u_nons = model.select_none_others()
    json = convert_two_to_json(u_nons, 'email', 'status')
    signal_nroll.emit(json)

    count = -1
    for x in u_nons:
        count += 1
        if count < 14:
            continue
        signal_status.emit(count, 'registering')
        print('log0')
        bow = loggin(x[0], x[1])
        sleep(0.2)
        if bow:
            signal_status.emit(count, 'in progress')
            ret = nroll_other(bow, linker)
            if ret:
                if model.add_users_course(x[0], co):
                    signal_status.emit(count, 'success')
                sleep(0.2)
            else:
                signal_status.emit(count, 'error')

            sleep(5)
        else:
            signal_status.emit(count, 'unable to log')
        # close out
        bow.close()


def watchers(co, cn, signal_n, signal_per):
    all_s = model.select_course_uu(cn)
    json = convert_two_to_json(all_s, 'email', 'percent')
    signal_n.emit(json)
    # https://www.udemy.com/home/my-courses/
    # https://www.udemy.com/course/python-gui-software-development-in-python/learn/
    # modal-content
    # card--learning
    # details__name

    # co = "Python Gui - Software development in python"
    # "/course/python-gui-software-development-in-python/learn/"
    count = -1
    for x in all_s:
        count += 1
        if count < 4:
            continue
        r_num = randrange(15, 75)
        print('log', r_num)
        browser = loggin(x[0], x[1])
        per = acther(browser, co, r_num)
        if per:
            signal_per.emit(count, int(per))
            ret = model.update_course(cn, x[0], per, int(time()))
            print(ret, '\n\n')
            sleep(1)
        browser.close()
