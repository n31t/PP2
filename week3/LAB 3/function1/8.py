def spy_game(nums):
    s = ''
    for i in nums:
        s = s + str(i)
    a = s.find('007')
    if int(a) > 0:
        return print('True')
    else:
        return print('False')

    # print(a)


spy_game([1, 2, 4, 0, 0, 7, 5])
spy_game([1, 0, 2, 4, 0, 5, 7])
spy_game([1, 7, 2, 0, 4, 5, 0])
