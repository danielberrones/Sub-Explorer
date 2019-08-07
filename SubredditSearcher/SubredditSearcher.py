import tkinter as tk
import praw


reddit = praw.Reddit(client_id='xZHnziUldeZEbg', client_secret="P52m77JjNefq4-XVyLEsrkaPGS8",user_agent='carldangerAPI33')


class myApp(tk.Frame):
    '''
    A tool to search Reddit.  The user enters a subreddit and the results open in new window.
    '''
    def __init__(self, master=None):
        super().__init__(root)
        self.grid()

        root.title("Subreddit Search Tool")
        root.geometry('400x400')
        self.create_widgets()

    def clear_text(self):
        '''
        Clears text in entry box where user types a subreddit
        '''

        try:
            self.query.delete(0,tk.END)
        except AttributeError:
            pass

    def prawReddit(self):
        '''
        Searches for the user requested subreddit and returns titles
        '''

        # user's search query
        self.stripped = self.str_variable.get()

        # creates new window
        self.toplevel = tk.Toplevel(root)
        self.toplevel.grid()
        self.toplevel.title("Your results for: {}".format(self.stripped))
        self.toplevel.geometry('1000x800')

        # closes the window
        self.quitButton = tk.Button(self.toplevel, command=self.toplevel.destroy,
                           highlightbackground='indian red',
                           text='QUIT',font=('Arial',20))
        self.quitButton.grid()


        # adds reddit image
        self.im1 = tk.PhotoImage(file='/Users/danielberrones/Desktop/red.png')
        self.imgLabel1 = tk.Label(self.toplevel, image=self.im1)
        self.imgLabel1.grid()

        # creates scrollbar
        self.scrollbar = tk.Scrollbar(self.toplevel)
        self.scrollbar.grid()

        # container for search results
        self.container = tk.Listbox(self.toplevel, height=75, width=100,
                                  yscrollcommand=self.scrollbar.set,
                                  font="verdana 14")

        # searches and saves results to listbox
        for submission in reddit.subreddit(self.stripped).new(limit=50):
            self.container.insert(tk.END, str(submission.title))
            self.container.grid()
            self.scrollbar.config(command=self.container.yview)

    def create_widgets(self):

        # NAME QUESTION
        l1 = tk.Label(root,
                      text="Type a Subreddit: ",
                      bg="khaki1", fg="tomato2",
                      font='Arial 25 bold',
                      borderwidth=3,
                      relief='groove')
        l1.grid(row=3,column=1)

        # ENTRY WIDGETS (GET DATA FROM THESE)
        self.str_variable = tk.StringVar()

        self.query = tk.Entry(root, textvariable=self.str_variable,font=('Sans serif',25))
        self.query.grid(row=4, column=1)


        # ENTER BUTTON
        button1 = tk.Button(root, text='ENTER', command=self.prawReddit, font=('Arial',18))
        button1.grid(row=5, column=1)

        # CLEAR BUTTON
        clear = tk.Button(root, command=self.clear_text, text='CLEAR',font=('Arial',18))
        clear.grid(row=6,column=1)

        # QUIT BUTTON
        button = tk.Button(root, command=root.destroy,
                           highlightbackground='indian red',
                           text='QUIT',font=('Arial',20),
                           height="5", width="10")
        button.grid(row=7,column=1)

        self.im = tk.PhotoImage(file='/Users/danielberrones/Desktop/red.png')
        self.imgLabel = tk.Label(image=self.im)
        self.imgLabel.grid(row=0,column=1)


if __name__ == '__main__':
    root = tk.Tk()
    app = myApp(root)
    app.mainloop()

