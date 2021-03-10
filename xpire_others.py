from time import sleep
from sel import other_page
from model import select_all_others, expire_other

def start():
    alls = select_all_others()
    print(alls)

    for x in alls:
        linker = x[0]
        link, title, expired = other_page(linker)
        if expired == 'True':
            print(f'expire {linker}')
            print(expire_other(linker))


start()

