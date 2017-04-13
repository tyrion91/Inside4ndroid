import urllib,urllib2,re,xbmcplugin,xbmcgui,urlresolver,sys,xbmc,xbmcaddon,os,random,urlparse,json,time,net,control,shutil,cf,cl
from t0mm0.common.addon import Addon
from metahandler import metahandlers
net = net.Net()
baseurl = control.part1
addon_id = 'plugin.video.ecgmovies'
selfAddon = xbmcaddon.Addon(id=addon_id)
datapath= xbmc.translatePath(selfAddon.getAddonInfo('profile'))
addon = Addon(addon_id, sys.argv)
artwork = baseurl+control.prop
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id , 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
filel = artwork+cf.film
mediapath = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + '/resources/media/'))
metaset = selfAddon.getSetting('enable_meta')
metatrue = filel+cl.end
User_Agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'
try:os.mkdir(datapath)
except:pass
execute = xbmc.executebuiltin
THDATA = xbmc.translatePath('special://userdata/Thumbnails/')
file_var = open(xbmc.translatePath(os.path.join(datapath, 'cookie.lwp')), "a")
cookie_file = os.path.join(os.path.join(datapath,''), 'cookie.lwp')
baseurl_1 = metatrue

def CATEGORIES():
	addDir2('[COLOR yellow][B]Search[/B][/COLOR]',baseurl_1,4,mediapath+'search.png','Here you can search a movie if you have something particular in mind.',fanart)
	addDir2('[COLOR yellow][B]Trending[/B][/COLOR]',baseurl_1+'trending/?get=movies',1,mediapath+'trending.png','This list is a mix of the most talked about movies.',fanart)
	addDir2('[COLOR yellow][B]Featured [/B][/COLOR]',baseurl_1+'genre/featured/',1,mediapath+'popular.png','This is a list of movies which are recommended as a good watch.',fanart)
	addDir2('[COLOR yellow][B]Most Popular [/B][/COLOR]',baseurl_1+'ratings/?get=movies',1,mediapath+'popular.png','This is a list of movies which are most popular by user rating.',fanart)
	addDir2('[COLOR yellow][B]Genres[/B][/COLOR]',baseurl_1,2,mediapath+'genres.png','If your just looking a for a particular type of film then this is the section for you.',fanart)
	addDir2('[COLOR yellow][B]Years[/B][/COLOR]',baseurl_1,3,mediapath+'years.png','If you fancy a classic film or a new film then this section wont fail you.',fanart)
	addDir2('[COLOR yellow][B]Settings[/B][/COLOR]',baseurl_1,5,mediapath+'settings.png','Here you can customize the look of the addon and also disable the artwork/descriptions which in turn loads the sections faster.',fanart)
	addDir2('[COLOR yellow][B]Tools[/B][/COLOR]',baseurl_1,6,mediapath+'tools.png','Here you can clear your cache, packages and even empty your thumbnails directories',fanart)
	addDir2('[COLOR yellow][B]Support[/B][/COLOR]',baseurl_1,1003,mediapath+'support.png','Here there is info on how to contact me to report errors/films not playing etc...',fanart)
	setView('movies', 'MAIN')

def GETMOVIES(url,name):
		link = open_url(url)
		match=re.compile('<article id=.+?class="item movies".+?<a href="(.+?)"><img src=".+?" alt="(.+?)">.+?<span class="quality">(.+?)</span>',re.DOTALL).findall(link)
		items = len(match)
		for url,name,quality in match:
			name2 = cleanHex(name)
			addDir(name2,quality,url,100,'',len(match))
		np = re.compile('class=.+?current.+?<a href=\'(.+?)\'',re.DOTALL).findall(link)
		for url in np:
			addDir2('[B][COLOR gold]Next Page  >>>[/COLOR][/B]',url,1,mediapath+'nextp.png','Click this to go on to the next page. To return to this page just press back or click the "..." at the top of the page.',fanart)
			url=url.replace("&amp;","&")
		setView('movies', 'MAIN')

def SEARCH_INDEX(url,name):
		link = open_url(url)
		match=re.compile('<div class="result-item">.+?<a href="(.+?)">.+?<img src=".+?" alt="(.+?)"',re.DOTALL).findall(link)
		items = len(match)
		for url,name in match:
			name2 = cleanHex(name)
			if '/tvseries/' not in url:
				addDir(name2,'N/A',url,100,'',len(match))
			else:pass
		setView('movies', 'MAIN')
	
def SEARCH():
	search_txt =''
	keyboard = xbmc.Keyboard(search_txt, 'What Would You Like To Watch?')
	keyboard.doModal()
	if keyboard.isConfirmed():
		search_txt = keyboard.getText().replace(' ','+')
	if len(search_txt)>1:
		url = baseurl_1+'/?s='+search_txt
		link = open_url(url)
		SEARCH_INDEX(url,name)

def YEARS():
	search_txt =''
	keyboard = xbmc.Keyboard(search_txt, 'Type A Year From 1968 To 2017')
	keyboard.doModal()
	if keyboard.isConfirmed():
		search_txt = keyboard.getText().replace(' ','+')
	if len(search_txt)>1:
		url = baseurl_1+'release/'+search_txt
		link = open_url(url)
		GETMOVIES(url,name)

def GENRES(url):
	link = open_url(url)
	#match=re.compile('class=".+?"><a href="(.+?)" >(.+?)',re.DOTALL).findall(link)
	ref = re.compile('<ul class="genres scrolling">(.+?)</ul>',re.DOTALL).findall(link)
	match = re.compile('<a href="(.+?)"',re.DOTALL).findall(str(ref))
	for url in match:
		name = url.split('/')[4]
		name = name.split('/')[0].split('.')[0].title()
		name2 = cleanHex(name)
		addDir2('[B][COLOR yellow]%s[/COLOR][/B]' %name2,url,1,mediapath+'genres.png','',fanart)
				#addDir2(name,url,mode,iconimage,description,fanart)
	setView('movies', 'MAIN')

def PLAYLINK(name,url,iconimage):
	OPEN = open_url(url)
	try:
		url = re.compile('file.+?"(.+?)"',re.DOTALL).findall(OPEN)[0]
		url = url.replace('\/','/')
		xbmcgui.Dialog.ok('',url)
	except:
		liz = xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
		liz.setInfo(type="Video", infoLabels={"Title": ''})
		liz.setProperty("IsPlayable","true")
		liz.setPath(url)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

	
def TOOLS():
	addDir2('[COLOR yellow][B]Clear Cache[/B][/COLOR]',baseurl_1,1000,mediapath+'cache.png','',fanart)
	addDir2('[COLOR yellow][B]Clear Packages[/B][/COLOR]',baseurl_1,1001,mediapath+'packages.png','',fanart)
	addDir2('[COLOR yellow][B]Clear Thumbnails[/B][/COLOR]',baseurl_1,1002,mediapath+'thumbs.png','',fanart)
	setView('movies', 'MAIN')

def SUPPORT():
	xbmcgui.Dialog().ok('[B][COLOR limegreen]ECG [/COLOR][COLOR gold]MOVIES [/COLOR][/B]','Thanks for using ECG MOVIES. If you require support or want to report non working films or errors please contact me via the following ways >>> \nEMAIL: inside4ndroid.techsup@gmail.com \nTWITTER: @Inside_4ndroid \nThank You')
	CATEGORIES(); return

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
        return param

def clearCache():
	metaset = selfAddon.getSetting('enable_meta')
	yes = xbmcgui.Dialog().yesno('[B][COLOR limegreen]ECG [/COLOR][COLOR gold]MOVIES [/COLOR][/B]','Are you sure you want to delete all cache files?',yeslabel='Yes',nolabel='No')
	if not yes: 
		add_link_info('[B][COLOR limegreen]** [COLOR gold]<< PRESS BACK[/COLOR] **[/COLOR][/B]', icon, fanart)
		setView('movies', 'MAIN')
		return
	import clear
	clear.CleanUP()
	xbmc.executebuiltin("XBMC.Notification([COLOR gold][B]ECG MOVIES[/B][/COLOR],'Your Cache Is Now Empty',5000,"+icon+")")
	add_link_info('[B][COLOR limegreen]** [COLOR gold]<< PRESS BACK[/COLOR] **[/COLOR][/B]', icon, fanart); return
	setView('movies', 'MAIN')

def clearPacks():
	metaset = selfAddon.getSetting('enable_meta')
	yes = xbmcgui.Dialog().yesno('[B][COLOR limegreen]ECG [/COLOR][COLOR gold]MOVIES [/COLOR][/B]','Are you sure you want to delete Package files?',yeslabel='Yes',nolabel='No')
	if not yes: 
		add_link_info('[B][COLOR limegreen]** [COLOR gold]<< PRESS BACK[/COLOR] **[/COLOR][/B]', icon, fanart)
		setView('movies', 'MAIN')
		return
	import clear
	clear.Clear_P()
	xbmc.executebuiltin("XBMC.Notification([COLOR gold][B]ECG MOVIES[/B][/COLOR],'Your Packages Is Now Empty',5000,"+icon+")")
	add_link_info('[B][COLOR limegreen]** [COLOR gold]<< PRESS BACK[/COLOR] **[/COLOR][/B]', icon, fanart); return
	setView('movies', 'MAIN')
	
def ClearThumbs():
	metaset = selfAddon.getSetting('enable_meta')
	yes = xbmcgui.Dialog().yesno('[COLOR gold][B]ECG MOVIES[/B][/COLOR]','Clearing the Thumbs will require you to force close kodi. After you have cleared the Thumbs FOLLOW AND READ the on screen instructions. \nDO YOU WANT TO CONTINUE?',yeslabel='Yes',nolabel='No')
	if not yes: 
		add_link_info('[B][COLOR limegreen]** [COLOR gold]<< PRESS BACK[/COLOR] **[/COLOR][/B]', icon, fanart)
		setView('movies', 'MAIN')
		return
	shutil.rmtree(THDATA)
	killxbmc()

def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'

def killxbmc():
    choice = xbmcgui.Dialog().yesno('[B][COLOR limegreen]ECG [/COLOR][COLOR gold]MOVIES [/COLOR][/B]', 'You are about to close Kodi', 'Would you like to continue?', nolabel='No, Cancel',yeslabel='Yes, Close')
    if choice == 0:
        add_link_info('[B][COLOR limegreen]** [COLOR gold]<< PRESS BACK[/COLOR] **[/COLOR][/B]', icon, fanart)
        setView('movies', 'MAIN')
        return
    elif choice == 1:
        pass
    myplatform = platform()
    print "Platform: " + str(myplatform)
    if myplatform == 'osx': # OSX
        print "############   try osx force close  #################"
        try: os.system('killall -9 XBMC')
        except: pass
        try: os.system('killall -9 Kodi')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.",'')
    elif myplatform == 'linux': #Linux
        print "############   try linux force close  #################"
        try: os.system('killall XBMC')
        except: pass
        try: os.system('killall Kodi')
        except: pass
        try: os.system('killall -9 xbmc.bin')
        except: pass
        try: os.system('killall -9 kodi.bin')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.",'')
    elif myplatform == 'android': # Android  
        print "############   try android force close  #################"
        try: os._exit(1)
        except: pass
        try: os.system('adb shell am force-stop org.kodi')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc.xbmc')
        except: pass
        try: os.system('adb shell am force-stop org.xbmc')
        except: pass        
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Press the HOME button on your remote and [COLOR=red][B]FORCE STOP[/COLOR][/B] KODI via the Manage Installed Applications menu in settings on your Amazon home page then re-launch KODI")
    elif myplatform == 'windows': # Windows
        print "############   try windows force close  #################"
        try:
            os.system('@ECHO off')
            os.system('tskill XBMC.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('tskill Kodi.exe')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im Kodi.exe /f')
        except: pass
        try:
            os.system('@ECHO off')
            os.system('TASKKILL /im XBMC.exe /f')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit cleanly via the menu.","Use task manager and NOT ALT F4")
    else: #ATV
        print "############   try atv force close  #################"
        try: os.system('killall AppleTV')
        except: pass
        print "############   try raspbmc force close  #################" #OSMC / Raspbmc
        try: os.system('sudo initctl stop kodi')
        except: pass
        try: os.system('sudo initctl stop xbmc')
        except: pass
        dialog.ok("[COLOR=red][B]WARNING  !!![/COLOR][/B]", "If you\'re seeing this message it means the force close", "was unsuccessful. Please force close XBMC/Kodi [COLOR=lime]DO NOT[/COLOR] exit via the menu.","iOS detected.  Press and hold both the Sleep/Wake and Home button for at least 10 seconds, until you see the Apple logo.")    

def addDir2(name,url,mode,iconimage,description,fanart):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage=iconimage, thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def addDir(name,quality,url,mode,iconimage,itemcount,isFolder=False):
        if metaset=='true':
            splitName=name.partition('(')
            simplename=""
            simpleyear=""
            if len(splitName)>0:
                simplename=splitName[0]
                simpleyear=splitName[2].partition(')')
            if len(simpleyear)>0:
                simpleyear=simpleyear[0]
            mg = metahandlers.MetaData()
            meta = mg.get_meta('movie', name=simplename ,year=simpleyear)
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&quality="+urllib.quote_plus(quality)+"&iconimage="+urllib.quote_plus(iconimage)
            ok=True
            liz=xbmcgui.ListItem(name, iconImage=meta['cover_url'], thumbnailImage=iconimage)
            liz.setInfo( type="Video", infoLabels=meta)
            liz.setInfo( type="Video", infoLabels={'title': '[B][COLOR blue]%s[/COLOR][/B]' %name+'[I][COLOR gold] (%s)[/COLOR][/I]' %quality})
            contextMenuItems = []
            contextMenuItems.append(('Movie Information', 'XBMC.Action(Info)'))
            liz.addContextMenuItems(contextMenuItems, replaceItems=True)
            if not meta['backdrop_url'] == '': liz.setProperty('fanart_image', meta['backdrop_url'])
            else: liz.setProperty('fanart_image', fanart)
            #ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False,totalItems=itemcount)
            if mode==100:
                liz.setProperty("IsPlayable","true")
                ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
            else:
                ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
            return ok
        else:
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&quality="+urllib.quote_plus(quality)+"&iconimage="+urllib.quote_plus(iconimage)
            ok=True
            liz=xbmcgui.ListItem(name, quality, iconImage=icon, thumbnailImage=iconimage)
            liz.setInfo( type="Video", infoLabels={"Title": name,"Plot":''})
            liz.setProperty('fanart_image', fanart)
            if mode==100:
                liz.setProperty("IsPlayable","true")
                ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
            else:
                ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
            return ok
            

def addLink(name,url,mode,iconimage,fanart,description=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def add_link_dummy(iconimage, fanart):
	u = sys.argv[0] + "&iconimage=" + urllib.quote_plus(iconimage)	
	liz = xbmcgui.ListItem(iconImage = "DefaultVideo.png", thumbnailImage = iconimage)
	liz.setProperty('fanart_image', fanart)
	liz.setProperty('IsPlayable', 'false') 
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz) 	

def add_link_info(name, iconimage, fanart):
	u = sys.argv[0] + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)	
	liz = xbmcgui.ListItem(name, iconImage = "DefaultVideo.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	liz.setProperty('IsPlayable', 'false') 
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz) 

def showText(heading, text):
    id = 10147
    xbmc.executebuiltin('ActivateWindow(%d)' % id)
    xbmc.sleep(100)
    win = xbmcgui.Window(id)
    retry = 50
    while (retry > 0):
        try:
            xbmc.sleep(10)
            retry -= 1
            win.getControl(1).setLabel(heading)
            win.getControl(5).setText(text)
            return
        except:
            pass
        
def open_url(url):
        try:
                net.set_cookies(cookie_file)
                link = net.http_GET(url).content
                link = cleanHex(link)
                return link
        except:
                cl.createCookie(url,cookie_file,'Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0')
                net.set_cookies(cookie_file)
                link = net.http_GET(url).content
                link = cleanHex(link)
                return link

def regex_from_to(text, from_string, to_string, excluding=True):
	if excluding:
		try: r = re.search("(?i)" + from_string + "([\S\s]+?)" + to_string, text).group(1)
		except: r = ''
	else:
		try: r = re.search("(?i)(" + from_string + "[\S\s]+?" + to_string + ")", text).group(1)
		except: r = ''
	return r


def regex_get_all(text, start_with, end_with):
	r = re.findall("(?i)(" + start_with + "[\S\s]+?" + end_with + ")", text)
	return r

def cleanHex(text):
    def fixup(m):
        text = m.group(0)
        if text[:3] == "&#x": return unichr(int(text[3:-1], 16)).encode('utf-8')
        else: return unichr(int(text[2:-1])).encode('utf-8')
    try :return re.sub("(?i)&#\w+;", fixup, text.decode('ISO-8859-1').encode('utf-8'))
    except:return re.sub("(?i)&#\w+;", fixup, text.encode("ascii", "ignore").encode('utf-8'))

def openSettings(query=None, id=addon_id):
	metaset = selfAddon.getSetting('enable_meta')
	try:
		execute('Addon.OpenSettings(%s)' % id)
		if query == None: raise Exception()
		c, f = query.split('.')
		execute('SetFocus(%i)' % (int(c) + 100))
		execute('SetFocus(%i)' % (int(f) + 200))
		add_link_info('[B][COLOR limegreen]** [COLOR gold]<< PRESS BACK[/COLOR] **[/COLOR][/B]', icon, fanart)
		setView('movies', 'MAIN')
	except:
		add_link_info('[B][COLOR limegreen]** [COLOR gold]<< PRESS BACK[/COLOR] **[/COLOR][/B]', icon, fanart)
		setView('movies', 'MAIN')
		return

def setView(content, viewType):
    ''' Why recode whats allready written and works well,
    Thanks go to Eldrado for it '''
    VT = '50'
    if content:
        xbmcplugin.setContent(int(sys.argv[1]), content)
    if addon.get_setting('auto-view') == 'true':

        print addon.get_setting(viewType)
        if addon.get_setting(viewType) == 'Info':
            VT = '504'
        elif addon.get_setting(viewType) == 'Info2':
            VT = '503'
        elif addon.get_setting(viewType) == 'Info3':
            VT = '515'
        elif addon.get_setting(viewType) == 'Fanart':
            VT = '508'
        elif addon.get_setting(viewType) == 'Poster Wrap':
            VT = '501'
        elif addon.get_setting(viewType) == 'Big List':
            VT = '51'
        elif addon.get_setting(viewType) == 'Low List':
            VT = '724'
        elif addon.get_setting(viewType) == 'Default View':
            VT = addon.get_setting('default-view')

        print viewType
        
        xbmc.executebuiltin("Container.SetViewMode(%s)" % ( int(VT) ) )

    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_UNSORTED )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_LABEL )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RATING )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_DATE )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_PROGRAM_COUNT )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RUNTIME )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_GENRE )
    xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_MPAA_RATING )

params=get_params(); url=None; name=None; quality=None; mode=None; site=None; iconimage=None; query=None
try: site=urllib.unquote_plus(params["site"])
except: pass
try: url=urllib.unquote_plus(params["url"])
except: pass
try: name=urllib.unquote_plus(params["name"])
except: pass
try: quality=urllib.unquote_plus(params["quality"])
except: pass
try: mode=int(params["mode"])
except: pass
try: iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
try: query=urllib.unquote_plus(params["query"])
except: pass

print "Site: "+str(site); print "Mode: "+str(mode); print "URL: "+str(url); print "Name: "+str(name); print "Quality: "+str(quality)
print params

if mode==None or url==None or len(url)<1: CATEGORIES()
elif mode==1: GETMOVIES(url,name)
elif mode==2: GENRES(url)
elif mode==3: YEARS()
elif mode==4: SEARCH()
elif mode==5: openSettings(query)
elif mode==6: TOOLS()
elif mode==100: PLAYLINK(name,url,iconimage)
elif mode==1000: clearCache()
elif mode==1001: clearPacks()
elif mode==1002: ClearThumbs()
elif mode==1003: SUPPORT()

xbmcplugin.endOfDirectory(int(sys.argv[1]))

