from random import randrange
from time import sleep
from misc import rand_num
from tb_sel import loggin, nroll_other
from model import add_python_gui, select_none_course


def start():
    u_nons = select_none_course('python_gui')
    print(len(u_nons))
    with open("co.txt", 'r') as co_:
        data = co_.read()
        info = data.splitlines()

    print(info)
    # harpernesti10@gmail.com
    # make a creative portfolio css 2
    co = info[0]

    count = 1
    for x in u_nons:
        print('log0')
        bow = loggin(x[0], x[1])
        if bow:
            ret = nroll_other(bow, co)
            if ret:
                ret_sta = add_python_gui(x[0])
                print(f'count {count}: {ret_sta}')
                sleep(2)
            print(ret, '\n\n')
            sleep(5)
        # close out
        bow.close()


start()
