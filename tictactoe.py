class TicTac:
    def __init__(self):
        self.l = [[" "," "," "],[" "," "," "],[" "," "," "]]
    def iswin(self):
        l = self.l
        
    #cheking row values
        for i in l:
            if i[0] == " ":
                continue
            if i[0] == i[1]and i[1] == i[2]:
                print("won",i[0])
                return True   
    #checking digonal values
        if l[0][0] == l[1][1] and l[1][1] == l[2][2]:
            print("won",l[0][0])
            return True
        if l[0][2] == l[1][1] and l[2][0] == l[1][1]:
            print("won",l[1][1])
            return True
        col = 0
        for i in range(3):
            if l[0][col] == l[1][col] and l[1][col] == l[2][col]:
                print("won",l[0][col])
                return True
            else:
                col+=1
    def game(self):
        l = self.l
        val = 0
        count = 0
        while True:
            x,y = map(int,input("Enter the position").split())
            if (x<1 and x>3) and (y<1 and y>3):
                print("Enter the correct coordinates")
                continue
            if l[x-1][y-1] != " ":
                print("Alread the value is there")
                continue
            if val%2== 0:
                l[x-1][y-1] = "X"
            else:
                l[x-1][y-1] = "O"
            for i in l:
                print("|---|---|---|")
                for j in i:
                    print("  "+j,end = " ")
                print('')
            print("|---|---|---|")
            if count == 8:
                break
            if count >= 4:
                print("check")
                if self.iswin():
                    return True
                    break
            count+=1
            val+=1
obj = TicTac()
if not obj.game():
    print("Draw")
    
        
    
    
    
