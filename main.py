import os,sys,time
import colorama
from colorama import Fore
from pytube import YouTube
from colorama import init as colorama_init
from tkinter import Tk, filedialog

colorama_init(autoreset=True)

print(Fore.MAGENTA + """ 
 __     __  _______   _____  
 \ \   / / |__   __| |  __ \ 
  \ \_/ /     | |    | |  | |
   \   /      | |    | |  | |
    | |       | |    | |__| |
    |_|       |_|    |_____/ 
                             
                             
""")

root = Tk()
root.withdraw()
root.attributes('-topmost', True)
link = ""
yt = ""
choice = ""
choice2 = ""
clear = lambda: os.system('cls')

def select_video():
 print(Fore.CYAN + "Insert video link : ")
 link = input()
 try:
  yt = YouTube(link)
 except:
  print(Fore.RED + "Insert a valid link!")
  select_video()
 print(Fore.CYAN + "-----------------------------------------------------------")
 print(Fore.CYAN + "Information : ")
 print(Fore.RED + "Title : ", Fore.WHITE + yt.title)

 print(Fore.RED + "Views : ", Fore.WHITE + str(yt.views))

 print(Fore.RED + "Lenght : ", Fore.WHITE + str(yt.length / 60), Fore.WHITE + "minutes")
 print(Fore.CYAN + "-----------------------------------------------------------")
 choice_1(yt)

def process_video(yt):
 print(Fore.CYAN + "Possible streams options : ")
 print(Fore.GREEN + "Audio only" + Fore.CYAN + str(": A"))
 print(Fore.GREEN + "Video" +  Fore.CYAN + str(": B"))

 choice = input()

 if(choice == "a" or choice == "A"):
  try:
   a = yt.streams.filter(only_audio=True).first()
  except:
   clear()
   print(Fore.RED + "There was an error while converting your video")
   time.sleep(3)
   clear()
   print(Fore.CYAN + "Please try again :")
   select_video()
  clear()
  path = filedialog.askdirectory()
  print("Downloading...")
  a.download(path)
  sys.exit(0)
 elif(choice == "b" or choice == "B"):
  b = yt.streams.get_highest_resolution()
  clear()
  print(Fore.CYAN + "!If no path given it will download in the folder of the .exe file!")
  path = filedialog.askdirectory()
  print(Fore.CYAN + "Downloading...")
  b.download(path)
  sys.exit(0)
  
def choice_1(yt):
 print(Fore.CYAN + "Insert C to confirm or B to go back")
 choice2 = input()
 if(choice2 == "C" or choice2 == "c"):
  time.sleep(1)
  clear()
  process_video(yt)
 
 elif(choice2 == "B" or choice2 == "b"):
  clear()
  select_video() 

 
select_video()
