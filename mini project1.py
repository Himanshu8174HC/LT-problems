import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os
wind = tk.Tk()
wind.title("GUI")

#creating Lable
name_lable=ttk.Label(wind, text="Enter your name :") # if we use pack() then it return in middel 
name_lable.grid(row=0,column=0, sticky=tk.W) #  remove the indentation  in initial

age_lable=ttk.Label(wind, text="Enter your age :")
age_lable.grid(row=1,column=0, sticky=tk.W)

email_label=ttk.Label(wind, text="Enter your email :")
email_label.grid(row=2,column=0,sticky=tk.W)

gender_label=ttk.Label(wind,text="Select Your Gender :")
gender_label.grid(row=3,column=0,sticky=tk.W)

#creating Entrybox
name_var=tk.StringVar()
name_entrybox=ttk.Entry(wind,width=16,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

age_var=tk.StringVar()
age_entrybox=ttk.Entry(wind,width=16,textvariable=age_var)
age_entrybox.grid(row=1,column=1)

email_var=tk.StringVar()
email_entrybox=ttk.Entry(wind,width=16,textvariable=email_var)
email_entrybox.grid(row=2,column=1)

#creat combobox
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(wind ,width=13,textvariable=gender_var,state="readonly")
gender_combobox["values"]=("Gender","Male","Female", "Other")
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)

#Radio Button
user_type = tk.StringVar()
radiobtn1=ttk.Radiobutton(wind,text="Student",value="Student",variable=user_type)
radiobtn1.grid(row=4,column=0)
radiobtn2=ttk.Radiobutton(wind,text="Teacher",value="Teacher",variable=user_type)
radiobtn2.grid(row=4,column=1)

#checkButton
checkbtn_var=tk.IntVar()
checkbtn=ttk.Checkbutton(wind,text="check if you if you want",variable=checkbtn_var)
checkbtn.grid(row=5,columnspan=1)







#creating Button

# def action():
#     username=name_var.get()
#     userage=age_var.get()
#     user_email=email_var.get()
#     print(f"{username} is  {userage} years old and his email address is {user_email}")
#     user_gender=gender_var.get()
#     usertype=user_type.get()
#     if checkbtn_var.get()==0:
#         subscribed="No"
#     else:
#         subscribed="Yes"

#     print(user_gender,usertype,subscribed)
#     with open("file.txt","a") as f:
#         f.write(f"{username},{userage},{user_email},{user_gender},{usertype},{subscribed}\n")
      
#     name_entrybox.delete(0,tk.END)
#     age_entrybox.delete(0,tk.END)
#     email_entrybox.delete(0,tk.END)
#     name_lable.configure(foreground="blue")
#     Submit_button.configure(foreground="red") #if we use tk,button then it"s right if we use .ttk the we have to use style
 

def action():
    username=name_var.get()
    userage=age_var.get()
    user_email=email_var.get()
    print(f"{username} is  {userage} years old and his email address is {user_email}")
    user_gender=gender_var.get()
    usertype=user_type.get()
    if checkbtn_var.get()==0:
        subscribed="No"
    else:
        subscribed="Yes"
    
    with open ("file.csv","a" ,newline="") as f:
        dict_writer=DictWriter(f,fieldnames=["userName","user email address","user age","user gender","user type" ,"subscribed"])
        if os.stat("file.csv").st_size==0:
            dict_writer.writeheader()
            
        dict_writer.writerow({
            "userName":username,
            "user email address" : user_email,
            "user age" : userage,
            "user gender" :user_gender,
            "user type" : usertype,
            "subscribed" :subscribed,
            
            
            

        })

    
    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    name_lable.configure(foreground="blue")

Submit_button=tk.Button(wind,text="Submit", command=action)
Submit_button.grid(row=6,column=0 ,sticky=tk.W)


wind.mainloop()