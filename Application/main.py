# from tkinter import *
# import backend
# backend.connect()
# def add_command():
#     backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
#     listb.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))
#
# def view_command():
#     listb.delete(0,END)
#     for row in backend.view():
#         listb.insert(END,row)
# def search_command():
#     listb.delete(0,END)
#     for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
#         listb.insert(END, row)
#
# def get_selected_row(event):
#     global selected_tuple
#     index=listb.curselection()[0]
#     selected_tuple=listb.get(index)
#     ent1.delete(0,END)
#     ent1.insert(END,selected_tuple[1])
#
#     ent2.delete(0, END)
#     ent2.insert(END, selected_tuple[2])
#
#     ent3.delete(0, END)
#     ent3.insert(END, selected_tuple[3])
#
#     ent4.delete(0, END)
#     ent4.insert(END, selected_tuple[4])
#
# def update_command():
#     backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
#
# def delete_command():
#     backend.delete(selected_tuple[0])
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# window=Tk()
# window.wm_title('Book Store')
#
# l1=Label(window,text='Title')
# l1.grid(row=0,column=0)
#
# l2=Label(window,text='Author')
# l2.grid(row=0,column=2)
#
# l3=Label(window,text='Year')
# l3.grid(row=1,column=0)
#
# l4=Label(window,text='ISBN')
# l4.grid(row=1,column=2)
#
# title_text=StringVar()
# ent1=Entry(window,textvariable=title_text)
# ent1.grid(row=0,column=1)
#
#
# author_text=StringVar()
# ent2=Entry(window,textvariable=author_text)
# ent2.grid(row=0,column=3)
#
#
# year_text=StringVar()
# ent3=Entry(window,textvariable=year_text)
# ent3.grid(row=1,column=1)
#
# isbn_text=StringVar()
# ent4=Entry(window,textvariable=isbn_text)
# ent4.grid(row=1,column=3)
#
# listb=Listbox(window,height=6,width=35)
# listb.grid(row=2,column=0,rowspan=6,columnspan=2)
#
# sb=Scrollbar(window)
# sb.grid(row=2,column=2,rowspan=6)
#
# listb.configure(yscrollcommand=sb.set)
# sb.configure(command=listb.yview)
#
# listb.bind('<<ListboxSelect>>',get_selected_row)
#
#
# b1=Button(window,text="View All ",width=12,command=view_command)
# b1.grid(row=2,column=3)
#
# b2=Button(window,text="Search Entry",width=12,command=search_command)
# b2.grid(row=3,column=3)
#
#
# b3=Button(window,text="Add Entry",width=12,command=add_command)
# b3.grid(row=4,column=3)
#
#
# b4=Button(window,text="Update Selected ",width=12,command=update_command)
# b4.grid(row=5,column=3)
#
#
# b5=Button(window,text="Delete Selected ",width=12,command=delete_command)
# b5.grid(row=6,column=3)
#
# b6=Button(window,text="Close",width=12,command=window.destroy)
# b6.grid(row=7,column=3)

from tkinter import *
import backend

backend.connect()

def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()

def view_command():
    listb.delete(0, END)
    for row in backend.view():
        listb.insert(END, row)

def search_command():
    listb.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        listb.insert(END, row)

def get_selected_row(event):
    global selected_tuple
    index = listb.curselection()
    if index:
        selected_tuple = listb.get(index)
        ent1.delete(0, END)
        ent1.insert(END, selected_tuple[1])

        ent2.delete(0, END)
        ent2.insert(END, selected_tuple[2])

        ent3.delete(0, END)
        ent3.insert(END, selected_tuple[3])

        ent4.delete(0, END)
        ent4.insert(END, selected_tuple[4])

def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


def delete_command():
    backend.delete(selected_tuple[0])
    view_command()

window = Tk()
window.wm_title('Book Store')
window.configure(bg='lightgray')

custom_font = ('Helvetica', 12)

l1 = Label(window, text='Title', font=custom_font)
l1.grid(row=0, column=0, padx=10, pady=5)

l2 = Label(window, text='Author', font=custom_font)
l2.grid(row=0, column=2, padx=10, pady=5)

l3 = Label(window, text='Year', font=custom_font)
l3.grid(row=1, column=0, padx=10, pady=5)

l4 = Label(window, text='ISBN', font=custom_font)
l4.grid(row=1, column=2, padx=10, pady=5)

title_text = StringVar()
ent1 = Entry(window, textvariable=title_text, font=custom_font)
ent1.grid(row=0, column=1, padx=10, pady=5)

author_text = StringVar()
ent2 = Entry(window, textvariable=author_text, font=custom_font)
ent2.grid(row=0, column=3, padx=10, pady=5)

year_text = StringVar()
ent3 = Entry(window, textvariable=year_text, font=custom_font)
ent3.grid(row=1, column=1, padx=10, pady=5)

isbn_text = StringVar()
ent4 = Entry(window, textvariable=isbn_text, font=custom_font)
ent4.grid(row=1, column=3, padx=10, pady=5)

listb = Listbox(window, height=6, width=35, font=custom_font)
listb.grid(row=2, column=0, rowspan=6, columnspan=2, padx=10, pady=5)

sb = Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6, pady=5, sticky=N+S)

listb.configure(yscrollcommand=sb.set)
sb.configure(command=listb.yview)

listb.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View All", width=12, command=view_command, bg='lightblue', font=custom_font, fg='white')
b1.grid(row=2, column=3, padx=10, pady=5)

b2 = Button(window, text="Search Entry", width=12, command=search_command, bg='lightblue', font=custom_font, fg='white')
b2.grid(row=3, column=3, padx=10, pady=5)

b3 = Button(window, text="Add Entry", width=12, command=add_command, bg='lightblue', font=custom_font, fg='white')
b3.grid(row=4, column=3, padx=10, pady=5)

b4 = Button(window, text="Update Selected", width=12, command=update_command, bg='lightblue', font=custom_font, fg='white')
b4.grid(row=5, column=3, padx=10, pady=5)

b5 = Button(window, text="Delete Selected", width=12, command=delete_command, bg='lightblue', font=custom_font, fg='white')
b5.grid(row=6, column=3, padx=10, pady=5)

b6 = Button(window, text="Close", width=12, command=window.destroy, bg='red', font=custom_font, fg='white')
b6.grid(row=7, column=3, padx=10, pady=5)

window.mainloop()













