from time import sleep, time
from json import loads
import string
import secrets
from random import randrange
from tb_sel import up, loggin, nroll_other, acther
import model
from misc import rand_num, gen_pq, gen_clas, convert_two_to_json

print('this page run')


def start():
    all = model.see_unr()
    count = 0
    for x in all:
        if count < 15:
            print(x)
            print('Sleeping...')
            sleep(1)
            if up(x[0], x[1], x[2]):
                #
                model.register_user(x[1])
                print(f'done {x}')
                count += 1
                print('sleeping...', '\n')
        else:
            print(count)
            return


def nroll_cou(co, linker, signal_nroll, signal_status):
    u_nons = model.select_none_course(co)
    json = convert_two_to_json(u_nons, 'email', 'status')
    signal_nroll.emit(json)

    count = -1
    for x in u_nons:
        count += 1
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

            sleep(1)
        else:
            signal_status.emit(count, 'unable to log')
        # close out
        bow.close()

def watchers(co):
    all_s = model.select_course_uu('python_gui')
    # https://www.udemy.com/home/my-courses/
    # https://www.udemy.com/course/python-gui-software-development-in-python/learn/
    # modal-content
    # card--learning
    # details__name

    # co = "Python Gui - Software development in python"
    # "/course/python-gui-software-development-in-python/learn/"
    count = 0
    for x in all_s:
        if count < 2:
            count += 1
        else:
            r_num = randrange(15, 50)
            print('log', r_num)
            browser = loggin(x[0], x[1])
            per = acther(browser, co, r_num)
            browser.close()
            ret = model.update_course('python_gui', x[0], per, int(time()))
            print(ret, '\n\n')
            sleep(30)
