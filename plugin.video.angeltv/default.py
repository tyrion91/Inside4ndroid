# -*- coding: utf-8 -*-
import urllib, urllib2, sys, re, os, unicodedata,cl,urlresolver
import xbmc, xbmcgui, xbmcplugin, xbmcaddon, xbmcvfs
from resources.lib.modules import net
from resources.lib import requests

#CODED BY INSIDE-4NDROID 04/2017

addon_id = 'plugin.video.angeltv'
selfAddon = xbmcaddon.Addon(id=addon_id)
datapath= xbmc.translatePath(selfAddon.getAddonInfo('profile'))
plugin_handle = int(sys.argv[1])
dialog = xbmcgui.Dialog()
mysettings = xbmcaddon.Addon(id = 'plugin.video.angeltv')
profile = mysettings.getAddonInfo('profile')
home = mysettings.getAddonInfo('path')
fanart = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))
mediapath = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + '/resources/media/'))
path   = xbmcaddon.Addon().getAddonInfo('path').decode("utf-8")
logfile = xbmcvfs.File(os.path.join(path, 'changelog.txt'))
text = logfile.read()
User_Agent = 'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'
baseurl = 'http://i4pro.co.uk/kodi/shadownet/pl1.html'
baseurlwwe = 'http://watchwrestling.uno'
u_r_l = 'http://i4pro.co.uk/kodi/shadownet/'
try:os.mkdir(datapath)
except:pass
online_xml = u_r_l+'xtrax.xml'
online_other = u_r_l+'othersport.m3u'
online_basics = u_r_l+'listspt2.m3u'
file_var = open(xbmc.translatePath(os.path.join(datapath, 'cookie.lwp')), "a")
cookie_file = os.path.join(os.path.join(datapath,''), 'cookie.lwp')
net = net.Net()
xml_regex = '<title>(.*?)</title>\s*<link>(.*?)</link>\s*<thumbnail>(.*?)</thumbnail>'
m3u_regex = '#(.+?),(.+)\s*(.+)\s*'
s = requests.session()
first = requests.utils.one

def make_request(url):
	try:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0')
		response = urllib2.urlopen(req)	  
		link = response.read()
		response.close()  
		return link
	except urllib2.URLError, e:
		print 'We failed to open "%s".' % url
		if hasattr(e, 'code'):
			print 'We failed with error code - %s.' % e.code	
		if hasattr(e, 'reason'):
			print 'We failed to reach a server.'
			print 'Reason: ', e.reason

def main():
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]WELCOME TO SPORTS ANGEL [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'welcome.png', fanart)
	add_link_dummy(icon, fanart)
	addDirMain('[COLOR yellow][B]>> Sports IPTV[/B][/COLOR]',u_r_l,3,mediapath+'welcome.png')
	addDirMain('[COLOR yellow][B]>> Wrestling[/B][/COLOR]',u_r_l,14,mediapath+'welcome.png')
	addDirMain('[COLOR yellow][B]>> Latest UFC Shows[/B][/COLOR]',baseurlwwe+'/category/ufc/',15,mediapath+'welcome.png')
	add_link_dummy(icon, fanart)
	add_link_info('[B][COLOR gold]**[/COLOR][COLOR FFFF051E]SUBMIT A COMMENT OR SUGGESTION [/COLOR][COLOR gold]**[/COLOR][/B]',mediapath+'error.png', fanart)
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]Twitter: @Inside_4ndroid [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'twitter.png', fanart)
	
def WWE_CAT(url):
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]SPORTS ANGEL - CATEGORIES [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'welcome.png', fanart)
	add_link_dummy(icon, fanart)
	addDirMain('[COLOR yellow][B]>> Latest WWE Shows[/B][/COLOR]',baseurlwwe+'/category/wwe/',15,icon)
	addDirMain('[COLOR yellow][B]>> Latest TNA Shows[/B][/COLOR]',baseurlwwe+'/category/tna/',15,icon)
	addDirMain('[COLOR yellow][B]>> Latest RAW Shows[/B][/COLOR]',baseurlwwe+'/category/raw/',15,icon)
	addDirMain('[COLOR yellow][B]>> Latest NXT Shows[/B][/COLOR]',baseurlwwe+'/category/nxt/',15,icon)
	addDirMain('[COLOR yellow][B]>> Latest NJPW Shows[/B][/COLOR]',baseurlwwe+'/category/njpw/',15,icon)
	addDirMain('[COLOR yellow][B]>> Latest Indy Shows[/B][/COLOR]',baseurlwwe+'/category/indy/',15,icon)
	addDirMain('[COLOR yellow][B]>> Latest Smackdown Shows[/B][/COLOR]',baseurlwwe+'/category/smackdown/',15,icon)
	addDirMain('[COLOR yellow][B]>> Latest Main Event Shows[/B][/COLOR]',baseurlwwe+'/category/main-event/',15,icon)
	addDirMain('[COLOR yellow][B]>> Latest Toatal Divas Shows[/B][/COLOR]',baseurlwwe+'/category/wwe-total-divas/',15,icon)
	add_link_dummy(icon, fanart)
	add_link_info('[B][COLOR gold]**[/COLOR][COLOR FFFF051E]SUBMIT A COMMENT OR SUGGESTION [/COLOR][COLOR gold]**[/COLOR][/B]',mediapath+'error.png', fanart)
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]Twitter: @Inside_4ndroid [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'twitter.png', fanart)

def WWE_PPV(url):
	link = open_url(url)
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]SPORTS ANGEL - TITLES [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'welcome.png', fanart)
	add_link_dummy(icon, fanart)
	all_links = regex_get_all(link, '<li class="item-post">', '<span class="vertical-align">')
	for a in all_links:
		name = regex_from_to(a, 'title="', '"').replace("&amp;","&").replace('Watch WWE','').replace('Watch TNA','').replace('Watch ROH','').replace('Watch NJPW','').replace('Watch UFC','').replace('Watch The','').replace('&#8211;','-')
		url = regex_from_to(a, 'href="', '"').replace("&amp;","&")
		thumb = regex_from_to(a, 'src="', '"').replace("&amp;","&")
		nextp = regex_from_to(a, '', '').replace("&amp;","&")
		addDirMain('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name,url,16,thumb)
	add_link_dummy(icon, fanart)
	add_link_info('[B][COLOR gold]**[/COLOR][COLOR FFFF051E]SUBMIT A COMMENT OR SUGGESTION [/COLOR][COLOR gold]**[/COLOR][/B]',mediapath+'error.png', fanart)
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]Twitter: @Inside_4ndroid [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'twitter.png', fanart)
	
def WWE_PPV_LINKS(url):
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]SPORTS ANGEL - PROVIDERS [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'welcome.png', fanart)
	add_link_dummy(icon, fanart)
	link = open_url(url)
	ref = regex_get_all(link,'<div class="entry-content rich-content">','<p class="no-break"')
	match = re.compile('href="(.+?)" class="small cool-blue vision-button" target="_blank">(.+?)</a>',re.DOTALL).findall(str(ref))
	for url,name in match:
		if 'DProtect' in url:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name+' [COLOR FFEDD24B](DailyMotion)[/COLOR]', url, 300, mediapath+'dailymotion.png', fanart, '')
		if 'OProtect' in url:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name+' [COLOR FFEDD24B](OpenLoad)[/COLOR]', url, 300, mediapath+'openload.png', fanart, '')
		if 'LProtect' in url:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name+' [COLOR FFEDD24B](LetWatch)[/COLOR]', url, 300, mediapath+'letwatch.png', fanart, '')
		if 'vidto' in url:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name+' [COLOR FFEDD24B](Vidto.Me)[/COLOR]', url, 300, mediapath+'vidto.png', fanart, '')
		if 'Countdown' in name:
			timeandate = url
			link1 = open_url(timeandate)
			timeuntil = regex_get_all(link1,'tad-bind=until>until</span>','</div></div></div>')
			matcht = re.compile('<span tad-bind=date>(.+?)</span>.+?title=".+?">.+?</a>',re.DOTALL).findall(str(timeuntil))
			for n1 in matcht:
				name = n1
				add_link_info('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name+ '[COLOR FF42F4E2] - USA Time[/COLOR]', mediapath+'welcome.png', fanart)
				link = open_url('http://i4pro.co.uk/kodi/shadownet/other.html')
				all_links = regex_get_all(link, '<div class="ProductImage">', '</div>')
				for a in all_links:
					name = regex_from_to(a, 'alt="', '"').replace("&amp;","&")
					url = regex_from_to(a, 'href="', '"').replace("&amp;","&")
					iconlogo = regex_from_to(a, 'src="', '"').replace("&amp;","&")
					if 'WWE Network' in name:
						add_link_dummy(icon, fanart)
						add_link_info('[B][COLOR gold]WATCH IT LIVE USING THE BELOW LINK[/COLOR][/B]',mediapath+'error.png', fanart)
						add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
				
	add_link_dummy(icon, fanart)
	add_link_info('[B][COLOR gold]**[/COLOR][COLOR FFFF051E]SUBMIT A COMMENT OR SUGGESTION [/COLOR][COLOR gold]**[/COLOR][/B]',mediapath+'error.png', fanart)
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]Twitter: @Inside_4ndroid [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'twitter.png', fanart)

def HOSTS(url):
	if 'DProtect' in url:
		url = url.replace('DProtect.php?File=','http://dailymotion.com/embed/video/')
		PLAYHOSTED(url)
	if 'OProtect' in url:
		url = url.replace('OProtect.php?File=','https://openload.co/embed/')
		PLAYHOSTED(url)
	if 'LProtect' in url:
		url = url.replace('LProtect.php?File=','http://letwatch.to/embed-')
		PLAYHOSTED(url)
	if 'vidto' in url:
		url = url.replace('http://vidto.me/','http://vidto.me/embed-')
		PLAYHOSTED(url)

def SPORTS_CAT(url):
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]SPORTS ANGEL - CATEGORIES [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'welcome.png', fanart)
	add_link_dummy(icon, fanart)
	addDirMain('[COLOR yellow][B]>> All Sports[/B][/COLOR]',u_r_l,4,icon)
	addDirMain('[COLOR yellow][B]>> BT Sports[/B][/COLOR]',u_r_l,5,icon)
	addDirMain('[COLOR yellow][B]>> Sky Sports[/B][/COLOR]',u_r_l,6,icon)
	addDirMain('[COLOR yellow][B]>> SportsNet[/B][/COLOR]',u_r_l,7,icon)
	addDirMain('[COLOR yellow][B]>> TSN Sports[/B][/COLOR]',u_r_l,8,icon)
	addDirMain('[COLOR yellow][B]>> Astro Supersport[/B][/COLOR]',u_r_l,9,icon)
	addDirMain('[COLOR yellow][B]>> Bein Sports[/B][/COLOR]',u_r_l,10,icon)
	addDirMain('[COLOR yellow][B]>> PAC 12 Sports[/B][/COLOR]',u_r_l,11,icon)
	addDirMain('[COLOR yellow][B]>> Other Sports[/B][/COLOR]',u_r_l,12,icon)
	add_link_dummy(icon, fanart)
	add_dir('[B][COLOR gold]>> [/COLOR][COLOR FFFF051E]SUBMIT A COMMENT OR SUGGESTION [/COLOR][/B]', u_r_l, 100, mediapath+'error.png', fanart)
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]Twitter: @Inside_4ndroid [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'twitter.png', fanart)

def SPORTS_ALL():
	content = make_request(online_xml)
	link = open_url('http://shadow-net.org/search.php?search_query=BT')
	all_links = regex_get_all(link, '<div class="ProductImage">', '</div>')
	match = re.compile(xml_regex).findall(content)
	for a in all_links:
		name = regex_from_to(a, 'alt="', '"').replace("&amp;","&")
		url = regex_from_to(a, 'href="', '"').replace("&amp;","&")
		iconlogo = regex_from_to(a, 'src="', '"').replace("&amp;","&")
		if 'Sport 1' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Sport 2' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
	for name,url,thumb in match:
		if 'BT Sport' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, thumb, fanart, '')
	
			
	link = open_url('http://shadow-net.org/search.php?search_query=sky')
	all_links = regex_get_all(link, '<div class="ProductImage">', '</div>')
	match = re.compile(xml_regex).findall(content)
	for a in all_links:
		name = regex_from_to(a, 'alt="', '"').replace("&amp;","&")
		url = regex_from_to(a, 'href="', '"').replace("&amp;","&")
		iconlogo = regex_from_to(a, 'src="', '"').replace("&amp;","&")
		if 'Sky Sports News' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Sky Sports 5' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Sky Sports F1' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Sky Sports1' in name:
			name = name.replace('Sky Sports1','Sky Sports 1')
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
	for name,url,thumb in match:
		if 'Sky Sport' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, thumb, fanart, '')

	link = open_url('http://shadow-net.org/search.php?search_query=sportsnet')
	all_links = regex_get_all(link, '<div class="ProductImage">', '</div>')
	for a in all_links:
		name = regex_from_to(a, 'alt="', '"').replace("&amp;","&")
		url = regex_from_to(a, 'href="', '"').replace("&amp;","&")
		iconlogo = regex_from_to(a, 'src="', '"').replace("&amp;","&")
		if 'Sportsnet' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')

	link = open_url('http://shadow-net.org/search.php?search_query=TSN')
	all_links = regex_get_all(link, '<div class="ProductImage">', '</div>')
	for a in all_links:
		name = regex_from_to(a, 'alt="', '"').replace("&amp;","&")
		url = regex_from_to(a, 'href="', '"').replace("&amp;","&")
		iconlogo = regex_from_to(a, 'src="', '"').replace("&amp;","&")
		if 'TSN' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')

	link = open_url('http://shadow-net.org/search.php?search_query=Astro')
	all_links = regex_get_all(link, '<div class="ProductImage">', '</div>')
	for a in all_links:
		name = regex_from_to(a, 'alt="', '"').replace("&amp;","&")
		url = regex_from_to(a, 'href="', '"').replace("&amp;","&")
		iconlogo = regex_from_to(a, 'src="', '"').replace("&amp;","&")
		if 'Astro' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')

	link = open_url('http://shadow-net.org/search.php?search_query=Bein')
	match = re.compile(xml_regex).findall(content)
	for name,url,thumb in match:
		if 'BeIn' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, thumb, fanart, '')

	link = open_url('http://shadow-net.org/search.php?search_query=Pac')
	all_links = regex_get_all(link, '<div class="ProductImage">', '</div>')
	for a in all_links:
		name = regex_from_to(a, 'alt="', '"').replace("&amp;","&")
		url = regex_from_to(a, 'href="', '"').replace("&amp;","&")
		iconlogo = regex_from_to(a, 'src="', '"').replace("&amp;","&")
		if 'Pac 12 National' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Pac 12 Arizona' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Pac 12 Los Angeles' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Pac 12 Mountain' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Pac 12 Oregon' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Pac 12 Washington' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
	
	opener = urllib.FancyURLopener({})
	response = opener.open(online_other)
	online_m3u = response.read()
	response.close()	
	content = online_m3u
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 400, icon, fanart, '')
	opener = urllib.FancyURLopener({})
	response = opener.open(online_basics)
	online_m3u = response.read()
	response.close()	
	content = online_m3u
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		url=url.replace('ipsatv',first+'iptv').replace('9090','8127')
		add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 400, icon, fanart, '')
		
def SPORTS_OTHER():
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]SPORTS ANGEL - OTHER SPORTS [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'welcome.png', fanart)
	add_link_dummy(icon, fanart)
	link = open_url('http://i4pro.co.uk/kodi/shadownet/other.html')
	all_links = regex_get_all(link, '<div class="ProductImage">', '</div>')
	for a in all_links:
		name = regex_from_to(a, 'alt="', '"').replace("&amp;","&")
		url = regex_from_to(a, 'href="', '"').replace("&amp;","&")
		iconlogo = regex_from_to(a, 'src="', '"').replace("&amp;","&")
		if 'At The Races' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'BoxNation' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Chelsea TV' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'ESPN 2' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'ESPN US' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Eurosport France' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Fight Network' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Golf Channel' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Manchester' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'NBA TV' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Premier Sports' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'PTV Sports' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Real Madrid' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Setanta Ireland' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'WWE Network' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
	opener = urllib.FancyURLopener({})
	response = opener.open(online_other)
	online_m3u = response.read()
	response.close()	
	content = online_m3u
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 400, icon, fanart, '')
	add_link_dummy(icon, fanart)
	add_link_info('[B][COLOR gold]**[/COLOR][COLOR FFFF051E]SUBMIT A COMMENT OR SUGGESTION [/COLOR][COLOR gold]**[/COLOR][/B]',mediapath+'error.png', fanart)
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]Twitter: @Inside_4ndroid [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'twitter.png', fanart)

def SPORTS_PAC12():
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]SPORTS ANGEL - PAC 12 [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'welcome.png', fanart)
	add_link_dummy(icon, fanart)
	link = open_url('http://shadow-net.org/search.php?search_query=Pac')
	all_links = regex_get_all(link, '<div class="ProductImage">', '</div>')
	for a in all_links:
		name = regex_from_to(a, 'alt="', '"').replace("&amp;","&")
		url = regex_from_to(a, 'href="', '"').replace("&amp;","&")
		iconlogo = regex_from_to(a, 'src="', '"').replace("&amp;","&")
		if 'Pac 12 National' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Pac 12 Arizona' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Pac 12 Los Angeles' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Pac 12 Mountain' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Pac 12 Oregon' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Pac 12 Washington' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
	add_link_dummy(icon, fanart)
	add_link_info('[B][COLOR gold]**[/COLOR][COLOR FFFF051E]SUBMIT A COMMENT OR SUGGESTION [/COLOR][COLOR gold]**[/COLOR][/B]',mediapath+'error.png', fanart)
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]Twitter: @Inside_4ndroid [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'twitter.png', fanart)

def SPORTS_BEIN():
	content = make_request(online_xml)
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]SPORTS ANGEL - BEIN [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'welcome.png', fanart)
	add_link_dummy(icon, fanart)
	link = open_url('http://shadow-net.org/search.php?search_query=Bein')
	match = re.compile(xml_regex).findall(content)
	for name,url,thumb in match:
		if 'BeIn' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, thumb, fanart, '')
	add_link_dummy(icon, fanart)
	add_link_info('[B][COLOR gold]**[/COLOR][COLOR FFFF051E]SUBMIT A COMMENT OR SUGGESTION [/COLOR][COLOR gold]**[/COLOR][/B]',mediapath+'error.png', fanart)
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]Twitter: @Inside_4ndroid [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'twitter.png', fanart)

def SPORTS_ASTRO():
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]SPORTS ANGEL - ASTRO SUPERSPORT [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'welcome.png', fanart)
	add_link_dummy(icon, fanart)
	link = open_url('http://shadow-net.org/search.php?search_query=Astro')
	all_links = regex_get_all(link, '<div class="ProductImage">', '</div>')
	for a in all_links:
		name = regex_from_to(a, 'alt="', '"').replace("&amp;","&")
		url = regex_from_to(a, 'href="', '"').replace("&amp;","&")
		iconlogo = regex_from_to(a, 'src="', '"').replace("&amp;","&")
		if 'Astro' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
	add_link_dummy(icon, fanart)
	add_link_info('[B][COLOR gold]**[/COLOR][COLOR FFFF051E]SUBMIT A COMMENT OR SUGGESTION [/COLOR][COLOR gold]**[/COLOR][/B]',mediapath+'error.png', fanart)
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]Twitter: @Inside_4ndroid [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'twitter.png', fanart)

def SPORTS_TSN():
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]SPORTS ANGEL - TSN [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'welcome.png', fanart)
	add_link_dummy(icon, fanart)
	link = open_url('http://shadow-net.org/search.php?search_query=TSN')
	all_links = regex_get_all(link, '<div class="ProductImage">', '</div>')
	for a in all_links:
		name = regex_from_to(a, 'alt="', '"').replace("&amp;","&")
		url = regex_from_to(a, 'href="', '"').replace("&amp;","&")
		iconlogo = regex_from_to(a, 'src="', '"').replace("&amp;","&")
		if 'TSN' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
	opener = urllib.FancyURLopener({})
	response = opener.open(online_basics)
	online_m3u = response.read()
	response.close()	
	content = online_m3u
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		if 'TSN' in name:
			url=url.replace('ipsatv',first+'iptv').replace('9090','8127')
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 400, icon, fanart, '')
	add_link_dummy(icon, fanart)
	add_link_info('[B][COLOR gold]**[/COLOR][COLOR FFFF051E]SUBMIT A COMMENT OR SUGGESTION [/COLOR][COLOR gold]**[/COLOR][/B]',mediapath+'error.png', fanart)
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]Twitter: @Inside_4ndroid [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'twitter.png', fanart)

def SPORTS_SPORTSNET():
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]SPORTS ANGEL - SPORTSNET [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'welcome.png', fanart)
	add_link_dummy(icon, fanart)
	link = open_url('http://shadow-net.org/search.php?search_query=sportsnet')
	all_links = regex_get_all(link, '<div class="ProductImage">', '</div>')
	for a in all_links:
		name = regex_from_to(a, 'alt="', '"').replace("&amp;","&")
		url = regex_from_to(a, 'href="', '"').replace("&amp;","&")
		iconlogo = regex_from_to(a, 'src="', '"').replace("&amp;","&")
		if 'Sportsnet' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
	add_link_dummy(icon, fanart)
	add_link_info('[B][COLOR gold]**[/COLOR][COLOR FFFF051E]SUBMIT A COMMENT OR SUGGESTION [/COLOR][COLOR gold]**[/COLOR][/B]',mediapath+'error.png', fanart)
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]Twitter: @Inside_4ndroid [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'twitter.png', fanart)

def SPORTS_SKY():
	content = make_request(online_xml)
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]SPORTS ANGEL - SKY SPORTS [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'welcome.png', fanart)
	add_link_dummy(icon, fanart)
	link = open_url('http://shadow-net.org/search.php?search_query=sky')
	all_links = regex_get_all(link, '<div class="ProductImage">', '</div>')
	match = re.compile(xml_regex).findall(content)
	for a in all_links:
		name = regex_from_to(a, 'alt="', '"').replace("&amp;","&")
		url = regex_from_to(a, 'href="', '"').replace("&amp;","&")
		iconlogo = regex_from_to(a, 'src="', '"').replace("&amp;","&")
		if 'Sky Sports News' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Sky Sports 5' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Sky Sports F1' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Sky Sports1' in name:
			name = name.replace('Sky Sports1','Sky Sports 1')
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
	for name,url,thumb in match:
		if 'Sky Sport' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, thumb, fanart, '')
	opener = urllib.FancyURLopener({})
	response = opener.open(online_basics)
	online_m3u = response.read()
	response.close()	
	content = online_m3u
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		if 'Sky Sports' in name:
			url=url.replace('ipsatv',first+'iptv').replace('9090','8127')
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 400, icon, fanart, '')
	add_link_dummy(icon, fanart)
	add_link_info('[B][COLOR gold]**[/COLOR][COLOR FFFF051E]SUBMIT A COMMENT OR SUGGESTION [/COLOR][COLOR gold]**[/COLOR][/B]',mediapath+'error.png', fanart)
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]Twitter: @Inside_4ndroid [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'twitter.png', fanart)

def SPORTS_BT():
	content = make_request(online_xml)
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]SPORTS ANGEL - BT SPORTS [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'welcome.png', fanart)
	add_link_dummy(icon, fanart)
	link = open_url('http://shadow-net.org/search.php?search_query=BT')
	all_links = regex_get_all(link, '<div class="ProductImage">', '</div>')
	match = re.compile(xml_regex).findall(content)
	for a in all_links:
		name = regex_from_to(a, 'alt="', '"').replace("&amp;","&")
		url = regex_from_to(a, 'href="', '"').replace("&amp;","&")
		iconlogo = regex_from_to(a, 'src="', '"').replace("&amp;","&")
		if 'Sport 1' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
		if 'Sport 2' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconlogo, fanart, '')
	for name,url,thumb in match:
		if 'BT Sport' in name:
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, thumb, fanart, '')
	opener = urllib.FancyURLopener({})
	response = opener.open(online_basics)
	online_m3u = response.read()
	response.close()	
	content = online_m3u
	match = re.compile(m3u_regex).findall(content)
	for thumb, name, url in match:
		if 'BT Sport' in name:
			url=url.replace('ipsatv',first+'iptv').replace('9090','8127')
			add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 400, icon, fanart, '')
	add_link_dummy(icon, fanart)
	add_link_info('[B][COLOR gold]**[/COLOR][COLOR FFFF051E]SUBMIT A COMMENT OR SUGGESTION [/COLOR][COLOR gold]**[/COLOR][/B]',mediapath+'error.png', fanart)
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]Twitter: @Inside_4ndroid [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'twitter.png', fanart)

def PAGE_INDEX(url):
	add_link_info('[B][COLOR gold]** [/COLOR][COLOR FFF442BC]WELCOME TO SPORTS ANGEL [/COLOR][COLOR gold]**[/COLOR][/B]', mediapath+'welcome.png', fanart)
	add_link_dummy(icon, fanart)
	link = open_url(url)
	match=re.compile('<a href="(.+?)"  ><img src="(.+?)" alt="(.+?)" /></a>',re.DOTALL).findall(link)
	for url,iconimage,name in match:
		add_link('[I][B][COLOR FF42F4E2] %s [/COLOR][/B][/I]' %name, url, 200, iconimage, fanart, '')
	np = re.compile('<div class="FloatRight"><a href="(.+?)"',re.DOTALL).findall(link)
	for url in np:
		add_link_dummy(icon, fanart)
		add_dir('[B][COLOR gold]Next Page  >>>[/COLOR][/B]',url,2,mediapath+'next.png',fanart)
		url=url.replace("&amp;","&")
	pr = re.compile('<div class="FloatLeft"><a href="(.+?)"',re.DOTALL).findall(link)
	for url in pr:
		add_dir('[B][COLOR gold]<<<  Previous Page[/COLOR][/B]',url,2,mediapath+'prev.png',fanart)
		url=url.replace("&amp;","&")
	add_link_dummy(icon, fanart)
	add_dir('[B][COLOR limegreen]>> [/COLOR][COLOR FFFF051E]SUBMIT A COMMENT OR SUGGESTION[/COLOR][/B]', u_r_l, 100, mediapath+'error.png', fanart)
	add_link_info('[B][COLOR limegreen]** [/COLOR][COLOR FFF442BC]Twitter: @Inside_4ndroid [/COLOR][COLOR limegreen]**[/COLOR][/B]', mediapath+'twitter.png', fanart)

def PLAYLINK(name,url,iconimage):
	try:
		OPEN = open_url(url)
		url = re.compile('<source src="(.+?)"',re.DOTALL).findall(OPEN)[1]
		item = xbmcgui.ListItem(name, path = url)
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
	except:
		liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
		liz.setInfo(type='Video', infoLabels={'Title':description})
		liz.setProperty("IsPlayable","true")
		liz.setPath(str(url))
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)

def playmediaurl(url):
	media_url = url
	item = xbmcgui.ListItem(name, path = media_url)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
	return

def PLAYHOSTED(url):
	try:
		headers = {}
		headers['User-Agent'] = User_Agent
		link = requests.get(url, headers=headers, verify=False,allow_redirects=True)
		link = link.url
		link = urlresolver.HostedMediaFile(link).resolve()
		liz = xbmcgui.ListItem(name, iconImage='DefaultVideo.png', thumbnailImage=iconimage)
		liz.setInfo(type='Video', infoLabels={'Title':description})
		liz.setProperty("IsPlayable","true")
		liz.setPath(str(link))
		xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
	except:
		xbmcgui.Dialog().ok('SPORTS ANGEL','WOOOPSS!! Something went very wronng - Inside4ndroid')

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

def addDirMain(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setProperty('fanart_image', fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def add_dir(name, url, mode, iconimage, fanart):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage = "DefaultFolder.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	if ('youtube.com/user/' in url) or ('youtube.com/channel/' in url) or ('youtube/user/' in url) or ('youtube/channel/' in url):
		u = 'plugin://plugin.video.youtube/%s/%s/' % (url.split( '/' )[-2], url.split( '/' )[-1])
		ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
		return ok		
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
	return ok

def add_link(name, url, mode, iconimage, fanart, description):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage) + "&description=" + str(description)
	liz = xbmcgui.ListItem(name, iconImage = icon, thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name, 'plot': description  } )
	liz.setProperty('fanart_image', fanart)
	liz.setProperty('IsPlayable', 'true') 
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = False)  

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

def open_url(url):
	try:
		net.set_cookies(cookie_file)
		link = net.http_GET(url).content
		link = cleanHex(link)
		return link
	except:
		try:
			cl.createCookie(url,cookie_file,'Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0')
			net.set_cookies(cookie_file)
			link = net.http_GET(url).content
			link = cleanHex(link)
			return link
		except:
			try:
				headers = {}
				headers['User-Agent'] = User_Agent
				link = s.get(url, headers=headers, allow_redirects=True).text
				link = link.encode('ascii', 'ignore')
				return link
			except:pass

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
		
params=get_params()
url=None
name=None
iconimage=None
mode=None
description=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print ""
        main()

elif mode == 1:
	play_video(url)

elif mode == 2:
	PAGE_INDEX(url)
	
elif mode == 3:
	SPORTS_CAT(url)

elif mode == 4:
	SPORTS_ALL()

elif mode == 5:
	SPORTS_BT()

elif mode == 6:
	SPORTS_SKY()

elif mode == 7:
	SPORTS_SPORTSNET()

elif mode == 8:
	SPORTS_TSN()

elif mode == 9:
	SPORTS_ASTRO()

elif mode == 10:
	SPORTS_BEIN()

elif mode == 11:
	SPORTS_PAC12()

elif mode == 12:
	SPORTS_OTHER()

elif mode == 14:
	WWE_CAT(url)

elif mode == 15:
	WWE_PPV(url)

elif mode == 16:
	WWE_PPV_LINKS(url)
	
elif mode == 200:
	PLAYLINK(name,url,iconimage)

elif mode == 300:
	HOSTS(url)

elif mode == 400:
	playmediaurl(url)
	
xbmcplugin.endOfDirectory(plugin_handle)