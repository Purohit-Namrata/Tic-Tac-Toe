import tkinter as tk
from tkinter import messagebox


current_player=1
counter=0

def restart():
    current_player=2
    counter=0
    b1['text']=""
    b2['text']=""
    b3['text']=""
    b4['text']=""
    b5['text']=""
    b6["text"]=""
    b7['text']=""
    b8['text']=""
    b9['text']=""


def buttonclick(x):
    global current_player,counter
    if (x==1 and current_player==1 and b1['text']==""):
        b1['text']=="X"
        current_player=2
        counter+=1
    if(x==2 and current_player==1 and b2['text']==""):
        b2['text']=="X"
        current_player=2
        counter+=1
    if(x==3 and current_player==1 and b3['text']==""):
        b3['text']=="X"
        current_player=2
        counter+=1
    if(x==4 and current_player==1 and b4['text']==""):
        b4['text']=="X"
        current_player=2
        counter+=1
    if(x==5 and current_player==1 and b5['text']==""):
        b5['text']=="X"
        current_player=2
        counter+=1
    if(x==6 and current_player==1 and b6['text']==""):
        b6['text']=="X"
        current_player=2
        counter+=1
    if(x==7 and current_player==1 and b7['text']==""):
        b7['text']=="X"
        current_player=2
        counter+=1
    if(x==8 and current_player==1 and b8['text']==""):
         b8['text']="X"
         current_player=2
         counter+=1
    if(x==9 and current_player==1 and b9['text']==""):
        b9['text']=="X"
        current_player=2
        counter+=1
    
    if ((x==1) and (current_player==2) and (b1['text']=="")):
        b1['text']=="O"
        current_player=1
        counter+=1
    if(x==2 and current_player==2 and b2['text']==""):
        b2['text']=="O"
        current_player=1
        counter+=1
    if(x==3 and current_player==2 and b3['text']==""):
        b3['text']=="O"
        current_player=1
        counter+=1
    if(x==4 and current_player==2 and b4['text']==""):
        b4['text']=="O"
        current_player=1
        counter+=1
    if(x==5 and current_player==2 and b5['text']==""):
        b5['text']=="O"
        current_player=1
        counter+=1
    if(x==6 and current_player==2 and b6['text']==""):
        b6['text']=="O"
        current_player=1
        counter+=1
    if(x==7 and current_player==2 and b7['text']==""):
        b7['text']=="O"
        current_player=1
        counter+=1
    if(x==8 and current_player==2 and b8['text']==""):
         b8['text']="O"
         current_player=1
         counter+=1
    if(x==9 and current_player==2 and b9['text']==""):
        b9['text']=="O"
        current_player=1
        counter+=1



root=tk.Tk()
root.title("Tic-Tac-Toe")

b1=tk.Button(root,text='',width=8,height=4,fg="black",command=lambda : buttonclick(1))
b1.grid(row=0,column=0)

b2=tk.Button(root,text='',width=8,height=4,fg="black",command=lambda : buttonclick(2))
b2.grid(row=0,column=1)

b3=tk.Button(root,text='',width=8,height=4,fg="black",command=lambda : buttonclick(3))
b3.grid(row=0,column=2)

b4=tk.Button(root,text='',width=8,height=4,fg="black",command=lambda : buttonclick(4))
b4.grid(row=1,column=0)

b5=tk.Button(root,text='',width=8,height=4,fg="black",command=lambda : buttonclick(5))
b5.grid(row=1,column=1)

b6=tk.Button(root,text='',width=8,height=4,fg="black",command=lambda : buttonclick(6))
b6.grid(row=1,column=2)

b7=tk.Button(root,text='',width=8,height=4,fg="black",command=lambda : buttonclick(7))
b7.grid(row=2,column=0)

b8=tk.Button(root,text='',width=8,height=4,fg="black",command=lambda : buttonclick(8))
b8.grid(row=2,column=1)

b9=tk.Button(root,text='',width=8,height=4,fg="black",command=lambda : buttonclick(9))
b9.grid(row=2,column=2)

b10=tk.Button(root,text="Exit",command=root.destroy)
b10.grid(row=4,column=1)
if counter==9:
    if(b1['text']=='X' and b2['text']=='X' and b3['text']=='X' or
        b4['text']=='X' and b5['text']=='X' and b6['text']=='X' or
        b7['text']=='X' and b8['text']=='X' and b9['text']=='X' or
        b1['text']=='X' and b4['text']=='X' and b7['text']=='X' or
        b2['text']=='X' and b5['text']=='X' and b8['text']=='X' or
        b3['text']=='X' and b6['text']=='X' and b9['text']=='X' or
        b1['text']=='X' and b5['text']=='X' and b9['text']=='X' or
        b3['text']=='X' and b5['text']=='X' and b7['text']=='X'):
        answer= tk.messagebox.askyesno("Result","Player 1 is winner. Do you want to  resart the game?","Yes","No")
    elif( b1['text']=='O' and b2['text']=='O' and b3['text']=='O' or
        b4['text']=='O' and b5['text']=='O' and b6['text']=='O' or
        b7['text']=='O' and b8['text']=='O' and b9['text']=='O' or
        b1['text']=='O' and b4['text']=='O' and b7['text']=='O' or
        b4['text']=='O' and b5['text']=='O' and b8['text']=='O' or
        b3['text']=='O' and b6['text']=='O' and b9['text']=='O' or
        b1['text']=='O' and b5['text']=='O' and b9['text']=='O' or
        b3['text']=='O' and b5['text']=='O' and b7['text']=='O'):
            answer=tk.messagebox.askyesno("Result","Player 1 is winner. Do you want to  resart the game?","Yes","No")
    else:
        
        tk.messagebox.showinfo("Result","Match is Draw.")
    
    if answer:
        restart()


root.mainloop()