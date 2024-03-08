import time
from datetime import datetime
import platform
import shutil
import speedtest
import kivy
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from kivymd.uix.textfield import MDTextField
from kivy.uix.checkbox import CheckBox
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.label import MDLabel
from kivy.uix.widget import Widget
from kivy.uix.switch import Switch
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager,Screen,SlideTransition
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
import psutil
from pywinauto import Desktop,application
from pywinauto.application import Application
import pywinauto
from kivy.clock import Clock
from AppOpener import open,close
import datetime
import os
from pathlib import Path
import matplotlib.pyplot as plt
from kivy.uix.progressbar import ProgressBar
from geopy.geocoders import Nominatim
from geopy.point import Point
import geocoder
import mouse
import urllib.request
import subprocess
from subprocess import check_output
import re
import socket

kivy.require('2.2.1')



  
   

class SystemConfig(MDApp):
     def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        #self.screen = Builder.load_file('kvfile.kv')
        self.clicks = 0
        self.running = []
        self.count = 0
        self.apps = ['History']
        self.isStopped = False
        self.clickCount = 0
        self.Fname='x'
        self.confirmed=False
        self.confirmClicks = 0
        
        #self.confirmed = False



     def findFile(self,filepath):
        self.clickCount = self.clickCount +1
        if self.clickCount % 2 !=0:
           self.root.ids.name.text=""
           self.root.ids.FindBtn.text="Search from "+ str(filepath)
        elif self.clickCount % 2 == 0:
            filename = self.root.ids.name.text
            for root,dir,files in os.walk(filepath):
               if filename in files:
                   self.filename = filename
                   self.fullpath=filepath+"\\"+filename
                   fileSize = os.stat(self.fullpath).st_size
                   sizeInKb = fileSize / 1024
                   sizeInKb = round(sizeInKb,2)
                   print(sizeInKb)
                   #boxlayoutilla voidaan antaa useita eri komponentteja, kuten label ja button popup ikkunaan
                   box = BoxLayout(orientation='vertical')
                   box.add_widget(Label(text=str(self.fullpath)))
                   box.add_widget(Label(text='File size: '+str(sizeInKb)+' KB'))
                   box.add_widget(Button(text='Open',height=20,width=100,size_hint_x=None,size_hint_y=None,on_press=self.openFile))
   
                   #box.add_widget(Label(text=str(filename)))
                   popup = Popup(title="File  found in directory: ",content=box)
                   box.add_widget(Button(text='Close',height=40,width=200,size_hint_x=None,size_hint_y=None,on_press=popup.dismiss))
                   #closeBtn = Button(text='Close',height=40,width=200,size_hint_x=None,size_hint_y=None)
                  
                   #closeBtn.bind(on_press=popup.dismiss)
                   popup.open()
                   
                  #self.root.ids.fileFound.opacity=1
                  #self.root.ids.fileFound.text=str(filename)+ ' found in directory '+str(filepath)
                  
      #TÄRKEÄ: instance parametrina, vaikka sitä ei käytetä, muuten ylämpänä oleva on_press=openfile ei toimi
     def openFile(self,instance):
        os.startfile(self.fullpath)

     def batteryStats(self):
       
         if psutil.sensors_battery()[2] == True:
              onPlugged = "Yes"
         elif psutil.sensors_battery()[2] == False:
              onPlugged = "No"
         self.root.ids.info.text=''
         btrValue = psutil.sensors_battery()[0]
         self.root.ids.bar.opacity=1
         self.root.ids.info.text="Battery charge "+str(btrValue)+" %" +"\n"+ " on plug: "+str(onPlugged)
         self.root.ids.bar.value=btrValue
         
      
   #valitun tiedoston statistiikka popup ikkunassa
     def fileStatsPopup(self):
      
    
      try:
         filename = self.root.ids.name.text
         statistics = os.stat(filename)
         closeBtn = Button(text='Close',height=40,width=200,size_hint_x=None,size_hint_y=None)
         popup = Popup(title=str(statistics),content=closeBtn)
      #bindataan buttoniin poppup ikkunan sulkemismetodi
         closeBtn.bind(on_press=popup.dismiss)
         popup.open()
         #jos tiedostoa ei löydy toteutetaan allaoleva lohko
      except FileNotFoundError:
         closeBtn = Button(text='Close',height=40,width=200,size_hint_x=None,size_hint_y=None)
         popup = Popup(title="Select the file first!",content=closeBtn)
         popup.open()
    



     
    
    
     
     def showPath(self,pname):
        print('path ',pname)
     #fname saadaan parametrina funktiokutsussa kv-filessä
     
     def selected(self,fname):
      fileStats = os.stat(fname[0])
      print(fileStats)
      self.root.ids.name.text=fname[0]
      #print("path:",pname)
      print(fname[0])
    
     def PathNameOnly(self,pname):
        
        print(pname)
        return pname
      

     def FcGoBack(self,pathName):
      
         #self.pList.append(pathName)
        #pathName= self.PathNameOnly()
         pathList = []
         pathList.append(pathName)
         newPath = ''
         target = "\\"
         #lasketaan \ merkkien määrä polkunimessä
         count = pathName.count(target)
         print("total ",count)
         #jaetaan polkunimi niin moneen osaan, kuin siinä on \ merkkejä
         #ja tallennetaan splitit plist listaan lista määritellään vasta tässä vaiheessa
         #allaolevalla syntaksilla, että se toimii oikein

         
         plist = pathName.split("\\",count)
         indexCounter = 1
         plist.insert(1,"\\")
         #toistetaan silmukkaan yhtä monta kertaa, kuin listalla on elementtejä
         listSize = len(plist)
         for i in range(len(plist)):
            #laskurin kasvatus eli joka toiseen kohtaan listassa lisätään \ merkki
            indexCounter = indexCounter +2
            plist.insert(indexCounter,'\\')
            #poistetaan viimeiset 3 alkiota listasta
         print(listSize)
         finalPlist = plist[:len(plist)-4]
         finalPlistStr = "".join(finalPlist)
         print(finalPlistStr)
         
                  
         self.root.ids.explorer.path=''
         self.root.ids.explorer.path=str(finalPlistStr)
         #self.root.ids.dirselect = True
         
       
         #self.root.ids.explorer.path=''
        
   

      #jos cb on valittu isstopped saa arvoksi true, samaa muuttujaa käytetään secondcount metodissa
      #if ehdossa, jos istopped on true, sekuntien lasku pysähtyy
     def setStop(self,checkbox,cbval):
        if cbval:
            Clock.schedule_interval(lambda sec:self.secondCount(),1)
            Clock.schedule_once(lambda dt:self.on_start(),6)
      
        

     def changeOpacity(self,cb,cbvalue):
      if cbvalue:
         self.root.ids.runBtn.opacity=1
      else:
         self.root.ids.runBtn.opacity=0

   #sovelluksen käynnistysmetodi
     def RunApplication(self):
       
        name = self.root.ids.name.text
        
        self.apps.append(name)
        
        
        #try/except lohko, muuten ohjelma kaatuu jos syöttää tiedoston nimen jota ei löydy
        try:
            open(name,match_closest=True)
            for i in self.apps:
               self.root.ids.listplace.text=str(txt)
        except:
            txt = '\n'.join(self.apps)
            for i in self.apps:
               self.root.ids.listplace.text=str(txt)
               print(txt)
            self.root.ids.status.text="can't find app "+ str(name)
           
     

        
   
     def latestReboot(self):
      dateNow = datetime.datetime.now()
      dateNowStr = dateNow.strftime("%d.%m.%Y")
      reboot = psutil.boot_time()
      formattedTime = datetime.datetime.fromtimestamp(reboot)
      final = formattedTime.strftime("%d.%m.%Y %H:%M:%S")
      #muunto jossa huomioidaan vain päivät, ei tunteja minuutteja tai sekunteja
      formattedFinal = formattedTime.strftime("%d.%m.%Y")
      #muunto datetime muutujiksi
      dtNow = datetime.datetime.strptime(dateNowStr,"%d.%m.%Y")
      dtLatest = datetime.datetime.strptime(formattedFinal,"%d.%m.%Y")
      result = dtNow - dtLatest
      print(dateNow)
      print(formattedFinal)
      #result.days antaa tuloksen pelkästään päivinä
      self.root.ids.reboot.text="Latest reboot: "+final +"\n"+ str(result.days)+" days ago"

   
     def checkRunningApp(self):
        name = self.root.ids.name.text
        if name in (i.name() for i in psutil.process_iter()):
           self.root.ids.status.color=("green")
           self.root.ids.status.text = name + ' is running'
        else:
           self.root.ids.status.color=("red")
           self.root.ids.status.text = name + ' is not running'
           
         #print(name,' running')
    
  

     def osStats(self):
        self.platformStuff = ''
        #pos_hint avulla voi muuttaa widhetin sijoittelua suoraan koodissa eli kv-fileen ei tarvitse koskea
        #self.moreInfoLbl = MDLabel(text="More specifics?",pos_hint={'center_x':0.8})

        #self.moreInfo = MDCheckbox(on_active=self.osSpesificStats,size_hint=[0.5,0.3])
        #self.root.add_widget(self.moreInfoLbl)
        #self.root.add_widget(self.moreInfo)
        self.root.ids.info.text=''
        self.root.ids.info.text='[b]Operating System: [/b]'+str(platform.system()+' '+platform.release()) + ' '+platform.win32_edition()\
        +"\n"+"[b]Processor: [/b]"+ str(platform.processor())
        self.platformStuff= self.root.ids.info.text
      
        #opacirty eli muutetaan buttoni näkyväksi
        self.root.ids.moreInfoBtn.opacity=1
        return self.platformStuff
        

    
     def osSpesificStats(self):
      
      #talletetaan muuttujaan osstats metodin palautusarvo eli lista johon on tallennettu sen metodin
      #näyttämä tieto
      earlierInfo = self.osStats()
      self.clicks = self.clicks+1
      #jakojäännöksen avulla toteutetaan vuoroin näytettävä data. eli yhdellä jaollisella näytetään
      #ensimäinen if lohko ja kahdella jaollinen näyttää alemman if lohkon
      if self.clicks % 1 == 0:
         self.root.ids.info.text=''
         self.root.ids.moreInfoBtn.text='Show less'
         '''
         for i in range(4):
            unameList.append(platform.uname()[i])
         self.root.ids.info.text = str(unameList)+str(earlierInfo)+"\n"+str(platform.platform())
         '''
         unameReplaced = str(platform.uname())
         unameReplaced = unameReplaced.replace("uname_result","").replace("(","").replace(")","")
         self.root.ids.info.text=str(earlierInfo)+"\n"+str(platform.platform())+"\n"+ str(unameReplaced)
      if self.clicks % 2 == 0:
         self.root.ids.moreInfoBtn.text='Show more'
         self.osStats()

         #self.root.ids.info.text=''
         #self.root.ids.info.text='Operating System: '+str(platform.system()+' '+platform.release())+ ' '+platform.win32_edition()
     
     

     def memoryStats(self):
      self.mouseMoved()
      self.seconds = 5
      self.root.ids.stopCB.opacity=1
      self.root.ids.stopCB.disabled=False

      self.total =psutil.virtual_memory()[0]/1000000000
      self.free=psutil.virtual_memory()[1]/1000000000
      self.used = psutil.virtual_memory()[3]/1000000000
      self.total=round(self.total,2)
      self.free=round(self.free,2)
      self.used=round(self.used,2)
      total,used,free = shutil.disk_usage("/")
      self.totalSize = total / (1024.0**3)
      self.freeSize = free / (1024.0**3)
      self.usedSize = used / (1024.0**3)
      self.totalSize = round(self.totalSize,2)
      self.freeSize = round(self.freeSize,2)
      self.usedSize = round(self.usedSize,2)
      
      #if self.spinner.text=="Memory & disk":
      self.root.ids.info.text = ''
   
      self.root.ids.infolbl.text=""
      #self.root.ids.info.color=(0,0,1,1)
      #markup täytyy asettaa trueksi kv-filessa että voidaan käyttää color ominaisuutta tekstissä
      self.root.ids.info.text="[u]Memory[/u]\n[color=#2986cc]Total:[b]" +str(self.total)+"[/b] GB "+"\n"+"Free: [b]"+str(self.free)+"[/b] GB"+"\n"+ "Used: [b]" +str(self.used)+"[/b] GB [/color]"\
      "\n [color=#38761d] Total Disk space: [b]"+str(self.totalSize)+" [/b]\n Used disk space: [b]"+str(self.usedSize)+"[/b] \n Free disk space [b]"+str(self.freeSize)+"[/b][/color]"
      self.root.ids.moreInfoBtn.opacity=0
     
      
      #self.root.ids.info.color=(0,1,0,1)
      #self.root.ids.info.text="\n Total Disk space: "+str(self.totalSize)+"\n Used disk space: "+str(self.usedSize)+"\n Free disk space "+str(self.freeSize)
    
      self.allMem = (self.free,self.used)

      #lambda viittauksella voidaan antaa on_start metodille parametrina 5 sekuntia ilman, että metodille
      #täytyy erikseen määritellä parametrimuuttuja
      
      '''
      if self.isStopped == False:
         Clock.schedule_interval(lambda sec:self.secondCount(),1)
         Clock.schedule_once(lambda dt:self.on_start(),6)
      elif self.isStopped == True:
         Clock.unschedule(lambda sec:self.secondCount(),1)
         Clock.unschedule(lambda dt:self.on_start(),6)
      print(self.isStopped)
      '''
      #return lauseella voidaan käyttää allmem muuttujaan tallennettuja arvoja toisessa funktiossa, ilman
      #että niitä tarvitsee määritellä uudelleen toisessa metodissa.
      return self.allMem
    
   #metodin internet yhteyden tarkistukseen, yhteyttä tarvitaan sijainnin selvittämiseen
   #jos yhteyttä ei ole, try/exceptin avulla ohjelma ei kaadu.
     def checkConnection(self):
           
           try:
               urllib.request.urlopen("https://www.google.com")
               return True
           except urllib.error.URLError:
               return False
           
     def networkStats(self):
        
        st=speedtest.Speedtest()
        down = st.download()/(1024*1024)
        down = round(down,2)
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        self.root.ids.info.text=''
        if self.checkConnection():
           self.root.ids.info.text="Your are online\n ip address: "+str(IPAddr)+"\n"+"Download speed: "+str(down)
        else:
           self.root.ids.info.text="You are offline"
   
     #sijainnin haku laitteen lat/long koordinaattien perusteella
     def getLocation(self):
       #jos metodin return arvo on true eli internet on yhdistetty
       if self.checkConnection():
          
         loc = geocoder.ip("me")
         geoLoc = Nominatim(user_agent="getLoc")
         locName = geoLoc.reverse(loc.latlng)
         address = locName.raw['address']
         city = address.get('city','')
         self.root.ids.location.text="Current location: "+str(city)
       else:
          print("No connection")
  
     #käynnissä olevien sovellusten haku on_start metodi suoritetaan heti ohjelman käynnistyttyä.
     def on_start(self):
       
       self.getLocation()
       
       #listan tyhjennys, ilman clearia listan sisältö tulostuu toisen kerran edellisen listan perään
       #jos valitsee ensin esim memory&disk vaihtoehdon ja sen jälkeen start screen vaihtoehdon
    
       self.running.clear()
       self.root.ids.info.text=" "
       self.root.ids.bar.opacity=0
       windows = Desktop(backend="uia").windows()
       for w in windows: 
         self.running.append(w.window_text())
         
         self.count = self.count +1
         #lasketaan listan alkioiden kokonaismäärä
       self.counter = 0
       dict = {}
        #muutetaan lista merkkijonoksi ja lisätään jokaisen merkkijonon jälkeen rivinvaihto
       txt = '\n'.join(self.running)
       


       #lasketaan listan alkioiden määrä
       for i in self.running:
         self.counter = self.counter +1
         self.root.ids.info.text=' Currently running apps:\n' +"[color=#2986cc]"+str(txt)+"[/color]"+"\n"
         
       apps = self.root.ids.info.text 
       self.root.ids.info.text=str(apps)+"Total: "+str(self.counter)
         
         #dict[counter]=i
         #print(dict)
       
       #for j in dict:
       #  print(j)
     
       self.latestReboot()
       #self.ShowCloseTasks()
      
     def ShowCloseTasks(self):
        self.apps = []
        self.processIds = []
        #haetaan käynnissä olevien ohjelmien nimet ja process id:t
        cmd = 'powershell "gps | where {$_.MainWindowTitle} | select Description,Id'
        #haetaan pelkästään process id
        proc = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
        
        for line in proc.stdout:
             #decode poistaa binary merkit
         if not line.decode()[0].isspace():
            linestr = line.decode().rstrip()
            #korvataan annetut merkit tyhjällä
            final = linestr.replace('-','').replace('Description','').replace('Id','')
            finalForRegEx = linestr.replace('-','').replace('Description','').replace('Id','').replace(" ","").replace("/","")
            #regex lauseke poistaa kaikki kirjaimet a-z
            finalre=re.sub('[a-zA-Z]'," ",finalForRegEx)
            self.apps.append(final)
            self.processIds.append(finalre)
            
          
            #rivinvaihto listan alkioiden väliin
            txt = "\n".join(self.apps)
            txt2 = "\n".join(self.processIds)
         print(self.processIds)
            
        #finalList.append(txt)
        self.apps.pop(0)
        self.apps.pop(1)
        self.listSize = len(self.apps)
        print(txt)
        confLbl = MDLabel(text='Always ask confirm for closing?')
        confCB = MDCheckbox(pos_hint={'right':0.9,'y':0.5},size_hint=(.5,.5),on_press=self.confirm)
        box = BoxLayout(orientation='vertical')
        
        popup = Popup(title="Close tasks: ",content=box)
        box.add_widget(Label(text='Name  Process id'))
        
        
        #muistin käyttö ja käynnistyajat tallennetaan listoihin.
        timeValues = []
        memoryValues = []
        #huomaa sisäkkäinen silmukka, molemmat silmukat käyvät eri listat läpi self.i.tä käytetään kierromuuttujana
        #kaikissa kolmessa läpikäytäväsää listassa
        for self.i in range(self.listSize):
         for x in self.processIds:
           #jos x eli taulukon alkio on tyhjä continue komennolla siirrytään seuraavaan lista-alkioon
           if x == '':
              continue
           else:

            xInt = int(x)
            p = psutil.Process(xInt)
            #ohjelman käynnistyajan selvitys
            p.create_time()
            startTime = time.strftime('%H:%M:%S',time.localtime(p.create_time())) 
            timeValues.append(startTime)
            mem = p.memory_percent()
            mem = round(mem,2)
            memoryValues.append(mem)
            

   
           
           
      
         box.add_widget(Button(markup=True, text="Starting time: "+str(timeValues[self.i]) +" Memory usage: " +str(memoryValues[self.i])+" % [b]"+str(self.apps[self.i]),on_press=self.closeTask))
        box.add_widget(confLbl)
        box.add_widget(confCB)
        
           
        popup.open()
        #popup ikkuna nousee aloitusikkunan päälle, joten takaisin menoon riittää pelkkä popup.dismiss
        GoBackBtn=(Button(text='Go back',color='lightblue',on_press=popup.dismiss))
        box.add_widget(GoBackBtn)
        

          
     def createConfirmWind(self):
           
           boxLayout = BoxLayout(orientation="horizontal")
           confirmPop = Popup(title='Confirm close',content=boxLayout)
           yesBtn = Button(text="yes",size=(50,25))
           noBtn = Button(text="No",size=(50,25))
        
        
           boxLayout.add_widget(yesBtn)
           boxLayout.add_widget(noBtn)
           noBtn.bind(on_press=confirmPop.dismiss)
           yesBtn.bind(on_press=self.DoClose)

        
           confirmPop.open()

      
     def closeTask(self,instance):
      name = instance.text
      self.Fname = name
      #print(name)
      #instancen avulla saatiin ratkaistua aiempi ongelma, jossa parametrin saanut metodi palauttaa arvon
      #antamalla instance parametriksi return arvon palautus ja uudelleenkäyttö toimii
      if self.confirmed==True:
         self.createConfirmWind()
      '''
      if not self.confirm(instance):

         self.DoClose(instance)
      return self.Fname
      '''
     
     

     def DoClose(self,instance):
      #koska namessa on prosessin nimi,muistin kulutus, pid jne splitataan se osiin
      pid = self.Fname.split()
      #viimeinen osa sisältää process id:n jota tarvitaan sulkemiseen, se täytyy muuttaa myös int-tyyppiseksi
      pidToInt = int(pid[-1])
      print(pidToInt)
      p = psutil.Process(pidToInt)
      p.terminate()
      pid=''
        #metodin uudelleen kutsu poistaa suljetun ohjelman buttonin ja näyttää jäljellä olevat
      self.ShowCloseTasks()
      #print(self.Fname)
  
        
     def confirm(self,cbval):
        self.confirmed=True
        print(self.confirmed)
        '''
        self.confirmClicks = self.confirmClicks+1
        if self.confirmClicks % 1 == 0:

         self.confirmed = True
         print(self.confirmed)
        elif self.confirmClicks % 2 ==0:
           self.confirmed=False
           print(self.confirmed)
         #return self.confirmed
      '''
       
      
        
      
           
         
        
        #print(instance.text)
        
           
       
      
       #self.DrawBars()
     def mouseMoved(self):
          current=mouse.get_position()
          print(current)
          while True:
               
            newPos = mouse.get_position()
            if current != newPos:
               print(newPos)
               break
              
      #jokaisella kutsulla vähennetään self.secondista aina luku yksi, metodia kutsutaan sekunnin välein, joten
       #sen avulla saadaan sekuntilaskuri luotua label komponenttiin. katso ajastus memorystats metodista
     def secondCount(self):
        
        self.seconds = self.seconds -1
        lblText =  "Seconds until get back to start screen: "
        
        
      

        #pysäytetään return komennolla laskeminen jos seconds on pienempi kuin 0
        if self.seconds < 0:
           return
        elif self.isStopped == True:
           self.root.ids.time.text="stopped"
           
        else:
         self.root.ids.time.text=" "

         self.root.ids.time.text=lblText+" "+ str(self.seconds)
      
        
    
      #piirretään pylväsdiagrammi käynnissä olevien sovellusten määrästä.
     def DrawBars(self,switch,value):
        if value:
           
           self.root.ids.FrontImg.source="runningBar.png"
        else:
           self.root.ids.FrontImg.source=""
             
        
           
           
        #value = self.count
        #label = "Running"
        #plt.bar(label,value)
        #plt.savefig("runningBar.png")
        

        
     def checkboxState(self,checkbox,value):
        #value on cb:n tila, jos se on valittu kutsutaan systemruntime2 metodia 5 sekunnin välein.
        if value:
           print("checkbox clicked")
           Clock.schedule_interval(self.systemRunTime,5)
        elif value != True:
           #pysäytetään ajastettu metodin kutsu
           Clock.unschedule(self.systemRunTime)

      
     def DrawPieValues(self,checkbox,cbval):
        memorylabels = []
        
        if cbval:
           self.root.ids.backBtn.opacity=1
           self.values = self.memoryStats()
           memoryValues = [self.values[0],self.values[1]]
           memorylblFree = "Free: "+str(self.values[0]) + " GB"
           memorylabels.append(memorylblFree)
           memorylblUsed = "Used: "+str(self.values[1])+ " GB"
           memorylabels.append(memorylblUsed)
           fig,ax = plt.subplots()
           ax.pie(memoryValues,labels=memorylabels,colors=["green","red"])
           #plt.pie(memoryValues,labels=memorylabels,colors=["green","red"])
           fig.savefig("memoryNumbers2.png")
           self.root.ids.img.source="memoryNumbers2.png"

     def DrawPiePercent(self,checkbox,cbvalue):
        if cbvalue:
         self.root.ids.backBtn.opacity=1
         #checkboksin piilotus
         self.root.ids.pieCBper.opacity=0
           # haetaan ja tallennetaan muuttujaan memorystats metodin return arvo
         self.values = self.memoryStats()
      
        
         memoryValues = [self.values[0],self.values[1]]
         memorylabels = ['Free','Used']
         plt.pie(memoryValues,labels=memorylabels,autopct='%1.2f%%',colors=["green","red"])
       
         plt.savefig("memory.png")
        #näytetään kuva img-id:llä varustetussa Image-objektissa (ks.kvfile)
         self.root.ids.img.source="memory.png"

     def ClearDrawnings(self):
        self.root.ids.img.source="" 
     

     def build(self):
        
        screen=Builder.load_file('kvfile.kv')
        #self.memoryStats()
        return screen
 



if __name__=="__main__":
    SystemConfig().run()
