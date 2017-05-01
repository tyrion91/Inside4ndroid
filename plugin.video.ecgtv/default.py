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
	l1ll1l1_opy_(l1ll1l_opy_ (u"࡛࠭ࡊ࡟࡞ࡆࡢࡡࡃࡐࡎࡒࡖࠥࡨ࡬ࡶࡧࡠࠤࠪࡹࠠ࡜࠱ࡆࡓࡑࡕࡒ࡞࡝࠲ࡆࡢࡡ࠯ࡊ࡟ࠪࠗ") %name, url, 1, l111l1_opy_, l11l1_opy_)
def l1lll11_opy_(url):
	l1ll11l_opy_ = url
	item = xbmcgui.ListItem(name, path = l1ll1l_opy_ (u"ࠧࡱ࡮ࡸ࡫࡮ࡴ࠺࠰࠱ࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡨ࠷ࡱ࡙࡫ࡳࡵࡧࡵ࠳ࡄࡹࡴࡳࡧࡤࡱࡹࡿࡰࡦ࠿ࡗࡗࡉࡕࡗࡏࡎࡒࡅࡉࡋࡒࠧࡰࡤࡱࡪࡃ࡛ࡃ࡟࡞ࡇࡔࡒࡏࡓࠢ࡯࡭ࡲ࡫ࡧࡳࡧࡨࡲࡢࡋࡃࡈࠢࡗ࡚ࡠ࠵ࡃࡐࡎࡒࡖࡢࡡ࠯ࡃ࡟ࠩࡹࡷࡲ࠽ࠨ࠘") +l1ll11l_opy_)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
	return
def l1ll_opy_(query=None, id=l1ll1l_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮ࡦࡥࡪࡸࡻ࠭࠙")):
	xbmcgui.Dialog().ok(l1ll1l_opy_ (u"ࠩ࡞ࡆࡢࡡࡃࡐࡎࡒࡖࠥࡲࡩ࡮ࡧࡪࡶࡪ࡫࡮࡞ࡇࡆࡋࠥࡡ࠯ࡄࡑࡏࡓࡗࡣ࡛ࡄࡑࡏࡓࡗࠦࡧࡰ࡮ࡧࡡ࡙࡜ࠠ࡜࠱ࡆࡓࡑࡕࡒ࡞࡝࠲ࡆࡢ࠭ࠚ"),l1ll1l_opy_ (u"ࠪࡘ࡭࡫ࠠࡑࡣࡶࡷࡼࡵࡲࡥࠢ࡬ࡷࠥ࡯࡮ࡤࡱࡵࡶࡪࡩࡴࠡࡱࡵࠤࡾࡵࡵࠡࡪࡤࡺࡪࠦ࡮ࡰࡶࠣ࡫ࡴࡺࠠࡺࡱࡸࡶࠥࡶࡡࡴࡵࡺࡳࡷࡪࠠࡺࡧࡷࠤࡕࡲࡥࡢࡵࡨࠤ࡫ࡵ࡬࡭ࡱࡺࠤࡹ࡮ࡥࠡ࡫ࡱࡷࡹࡸࡵࡤࡶ࡬ࡳࡳࡹࠠࡪࡰࠣࡸ࡭࡫ࠠࡴࡧࡷࡸ࡮ࡴࡧࡴࠢࡺ࡭ࡳࡪ࡯ࡸࠢࡷࡳࠥ࡭ࡡࡪࡰࠣࡥࡨࡩࡥࡴࡵࠣࡸࡴࠦࡴࡩ࡫ࡶࠤ࡬ࡸࡥࡢࡶࠣࡪࡷ࡫ࡥࠡࡣࡧࡨࡴࡴ࠮ࠨࠛ"))
	l1111l_opy_(l1ll1l_opy_ (u"ࠫࡆࡪࡤࡰࡰ࠱ࡓࡵ࡫࡮ࡔࡧࡷࡸ࡮ࡴࡧࡴࠪࠨࡷ࠮࠭ࠜ") % id)
def l1llll_opy_():
        l1111_opy_=[]
        l1l11_opy_=sys.argv[2]
        if len(l1l11_opy_)>=2:
                params=sys.argv[2]
                l1llll1_opy_=params.replace(l1ll1l_opy_ (u"ࠬࡅࠧࠝ"),l1ll1l_opy_ (u"࠭ࠧࠞ"))
                if (params[len(params)-1]==l1ll1l_opy_ (u"ࠧ࠰ࠩࠟ")):
                        params=params[0:len(params)-2]
                l1l_opy_=l1llll1_opy_.split(l1ll1l_opy_ (u"ࠨࠨࠪࠠ"))
                l1111_opy_={}
                for i in range(len(l1l_opy_)):
                        l11_opy_={}
                        l11_opy_=l1l_opy_[i].split(l1ll1l_opy_ (u"ࠩࡀࠫࠡ"))
                        if (len(l11_opy_))==2:
                                l1111_opy_[l11_opy_[0]]=l11_opy_[1]
        return l1111_opy_
def l11l11_opy_(name, url, mode, l111l_opy_, l11l1_opy_):
	u = sys.argv[0] + l1ll1l_opy_ (u"ࠥࡃࡺࡸ࡬࠾ࠤࠢ") + urllib.quote_plus(url) + l1ll1l_opy_ (u"ࠦࠫࡳ࡯ࡥࡧࡀࠦࠣ") + str(mode) + l1ll1l_opy_ (u"ࠧࠬ࡮ࡢ࡯ࡨࡁࠧࠤ") + urllib.quote_plus(name) + l1ll1l_opy_ (u"ࠨࠦࡪࡥࡲࡲ࡮ࡳࡡࡨࡧࡀࠦࠥ") + urllib.quote_plus(l111l_opy_)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage = l1ll1l_opy_ (u"ࠢࡅࡧࡩࡥࡺࡲࡴࡇࡱ࡯ࡨࡪࡸ࠮ࡱࡰࡪࠦࠦ"), thumbnailImage = l111l_opy_)
	liz.setInfo( type = l1ll1l_opy_ (u"ࠣࡘ࡬ࡨࡪࡵࠢࠧ"), infoLabels = { l1ll1l_opy_ (u"ࠤࡗ࡭ࡹࡲࡥࠣࠨ"): name } )
	liz.setProperty(l1ll1l_opy_ (u"ࠪࡪࡦࡴࡡࡳࡶࡢ࡭ࡲࡧࡧࡦࠩࠩ"), l11l1_opy_)
	if (l1ll1l_opy_ (u"ࠫࡾࡵࡵࡵࡷࡥࡩ࠳ࡩ࡯࡮࠱ࡸࡷࡪࡸ࠯ࠨࠪ") in url) or (l1ll1l_opy_ (u"ࠬࡿ࡯ࡶࡶࡸࡦࡪ࠴ࡣࡰ࡯࠲ࡧ࡭ࡧ࡮࡯ࡧ࡯࠳ࠬࠫ") in url) or (l1ll1l_opy_ (u"࠭ࡹࡰࡷࡷࡹࡧ࡫࠯ࡶࡵࡨࡶ࠴࠭ࠬ") in url) or (l1ll1l_opy_ (u"ࠧࡺࡱࡸࡸࡺࡨࡥ࠰ࡥ࡫ࡥࡳࡴࡥ࡭࠱ࠪ࠭") in url):
		u = l1ll1l_opy_ (u"ࠨࡲ࡯ࡹ࡬࡯࡮࠻࠱࠲ࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡼࡳࡺࡺࡵࡣࡧ࠲ࠩࡸ࠵ࠥࡴ࠱ࠪ࠮") % (url.split( l1ll1l_opy_ (u"ࠩ࠲ࠫ࠯") )[-2], url.split( l1ll1l_opy_ (u"ࠪ࠳ࠬ࠰") )[-1])
		ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
		return ok
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
	return ok
def l1ll1l1_opy_(name, url, mode, l111l_opy_, l11l1_opy_):
	u = sys.argv[0] + l1ll1l_opy_ (u"ࠦࡄࡻࡲ࡭࠿ࠥ࠱") + urllib.quote_plus(url) + l1ll1l_opy_ (u"ࠧࠬ࡭ࡰࡦࡨࡁࠧ࠲") + str(mode) + l1ll1l_opy_ (u"ࠨࠦ࡯ࡣࡰࡩࡂࠨ࠳") + urllib.quote_plus(name) + l1ll1l_opy_ (u"ࠢࠧ࡫ࡦࡳࡳ࡯࡭ࡢࡩࡨࡁࠧ࠴") + urllib.quote_plus(l111l_opy_)
	liz = xbmcgui.ListItem(name, iconImage = l1ll1l_opy_ (u"ࠣࡆࡨࡪࡦࡻ࡬ࡵࡘ࡬ࡨࡪࡵ࠮ࡱࡰࡪࠦ࠵"), thumbnailImage = l111l_opy_)
	liz.setInfo( type = l1ll1l_opy_ (u"ࠤ࡙࡭ࡩ࡫࡯ࠣ࠶"), infoLabels = { l1ll1l_opy_ (u"ࠥࡘ࡮ࡺ࡬ࡦࠤ࠷"): name } )
	liz.setProperty(l1ll1l_opy_ (u"ࠫ࡫ࡧ࡮ࡢࡴࡷࡣ࡮ࡳࡡࡨࡧࠪ࠸"), l11l1_opy_)
	liz.setProperty(l1ll1l_opy_ (u"ࠬࡏࡳࡑ࡮ࡤࡽࡦࡨ࡬ࡦࠩ࠹"), l1ll1l_opy_ (u"࠭ࡴࡳࡷࡨࠫ࠺"))
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz)
def l111ll_opy_(l111l_opy_, l11l1_opy_):
	u = sys.argv[0] + l1ll1l_opy_ (u"ࠢࠧ࡫ࡦࡳࡳ࡯࡭ࡢࡩࡨࡁࠧ࠻") + urllib.quote_plus(l111l_opy_)
	liz = xbmcgui.ListItem(iconImage = l1ll1l_opy_ (u"ࠣࡆࡨࡪࡦࡻ࡬ࡵࡘ࡬ࡨࡪࡵ࠮ࡱࡰࡪࠦ࠼"), thumbnailImage = l111l_opy_)
	liz.setProperty(l1ll1l_opy_ (u"ࠩࡩࡥࡳࡧࡲࡵࡡ࡬ࡱࡦ࡭ࡥࠨ࠽"), l11l1_opy_)
	liz.setProperty(l1ll1l_opy_ (u"ࠪࡍࡸࡖ࡬ࡢࡻࡤࡦࡱ࡫ࠧ࠾"), l1ll1l_opy_ (u"ࠫ࡫ࡧ࡬ࡴࡧࠪ࠿"))
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz)
def l1lllll_opy_(name, l111l_opy_, l11l1_opy_):
	u = sys.argv[0] + l1ll1l_opy_ (u"ࠧࠬ࡮ࡢ࡯ࡨࡁࠧࡀ") + urllib.quote_plus(name) + l1ll1l_opy_ (u"ࠨࠦࡪࡥࡲࡲ࡮ࡳࡡࡨࡧࡀࠦࡁ") + urllib.quote_plus(l111l_opy_)
	liz = xbmcgui.ListItem(name, iconImage = l1ll1l_opy_ (u"ࠢࡅࡧࡩࡥࡺࡲࡴࡗ࡫ࡧࡩࡴ࠴ࡰ࡯ࡩࠥࡂ"), thumbnailImage = l111l_opy_)
	liz.setInfo( type = l1ll1l_opy_ (u"ࠣࡘ࡬ࡨࡪࡵࠢࡃ"), infoLabels = { l1ll1l_opy_ (u"ࠤࡗ࡭ࡹࡲࡥࠣࡄ"): name } )
	liz.setProperty(l1ll1l_opy_ (u"ࠪࡪࡦࡴࡡࡳࡶࡢ࡭ࡲࡧࡧࡦࠩࡅ"), l11l1_opy_)
	liz.setProperty(l1ll1l_opy_ (u"ࠫࡎࡹࡐ࡭ࡣࡼࡥࡧࡲࡥࠨࡆ"), l1ll1l_opy_ (u"ࠬ࡬ࡡ࡭ࡵࡨࠫࡇ"))
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz)
params=l1llll_opy_()
url=None
name=None
l111l_opy_=None
mode=None
description=None
query=None
try:
        url=urllib.unquote_plus(params[l1ll1l_opy_ (u"ࠨࡵࡳ࡮ࠥࡈ")])
except:
        pass
try:
        name=urllib.unquote_plus(params[l1ll1l_opy_ (u"ࠢ࡯ࡣࡰࡩࠧࡉ")])
except:
        pass
try:
       query=urllib.unquote_plus(params[l1ll1l_opy_ (u"ࠣࡳࡸࡩࡷࡿࠢࡊ")])
except:
        pass
try:
        l111l_opy_=urllib.unquote_plus(params[l1ll1l_opy_ (u"ࠤ࡬ࡧࡴࡴࡩ࡮ࡣࡪࡩࠧࡋ")])
except:
        pass
try:
        mode=int(params[l1ll1l_opy_ (u"ࠥࡱࡴࡪࡥࠣࡌ")])
except:
        pass
print l1ll1l_opy_ (u"ࠦࡒࡵࡤࡦ࠼ࠣࠦࡍ")+str(mode)
print l1ll1l_opy_ (u"࡛ࠧࡒࡍ࠼ࠣࠦࡎ")+str(url)
print l1ll1l_opy_ (u"ࠨࡎࡢ࡯ࡨ࠾ࠥࠨࡏ")+str(name)
if mode==None or url==None or len(url)<1:
        print l1ll1l_opy_ (u"ࠢࠣࡐ")
        main()
elif mode == 1:
	l1lll11_opy_(url)
xbmcplugin.endOfDirectory(l1lll1l_opy_)