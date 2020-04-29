def board(bo):
    print("-----------")
    print("   |   |   ")
    print(" "+bo[0]+" | "+bo[1]+" | "+ bo[2])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" "+bo[3]+" | "+bo[4]+" | "+ bo[5])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" "+bo[6]+" | "+bo[7]+" | "+ bo[8])
    print("   |   |   ")
    print("-----------")

def notfree(bo, n):
    if bo[n]=="X" or bo[n]=="0":
        return 1
    else: return 0

def move(bo, n, m):
    bo[n]=m

def isfull(bo):
    ok=1
    for x in bo:
        if x!="0" and x!="X":
            ok=0
    return ok

def win(bo, m):
    if (bo[0]==m and bo[1]==m and bo[2]==m) or (bo[3]==m and bo[4]==m and bo[5]==m) or (bo[6]==m and bo[7]==m and bo[8]==m) or (bo[0] == m and bo[3] == m and bo[6] == m) or (bo[1] == m and bo[4] == m and bo[7] == m) or (bo[2] == m and bo[5] == m and bo[8] == m) or (bo[0] == m and bo[4] == m and bo[8] == m) or (bo[2] == m and bo[4] == m and bo[6] == m):
        return 1
    else: return 0

def play():
    bo=["1","2","3","4","5","6","7","8","9"]
    i=0

    while True:
        board(bo)

        if i%2==0:
            print("Is X move!")
        else: print("Is 0 move!")

        n=int(input())-1
        while notfree(bo, n):
            print("Wrong!")
            n=int(input())-1

        if i%2==0:
            move(bo, n, "X")
            if win(bo, "X"):
                print("X Win!")
                break

        else:
            move(bo, n, "0")
            if win(bo, "0"):
                print("0 Win!")
                break
        i+=1

        if isfull(bo):
            print("End Game")
            break
    board(bo)

play()