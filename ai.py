import os
import sys
import wikipedia
import pyttsx3
import pprint
from googleapiclient.discovery import build
from colorama import Fore, Back, Style

def wiki():
   wikipedia.set_lang("id")
   engine = pyttsx3.init()
   engine.setProperty('rate', 110)
   voices = engine.getProperty('voices')
   engine.setProperty('voice', voices[0].id)
   engine.setProperty('volume', 1)
   engine.say('Masukkan kata kunci pencarian Anda.')
   engine.runAndWait()
   value=input(Fore.CYAN + "Masukkan Kata kunci pencarian nya : ")
   data=wikipedia.search(value,3)
   print()
   print(wikipedia.summary(data[0],sentences=2))
   engine.say(wikipedia.summary(data[0],sentences=2))
   engine.runAndWait()
def google():
   my_api_key = "AIzaSyBzrRAVaHxjENMFX48hsQfMzfE9b4yGzrM"
   my_cse_id = "84cd48900faca7110"
   value=input(Fore.CYAN + "Masukkan Kata kunci pencarian anda : ")
   def google_search(search_term, api_key, cse_id, **kwargs):
       service = build("customsearch", "v1", developerKey=api_key)
       res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
       return res['items']

   results = google_search(value, my_api_key, my_cse_id, num=2)

   for result in results:
       '''pprint.pprint(result)'''
       title = result['title']
       link = result['formattedUrl']
       dis = result['snippet']
       print (title)
       print (dis)
       print (Fore.RED + link)
       def web():
           web = input(Fore.CYAN + "buka link kah (y/t)?")
           if web == 'y':
              os.system('xdg-open' + ' '+ link + '')
       engine = pyttsx3.init()
       engine.setProperty('rate', 110)
       engine.setProperty('volume', 1)
       engine.say(dis)
       web()
       engine.runAndWait()
def wiki_ono():
   my_api_key = "AIzaSyBzrRAVaHxjENMFX48hsQfMzfE9b4yGzrM"
   my_cse_id = "e55bb4d3e100ee347"
   value=input(Fore.CYAN + "Masukkan Kata kunci pencarian anda : ")
   def wiki_ono_search(search_term, api_key, cse_id, **kwargs):
       service = build("customsearch", "v1", developerKey=api_key)
       res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
       return res['items']

   results = wiki_ono_search(value, my_api_key, my_cse_id, num=2)

   for result in results:
       '''pprint.pprint(result)'''
       title = result['title']
       link = result['formattedUrl']
       dis = result['snippet']
       print (title)
       print (dis)
       print (Fore.RED + link)
       def web():
           web = input(Fore.CYAN + "buka link kah (y/t)?")
           if web == 'y':
              os.system('xdg-open' + ' '+ link + '')
       engine = pyttsx3.init()
       engine.setProperty('rate', 110)
       engine.setProperty('volume', 1)
       engine.say(dis)
       web()
       engine.runAndWait()
def brainly():
   my_api_key = "AIzaSyBzrRAVaHxjENMFX48hsQfMzfE9b4yGzrM"
   my_cse_id = "fe2f6d6d7ec5b0dbd"
   value=input(Fore.CYAN + "Masukkan Kata kunci pencarian anda : ")
   def brainly_search(search_term, api_key, cse_id, **kwargs):
       service = build("customsearch", "v1", developerKey=api_key)
       res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
       return res['items']

   results = brainly_search(value, my_api_key, my_cse_id, num=4)

   for result in results:
       '''pprint.pprint(result)'''
       title = result['title']
       link = result['formattedUrl']
       dis = result['snippet']
       print (title)
       print (dis)
       print (Fore.RED + link)
       def web():
           web = input(Fore.CYAN + "buka link kah (y/t)?")
           if web == 'y':
              os.system('xdg-open' + ' '+ link + '')
       engine = pyttsx3.init()
       engine.setProperty('rate', 110)
       engine.setProperty('volume', 1)
       engine.say(dis)
       web()
       engine.runAndWait()
def error():
   menu()
def menu():
    os.system('clear')
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('volume', 1)
    print ("")
    print ("")
    print (Fore.RED + " / \ / \ / \ / \ / \ / \ " +Fore.WHITE + "  / \ / \ / \ / \ / \ / \ ")
    print (Fore.RED + "( S | E | A | R | C | H )" +Fore.WHITE + " ( E | N | G | I | N | E )")
    print (Fore.RED + " \_/ \_/ \_/ \_/ \_/ \_/  " +Fore.WHITE + " \_/ \_/ \_/ \_/ \_/ \_/ ")
    print (Fore.BLUE + "				by mr_dilz v1")
    print ("")
    engine.say('Tools ini Di Tulis Oleh Fadol, Berikut menu menu Yang Tersedia')
    engine.runAndWait()
    print (Fore.YELLOW + "1 search pengetahuan wiki.")
    engine.say('Cari pengetahuan wiki.')
    engine.runAndWait()
    print (Fore.GREEN + "2 search pengetahuan google.")
    engine.say('Cari pengetahuan google.')
    engine.runAndWait()
    print (Fore.MAGENTA + "3 search pertanyaan apa aja.")
    engine.say('Cari pertanyaan apa aja.')
    engine.runAndWait()
    print (Fore.CYAN + "4 search pengetahuan pak onno center.")
    engine.say('Cari pengetahuan pak onno center.')
    engine.runAndWait()
    print ("")
    engine.say('Masukkan pilihan Anda.')
    engine.runAndWait()
    menu = input(Fore.RESET + "hayu mau pilih yang mana? : ")
    
    if menu == '1':
       wiki()
       tanya()
    elif menu == '2':
       google()
    elif menu == '3':
       brainly()
    elif menu == '4':
       wiki_ono()
    else:
       error()
def tanya():
    tanya = input(Fore.CYAN + "Kembali ke menu (y/t)?")
    if tanya == 'y':
        os.system('clear')
        menu()
    elif tanya == 't':
        os.system('clear')
        exit
    elif tanya == '':
        os.system('clear')
        error()
menu()
tanya()
