#!/usr/bin/python3

"""
A Tkinter GUI tool to search Reddit subs. 

Created by: Daniel Berrones 
Email: daniel.a.berrones@gmail.com
Website: http://www.danielberrones.com
"""

import tkinter as tk
from tkinter import ttk
import praw


class myApp:
    def __init__(self, master):
        self.master = master
        master.title("Sub Explorer")
        master.geometry("900x650")
        self.create_widgets()

    def create_widgets(self):
        # MAIN REDDIT IMAGE
        self.im = tk.PhotoImage(file='/Users/danielberrones/Desktop/todo/pics/reddit.png')
        self.imgLabel = tk.Label(image=self.im)
        self.imgLabel.grid(row=0, column=0, columnspan=4,padx=5,pady=5,sticky=tk.NSEW)

        # LABEL - "TYPE A SUBREDDIT"
        l1 = tk.Label(root,text="Type a Sub: ",bg="khaki1", fg="tomato2",font='Arial 25 bold',borderwidth=3,relief='groove')
        l1.grid(row=1,column=0,padx=50,pady=25,sticky=tk.W+tk.E)

        # ENTRY WIDGETS (GET DATA FROM THESE) ---  "TYPE A SUBREDDIT"
        self.str_variable = tk.StringVar()
        self.query = tk.Entry(root, textvariable=self.str_variable,font=('Courier 25'))
        self.query.grid(row=1,column=1,padx=50,sticky=tk.W)

        # LABEL - Hot, New, Rising?
        l1 = tk.Label(root,text="Hot, New, Rising?",bg="khaki1", fg="tomato2",font='Arial 25 bold',borderwidth=3,relief='groove')
        l1.grid(row=2,column=0,padx=50,pady=25,sticky=tk.W+tk.E)


        # ENTRY WIDGETS (GET DATA FROM THESE)---    Hot, New, Rising?
        self.str_variable1 = tk.StringVar()
        self.query1 = tk.Entry(root, textvariable=self.str_variable1,font=('Courier 25'))
        self.query1.grid(row=2,column=1,padx=50,sticky=tk.W)

    
        # LABEL - "# YOUR SEARCH"
        l1 = tk.Label(root,text="Enter # to search: ",bg="khaki1", fg="tomato2",font='Arial 25 bold',borderwidth=3,relief='groove')
        l1.grid(row=3,column=0,padx=50,pady=25,sticky=tk.W+tk.E)


        # ENTRY WIDGETS (GET DATA FROM THESE) ----"# YOUR SEARCH"
        self.str_variable2 = tk.StringVar()
        self.query2 = tk.Entry(root, textvariable=self.str_variable2,font=('Courier 25'))
        self.query2.grid(row=3,column=1,padx=50,sticky=tk.W)



        #RADIOBUTTON HOT/NEW/RISING/CONTROVERSIAL
        ### TO DO: ADD RADIO BUTTON AND VALUES####



        # SUBMIT BUTTON
        button1 = tk.Button(root, text='Submit', command=self.prawReddit, font=('Courier 20'),height=2,width=12)
        button1.grid(row=4, column=1,ipadx=10,padx=50,pady=10, sticky=tk.W)

        # CLEAR BUTTON
        clear = tk.Button(root, command=self.clear_text,highlightbackground='wheat',text='Clear Screen',font=('Courier 20'),height=2,width=12)
        clear.grid(ipadx=10,padx=50,row=4,column=1,pady=10,sticky=tk.E)

        # QUIT BUTTON
        button = tk.Button(root, command=root.destroy,highlightbackground='indian red',text='QUIT',
                            font=('Arial 18'),height=2,width=8)
        button.grid(row=5,column=1,padx=100,sticky=tk.NSEW)



    def prawReddit(self):
        '''
        Searches for the user requested subreddit and returns titles
        '''

        # user's search query
        self.stripped = self.str_variable.get()
        stripped1 = self.str_variable1.get()
        self.stripped2 = int(self.str_variable2.get())


        # creates new window
        self.toplevel = tk.Toplevel(root)
        self.toplevel.grid()
        self.toplevel.title("Your results for: {}".format(self.stripped))
        self.toplevel.geometry('1250x750')


        # adds reddit image
        self.im1 = tk.PhotoImage(file='/Users/danielberrones/Desktop/todo/pics/subreddit1.png')
        self.imgLabel1 = tk.Label(self.toplevel, image=self.im1)
        self.imgLabel1.grid(row=0,column=0)


        #CUSTOMIZES LABEL WITH USERS SUBREDDIT
        self.customFrame = tk.Frame(self.toplevel,height=5,width=5,bg='khaki1').grid(row=0,column=1)
        self.userLabel = tk.Label(self.toplevel,text=f"results for: {self.stripped}", bg='tomato2',fg="khaki1",font='courier 30',borderwidth=3,relief='groove')
        self.userLabel.grid(row=0,column=1)

        # closes the window
        self.quitButton = tk.Button(self.toplevel, command=self.toplevel.destroy,highlightbackground='indian red',text='QUIT',font=                             ('Arial',20))
        self.quitButton.grid(row=0,column=2)

        # searches and saves results to listbox
        
        ########################################################################################
        #TITLE LABEL   
        self.labelContainer = tk.Label(self.toplevel,text="1.)Title",fg="tomato2",bg='khaki1',font='Arial 25 bold',borderwidth=3,relief='groove').grid(row=1,column=0,sticky=tk.W,padx=50,pady=50)
        #TITLE CONTAINER/OUTPUT
        self.container = tk.Listbox(self.toplevel,height=6, width=80,font="Courier 16")
        self.subTitleBox = [submission.title for submission in reddit.subreddit(self.stripped).new(limit=self.stripped2)]
        for i, j in enumerate(self.subTitleBox,start=1):
            self.container.insert(tk.END,str(i)+'.)'+str(j))
            self.container.grid(row=1,column=1,padx=3,pady=3,sticky=tk.W+tk.E)
        ########################################################################################


        #######################################################################################
        #URL LABEL
        self.labelContainer2 = tk.Label(self.toplevel,text="2.)URL",fg="tomato2",bg='khaki1',font='Arial 25 bold',borderwidth=3,relief='groove').grid(row=2,column=0,sticky=tk.W,padx=50,pady=50)
        #URL CONTAINER/OUTPUT
        self.subURLBox = [submission.url for submission in reddit.subreddit(self.stripped).new(limit=self.stripped2)]
        self.container2 = tk.Listbox(self.toplevel,height=6, width=80,font="Courier 16")
        for i, j in enumerate(self.subURLBox,start=1):
            self.container2.insert(tk.END,str(i)+'.)'+str(j))
            self.container2.grid(row=2,column=1,padx=3,pady=3,sticky=tk.W+tk.E)
        #######################################################################################


        ########################################################################################
        #SCORE LABEL
        self.labelContainer3 = tk.Label(self.toplevel,text="3.)Score",fg="tomato2",bg='khaki1',font='Arial 25 bold',borderwidth=3,relief='groove').grid(row=3,column=0,sticky=tk.W,padx=50,pady=50)
        #SCORE CONTAINER/OUTPUT
        self.subScoreBox = [submission.score for submission in reddit.subreddit(self.stripped).new(limit=self.stripped2)]
        self.container3 = tk.Listbox(self.toplevel,height=6, width=20,font="Courier 16")

        for i, j in enumerate(self.subScoreBox,start=1):
            self.container3.insert(tk.END,str(i)+'.)'+str(j))
            self.container3.grid(row=3,column=1,padx=3,pady=3,sticky=tk.W)
        ########################################################################################


        ########################################################################################
        #ID LABEL
        self.labelContainer4 = tk.Label(self.toplevel,text="4.)ID",fg="tomato2",bg='khaki1',font='Arial 25 bold',borderwidth=3,relief='groove').grid(row=4,column=0,sticky=tk.W,padx=50,pady=50)
        #ID CONTAINER/OUTPUT
        self.subIDBox = [submission.id for submission in reddit.subreddit(self.stripped).new(limit=self.stripped2)]
        self.container4 = tk.Listbox(self.toplevel,height=6, width=20,font="Courier 16")

        for i, j in enumerate(self.subIDBox,start=1):
            self.container4.insert(tk.END,str(i)+'.)'+str(j))
            self.container4.grid(row=4,column=1,padx=3,pady=3,sticky=tk.W)
        ########################################################################################


        ########################################################################################
        #AUTHOR LABEL
        self.labelContainer5 = tk.Label(self.toplevel,text="5.)Author",fg="tomato2",bg='khaki1',font='Arial 25 bold',borderwidth=3,relief='groove').grid(row=3,column=1,sticky=tk.N+tk.S,padx=50,pady=50)

        # AUTHOR CONTAINER/OUTPUT
        self.subAuthorBox = [submission.author for submission in reddit.subreddit(self.stripped).new(limit=self.stripped2)]

        self.container5 = tk.Listbox(self.toplevel,height=6, width=20,font="Courier 16")

        for i, j in enumerate(self.subAuthorBox,start=1):
            self.container5.insert(tk.END,str(i)+'.)'+str(j))
            self.container5.grid(row=3,column=1,padx=3,pady=3,sticky=tk.E)
        ########################################################################################

        ########################################################################################
        #KARMA LABEL
        self.labelContainer6 = tk.Label(self.toplevel,text="6.)Karma",fg="tomato2",bg='khaki1',font='Arial 25 bold',borderwidth=3,relief='groove').grid(row=4,column=1,sticky=tk.N+tk.S,padx=50,pady=50)

        # KARMA CONTAINER/OUTPUT
        self.subKarmaBox=[]
        for x in range(len(self.subAuthorBox)):
            self.subKarmaBox.append(self.subAuthorBox[x].link_karma)
        self.container6 = tk.Listbox(self.toplevel,height=6, width=20,font="Courier 16")

        for i, j in enumerate(self.subKarmaBox,start=1):
            self.container6.insert(tk.END,str(i)+'.)'+str(j))
            self.container6.grid(row=4,column=1,padx=3,pady=3,sticky=tk.E)
        ########################################################################################

        with open('/Users/danielberrones/testDIR/test1/test.txt','w') as f:
            for i in range(len(self.subAuthorBox)):
                f.write(str(self.subAuthorBox))

        
        #COMMENT CONTAINER/OUTPUT
        # self.commentBox = []
        # print(self.subIDBox)


    def clear_text(self):
        '''
        Clears text in entry box where user types a subreddit
        '''

        try:
            self.query.delete(0,tk.END)
            self.query1.delete(0,tk.END)
            self.query2.delete(0,tk.END)
        except AttributeError:
            pass



root = tk.Tk()
app = myApp(root)
root.mainloop()
