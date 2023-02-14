def gist(listt):
    for j in range(len(listt)):
        for k in range(int(listt[j])):
            print('*', end='')
        print()


listt = []
a = int(input('list size '))
for i in range(a):
    listt.append(int(input()))
gist(listt)
