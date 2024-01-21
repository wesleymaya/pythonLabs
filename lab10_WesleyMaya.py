class BankAccount():

    def __init__(self,num=0):
        self.bal = num

    def withdraw(self,with1):
        self.bal -= with1

    def deposit(self,dep):
        self.bal += dep

    def balance(self):
        return self.bal

    def __repr__(self):
        return "BankAccount"+"("+ str(self.bal)+")"

wesley = BankAccount(700)


class PingPong():

    def __init__(self):
        self.play = "PONG"

    def next(self):
        if self.play == "PING":
            self.play = "PONG"
            print(self.play)

        else:
            self.play = "PING"
            print(self.play)

ball = PingPong()

class Queue():

    def __init__(self):
        self.list = []

    def enqueue(self,new):
        self.list += [new]

    def dequeue(self):
        qr = self.list[0]
        del self.list[0]
        return qr

    def isEmpty(self):
        return len(self.list) == 0

    def get(self):
        return self.list

    def __eq__(self,c2):
        return self.list == c2

    def __repr__(self):
        return "Queue"+"("+str(self.list)+")"

    def __len__(self):
        return len(self.list)

appts = Queue()
appts.enqueue('John')
appts.enqueue('Annie')
appts.enqueue('Sandy')

q1=Queue()
q1.enqueue('kiwi')
q1.enqueue('apple')
q2=Queue()
q2.enqueue('apple')


class Marsupial():

    def __init__(self, col):
        self.c  = col
        self.pouch = []

    def put_in_pouch(self, new1):
        self.pouch += [new1]

    def pouch_contents(self):
        return self.pouch

    def __repr__(self):
        return "I am a "+ self.c +" Marsupial"


m = Marsupial("red")
m.put_in_pouch('doll')
m.put_in_pouch('firetruck')
m.put_in_pouch('kitten')


class Kangaroo(Marsupial):

    def __init__(self,col,xc=0,yc=0):
        self.c = col
        self.pouch = []
        self.x = xc
        self.y = yc
        self.t = "Kangaroo"
        

    def jump(self,dx,dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return("I am a {0} {1} located at coordinates ({2},{3})".format(self.c,self.t,self.x,self.y))

k = Kangaroo("blue", 0,0)   
k.put_in_pouch('doll')
k.put_in_pouch('firetruck')
k.put_in_pouch('kitten')


k.jump(1,0)
k.jump(1,0)
k.jump(1,0)
    
