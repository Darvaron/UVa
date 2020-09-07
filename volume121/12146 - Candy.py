def get_candies_num(m, n):
    global my_arr
    num, x, y, temp = 0, 0, 0, 0
    null_m = False
    elim = 0
    while not null_m:
        for r in my_arr:
            print(r)
        print(' ')
        x, y, temp = 0, 0, 0
        for ir, r in enumerate(my_arr):
            for ic, c in enumerate(r):
                if c > temp:
                    elim = 0
                    temp = c
                    x = ir
                    y = ic
                    if ic == 0 and n > 1:
                        elim += my_arr[ir][ic+1]
                    elif ic == n-1 and n > 1:
                        elim += my_arr[ir][ic-1]
                    elif ic == 0 and n == 1:
                        pass
                    elif ic == n-1 and n == 1:
                        pass
                    else:
                        elim += my_arr[ir][ic+1]
                        elim += my_arr[ir][ic-1]
                    if ir == 0 and m > 1:
                        for i in range(n):
                            elim += my_arr[ir+1][i]
                    elif ir == m-1 and m > 1:
                        for i in range(n):
                            elim += my_arr[ir-1][i]
                    elif ir == 0 and m == 1:
                        pass
                    elif ir == m-1 and m == 1:
                        pass
                    else:
                        for i in range(n):
                            elim += my_arr[ir+1][i]
                            elim += my_arr[ir-1][i]
                elif c == temp:
                    elim2 = 0
                    if ic == 0 and n > 1:
                        elim2 += my_arr[ir][ic+1]
                    elif ic == n-1 and n > 1:
                        elim2 += my_arr[ir][ic-1]
                    elif ic == 0 and n == 1:
                        pass
                    elif ic == n-1 and n == 1:
                        pass
                    else:
                        elim2 += my_arr[ir][ic+1]
                        elim2 += my_arr[ir][ic-1]
                    if ir == 0 and m > 1:
                        for i in range(n):
                            elim2 += my_arr[ir+1][i]
                    elif ir == m-1 and m > 1:
                        for i in range(n):
                            elim2 += my_arr[ir-1][i]
                    elif ir == 0 and m == 1:
                        pass
                    elif ir == m-1 and m == 1:
                        pass
                    else:
                        for i in range(n):
                            elim2 += my_arr[ir+1][i]
                            elim2 += my_arr[ir-1][i]
                    if elim > elim2:
                        temp = c
                        x = ir
                        y = ic
                        elim = elim2
        num += my_arr[x][y]
        my_arr[x][y] = 0
        if y == 0 and n > 1:
            my_arr[x][y+1] = 0
        elif y == n-1 and n > 1:
            my_arr[x][y-1] = 0
        elif y == 0 and n == 1:
            pass
        elif y == n-1 and n == 1:
            pass
        else:
            my_arr[x][y+1] = 0
            my_arr[x][y-1] = 0
        if x == 0 and m > 1:
            for i in range(n):
                my_arr[x+1][i] = 0
        elif x == m-1 and m > 1:
            for i in range(n):
                my_arr[x-1][i] = 0
        elif x == 0 and m == 1:
            pass
        elif x == m-1 and m == 1:
            pass
        else:
            for i in range(n):
                my_arr[x+1][i] = 0
                my_arr[x-1][i] = 0
        null_m = True
        for r in my_arr:
            for c in r:
                if c != 0:
                    null_m = False
    return num

if __name__ == '__main__':
    my_arr = []
    while True:
        my_arr = []
        inp = input()
        if inp == '0 0':
            break
        size = inp.split(' ')
        m, n = int(size[0]), int(size[1])
        for i in range(m):
            row = input().split(' ')
            new_r = []
            for r in row:
                new_r.append(int(r))
            my_arr.append(new_r)
        print(get_candies_num(m, n))
        
    
