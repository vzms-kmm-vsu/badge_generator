import csv


def replace_names(fio, line):
    new_line = line
    for y, x in enumerate(['participsurname', 'participname', 'particippatronymic', 'participcity']):
        new_line = new_line.replace(x, fio[y])
    return new_line


def names_gen(file):
    with open(file, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        name_list = list(reader)[1:]
    return name_list


names_list = names_gen('list_partics.csv')
iterator = 0
f_write = open('./output/auto_participants.fodg', 'w', encoding='utf-8')
with open('./input/participants.fodg', 'r', encoding='utf-8') as f_read:
    for line in f_read:
        if ('participsurname' in line) and len(names_list) > iterator:
            f_write.write(replace_names(names_list[iterator], line))
            iterator += 1
        else:
            f_write.write(line)
f_write.close()
