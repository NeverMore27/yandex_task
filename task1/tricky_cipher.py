import re
def count_unique_chars(text):
    chars = set()

    for char in text:
        chars.add(char)

    return len(chars)

def char_num (sim):
    return ord(sim.lower()) - ord('a') + 1

def incription(letter):
    count = count_unique_chars(letter)

def partition(str):
    parts = str.split(',')
    fio = ''.join(parts[:3])
    date = ','.join(parts[3:])
    return (fio, date)

def summ_date(date):
    summ_date = 0
    date = re.sub(",", "", date)
    for i in date:
        summ_date= summ_date+int(i)
    return summ_date

def hex_result(s):
    list = partition(s)
    summ = summ_date(list[1][:-4])
    count = count_unique_chars(list[0])
    first = char_num(list[0][:1])
    result = summ * 64 + count + first * 256
    return f'{result:x}'.upper()

def format (an):
    if len(an) > 3:
        result = an[-3:]
    else:
        result = an + '0' * (3 - len(an))
    return result

count = int(input())
list = []
answer = []
for i in range(count):
    answer.append(format(hex_result(input())))


print(*answer)




