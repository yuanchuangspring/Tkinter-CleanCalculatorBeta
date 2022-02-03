"""
name:小沙雕计算器
edition：3.0.2   [eval复原版本]
author:yuanchuang
Email:3358851903@qq.com（欢迎交流）
"""
from tkinter import *
from tkinter import messagebox
from decimal import *





tip = 0
       
def shuru(a):
            global tip
            if shuchu.get()=="0":
                shuchu.set(a)
            else:
                
                if a == "%":
                    try:
                        shuchu.set(eval(shuchu.get()+"/100"))
                    except BaseException:
                        messagebox.showinfo("tip","计算力上限")
                        
                else:
                    shuchu.set(shuchu.get() + str(a))
                    if len(shuchu.get())>6 and tip == 0:
                          messagebox.showinfo("tip","超出七个字符可能显示不全")
                          
                          tip = 1
          
                
def de():
                shuchu.set("0")   
def dell():
            shuchu.set(shuchu.get()[:-1])
            
        
def dengyu():
             try:
                 shuchu.set(shuchu.get().replace("×","*"))
                 shuchu.set(shuchu.get().replace("÷","/"))
             
                 shuchu.set(eval(shuchu.get()))
                 
                 if len(shuchu.get())==7 and tip!=1:
                    
                    
                    messagebox.showinfo("tip","超出七个字符可能显示不全")
                        
             except SyntaxError:
                     messagebox.showinfo("tip","输入有误")
                     de()
             except ZeroDivisionError:
                     messagebox.showinfo("tip","输入有误")
                     de()
                     
                     
def kuaijie():
          try:
              shuchu.set(shuchu.get()[:shuchu.get().index(".")+3])                         
          except ValueError:
              messagebox.showinfo("tip","无小数点，不需要精确！")
        #创建主窗口
root = Tk()
zibs = 50


        #输出台架构
shuchu = StringVar()
shuchu.set("0")
result = LabelFrame(root,text="输出台        欢迎使用       小沙雕计算器3.0",bg="bisque")



reword = Entry(result,textvar=shuchu,font=(None,zibs),fg="black",bg="bisque")
        
reword.pack(anchor="e")
result.pack(fill="x",anchor="center")    
        #输入台架构
eve = LabelFrame(root,text="按键",bg="azure")
        
b1 = Button(eve,text=1,bd=10,bg="sandybrown",font=(None,40),command=lambda:shuru(1)).grid(row=1,column=0)
        
b2 = Button(eve,text=2,bd=10,bg="lavender",font=(None,40),command=lambda:shuru(2)).grid(row=1,column=1)
        
b3 = Button(eve,text=3,bd=10,bg="sandybrown",font=(None,40),command=lambda:shuru(3)).grid(row=1,column=2)
        
b4 = Button(eve,text=4,bd=10,bg="lavender",font=(None,40),command=lambda:shuru(4)).grid(row=2,column=0)
        
b5 = Button(eve,text=5,bd=10,bg="sandybrown",font=(None,40),command=lambda:shuru(5)).grid(row=2,column=1)
        
b6 = Button(eve,text=6,bd=10,bg="lavender",font=(None,40),command=lambda:shuru(6)).grid(row=2,column=2)
        
b7 = Button(eve,text=7,bd=10,bg="sandybrown",font=(None,40),command=lambda:shuru(7)).grid(row=3,column=0)
        
b8 = Button(eve,text=8,bd=10,bg="lavender",font=(None,40),command=lambda:shuru(8)).grid(row=3,column=1)
        
b9 = Button(eve,text=9,bd=10,bg="sandybrown",font=(None,40),command=lambda:shuru(9)).grid(row=3,column=2)
        
bcheng = Button(eve,text="×",bd=10,bg="wheat",font=(None,40),command=lambda:shuru("×")).grid(row=1,column=3)
        
bjian = Button(eve,text="-",bd=10,bg="wheat",font=(None,40),width=1,height=1,command=lambda:shuru("-")).grid(row=2,column=3)
        
bnone = Button(eve,text="C",bd=10,bg="wheat",font=(None,40),width=1,height=1,command=de).grid(row=0,column=0)
        
b0 = Button(eve,text=0,bd=10,bg="sandybrown",font=(None,40),command=lambda:shuru(0)).grid(row=4,column=1)
        
bshan = Button(eve,text="←",bd=10,bg="wheat",font=(None,40),width=1,height=1,command=dell).grid(row=0,column=1)
        
bbaifen = Button(eve,text="%",bd=10,bg="wheat",font=(None,40),width=1,height=1,command=lambda:shuru("%")).grid(row=0,column=2)
        
bchu = Button(eve,text="÷",bd=10,bg="wheat",font=(None,40),width=1,height=1,command=lambda:shuru("÷")).grid(row=0,column=3)
        
bjia = Button(eve,text="+",bd=10,bg="wheat",font=(None,40),width=1,height=1,command=lambda:shuru("+")).grid(row=3,column=3)
        
bpoint = Button(eve,text=".",bd=10,bg="wheat",font=(None,40),width=1,height=1,command=lambda:shuru(".")).grid(row=4,column=2)
        
bdengyu = Button(eve,text="=",bd=10,bg="coral",font=(None,40),width=1,height=1,command=dengyu).grid(row=4,column=3)
        
bgaoji = Button(eve,text="省",bd=10,bg="brown",width=1,height=1,font=(None,40),command=kuaijie).grid(row=4,column=0)
        
        
        
        
eve.pack(fill="x")

root.mainloop()
        