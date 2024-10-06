import statistics
import random
from random import shuffle
from model.player import player,warrior
from model.weapon import weapon
from tkinter import *
import os
import webbrowser
import shutil
import json
import time
import re

def main():
    fichier = open('tuto/data.json','r+')
    obj = json.load(fichier)
    print(obj)
    print(obj['message'])    


##### regex ######################################

def regex():
    text = "contact@raven.com" 
    pattern = r'^[a-zA-Z0-9_.-]+@[a-z]{2,}.(fr|us|com)$'
    
    if re.match(pattern, text):
        print("email valide")
    else:
        print("email invalide")

##### decorateur ######################################

def add_time(delay=1):
    def decorator(func):
        def wrapper():
            time.spleep(delay)  
            func()
        return wrapper
    return decorator

@add_time(delay=1)
def a_command():
    print("bonjour")

def is_admin(func):
    def wrapper(role):
        if role == "admin":
            func()
        else:
            print("pas la perm")
    return wrapper

@is_admin
def creer_fichier():
    print("creer fichier")
    
@is_admin
def suppr_fichier():
    print("suppr fichier")        

@is_admin
def modif_fichier():
    print("modif fichier")

def test_fichiers():
    creer_fichier("user")
    suppr_fichier("admin")
    modif_fichier("admin")

def decorator(func):
    def wrapper():
        print("avant")
        func()
        print("après")
    return wrapper

@decorator
def say_hello():
    print("bonjour ")

##### exceptions ######################################

def tryexceptions():
    exception('tuto/data.json')
    
def exception(filename):
    try:
        if not filename.endswith('.json'):
            raise Exception("que fichiers .json")
        fichier = open(filename)
        print(json.load(fichier)['message'])
        # print(fichier.readlines()[9])
        fichier.close()
    except Exception as e:
        print("Attention au format fichier : ",e)
    except FileNotFoundError:
        print("fichier {} inconnu".format(filename))
    except IndexError:
        print("ligne {} du fichier {} n'existe pas".format('9',filename))
               
    while True:
        try:
            prixht = int(input("Entrer le prix HT : "))
            prixttc = prixht * 1.20
            print(prixttc)
            break
        except ValueError:
            print("numerique requis")

##### dictionnary ######################################

def dict():
    a = {}
    a["nom"] = "Wayne"
    a["prenom"] = "Bruce"
    print(a)
    print(a.get("nom"))
    print(a.get("weapon","pas de weapon"))
    if "nom" in a:
        print("got nom")
    del a["nom"]
    print(a)
    
 ##### fichiers ######################################
    
def fichiers():
    students_list  = ["Michel", "Pauline", "Samantha"]
    #file = open("tuto\students.txt", "a+")
    
    with open("tuto/students.txt", "w+") as file:
        for student in students_list:
            file.write(student+"\n")
        file.close()
        
    if os.path.exists("tuto/meals.txt"):
        with open("tuto/meals.txt", "r+") as file:
            meals = file.readlines()
            meal_random = random.choice(meals)
            file.close()
            print(meal_random)
    else:
        print("doc n'exite pas")
        
    source = "tuto/logo.png"
    target = "tuto/loga.png"
    
    shutil.copy(source, target)
    os.remove(source)
    
##### interface graphique ######################################

def open_web_ytube_channel():
    webbrowser.open_new("http://www.youtube.fr")

def interfaceGRaphique():
    print(os.getcwd())
    window = Tk()
    window.title("My application")
    window.geometry("720x480")
    window.minsize(480,360)
    window.iconbitmap("tuto/foto1.ico")
    window.config(background='#41B77F')
    
    frame = Frame(window,bg='#41B77F')
    # bd=1,relief=SUNKEN 
    label_title = Label(frame,text="Bienvenu sur l'app", font=("Arial",40),bg='#41B77F',fg='white')
    label_title.pack()
    label_subtitle = Label(frame,text="sous titre", font=("Courrier",25),bg='#41B77F',fg='white')
    label_subtitle.pack()
    button = Button(frame, text="Ouvrir Youtube",font=("Courrier",25),bg='white', fg='#41B77F',command=open_web_ytube_channel)
    button.pack(pady=25, fill=X)
    frame.pack(expand=YES)

    window.mainloop()

##### heritage #################################################

def heritage():
    player1 = player("toto",20,2)
    player1.damage(3)
    print("info : joueur {} ayant {} vie et {} attack".format(player1.pseudo, player1.health, player1.attack))
    warrior1 = warrior("DarkWarrior",30,4)
    for i in range(1,5): 
        warrior1.damage(4)
        print("update au guerrier {} ayant {} vie {} armure et {} attack".format(warrior1.pseudo, warrior1.health, warrior1.armor,warrior1.attack))
    if issubclass(warrior,player):
        print("heritage ok")

##### objets #################################################

def objets():
    knife = weapon("couteau", 3)
    player1 = player("toto",20,0)
    player2 = player("tata",20,0)
    player1.equip_weapon(knife)
    print("round 1 : pseudos ",player1.get_pseudo()," ",player1.health," ",player2.get_pseudo()," ",player2.health)
    player1.attack_player(player2)
    print("round 2 : pseudos ",player1.get_pseudo()," ",player1.health," ",player2.get_pseudo()," ",player2.health)

##### functions #################################################

def welcome():
    print("hello bienvenu!")
    result = 5 + 6
    print ("resultat : ",result)

def next_year(year):
    # global year
    print("fin de l'année ",year)
    year +=1
    print("debut de l'année ",year)
    
def addition(val1 = 0,val2 = 0):
    total = val1 + val2
    return total

def max(val1,val2):
    return val1 if (val1 > val2) else val2

def add(a):
    a+=1
    print(a)
    if a < 10:
        add(a)

def functions():
    next_year(2024)
    print("addition de {} + {} = {}".format(5,6,addition(5,6)))
    print("addition de {} + {} = {}".format(0,0,addition()))
    print("max de {} et {} est {}".format(10,50,max(10,50)))
    add(2)

##### loops #################################################

def boucles():
    for num_client in range(1,6): 
        print("vous etes le client ", num_client)
        
    blacklist = ['client2@gmail.com']
    emails = ['client@gmail.com', 'client2@gmail.com', 'client3@gmail.com']    
    for email in emails:
        if email in blacklist:
            print("black list for ", email)
            continue
           # break
        print("email envoyé à ", email)
    
    salaire = 1500
    
    while salaire < 2000:
        salaire += 200
        print("salaire est ",salaire)
        
##### lists #################################################

def listes():
    online_players = ["Graven", "Bob","john"]
    notes = [105,10,77]
    print(online_players[len(online_players) - 1])
    online_players[0] = "new one"
    online_players.insert(2, "toto")
    online_players[2:4] = ["a", "b"]
    online_players.append("00")
    online_players.extend(["aa","bb"])
    del online_players[5]
    online_players.remove("00")
    print(online_players)
    online_players.clear()
    result = statistics.mean(notes)
    print(result)
    print(notes)
    shuffle(notes)
    print(notes)

##### conditions #################################################

def conditions():
    wallet = 5000
    computer_price = 1500
    if wallet >= computer_price and computer_price > 1000:
        print("tu peux acheter, il te restera {}€".format(wallet - computer_price))
    #elif 8 < value < 15:
        #print("e")
    else:
        print("Tu ne peux pas")
    
    
    text = ("achat possible","achat impossible")[computer_price >= wallet]
    print(text," ",len(text))

##### variables #################################################

def variables():
    note1 = 12
    note2 = 13
    note3 = 15
    avg = (note1 + note2 + note3) / 3
    message = "la moyenne est {} ".format(avg)
    
    print(message)

##### first #################################################

def first():
    username = "Graven"
    age = 19
    wallet = 125.7
    print(username, age, wallet)
    age = age + 1 
    print("salut " + username, "tu as : " + str(age), "argent : " + str(wallet))
    #print("Hello world!")
    #print("Welcome")
    #note1 = int(input('Note 1'))
    
    
if __name__ == "__main__":
    main()
