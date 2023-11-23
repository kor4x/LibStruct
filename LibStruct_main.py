
#Library Database Management System-GUI

print("Connecting Server...")
import mysql.connector
import sys
import pygame
from pygame.locals import *
mydb = mysql.connector.connect(
     host ="localhost", 
     user ="root", 
     password ="mysquirrel#6T9", 
     database = "Library")
print("Connection Succeeded")
mycursor = mydb.cursor()
pygame.init()

# Display Values:
FPS = 60
WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Library Database Management System - GUI                                  by Kushagra Bhagat 12-Science')

#Elements:
sprites ={}
Hfont = pygame.font.SysFont("Montserrat SemiBold", 39)
Bfont = pygame.font.SysFont("Montserrat", 25)
text_clr = (255, 255, 255)
bg = 'bg.jpg'

#Classes:
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		pos = pygame.mouse.get_pos()

		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action
    
#FUNCTIONS:
global data
global ctr
global state

#PYGAME:
def dtext(text, font, text_col,x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#SEARCH FUNCTIONS:
def BookCodeSearch():
    BookN = int(input("Enter Book Code to find record: ")) 
    q1 = "select * from librarydb"
    mycursor.execute(q1)
    data = mycursor.fetchall()
    leest = list(data)
    for i in leest:
        if i[0]== BookN:
            print(i)

def BookNameSearch():
    BookN = input("Enter Book Name to find record: ") 
    q1 = "select * from librarydb"
    mycursor.execute(q1)
    data = mycursor.fetchall()
    leest = list(data)
    for i in leest:
        if i[1]== BookN:
            print(i)

def AuthorSearch():
    BookN = input("Enter Author Name to find record: ") 
    q1 = "select * from librarydb"
    mycursor.execute(q1)
    data = mycursor.fetchall()
    leest = list(data)
    for i in leest:
        if i[2]== BookN:
            print(i)

def PriceSearch():
    BookN = int(input("Enter Book Price to find record: ")) 
    q1 = "select * from librarydb"
    mycursor.execute(q1)
    data = mycursor.fetchall()
    leest = list(data)
    for i in leest:
        if i[3] == BookN:
            print(i)

def StockSearch():
    
    sql = "SELECT Sno, BookName, TotalQty FROM librarydb"
    mycursor.execute(sql)

    results = mycursor.fetchall()

    widths = []
    columns = []
    t = '|'
    separator = '+' 

    for cd in mycursor.description:
        tup = 20
        widths.append(max((tup), len(cd[0])))
        columns.append(cd[0])
        

    for w in widths:
        t += " %-"+"%ss |" % (w,)
        separator += '-'*w + '--+'

    print(separator)
    print(t % tuple(columns))
    print(separator)
    for row in results:
        print(t % row)
    print(separator)

def ASearch():
    sql = "SELECT Sno, BookName, Available FROM librarydb"
    mycursor.execute(sql)

    results = mycursor.fetchall()

    widths = []
    columns = []
    t = '|'
    separator = '+' 

    for cd in mycursor.description:
        tup = 20
        widths.append(max((tup), len(cd[0])))
        columns.append(cd[0])
        

    for w in widths:
        t += " %-"+"%ss |" % (w,)
        separator += '-'*w + '--+'

    print(separator)
    print(t % tuple(columns))
    print(separator)
    for row in results:
        print(t % row)
    print(separator)

#PRIMARY FUNCTIONS
def ViewAll ():
    q1 = "select * from librarydb"
    mycursor.execute(q1)
    data = mycursor.fetchall()
    for i in data:
        print(i)

def newView():
    sql = "SELECT * FROM librarydb"
    mycursor.execute(sql)

    results = mycursor.fetchall()

    widths = []
    columns = []
    t = '|'
    separator = '+' 

    for cd in mycursor.description:
        tup = 20
        widths.append(max((tup), len((cd[0]))))
        columns.append(cd[0])

    for w in widths:
        t += " %-"+"%ss |" % (w,)
        separator += '-'*w + '--+'

    print(separator)
    print(t % tuple(columns))
    print(separator)
    for row in results:
        print(t % row)
    print(separator)
        
def InsertVal():
    SNo = int(input("Enter BookCode: "))
    BookName = str(input("Enter Book Name: "))
    AuthorName = str(input("Enter Author Name: "))
    Price = int(input("Enter price of book: "))
    TotalQty = int(input("Enter total stock of book: "))
    Available = 0 + TotalQty

    q2 = "insert into librarydb (Sno, BookName, AuthorName, Price, TotalQty, Available) values(%s, %s, %s, %s,%s,%s)"
    val = (SNo, BookName, AuthorName, Price, TotalQty, Available)
    mycursor.execute(q2,val)
    mydb.commit()
    print("\nRecord added successfully")

def delete():
    sql = "SELECT Sno, BookName FROM librarydb"
    mycursor.execute(sql)

    results = mycursor.fetchall()

    widths = []
    columns = []
    t = '|'
    separator = '+' 

    for cd in mycursor.description:
        tup = 20
        widths.append(max((tup), len((cd[0]))))
        columns.append(cd[0])

    for w in widths:
        t += " %-"+"%ss |" % (w,)
        separator += '-'*w + '--+'

    print(separator)
    print(t % tuple(columns))
    print(separator)
    for row in results:
        print(t % row)
    print(separator)

    Snow = int(input("\nEnter Book Code of record to be deleted: "))
    q3 = "delete from librarydb where SNo = %s"
    mycursor.execute(q3,(Snow,))
    mydb.commit()
    print("Record deleted")

def search ():
    print("1. Book Code Search")
    print("2. Book Name Search")
    print("3. Author Name Search")
    print("4. Price Search")
    print("5. Total Stock Search")
    print("6. Availability Search\n")
    
    What = input("Select Category Number to search: ")
    
    if What == "1":
        BookCodeSearch()
    elif What == "2":
        BookNameSearch()
    elif What == "3":
        AuthorSearch()
    elif What == "4":
        PriceSearch()
    elif What == "5":
        StockSearch()
    elif What == "6":
        ASearch()
    else:
        print("invalid input")

def update ():

    newView()
    Code = int(input("\nEnter Book Code of record to be updated: "))
    print("1. Book Name")
    print("2. Author Name")
    #print("3. Price")
    print("3. Total Quantity")
    #print("5. Available Stock")

    What = str(input("Select Category to Update in record: "))
    
    if What == "Admin":

        q1 = "select * from librarydb"
        mycursor.execute(q1)
        data = mycursor.fetchall()
        leest = list(data)
        for i in leest:
            j = list(i)
            if j[0] == Code:
                j[0] = int(input("Enter New Book Code: "))
                print("Updated Entry: ", j )
                up = j[0]
                q2 = "update librarydb set Sno = %s where SNo = %s"
                mycursor.execute(q2,(up,Code))
                mydb.commit()

            
    elif What == "1":
        q1 = "select * from librarydb"
        mycursor.execute(q1)
        data = mycursor.fetchall()
        leest = list(data)
        for i in leest:
            j = list(i)
            if j[0] == Code:
                j[1] = input("Enter New Book Name: ")
                print("Updated Entry: ", j )
                up = str(j[1])
                q2 = "update librarydb set BookName = %s where SNo = %s"
                mycursor.execute(q2,(up,Code))
                mydb.commit()

    elif What == "2":
        q1 = "select * from librarydb"
        mycursor.execute(q1)
        data = mycursor.fetchall()
        leest = list(data)
        for i in leest:
            j = list(i)
            if j[0] == Code:
                j[2] = input("Enter New Author Name: ")
                print("Updated Entry: ", j )
                up = str(j[2])
                q2 = "update librarydb set AuthorName = %s where SNo = %s"
                mycursor.execute(q2,(up,Code))
                mydb.commit()

    elif What == "lol":
        q1 = "select * from librarydb"
        mycursor.execute(q1)
        data = mycursor.fetchall()
        leest = list(data)
        for i in leest:
            j = list(i)
            if j[0] == Code:
                j[3] = int(input("Enter New book Price: "))
                up = j[3]
                q2 = "update librarydb set Price = %s where SNo = %s"
                mycursor.execute(q2,(up,Code))
                mydb.commit()
                print("Updated Entry: ", j )

    elif What == "3":
        q1 = "select * from librarydb"
        mycursor.execute(q1)
        data = mycursor.fetchall()
        leest = list(data)
        for i in leest:
            j = list(i)
            if j[0] == Code:
                print("1. Add Books")
                print("2. Remove Books")
                ar = int(input("Enter operation: ")) 
                
                if ar == 1:
                    j[4] = int(input("Enter Number of books to add: "))
                    print("Updated Entry: ", j )
                    up = j[4]
                    q2 = "update librarydb set TotalQty= %s where SNo = %s"
                    mycursor.execute(q2,(up,Code))
                    mydb.commit()
                elif ar == 2:
                    j[4] = int(input("Enter Number of books to remove: "))
                    print("Updated Entry: ", j )
                    up = j[4] * -1
                    q2 = "update librarydb set TotalQty= %s where SNo = %s"
                    mycursor.execute(q2,(up,Code))
                    mydb.commit()
                else:
                    print("invalid input")
    elif What == "lol1":
        q1 = "select * from librarydb"
        mycursor.execute(q1)
        data = mycursor.fetchall()
        leest = list(data)
        for i in leest:
            j = list(i)
            if j[0] == Code:
                j[5] = int(input("Enter Updated Availability of books: "))
                print("Updated Entry: ", j )
                up = j[5]
                q2 = "update librarydb set Available = %s where SNo = %s"
                mycursor.execute(q2,(up,Code))
                mydb.commit()
    else:
        print("invalid input")

def ctr():
    q1 = "select * from librarydb"
    mycursor.execute(q1)
    data = mycursor.fetchall()
    ctr1 =0
    for i in data:
        ctr1 +=1
    print("Total number of records in database is ",ctr1)

def top():
    q1 = "select * from librarydb"
    mycursor.execute(q1)
    data = mycursor.fetchall()
    print(data[-1])
    
def issue():
    ASearch()
    Code = int(input("\nEnter Book Code of book to be issued: "))
    q1 = "select * from librarydb"
    mycursor.execute(q1)
    data = mycursor.fetchall()
    leest = list(data)
    for i in leest:
        j = list(i)
        if j[0] == Code:
            print("Enter number of copies of ",j[1]," to be issued: ")
            amt = int(input())
            if amt <= j[5]:
                up = (int(j[5]) - amt)
                q2 = "update librarydb set Available= %s where SNo = %s"
                mycursor.execute(q2,(up,Code))
                mydb.commit()
                print("Successfully issued ",amt," copies of ", j[1])
            else:
                print("Sorry only ", j[5], "copies of ", j[1], " are available")

def returnb():
    
    q1 = "select * from librarydb"
    mycursor.execute(q1)
    data = mycursor.fetchall()
    leest = list(data)
    for i in leest:
        j = list(i)
        print(j[0],j[1])
    Code = int(input("Enter Book Code of book to be returned: "))
    for i in leest:
        j = list(i)
        if j[0] == Code:
            amt = 1
            up = (int(j[5]) + amt)
            q2 = "update librarydb set Available= %s where SNo = %s"
            mycursor.execute(q2,(up,Code))
            mydb.commit()
            print("Successfully returned 1 copy of ", j[1])

def help():
    print("Made by Kushagra of Class 12-Science.")
    print("P.S.- I am lazy so ask me personally, I am not filling this.")

#ButtonIMGs:
one = pygame.image.load("Buttons/1.png").convert_alpha()
two = pygame.image.load("Buttons/2.png").convert_alpha()
three = pygame.image.load("Buttons/3.png").convert_alpha()
four = pygame.image.load("Buttons/4.png").convert_alpha()
five = pygame.image.load("Buttons/5.png").convert_alpha()
six = pygame.image.load("Buttons/6.png").convert_alpha()
seven = pygame.image.load("Buttons/7.png").convert_alpha()
eight = pygame.image.load("Buttons/8.png").convert_alpha()
nine = pygame.image.load("Buttons/9.png").convert_alpha()
ten = pygame.image.load("Buttons/10.png").convert_alpha()
eleven = pygame.image.load("Buttons/11.png").convert_alpha()
twelve = pygame.image.load("Buttons/12.png").convert_alpha()

#BUTTONS:
bone = Button(110, 150, one, 1)
btwo = Button(110, 300, two, 1)
bthree = Button(110, 450, three, 1)
bfour = Button(260, 150, four, 1)
bfive = Button(260, 300, five, 1)
bsix = Button(260, 450, six, 1)
bseven = Button(410, 150, seven, 1)
beight = Button(410,300, eight, 1)
bnine = Button(410, 450, nine, 1)
bten = Button(560, 150, ten, 1)
beleven = Button(560, 300, eleven, 1)
btwelve = Button(560, 450, twelve, 1)

#PYMAIN:
run = True
while run:
    #persistent values:
    sprites['bg'] = (pygame.image.load(bg).convert())
    screen.blit(sprites['bg'], (0, 0))
    dtext("Library Database Management System", Hfont,text_clr, 10,25)
    state = 0
    #conditional values:
    if state == 0:
        dtext("Select operation to perform:", Bfont,text_clr, 15,125)
    if bone.draw(screen):
        newView()
        state = 1
    if btwo.draw(screen):
        InsertVal()
        state = 2
    if bthree.draw(screen):
        delete()
        state = 3
    if bfour.draw(screen):
        search()
        state = 4
    if bfive.draw(screen):
        update()
        state = 5
    if bsix.draw(screen):
        ctr()
        state = 6
    if bseven.draw(screen):
        top()
        state = 7
    if beight.draw(screen):
        StockSearch()
        state = 8
    if bnine.draw(screen):
        ASearch()
        state = 9
    if bten.draw(screen):
        issue()
        state = 10
    if beleven.draw(screen):
        returnb()
        state = 11
    if btwelve.draw(screen):
        help()
        state = 12
    pygame.display.update()

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()