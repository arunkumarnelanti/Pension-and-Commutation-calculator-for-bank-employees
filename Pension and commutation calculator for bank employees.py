from tkinter import *
from tkinter import messagebox
from random import *

#layout
root=Tk()
root.title("GUI")
root.geometry('600x500')

title_label=Label(root, text="Pension and Commutation Calculator for Bank Employees",font=('Verdana',13))
title_label.grid(row=1,column=0,columnspan=2, ipadx=20,ipady=20,padx=30,pady=(20,10))
title_label=Label(root, text="Select the Retirement:",font=13)
title_label.grid(row=4,column=0,columnspan=2, ipadx=20,ipady=20,padx=30,pady=(20,10))
    
#regular retirement calculaion
def calculate01():
    try:
        a=int(service_years.get())
        if(a>33):
            a=33
    except:
         messagebox.showinfo("Error in service years","Enter only integers; if you worked for more that half a year roundup the value or just write the base value")
    try:
        b=int(Basic_pay.get())
    except:
        messagebox.showinfo("Error in basic pay","Enter ony numbers or integers")
    try:
        c=float(DA.get())            
    except:
        messagebox.showinfo("Error in DA","Enter ony numbers")
    try:
        d=float(Commute.get())
        
    except:
        messagebox.showinfo("Error in commute","Enter ony numbers")
    if(d>33.33 or d==0):
            messagebox.showinfo("Error in commute","\nMax commute is 33.33 \ncommute cannot be zero")     
    else:
        e=(b*c/100)+b
        gross_pay=int((e*7*a)/300)
        commutation=int((gross_pay)*d*12*(10.13)/100) 
        monthly_pension=int(((gross_pay)*(100-d))/100)
        messagebox.showinfo("Result","age rate=10.13""Gross Pay   "+str(gross_pay)+'\n'+"Commutation   "+str(commutation)+'\n'+
                        "Monthly Pension   "+str(monthly_pension))
  
#retirement selection
def reg_retirement():
    reg=Tk()
    reg.geometry('500x200')
    reg.title("Regular Retirement calculator")

    
    #regular retairement labels
    L0=Label(reg,text="Total no of years of service (Max=33)")
    L0.grid(row=0, column=0,sticky=E,pady=10)
    L1=Label(reg,text="Enter Basic Pay at the time of Retirement")
    L1.grid(row=2,column=0,sticky=E,pady=10)
    L2=Label(reg,text="Enter Dareness Allowance(DA)(in %)")
    L2.grid(row=4,column=0,sticky=E,pady=10)
    L3=Label(reg,text="Commute(Max=33.33)")
    L3.grid(row=6,column=0,sticky=E)

    
    #Entry for  regular retirement
    global service_years
    service_years=Entry(reg)
    service_years.grid(row=0,column=1)
    global Basic_pay
    Basic_pay=Entry(reg)
    Basic_pay.grid(row=2,column=1)
    global DA
    DA=Entry(reg)
    DA.grid(row=4,column=1)
    global Commute
    Commute=Entry(reg)
    Commute.grid(row=6,column=1)
    submit=Button(reg,text="submit",command=calculate01)
    submit.grid(row=10,column=2)


#voluntary Retirement calculation
def calculate02():

    dict={"21":"9.187","22":"9.186","23":"9.185","24":"9.184","25":"9.183","26":"9.182","27":"9.180",
      "28":"9.178","29":"9.176","30":"9.173","31":"9.169","32":"9.164","33":"9.159","34":"9.152",
      "35":"9.145","36":"9.136","37":"9.126","38":"9.116","39":"9.103","40":"9.090","41":"9.075",
      "42":"9.059","43":"9.040","44":"9.019","45":"8.996","46":"8.971","47":"8.943","48":"8.913","49":"8.881",
      "50":"8.846","51":"8.808","52":"8.768","53":"8.724","54":"8.678","55":"8.627","56":"8.572","57":"8.512",
      "58":"8.446","59":"8.371"}

    try:
        a=int(service_years.get())
        if(a>33):
            a=33
    except:
         messagebox.showinfo("Error in service years","Enter only integers; if you worked for more that half a year roundup the value or just write the base value")
    try:
        b=int(Basic_pay.get())
    except:
        messagebox.showinfo("Error in basic pay","Enter ony numbers or integers")
    try:
        c=float(DA.get())            
    except:
        messagebox.showinfo("Error in DA","Enter ony numbers")
    try:
        d=float(commute.get())    
    except:
        messagebox.showinfo("Error in commute","Enter ony numbers")
    try:
        e=int(retirement_age.get())
        age=str(e)
    except:
        messagebox.showinfo("Error in retirement age","Enter only numbers\n Enter the age at which you retired")
    f=float(dict[age])
        
    if(d>33.33 or d==0):
            messagebox.showinfo("Error in commute","\nMax commute is 33.33 \ncommute cannot be zero")
    else:
        g=int((c*b/100)+b)
        gross_pay=int((g*7*a)/300)
        commutation=int((gross_pay)*d*12*f*0.01)
        monthly_pension=int(gross_pay*(100-d)/100)
        messagebox.showinfo("Result ","age rate="+str(f)+"\n"+"Gross pay="+str(gross_pay)+"\n"+"commutation"+str(commutation)+"\n"+"monthly pension="+str(monthly_pension))
    
        
    
#Voluntary Retirement Selection
def vol_retirement():
    vol=Tk()
    vol.geometry('400x400')
    vol.title("Voluntary Retirement Calculator")
    
#voluntary retirement labels
    L0=Label(vol,text="(Total no of service years(Max=33)")
    L0.grid(row=0,column=0,sticky=E,padx=8,pady=10)
    L1=Label(vol,text="Age at the time of retirement")
    L1.grid(row=1,column=0,sticky=E,pady=10)
    L2=Label(vol,text="Basic pay at the time of retirement")
    L2.grid(row=2,column=0,pady=10,sticky=E)
    L3=Label(vol,text="Enter dareness allowance(DA)(in %)")
    L3.grid(row=3,column=0,pady=10,sticky=E)
    L4=Label(vol,text="Commute(Max=33.3(in %)")
    L4.grid(row=4,column=0,pady=10,sticky=E)

#voluntry retairement entries
    global service_years
    service_years=Entry(vol)
    service_years.grid(row=0,column=1)
    global retirement_age
    retirement_age=Entry(vol)
    retirement_age.grid(row=1,column=1)
    global Basic_pay
    Basic_pay=Entry(vol)
    Basic_pay.grid(row=2,column=1)
    global DA
    DA=Entry(vol)
    DA.grid(row=3,column=1)
    global commute
    commute=Entry(vol)
    commute.grid(row=4,column=1)
    submit=Button(vol,text="submit",command=calculate02)
    submit.grid(row=5,column=2)
    
    

#buttons
Vol =Button(root,text="Voluntary Retirement",command=vol_retirement)
Vol.grid(row=10,column=0,sticky=N,padx=30,pady=10,ipadx=5,ipady=5)
Reg=Button(root,text="Regular Retirement(at age=60)",command=reg_retirement)
Reg.grid(row=10,column=1,sticky=N,padx=30,pady=10,ipadx=5,ipady=5)
root.mainloop()
