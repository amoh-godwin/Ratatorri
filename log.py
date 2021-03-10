from time import sleep
import model
from tb_sel import loggin

print("Log page run")

def log_for_others():
    all = model.select_none_others()
    count = 0
    for x in all:
        if count < 15:
            print(x)
            print('Sleeping...')
            sleep(1)
            if loggin(x[0], x[1]):
                #
                courses = ""
                model.add_user_others(x[1], courses)
                print(f'done {x}')
                count += 1
                print('sleeping...', '\n')
        else:
            print(count)
            return