# -*- coding: utf-8 -*-
import sys
l1l11l_opy_ = sys.version_info [0] == 2
l11ll1_opy_ = 2048
l1l1ll_opy_ = 7
def l1ll1l_opy_ (ll_opy_):
	global l1l1_opy_
	l1ll1_opy_ = ord (ll_opy_ [-1])
	l1l1l1_opy_ = ll_opy_ [:-1]
	l11l_opy_ = l1ll1_opy_ % len (l1l1l1_opy_)
	l111_opy_ = l1l1l1_opy_ [:l11l_opy_] + l1l1l1_opy_ [l11l_opy_:]
	if l1l11l_opy_:
		l11l1l_opy_ = unicode () .join ([unichr (ord (char) - l11ll1_opy_ - (l1lll1_opy_ + l1ll1_opy_) % l1l1ll_opy_) for l1lll1_opy_, char in enumerate (l111_opy_)])
	else:
		l11l1l_opy_ = str () .join ([chr (ord (char) - l11ll1_opy_ - (l1lll1_opy_ + l1ll1_opy_) % l1l1ll_opy_) for l1lll1_opy_, char in enumerate (l111_opy_)])
	return eval (l11l1l_opy_)
import urllib, urllib2, sys, re, os, unicodedata
import xbmc, xbmcgui, xbmcplugin, xbmcaddon, xbmcvfs
l1lll1l_opy_ = int(sys.argv[1])
mysettings = xbmcaddon.Addon(id = l1ll1l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡩࡨ࡭ࡴࡷࠩࠀ"))
l1_opy_ = mysettings.getAddonInfo(l1ll1l_opy_ (u"ࠬࡶࡲࡰࡨ࡬ࡰࡪ࠭ࠁ"))
home = mysettings.getAddonInfo(l1ll1l_opy_ (u"࠭ࡰࡢࡶ࡫ࠫࠂ"))
l11l1_opy_ = xbmc.translatePath(os.path.join(home, l1ll1l_opy_ (u"ࠧࡧࡣࡱࡥࡷࡺ࠮࡫ࡲࡪࠫࠃ")))
l111l1_opy_ = xbmc.translatePath(os.path.join(home, l1ll1l_opy_ (u"ࠨ࡫ࡦࡳࡳ࠴ࡰ࡯ࡩࠪࠄ")))
path   = xbmcaddon.Addon().getAddonInfo(l1ll1l_opy_ (u"ࠩࡳࡥࡹ࡮ࠧࠅ")).decode(l1ll1l_opy_ (u"ࠥࡹࡹ࡬࠭࠹ࠤࠆ"))
l11lll_opy_ = l1ll1l_opy_ (u"ࠫࡹࡼࡧ࠮࡮ࡲ࡫ࡴࡃ࡛࡝ࠩࠥࡡ࠭࠴ࠪࡀࠫ࡞ࡠࠬࠨ࡝ࠨࠇ")
l1l1l_opy_ = l1ll1l_opy_ (u"ࠬࠩࠨ࠯࠭ࡂ࠭࠱࠮࠮ࠬࠫ࡟ࡷ࠯࠮࠮ࠬࠫ࡟ࡷ࠯࠭ࠈ")
l11111_opy_ = l1ll1l_opy_ (u"࠭ࡨࡵࡶࡳ࠾࠴࠵ࡩ࠵ࡲࡵࡳ࠳ࡩ࡯࠯ࡷ࡮࠳ࡰࡵࡤࡪ࠱࡬ࡴࡹࡼ࠯࡭࡫ࡶࡸ࡮ࡴࡧࡴ࠰ࡰ࠷ࡺ࠭ࠉ")
l1111l_opy_ = xbmc.executebuiltin
def l1ll1ll_opy_(s):
	return l1ll1l_opy_ (u"ࠧࠨࠊ").join((c for c in unicodedata.normalize(l1ll1l_opy_ (u"ࠨࡐࡉࡈࠬࠋ"), s.decode(l1ll1l_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨࠌ"))) if unicodedata.category(c) != l1ll1l_opy_ (u"ࠪࡑࡳ࠭ࠍ")))
def l1lll_opy_(file):
    try:
        f = open(file, l1ll1l_opy_ (u"ࠫࡷ࠭ࠎ"))
        content = f.read()
        f.close()
        return content
    except:
        pass
def main():
	try:
		opener = urllib.FancyURLopener({})
		response = opener.open(l11111_opy_)
		l1l111_opy_ = response.read()
		response.close()
		content = l1l111_opy_
		match = re.compile(l1l1l_opy_).findall(content)
		for l11ll_opy_, name, url in match:
			try:
				l1ll11_opy_(name, url, l11ll_opy_)
				xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_TITLE_IGNORE_THE)
			except:
				pass
	except:
		l1ll_opy_(query)
def l1ll11_opy_(name, url, l11ll_opy_):
	name = re.sub(l1ll1l_opy_ (u"ࠬࡢࡳࠬࠩࠏ"), l1ll1l_opy_ (u"࠭ࠠࠨࠐ"), name).strip()
	url = url.replace(l1ll1l_opy_ (u"ࠧࠣࠩࠑ"), l1ll1l_opy_ (u"ࠨࠢࠪࠒ")).replace(l1ll1l_opy_ (u"ࠩࠩࡥࡲࡶ࠻ࠨࠓ"), l1ll1l_opy_ (u"ࠪࠪࠬࠔ")).replace(l1ll1l_opy_ (u"ࠫࠫࡧ࡭ࡱ࠽ࠪࠕ"), l1ll1l_opy_ (u"ࠬࠬࠧࠖ")).strip()
	url = url
	if l1ll1l_opy_ (u"࠭ࡌࡆࡇࡆࡌࡊࡘࠧࠗ") in url:
		l1ll1l1_opy_(l1ll1l_opy_ (u"ࠧ࡜ࡋࡠ࡟ࡇࡣ࡛ࡄࡑࡏࡓࡗࠦࡢ࡭ࡷࡨࡡࠥࠫࡳࠡ࡝࠲ࡇࡔࡒࡏࡓ࡟࡞࠳ࡇࡣ࡛࠰ࡋࡠࠫ࠘") %name, url, 1, l111l1_opy_, l11l1_opy_)
def l1lll11_opy_(url):
	url = url.replace(l1ll1l_opy_ (u"ࠨࡈࡘࡇࡐ࠵ࡏࡇࡈ࠲࡝ࡔ࡛࠯ࡍࡇࡈࡇࡍࡋࡒࠨ࠙"),l1ll1l_opy_ (u"ࠩ࡫ࡨࡱ࡯ࡶࡦࡶࡹ࠲ࡩ࡫࠺࠹࠲࠳࠴࠴ࡲࡩࡷࡧ࠲ࡘࡴࡳࡡࡴࡱ࠶࠳࡙ࡵ࡭ࡢࡵࡲ࠷ࠬࠚ"))
	l1ll11l_opy_ = url
	item = xbmcgui.ListItem(name, path = l1ll1l_opy_ (u"ࠪࡴࡱࡻࡧࡪࡰ࠽࠳࠴ࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲࡫࠺࡭ࡕࡧࡶࡸࡪࡸ࠯ࡀࡵࡷࡶࡪࡧ࡭ࡵࡻࡳࡩࡂ࡚ࡓࡅࡑ࡚ࡒࡑࡕࡁࡅࡇࡕࠪࡳࡧ࡭ࡦ࠿࡞ࡆࡢࡡࡃࡐࡎࡒࡖࠥࡲࡩ࡮ࡧࡪࡶࡪ࡫࡮࡞ࡇࡆࡋ࡚ࠥࡖ࡜࠱ࡆࡓࡑࡕࡒ࡞࡝࠲ࡆࡢࠬࡵࡳ࡮ࡀࠫࠛ") +l1ll11l_opy_)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
	return
def l1ll_opy_(query=None, id=l1ll1l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡩࡨ࡭ࡴࡷࠩࠜ")):
	xbmcgui.Dialog().ok(l1ll1l_opy_ (u"ࠬࡡࡂ࡞࡝ࡆࡓࡑࡕࡒࠡ࡮࡬ࡱࡪ࡭ࡲࡦࡧࡱࡡࡊࡉࡇࠡ࡝࠲ࡇࡔࡒࡏࡓ࡟࡞ࡇࡔࡒࡏࡓࠢࡪࡳࡱࡪ࡝ࡕࡘࠣ࡟࠴ࡉࡏࡍࡑࡕࡡࡠ࠵ࡂ࡞ࠩࠝ"),l1ll1l_opy_ (u"࠭ࡔࡩࡧࠣࡔࡦࡹࡳࡸࡱࡵࡨࠥ࡯ࡳࠡ࡫ࡱࡧࡴࡸࡲࡦࡥࡷࠤࡴࡸࠠࡺࡱࡸࠤ࡭ࡧࡶࡦࠢࡱࡳࡹࠦࡧࡰࡶࠣࡽࡴࡻࡲࠡࡲࡤࡷࡸࡽ࡯ࡳࡦࠣࡽࡪࡺࠠࡑ࡮ࡨࡥࡸ࡫ࠠࡧࡱ࡯ࡰࡴࡽࠠࡵࡪࡨࠤ࡮ࡴࡳࡵࡴࡸࡧࡹ࡯࡯࡯ࡵࠣ࡭ࡳࠦࡴࡩࡧࠣࡷࡪࡺࡴࡪࡰࡪࡷࠥࡽࡩ࡯ࡦࡲࡻࠥࡺ࡯ࠡࡩࡤ࡭ࡳࠦࡡࡤࡥࡨࡷࡸࠦࡴࡰࠢࡷ࡬࡮ࡹࠠࡨࡴࡨࡥࡹࠦࡦࡳࡧࡨࠤࡦࡪࡤࡰࡰ࠱ࠫࠞ"))
	l1111l_opy_(l1ll1l_opy_ (u"ࠧࡂࡦࡧࡳࡳ࠴ࡏࡱࡧࡱࡗࡪࡺࡴࡪࡰࡪࡷ࠭ࠫࡳࠪࠩࠟ") % id)
def l1llll_opy_():
        l1111_opy_=[]
        l1l11_opy_=sys.argv[2]
        if len(l1l11_opy_)>=2:
                params=sys.argv[2]
                l1llll1_opy_=params.replace(l1ll1l_opy_ (u"ࠨࡁࠪࠠ"),l1ll1l_opy_ (u"ࠩࠪࠡ"))
                if (params[len(params)-1]==l1ll1l_opy_ (u"ࠪ࠳ࠬࠢ")):
                        params=params[0:len(params)-2]
                l1l_opy_=l1llll1_opy_.split(l1ll1l_opy_ (u"ࠫࠫ࠭ࠣ"))
                l1111_opy_={}
                for i in range(len(l1l_opy_)):
                        l11_opy_={}
                        l11_opy_=l1l_opy_[i].split(l1ll1l_opy_ (u"ࠬࡃࠧࠤ"))
                        if (len(l11_opy_))==2:
                                l1111_opy_[l11_opy_[0]]=l11_opy_[1]
        return l1111_opy_
def l11l11_opy_(name, url, mode, l111l_opy_, l11l1_opy_):
	u = sys.argv[0] + l1ll1l_opy_ (u"ࠨ࠿ࡶࡴ࡯ࡁࠧࠥ") + urllib.quote_plus(url) + l1ll1l_opy_ (u"ࠢࠧ࡯ࡲࡨࡪࡃࠢࠦ") + str(mode) + l1ll1l_opy_ (u"ࠣࠨࡱࡥࡲ࡫࠽ࠣࠧ") + urllib.quote_plus(name) + l1ll1l_opy_ (u"ࠤࠩ࡭ࡨࡵ࡮ࡪ࡯ࡤ࡫ࡪࡃࠢࠨ") + urllib.quote_plus(l111l_opy_)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage = l1ll1l_opy_ (u"ࠥࡈࡪ࡬ࡡࡶ࡮ࡷࡊࡴࡲࡤࡦࡴ࠱ࡴࡳ࡭ࠢࠩ"), thumbnailImage = l111l_opy_)
	liz.setInfo( type = l1ll1l_opy_ (u"࡛ࠦ࡯ࡤࡦࡱࠥࠪ"), infoLabels = { l1ll1l_opy_ (u"࡚ࠧࡩࡵ࡮ࡨࠦࠫ"): name } )
	liz.setProperty(l1ll1l_opy_ (u"࠭ࡦࡢࡰࡤࡶࡹࡥࡩ࡮ࡣࡪࡩࠬࠬ"), l11l1_opy_)
	if (l1ll1l_opy_ (u"ࠧࡺࡱࡸࡸࡺࡨࡥ࠯ࡥࡲࡱ࠴ࡻࡳࡦࡴ࠲ࠫ࠭") in url) or (l1ll1l_opy_ (u"ࠨࡻࡲࡹࡹࡻࡢࡦ࠰ࡦࡳࡲ࠵ࡣࡩࡣࡱࡲࡪࡲ࠯ࠨ࠮") in url) or (l1ll1l_opy_ (u"ࠩࡼࡳࡺࡺࡵࡣࡧ࠲ࡹࡸ࡫ࡲ࠰ࠩ࠯") in url) or (l1ll1l_opy_ (u"ࠪࡽࡴࡻࡴࡶࡤࡨ࠳ࡨ࡮ࡡ࡯ࡰࡨࡰ࠴࠭࠰") in url):
		u = l1ll1l_opy_ (u"ࠫࡵࡲࡵࡨ࡫ࡱ࠾࠴࠵ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳ࡿ࡯ࡶࡶࡸࡦࡪ࠵ࠥࡴ࠱ࠨࡷ࠴࠭࠱") % (url.split( l1ll1l_opy_ (u"ࠬ࠵ࠧ࠲") )[-2], url.split( l1ll1l_opy_ (u"࠭࠯ࠨ࠳") )[-1])
		ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
		return ok
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
	return ok
def l1ll1l1_opy_(name, url, mode, l111l_opy_, l11l1_opy_):
	u = sys.argv[0] + l1ll1l_opy_ (u"ࠢࡀࡷࡵࡰࡂࠨ࠴") + urllib.quote_plus(url) + l1ll1l_opy_ (u"ࠣࠨࡰࡳࡩ࡫࠽ࠣ࠵") + str(mode) + l1ll1l_opy_ (u"ࠤࠩࡲࡦࡳࡥ࠾ࠤ࠶") + urllib.quote_plus(name) + l1ll1l_opy_ (u"ࠥࠪ࡮ࡩ࡯࡯࡫ࡰࡥ࡬࡫࠽ࠣ࠷") + urllib.quote_plus(l111l_opy_)
	liz = xbmcgui.ListItem(name, iconImage = l1ll1l_opy_ (u"ࠦࡉ࡫ࡦࡢࡷ࡯ࡸ࡛࡯ࡤࡦࡱ࠱ࡴࡳ࡭ࠢ࠸"), thumbnailImage = l111l_opy_)
	liz.setInfo( type = l1ll1l_opy_ (u"ࠧ࡜ࡩࡥࡧࡲࠦ࠹"), infoLabels = { l1ll1l_opy_ (u"ࠨࡔࡪࡶ࡯ࡩࠧ࠺"): name } )
	liz.setProperty(l1ll1l_opy_ (u"ࠧࡧࡣࡱࡥࡷࡺ࡟ࡪ࡯ࡤ࡫ࡪ࠭࠻"), l11l1_opy_)
	liz.setProperty(l1ll1l_opy_ (u"ࠨࡋࡶࡔࡱࡧࡹࡢࡤ࡯ࡩࠬ࠼"), l1ll1l_opy_ (u"ࠩࡷࡶࡺ࡫ࠧ࠽"))
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz)
def l111ll_opy_(l111l_opy_, l11l1_opy_):
	u = sys.argv[0] + l1ll1l_opy_ (u"ࠥࠪ࡮ࡩ࡯࡯࡫ࡰࡥ࡬࡫࠽ࠣ࠾") + urllib.quote_plus(l111l_opy_)
	liz = xbmcgui.ListItem(iconImage = l1ll1l_opy_ (u"ࠦࡉ࡫ࡦࡢࡷ࡯ࡸ࡛࡯ࡤࡦࡱ࠱ࡴࡳ࡭ࠢ࠿"), thumbnailImage = l111l_opy_)
	liz.setProperty(l1ll1l_opy_ (u"ࠬ࡬ࡡ࡯ࡣࡵࡸࡤ࡯࡭ࡢࡩࡨࠫࡀ"), l11l1_opy_)
	liz.setProperty(l1ll1l_opy_ (u"࠭ࡉࡴࡒ࡯ࡥࡾࡧࡢ࡭ࡧࠪࡁ"), l1ll1l_opy_ (u"ࠧࡧࡣ࡯ࡷࡪ࠭ࡂ"))
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz)
def l1lllll_opy_(name, l111l_opy_, l11l1_opy_):
	u = sys.argv[0] + l1ll1l_opy_ (u"ࠣࠨࡱࡥࡲ࡫࠽ࠣࡃ") + urllib.quote_plus(name) + l1ll1l_opy_ (u"ࠤࠩ࡭ࡨࡵ࡮ࡪ࡯ࡤ࡫ࡪࡃࠢࡄ") + urllib.quote_plus(l111l_opy_)
	liz = xbmcgui.ListItem(name, iconImage = l1ll1l_opy_ (u"ࠥࡈࡪ࡬ࡡࡶ࡮ࡷ࡚࡮ࡪࡥࡰ࠰ࡳࡲ࡬ࠨࡅ"), thumbnailImage = l111l_opy_)
	liz.setInfo( type = l1ll1l_opy_ (u"࡛ࠦ࡯ࡤࡦࡱࠥࡆ"), infoLabels = { l1ll1l_opy_ (u"࡚ࠧࡩࡵ࡮ࡨࠦࡇ"): name } )
	liz.setProperty(l1ll1l_opy_ (u"࠭ࡦࡢࡰࡤࡶࡹࡥࡩ࡮ࡣࡪࡩࠬࡈ"), l11l1_opy_)
	liz.setProperty(l1ll1l_opy_ (u"ࠧࡊࡵࡓࡰࡦࡿࡡࡣ࡮ࡨࠫࡉ"), l1ll1l_opy_ (u"ࠨࡨࡤࡰࡸ࡫ࠧࡊ"))
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz)
params=l1llll_opy_()
url=None
name=None
l111l_opy_=None
mode=None
description=None
query=None
try:
        url=urllib.unquote_plus(params[l1ll1l_opy_ (u"ࠤࡸࡶࡱࠨࡋ")])
except:
        pass
try:
        name=urllib.unquote_plus(params[l1ll1l_opy_ (u"ࠥࡲࡦࡳࡥࠣࡌ")])
except:
        pass
try:
       query=urllib.unquote_plus(params[l1ll1l_opy_ (u"ࠦࡶࡻࡥࡳࡻࠥࡍ")])
except:
        pass
try:
        l111l_opy_=urllib.unquote_plus(params[l1ll1l_opy_ (u"ࠧ࡯ࡣࡰࡰ࡬ࡱࡦ࡭ࡥࠣࡎ")])
except:
        pass
try:
        mode=int(params[l1ll1l_opy_ (u"ࠨ࡭ࡰࡦࡨࠦࡏ")])
except:
        pass
print l1ll1l_opy_ (u"ࠢࡎࡱࡧࡩ࠿ࠦࠢࡐ")+str(mode)
print l1ll1l_opy_ (u"ࠣࡗࡕࡐ࠿ࠦࠢࡑ")+str(url)
print l1ll1l_opy_ (u"ࠤࡑࡥࡲ࡫࠺ࠡࠤࡒ")+str(name)
if mode==None or url==None or len(url)<1:
        print l1ll1l_opy_ (u"ࠥࠦࡓ")
        main()
elif mode == 1:
	l1lll11_opy_(url)
xbmcplugin.endOfDirectory(l1lll1l_opy_)