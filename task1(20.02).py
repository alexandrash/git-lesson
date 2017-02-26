pl = int(input('количество тарелок:'))
det = float(input('количество моющего средства в литрах:'))
clean_pl = 0
while pl!= 0 and det >=0.5:
    pl -= 1
    det -= 0.5
    clean_pl += 1
    print('осталось еще', det, 'л')

if det < 0.5:
    print('Средство закончилось.','\n',
          'Количество вымытых тарелок:{}.'.format(clean_pl),'\n',
          'Количество оставшихся тарелок:{}'. format(pl))

if pl == 0:
    print('Осталось {} л моющего средства'.format(det))



