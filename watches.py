from random import randrange
from time import sleep, time
from misc import rand_num
from tb_sel import loggin, acther
from model import select_course_uu, update_course, select_y_others, \
    select_u_others, select_all_others, get_other_name

def start():
    all_s = select_course_uu('python_gui')
    # https://www.udemy.com/home/my-courses/
    # https://www.udemy.com/course/python-gui-software-development-in-python/learn/
    # modal-content
    # card--learning
    # details__name

    co = "Python Gui - Software development in python"
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
            ret = update_course('python_gui', x[0], per, int(time()))
            print(ret, '\n\n')
            sleep(30)

def start_other():
    all_s = select_u_others()
    print(len(all_s))

    count = 0
    for x in all_s:
        if count < 9:
            print(x[0])
            count += 1
            continue
        print(x[0])
        oth_str = x[2]
        oth_s = oth_str.split(',')
        oths = [int(n) for n in oth_s if n !='' and int(n) <10 ]
        print(oths)

        if oths:
            browser = loggin(x[0], x[1])
            for y in oths:
                all_ = select_all_others()
                co_ = all_[y][0]
                if co_[-1] == '/':
                    co = co_ + "learn/"
                else:
                    co = co_ + "/learn/"
                # co = get_other_name(co_)[0]
                r_num = randrange(15, 50)
                print('log', r_num)
                per = acther(browser, co, r_num)
                ret = per
                print(ret, '\n\n')
                sleep(30)
            browser.close()

start_other()
