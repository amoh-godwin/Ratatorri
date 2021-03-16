from time import sleep
from json import loads
import string
import secrets
from random import randrange
from tb_sel import up, loggin, nroll_other
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
    json = convert_two_to_json(u_nons, 'email', 'passcode')
    signal_nroll.emit(json)

    return
    count = -1
    for x in u_nons:
        count += 1
        signal_status.emit(count, 'registering')
        print('log0')
        bow = loggin(x[0], x[1])
        if bow:
            signal_status.emit(count, 'in progress')
            ret = nroll_other(bow, linker)
            if ret:
                signal_status.emit(count, 'success')
                ret_sta = model.add_users_course(x[0], co)
                print(f'count {count}: {ret_sta}')
                sleep(2)
            print(ret, '\n\n')
            sleep(5)
        # close out
        bow.close()
