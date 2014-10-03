# coding:utf-8
def bsearch(data, value):
    num = 0
    size = len(data)
    while num < size:
        tmp = (num + size)/2
        if data[tmp] < value:
            num = tmp + 1
        else:
            num = tmp 

        if data[num] == value:
            print 'Found', value, 'position', num
            break
        else:
            print 'Not Found'

if __name__ == '__main__':
    date = [0, 1, 2, 3, 4, 5, 6]
    bsearch(date, 3)
    bsearch(date, 4)
    bsearch(date, 5)
    bsearch(date, 6)

