from time import sleep
from json import loads
import string
import secrets
from random import randrange
from tb_sel import up
import model
from misc import rand_num, gen_pq, gen_clas

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


start()
