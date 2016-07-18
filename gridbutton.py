import Tkinter
import tkMessageBox


top = Tkinter.Tk()

#button callbacks the entry insert 100 is so the nubers go in order
def number1():
    Entry.insert(20, "1")
def number2():
    Entry.insert(20, "2")
def number3():
    Entry.insert(20, "3")
def number4():
    Entry.insert(20,"4")
def number5():
    Entry.insert(20,"5")    
def number6():
    Entry.insert(20,"6")  
def number7():
    Entry.insert(20,"7")
def number8():
    Entry.insert(20,"8")  
def number9():
    Entry.insert(20,"9")  
def number0():
    Entry.insert(20,"0")  
def pound():
    Entry.insert(20,"#")  
def star():
    Entry.insert(20,"*") 

#calling functions
#make call sends number to call to serial the entry.get collects the numbers entered in the dialer. 
 
#deletes one diget at a time
def delete():
    Entry.delete(0)
def textMessage():
    print "text message"

    
          
#buttons .grid followed by column and row placement puts in grid
A = Tkinter.Button(top, text="1", command = number1)
A.grid(column=0, row=1)
B = Tkinter.Button(top, text="2", command = number2)
B.grid(column=1, row=1)
C = Tkinter.Button(top, text="3", command = number3)
C.grid(column=2, row=1)
D = Tkinter.Button(top, text="4", command = number4)
D.grid(column=0, row=2)
E = Tkinter.Button(top, text="5", command = number5)
E.grid(column=1, row=2)
F = Tkinter.Button(top, text="6", command = number6)
F.grid(column=2, row=2)
G = Tkinter.Button(top, text="7", command = number7)
G.grid(column=0, row=3)
H = Tkinter.Button(top, text="8", command = number8)
H.grid(column=1, row=3)
I = Tkinter.Button(top, text="9", command = number9)
I.grid(column=2, row=3)
J = Tkinter.Button(top, text="*", command = star)
J.grid(column=0, row=4)
K = Tkinter.Button(top, text="0", command = number0)
K.grid(column=1, row=4)
L = Tkinter.Button(top, text="#", command = pound)
L.grid(column=2, row=4)
M = Tkinter.Button(top, text="del", command = delete)
M.grid(column=3, row=1)
N = Tkinter.Button(top, text="call", command = make_call)
N.grid(column=3, row=2)
O = Tkinter.Button(top, text="end", command = end_call)
O.grid(column=3, row=3)
P = Tkinter.Button(top, text="text", command = textMessage)
P.grid(column=3, row=4)


#numbers dialed printout .grid(rowspan=1) means how many rows it spans
Entry = Tkinter.Entry(top, width= 15 ,bd=5)
Entry.grid(row=0, columnspan=4, rowspan=1)


