import pandas

base = pandas.read_csv('base.csv')
FIO = [x.rstrip() for x in open('Математика.txt', encoding='utf-8').readlines()]
result = open('resultМатематика.txt', 'w')
for obj in FIO: 
    try:
        buf = base.loc[base['ФИО'] == obj]['Контакты'].values[0].split('\n')
    except:
        print('Какие-то беды с {}'.format(obj))
        continue
    buf = str(buf[-1])
    result.writelines(buf + '\n')
