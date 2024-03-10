def tictaktoe(a):
    print("|  {}  |  {}  |  {}  |".format(a[1],a[2],a[3]))
    print("|  {}  |  {}  |  {}  |".format(a[4],a[5],a[6]))
    print("|  {}  |  {}  |  {}  |".format(a[7],a[8],a[9]))
print("""enter b/w (1,2,3,4,5,6,7,8,9)
Player1 = X
player2 = O""")

list = ["","","","","","","","","",""]
tictaktoe(list)
for x in range(1,10):

    inp1 = int(input("player 1>>")) #X
    list[inp1] = "X"
    tictaktoe(list)
    inp2 = int(input("player 2>>"))
    list[inp2]= "O"
    tictaktoe(list)