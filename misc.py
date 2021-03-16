import string
from random import randrange
import secrets
import model


def convert_users_to_json(data):
    info = []

    for x in data:
        row = {}
        row['fullname'], row['email'], row['passcode'], \
            row['country'], row['registered'], row['others'], \
            row['win_photos'], row['python_gui'], row['py_gui_ufb'], \
            row['pyqt'], row['toda'], row['soft_dev'], \
            row['last_visited'], row['pratical_project_py'] = x
        info.append(row)

    return info


def convert_two_to_json(data, col1, col2):
    info = []

    for x in data:
        row = {}
        row[col1], row[col2] = x
        info.append(row)

    return info

def gen_pq(rge):
    alphabet = string.ascii_letters + string.digits
    return ''.join([secrets.choice(alphabet) for i in range(rge)])


def gen_clas():
    emm = ['yahoo', 'gmail']
    srus = model.select_names('sru')
    others = model.select_names('other')
    sum_srus = len(srus)
    s_rand = rand_num(sum_srus)
    o_rand = rand_num(sum_srus)
    for x in range(sum_srus):
        other = others[o_rand[x]][0]
        sru = srus[s_rand[x]][0]
        em = emm[s_rand[x]%2]
        fname = ' '.join([other, sru])
        real_em = ''.join([other, sru, gen_pq(1), str(randrange(1,24)), '@', em, '.com']).lower()
        pq = gen_pq(randrange(8, 11))
        model.insert_user(fname, real_em, pq)
        model.update_uses('sru', ''.join(['"', sru, '"']))
        model.update_uses('other', ''.join(['"', other, '"']))
        print(fname, real_em, pq)


def rand_num(total):
    all = []
    while len(all) < total:
        for _ in range(total * 3):
            y = randrange(0,total)
            if y not in all:
                all.append(y)

    return all


def rand_ran(s, e):
    all = []
    total = 0
    while total < e-s:
        y = randrange(s, e)
        if y not in all:
            all.append(y)
            total += 1
    return all
