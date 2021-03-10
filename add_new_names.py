import model

with open('usrmo02.txt', 'r') as t_f:
    data = t_f.read()
    info = data.splitlines()

print(info)

print(model.add_names('other', info))
