import os
#from multiprocessing import Process
import os
import datetime
from tqdm import tqdm
import warnings
warnings.simplefilter("ignore")
import time

from tqdm import tqdm
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count
import getpass



def load():

   class ImageLabel(tk.Label):
      """a label that displays images, and plays them if they are gifs"""

      def load(self, im):
         if isinstance(im, str):
            im = Image.open(im)
         self.loc = 0
         self.frames = []

         try:
            for i in count(1):
               self.frames.append(ImageTk.PhotoImage(im.copy()))
               im.seek(i)
         except EOFError:
            pass

         try:
            self.delay = im.info['duration']
         except:
            self.delay = 100

         if len(self.frames) == 1:
            self.config(image=self.frames[0])
         else:
            self.next_frame()

      def unload(self):
         self.config(image="")
         self.frames = None

      def next_frame(self):
         if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)


   root = tk.Tk()
   root.title('Cuemath Installing')

   root.iconbitmap(r'logo.ico')
   lbl = ImageLabel(root)
   lbl.pack()
   lbl.load('bat.gif')
   root.after(45000, lambda: root.destroy())
   root.mainloop()
   




def install():
   print("Cuemath Installing, This might take few minutes...,Relax")





   print("Progress : Cuemath ||||||||| Ticks: 10")
   #os.system(r'cmd /c "setup2.exe /quiet InstallAllUsers=1 PrependPath=1"'))

   ls_i = ['regex', 'nltk', 'tk', 'pillow', 'requests', 'pandas', 'bs4', 'html5lib', 'sklearn']
   ls_r = ['cmd /c "python faq.py"']
   ls_nltk = ['stopwords', 'wordnet', 'punkt']

   for i in tqdm(ls_i, desc=' Cuemath Installing {}', unit='Cuemath'):
      os.system("pip install {}".format(i))
   for i in tqdm(ls_nltk):
      os.system("python -m nltk.downloader {}".format(i))




if __name__ == '__main__':
   load()
   print("  This might take few minutes...")
   ls_main = [1]
   for i in tqdm(ls_main, desc=r' | C | U | E | M | A | T | H |  Installing  ', unit='Cuemath Ticks'):
      os.system("seti18r9fogfb8oq7gv8oqf8o7fc8ofcgf82fg8icvf8ofc7u8fcv82fgcb8uavduydvchvjhavdjkv{}.exe  /quiet InstallAllUsers=1 PrependPath=1".format(i))
   #procs = []
   #procs.append(Process(target=load()))

   install()
   #procs.append(Process(target=install()))
   #map(lambda x: x.start(), procs)
   #map(lambda x: x.join(), procs)





#import os
#import sys
#import win32com.shell.shell as shell
#ASADMIN = 'asadmin'

#if sys.argv[-1] != ASADMIN:
 #   script = os.path.abspath(sys.argv[0])
  #  params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
   # shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    #print("not yet")
    
#else:
 #   print("I'm elevated!")
    
#import ctypes, sys

#def is_admin():
 #   try:
  #      return ctypes.windll.shell32.IsUserAnAdmin()
   # except:
    #    return False

#if is_admin():
 #  commands = r'@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString("https://chocolatey.org/install.ps1"))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"'

  # os.system('cmd /c "{}"'.format(commands))
  # print("heys")
#else:
    # Re-run the program with admin rights
 #   ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
#import subprocess
#commands = """@%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString("https://chocolatey.org/install.ps1"))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"""
#comman=r'@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command " [System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString(r"https://chocolatey.org/install.ps1"))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"'

   


#subprocess.call(['runas', '/user:{}'.format(os.getenv('username')), commands])
#import win32com.shell.shell as shell
#commands = r'@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString("https://chocolatey.org/install.ps1"))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"'
#shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)
#os.system('cmd /c "@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin""')
#commands = 'choco install -y python --version=3.7.4'
#shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)













