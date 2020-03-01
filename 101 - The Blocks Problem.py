import sys

def opetarions(op): #Selector of operations
    op = line.split(' ')
    if len(op) == 4:
        a1,a,a2,b = op[0],int(op[1]),op[2],int(op[3])
    if a != b:
        if a1 == 'move':
            if a2 == 'onto':
                move_onto(a,b)
            elif a2 == 'over':
                move_over(a,b)
        elif a1 == 'pile':
            if a2 == 'onto':
                pile_onto(a,b)
            if a2 == 'over':
                pile_over(a,b)

def move_onto(a,b):
    apos, bpos = get_pos(a,b)
    if apos[0] != bpos[0]:
        opreturn(apos[0], apos[1])
        opreturn(bpos[0], bpos[1])
        add_number(b,bpos)
        add_number(a,bpos)
        restore()

def move_over(a,b):
    apos, bpos = get_pos(a,b)
    if apos[0] != bpos[0]:
        opreturn(apos[0],apos[1])
        add_number(a,bpos)
        restore()

def pile_onto(a,b):
    apos, bpos = get_pos(a,b)
    if apos[0] != bpos[0]:
        opreturn(bpos[0],bpos[1])
        pi = get_pile(apos[0],apos[1])
        add_number(b,bpos)
        sum_pile(pi, bpos[0])
        restore()

def pile_over(a,b):
    apos, bpos = get_pos(a,b)
    if apos[0]!= bpos[0]:
        pi = get_pile(apos[0],apos[1])
        sum_pile(pi, bpos[0])

def sum_pile(pi,x): #Add the pile to b pile
    for n in pi:
        table[x].append(n)

def get_pos(a,b): #Get the position of a and b
    itl = 0
    for ls in table:
        itn = 0
        for num in ls:
            if num == a:
                apos = (itl,itn)
            if num == b:
                bpos = (itl, itn)
            itn += 1
        itl += 1
    return apos, bpos

def add_number(num, bpos): #Puts a num onto another num
    table[bpos[0]].append(num)

def opreturn(x,y): #Return a block to it's initial position
    if len(table[x])-1 != y:
        for num in range(y,len(table[x])):
            s = table[x].pop(y)
    else:
        s = table[x].pop(y)

def restore(): #Restore to initial position
    patt = []
    for n in range(0,len(table)):
        patt.append(n)
    for ls in table:
        for num in ls:
            patt.remove(num)
    for n in patt:
        table[n].insert(0,n)

def get_pile(x,y): #Obtain the pile
    pi = []
    for n in range(y,len(table[x])):
        pi.append(table[x][y])
        table[x].pop(y)
    return pi

def create_table(n):
    for i in range(0,n):
        col= []
        col.append(i)
        table.append(col)

n = int(input()) #number of blocks
table = []
create_table(n)
for line in sys.stdin: #While not quit
    if 'quit'== line.rstrip():
        counter = 0
        for p in table:
            stri = str(counter)+':'
            for num in p:
                stri += ' '+str(num)
            print(stri)
            counter += 1
        quit()
    else:
        opetarions(line)
