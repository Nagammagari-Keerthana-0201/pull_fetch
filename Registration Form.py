import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Registration Form')
root.geometry('500x500')
root.minsize(500, 500)
root.configure(bg='#8FBC8F')

form = tk.Label(root, text='Registration form', width=20, font=('Cambria', 10, 'bold'),bg='#0000FF',fg='#FFFFFF')
form.grid(padx=150,pady=50,sticky='n',columnspan=4)

F_Name = tk.Label(root, text='First_Name', width=20, font=('Cambria', 10))
F_Name.grid(row=1, column=1,padx=18,pady=5,sticky='w')
text1 = tk.Entry(root,width=25)
text1.grid(row=1, column=2,sticky='w',padx=10)

L_Name=tk.Label(root,text='Last_Name',width=20,font=('Cambria',10))
L_Name.grid(row=2,column=1,padx=18,pady=5,sticky='w')
text2=tk.Entry(root,width=25)
text2.grid(row=2,column=2,sticky='w',padx=10)

R_No=tk.Label(root,text='Reg_No',width=20,font=('Cambria',10))
R_No.grid(row=3,column=1,padx=18,pady=5,sticky='w')
text3=tk.Entry(root,width=25)
text3.grid(row=3,column=2,sticky='w',padx=10)

Gender=tk.Label(root,text='Gender',width=20,font=('Cambria',10))
Gender.grid(row=4,column=1,padx=18,pady=5,sticky='w')

Gender_Selection = tk.StringVar(value=' ')
Gender_Male = tk.Radiobutton(root, text='Male', value='Male', variable=Gender_Selection,font=('Cambria',10))
Gender_Male.grid(row=4, column=2, sticky='w', padx=10)

Gender_Female = tk.Radiobutton(root, text='Female', value='Female', variable=Gender_Selection,font=('Cambria',10))
Gender_Female.grid(row=5, column=2, sticky='w', padx=10)

Year=tk.Label(root,text='Year Of Study',width=20,font=('Cambria',10))
Year.grid(row=6,column=1,padx=18,pady=5,sticky='w')

Menu_List=('Select the Year','I-Year','II-Year','III-Year','IV-Year')
Menu=ttk.Combobox(root,values=Menu_List,font=('Cambria',10))
Menu.grid(row=6,column=2,sticky='w',padx=10)
Menu.set(Menu_List[0])

Branch=tk.Label(root,text='Branch',width=20,font=('Cambria',10))
Branch.grid(row=7,column=1,padx=18,pady=5,sticky='w')

#Branch_1=tk.Checkbutton(root,text='CSE')
#Branch_1.grid(row=7,column=2padx=10,sticky='w')
#Branch_2=tk.Checkbutton(root,text='CB/DS')
#Branch_2.grid(row=8,column=2padx=10,sticky='w')
#Branch_3=tk.Checkbutton(root,text='AIML')
#Branch_3.grid(row=9,column=2padx=10,sticky='w')

Branch_List=('Select the Branch','CSE','CB/DS','AIML','ECE','EEE','CIVIL','MECH','Other')
Branch=ttk.Combobox(root,values=Branch_List,font=('Cambria',10))
Branch.grid(row=7,column=2,padx=10,sticky='w')
Branch.set(Branch_List[0])
def on_Branch_select(event):
            if  Branch.get() =='Other':
                text4=tk.Entry(root,width=25)
                text4.grid(row=8,column=2,padx=10,sticky='w')      
Branch.bind('<<ComboboxSelected>>',on_Branch_select)

Submit=tk.Button(root,text='Submit',width=10,bg='#FFA07A', fg='#FFFFFF')
Submit.grid(padx=150,pady=20,sticky='s',columnspan=4)

root.mainloop()

