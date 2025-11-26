lst = list(map(int, input('Enter some numbers here : ').split()))
evn_lst = [i for i in lst if i%2 == 0]

print('Even numbers present in the given list : ',evn_lst)