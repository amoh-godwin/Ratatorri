from sel import other_page
from model import select_all_others, insert_other

print('this page run')

def get_links():
    with open('en.txt', 'r') as cos_file:
        data = cos_file.read()
        info = data.splitlines()
    return info


def start():
    links = get_links()
    courses = select_all_others()
    print(f'courses {courses}')
    for x_link in links:
        if (x_link,) not in courses: # Link not in db
            link, title, expired = other_page(x_link)
            insert_other(link, title, expired)
            print(f'{x_link} done')


start()

