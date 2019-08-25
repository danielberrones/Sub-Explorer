#!/usr/bin/env python3

"""
A Tkinter GUI tool to search Reddit subs.  The user enters a subreddit and results open in new window.

Created by: Daniel Berrones
Email: daniel.a.berrones@gmail.com
"""

import tkinter as tk
import praw

reddit = praw.Reddit(client_id="########", client_secret="########",user_agent="########")

class myApp(tk.Frame):
    """ Tkinter tool to search Reddit """

    def __init__(self, master=None):
        """ Inititalizer """
       super().__init__(root)
        self.grid()

        # sets title & root size
        root.title("Subreddit Searcher")
        root.geometry("400x400")

        # places main widgets on root
        self.main_widgets()

    def main_widgets(self):
        """ Adds main widgets to root. """

        # places Reddit image
        self.img = tk.PhotoImage(file="reddit.png")
        self.imgLabel = tk.Label(image=self.img)
        self.imgLabel.grid(row=0,column=1)

        # creates Subreddit label
        self.label1 = tk.Label(root,
                      text="Type a Subreddit: ",
                      bg="khaki1", fg="tomato2",
                      font="Arial 25 bold",
                      borderwidth=3,
                      relief="groove")
        self.label1.grid(row=3,column=1)

        # stores Subreddit search as string variable
        self.searchSub = tk.StringVar()

        # entry box -- user types the Subreddit
        self.query = tk.Entry(root, text="", textvariable=self.searchSub,font="Serif 25")
        self.query.grid(row=4, column=1)

        # enter button -- searches for Subreddit
        self.button1 = tk.Button(root, text="ENTER", command=self.prawReddit, font="Arial 18")
        self.button1.grid(row=5, column=1)

        # clear button -- removes text in entry box
        self.clear = tk.Button(root, command=self.clear_text, text="CLEAR",font="Arial 18")
        self.clear.grid(row=6,column=1)

        # quit button -- destroys window
        self.button = tk.Button(root, command=root.destroy,
                           highlightbackground="indian red",
                           text="QUIT",font="Arial 20",
                           height="5", width="10")
        self.button.grid(row=7,column=1)


    def clear_text(self):
        """ Clears text in entry box where user types a Subreddit. """

        # removes text
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
        self.im1 = tk.PhotoImage(file="subreddit1.png")
        self.imgLabel1 = tk.Label(self.topFrame, image=self.im1)
        self.imgLabel1.grid(row=0,column=0)

        # quit button -- destroys top level window
        self.quitButton = tk.Button(self.topFrame, command=self.toplevel.destroy,
                                    highlightbackground="indian red",
                                    text="QUIT",font="Arial 20",
                                    padx=5, pady=5)
        self.quitButton.grid(row=1,column=0)

        # contains search results
        self.container = tk.Listbox(self.topFrame, height=20, width=80, font="Verdana 14")
        self.container.grid(row=2)

        # creates scrollbar
        self.scroll = tk.Scrollbar(self.topFrame, orient="vertical")

        self.scroll.configure(command=self.container.yview)

        # stores 75 newest Subreddit titles in listbox
        for submission in reddit.subreddit(self.results).new(limit=75):
            self.container.insert(tk.END, str(submission.title))
            self.container.grid()
        self.scroll.grid()



if __name__ == "__main__":
    root = tk.Tk()
    app = myApp(root)
    app.mainloop()

