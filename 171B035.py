from Tkinter import *
root1=Tk()
root1.geometry('1080x640')
root1.configure(background='black')
root1.title('Splash Screen')
img=PhotoImage(file='my.gif')
l=Label(root1,text='Name - Anshraj Shrivastava\nEnrollment Number - 171B035\nBatch - B1\nPhone Number - 7000540479\nEmail - rajansh87@gmail.com\nTopic-School Management System',font=("Bradley Hand ITC",20,"bold"),bg='black',fg='white')
l.place(x=350,y=350)
def fun(e):
    root1.destroy()
    import newproject_2
    root1.mainloop()
l=Label(root1,image=img)
l.bind('<Motion>',fun)
l.place(x=400,y=5)
root1.mainloop()
