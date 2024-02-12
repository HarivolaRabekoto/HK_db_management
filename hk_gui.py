# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 17:52:35 2024

@author: Harivola RABEKOTO
"""

import tkinter as tk
from tkinter import ttk

class MyApp(tk.Frame):
    def __init__ (self, root):
        super().__init__(root)
        self.pack(fill=tk.BOTH, expand= True)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        self.main_page()
    
    def main_page(self):
        self.welcome = tk.Label(self, 
                        text='Bienvenue sur l\'application de gestion de Haikintana!',
                        anchor='center',
                        pady=10,
                        font=('Arial',20)
                        )
        self.welcome.pack(expand= True)
        
        self.membre = tk.Button(self,
                             text='Membres',
                             bg='green',
                             width=20,
                             height=3,
                             font=('Arial',15),
                             command= lambda: self.switch('membres')
                             )
        self.membre.pack(expand = True)
        
        self.activite = tk.Button(self,
                             text='Activités',
                             bg='blue',
                             width=20,
                             height=3,
                             font=('Arial',15))
        self.activite.pack(expand = True)
        
        self.pole = tk.Button(self,
                             text='Pôles',
                             bg='grey',
                             width=20,
                             height=3,
                             font=('Arial',15))
        self.pole.pack(expand = True)
        
    def switch(self,frame):
        for child in self.winfo_children():
            child.destroy()
        if frame=='membres':
            self.membres()
    
    def membres(self):
        search = tk.StringVar()
        self.barre= tk.Entry(self, 
                             textvariable = search, 
                             width = 40,)
        self.barre.grid(column=3,row=0, padx=10)
        self.barre.insert(0,'Entrez un identifiant')
        
        self.search_button = tk.Button(self,
                                       text='Rechercher',
                                       bg='grey',
                                       width=10)
        self.search_button.grid(column=4,row=0)
        
        
        
        
        
root = tk.Tk()
root.title('Haikintana')
root.geometry('700x400')
root.resizable(False,False) 

app = MyApp(root)

root.mainloop()
