from random import randrange
from time import sleep
from misc import rand_ran
from tb_sel import loggin, nroll_other
from model import add_user_others, select_none_others, select_all_others, select_y_others


def fix_list(old_str):
    listed = [n for n in old_str.split(',') if n != '']
    new_str = ','.join(listed)
    return new_str

def start():
    all_other = select_all_others()
    u_nons = select_none_others()
    print(len(u_nons))
    #r_num = randrange(46, 52)
    #nums = rand_num(r_num)
    nums = rand_ran(6, 11)
    print(nums)
    # harpernesti10@gmail.com
    # make a creative portfolio css 2

    skip = 0
    for x in u_nons:
        if skip > 16:
            print('log0')
            bow = loggin(x[0], x[1])
            if bow:
                print(x[0])
                for c in nums:
                    other = all_other[c]
                    print(f'nroll {other[0]}')
                    ret = nroll_other(bow, other[0])
                    if ret:
                        print(f'add {c} to other str')
                        curr_ot = select_y_others(x[0])[0]
                        if curr_ot == 'False':
                            curr_other = ''
                        else:
                            curr_other = curr_ot
                        curr_other = fix_list(curr_other)
                        print(f'current other {curr_other}')
                        other_str = ','.join([curr_other, str(c)])
                        ret_sta = add_user_others(x[0], other_str)

                    else:
                        print('what happened or buy now')
                        sleep(3)

                # close out
                bow.close()
                print(ret_sta)
            else:
                pass
        skip += 1


start()
