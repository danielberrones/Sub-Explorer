#!/usr/bin/python3

"""
A Tkinter GUI tool to search Reddit subs.  The user enters a subreddit and results open in new window.

Created by: Daniel Berrones 
Email: daniel.a.berrones@gmail.com
Website: http://www.danielberrones.com
"""

import tkinter as tk
import praw


# reddit = praw.Reddit(client_id="##YOUR_CLIENT_ID_HERE##", client_secret="##YOUR_CLIENT_SECRET_HERE##",user_agent="YOUR_USER_AGENT_HERE")
reddit = praw.Reddit(client_id="xZHnziUldeZEbg", client_secret="P52m77JjNefq4-XVyLEsrkaPGS8",user_agent="cdanger")

# please dont putt your password here


class myApp(tk.Frame):
    """ Tkinter tool to search Reddit """

    def __init__(self,master=None):
        super().__init__(root)
        self.grid()

        # sets title & root size
        root.title("The Mini Reddit Rocket!!")
        root.geometry("500x620")

        # places main widgets on root
        self.main_widgets()

    def main_widgets(self):
        """ Adds main widgets to root. """

        # places Reddit image
        self.img = tk.PhotoImage(file="img/Reddit.png")
        self.imgLabel = tk.Label(image=self.img)
        self.imgLabel.grid(row=0,column=1,padx=50,pady=40)

        # creates Subreddit label
        self.label1 = tk.Label(root, text="Type a Subreddit: ", bg="khaki1", fg="tomato2",font="Monospace 22 bold",                        borderwidth=1,relief="solid")
        self.label1.grid(row=3,column=1)

        # stores Subreddit search as string variable
        self.searchSub = tk.StringVar()

        # entry box -- user types the Subreddit
        self.query = tk.Entry(root, text="", textvariable=self.searchSub,font="Serif 25")
        self.query.grid(row=4, column=1, pady=20)

        # enter button -- searches for Subreddit
        self.button1 = tk.Button(root, text="ENTER", command=self.prawReddit, font="Monospace 18")
        self.button1.grid(row=5, column=1)

        # clear button -- removes text in entry box
        self.clear = tk.Button(root, command=self.clear_text, text="CLEAR",font="Monospace 18")
        self.clear.grid(row=6,column=1)

        # quit button -- destroys window
        self.button = tk.Button(root, command=root.destroy, highlightbackground="indian red", text="QUIT",                                  font="Arial 20", height="5", width="10")
        self.button.grid(row=7,column=1, pady=20)


    def clear_text(self):
        """ Clears text in entry box where user types a Subreddit. """

        try:
            self.query.delete(0,tk.END)
        except AttributeError:
            pass

    def prawReddit(self):
        """ Searches for Subreddit and returns submission titles. """

        # user's search results
        self.results = self.searchSub.get()

        # creates new window
        self.toplevel = tk.Toplevel(root)
        self.toplevel.grid()
        self.toplevel.title("Your search results for: {}".format(self.results))

        # creates top frame
        self.topFrame = tk.Frame(self.toplevel, height=80, width=20, padx=10,pady=10)
        self.topFrame.grid()

        # adds reddit image
        self.im1 = tk.PhotoImage(file="img/YourReddit.png")
        self.imgLabel1 = tk.Label(self.toplevel, image=self.im1)
        self.imgLabel1.grid(row=0,column=0)

        # quit button -- destroys top level window
        self.quitButton = tk.Button(self.toplevel, command=self.toplevel.destroy,
                                    highlightbackground="indian red",
                                    text="QUIT",font="Arial 20",
                                    padx=5, pady=5)
        self.quitButton.grid(row=1,column=0)    

        # contains search results
        self.container = tk.Listbox(self.toplevel, height=20, width=80, font="Roboto 20")
        self.container.grid(row=2)

        # stores titles in listbox
        for submission in reddit.subreddit(self.results).new(limit=10):
            self.container.insert(tk.END, str(submission.title))
            self.container.grid()



if __name__ == "__main__":
    root = tk.Tk()
    app = myApp(root)
    app.mainloop()
