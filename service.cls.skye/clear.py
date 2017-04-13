# coding: UTF-8
import sys
l1_opy_ = sys.version_info [0] == 2
l11ll1l_opy_ = 2048
l11ll_opy_ = 7
def l1ll11_opy_ (ll_opy_):
	global l11l1l_opy_
	l11llll_opy_ = ord (ll_opy_ [-1])
	l11lll_opy_ = ll_opy_ [:-1]
	l1l1lll_opy_ = l11llll_opy_ % len (l11lll_opy_)
	l1lll_opy_ = l11lll_opy_ [:l1l1lll_opy_] + l11lll_opy_ [l1l1lll_opy_:]
	if l1_opy_:
		l1llll1_opy_ = unicode () .join ([unichr (ord (char) - l11ll1l_opy_ - (l1ll1l_opy_ + l11llll_opy_) % l11ll_opy_) for l1ll1l_opy_, char in enumerate (l1lll_opy_)])
	else:
		l1llll1_opy_ = str () .join ([chr (ord (char) - l11ll1l_opy_ - (l1ll1l_opy_ + l11llll_opy_) % l11ll_opy_) for l1ll1l_opy_, char in enumerate (l1lll_opy_)])
	return eval (l1llll1_opy_)
import time
import xbmc
import os
import xbmcgui
import xbmcaddon
l1l11l1_opy_ = l1ll11_opy_ (u"ࠫࡸ࡫ࡲࡷ࡫ࡦࡩ࠳ࡩ࡬ࡴ࠰ࡶ࡯ࡾ࡫ࠧࠀ")
l1l11ll_opy_       = xbmcaddon.Addon()
l1llll_opy_ = xbmcaddon.Addon(id=l1l11l1_opy_)
l1lll1l_opy_ = xbmc.translatePath(l1ll11_opy_ (u"ࠬࡹࡰࡦࡥ࡬ࡥࡱࡀ࠯࠰ࡣࡧࡨࡴࡴ࡟ࡥࡣࡷࡥ࠴ࡹࡥࡳࡸ࡬ࡧࡪ࠴ࡣ࡭ࡵ࠱ࡷࡰࡿࡥ࠰ࡵࡨࡸࡹ࡯࡮ࡨࡵ࠱ࡼࡲࡲࠧࠁ"))
l1ll111_opy_ = xbmc.translatePath(l1ll11_opy_ (u"࠭ࡳࡱࡧࡦ࡭ࡦࡲ࠺࠰࠱ࡷ࡬ࡺࡳࡢ࡯ࡣ࡬ࡰࡸ࠵࠰ࠨࠂ"))
l11l1_opy_ = xbmc.translatePath(l1ll11_opy_ (u"ࠧࡴࡲࡨࡧ࡮ࡧ࡬࠻࠱࠲ࡸ࡭ࡻ࡭ࡣࡰࡤ࡭ࡱࡹ࠯࠲ࠩࠃ"))
l1ll1l1_opy_ = xbmc.translatePath(l1ll11_opy_ (u"ࠨࡵࡳࡩࡨ࡯ࡡ࡭࠼࠲࠳ࡹ࡮ࡵ࡮ࡤࡱࡥ࡮ࡲࡳ࠰࠴ࠪࠄ"))
l1ll11l_opy_ = xbmc.translatePath(l1ll11_opy_ (u"ࠩࡶࡴࡪࡩࡩࡢ࡮࠽࠳࠴ࡺࡨࡶ࡯ࡥࡲࡦ࡯࡬ࡴ࠱࠶ࠫࠅ"))
l1l1l11_opy_ = xbmc.translatePath(l1ll11_opy_ (u"ࠪࡷࡵ࡫ࡣࡪࡣ࡯࠾࠴࠵ࡴࡩࡷࡰࡦࡳࡧࡩ࡭ࡵ࠲࠸ࠬࠆ"))
l1l1l1_opy_ = xbmc.translatePath(l1ll11_opy_ (u"ࠫࡸࡶࡥࡤ࡫ࡤࡰ࠿࠵࠯ࡵࡪࡸࡱࡧࡴࡡࡪ࡮ࡶ࠳࠺࠭ࠇ"))
l1l1ll1_opy_ = xbmc.translatePath(l1ll11_opy_ (u"ࠬࡹࡰࡦࡥ࡬ࡥࡱࡀ࠯࠰ࡶ࡫ࡹࡲࡨ࡮ࡢ࡫࡯ࡷ࠴࠼ࠧࠈ"))
l1l1l1l_opy_ = xbmc.translatePath(l1ll11_opy_ (u"࠭ࡳࡱࡧࡦ࡭ࡦࡲ࠺࠰࠱ࡷ࡬ࡺࡳࡢ࡯ࡣ࡬ࡰࡸ࠵࠷ࠨࠉ"))
l1lll11_opy_ = xbmc.translatePath(l1ll11_opy_ (u"ࠧࡴࡲࡨࡧ࡮ࡧ࡬࠻࠱࠲ࡸ࡭ࡻ࡭ࡣࡰࡤ࡭ࡱࡹ࠯࠹ࠩࠊ"))
l1ll1ll_opy_ = xbmc.translatePath(l1ll11_opy_ (u"ࠨࡵࡳࡩࡨ࡯ࡡ࡭࠼࠲࠳ࡹ࡮ࡵ࡮ࡤࡱࡥ࡮ࡲࡳ࠰࠻ࠪࠋ"))
l1ll_opy_ = xbmc.translatePath(l1ll11_opy_ (u"ࠩࡶࡴࡪࡩࡩࡢ࡮࠽࠳࠴ࡺࡨࡶ࡯ࡥࡲࡦ࡯࡬ࡴ࠱ࡤࠫࠌ"))
l1l_opy_ = xbmc.translatePath(l1ll11_opy_ (u"ࠪࡷࡵ࡫ࡣࡪࡣ࡯࠾࠴࠵ࡴࡩࡷࡰࡦࡳࡧࡩ࡭ࡵ࠲ࡦࠬࠍ"))
l11_opy_ = xbmc.translatePath(l1ll11_opy_ (u"ࠫࡸࡶࡥࡤ࡫ࡤࡰ࠿࠵࠯ࡵࡪࡸࡱࡧࡴࡡࡪ࡮ࡶ࠳ࡨ࠭ࠎ"))
l11l_opy_ = xbmc.translatePath(l1ll11_opy_ (u"ࠬࡹࡰࡦࡥ࡬ࡥࡱࡀ࠯࠰ࡶ࡫ࡹࡲࡨ࡮ࡢ࡫࡯ࡷ࠴ࡪࠧࠏ"))
l111_opy_ = xbmc.translatePath(l1ll11_opy_ (u"࠭ࡳࡱࡧࡦ࡭ࡦࡲ࠺࠰࠱ࡷ࡬ࡺࡳࡢ࡯ࡣ࡬ࡰࡸ࠵ࡥࠨࠐ"))
l1l1_opy_ = xbmc.translatePath(l1ll11_opy_ (u"ࠧࡴࡲࡨࡧ࡮ࡧ࡬࠻࠱࠲ࡸ࡭ࡻ࡭ࡣࡰࡤ࡭ࡱࡹ࠯ࡧࠩࠑ"))
l1l11_opy_ = xbmc.translatePath(l1ll11_opy_ (u"ࠨࡵࡳࡩࡨ࡯ࡡ࡭࠼࠲࠳ࡹ࡮ࡵ࡮ࡤࡱࡥ࡮ࡲࡳ࠰ࡘ࡬ࡨࡪࡵࠧࠒ"))
if __name__ == l1ll11_opy_ (u"ࠩࡢࡣࡲࡧࡩ࡯ࡡࡢࠫࠓ"):
	l111l_opy_ = xbmc.Monitor()
	while not l111l_opy_.abortRequested():
		l11l1ll_opy_ = float(l1llll_opy_.getSetting(l1ll11_opy_ (u"ࠥࡗࡪࡩ࡯࡯ࡦࡶࠦࠔ")))
		if l111l_opy_.waitForAbort(l11l1ll_opy_):
			break
		for l111l1_opy_ in os.listdir(l1ll111_opy_):
			l1l111_opy_ = os.path.join(l1ll111_opy_, l111l1_opy_)
			if os.path.isfile(l1l111_opy_):
				os.unlink(l1l111_opy_)
		for l111l1_opy_ in os.listdir(l11l1_opy_):
			l1l111_opy_ = os.path.join(l11l1_opy_, l111l1_opy_)
			if os.path.isfile(l1l111_opy_):
				os.unlink(l1l111_opy_)
		for l111l1_opy_ in os.listdir(l1ll1l1_opy_):
			l1l111_opy_ = os.path.join(l1ll1l1_opy_, l111l1_opy_)
			if os.path.isfile(l1l111_opy_):
				os.unlink(l1l111_opy_)
		for l111l1_opy_ in os.listdir(l1ll11l_opy_):
			l1l111_opy_ = os.path.join(l1ll11l_opy_, l111l1_opy_)
			if os.path.isfile(l1l111_opy_):
				os.unlink(l1l111_opy_)
		for l111l1_opy_ in os.listdir(l1l1l11_opy_):
			l1l111_opy_ = os.path.join(l1l1l11_opy_, l111l1_opy_)
			if os.path.isfile(l1l111_opy_):
				os.unlink(l1l111_opy_)
		for l111l1_opy_ in os.listdir(l1l1l1_opy_):
			l1l111_opy_ = os.path.join(l1l1l1_opy_, l111l1_opy_)
			if os.path.isfile(l1l111_opy_):
				os.unlink(l1l111_opy_)
		for l111l1_opy_ in os.listdir(l1l1ll1_opy_):
			l1l111_opy_ = os.path.join(l1l1ll1_opy_, l111l1_opy_)
			if os.path.isfile(l1l111_opy_):
				os.unlink(l1l111_opy_)
		for l111l1_opy_ in os.listdir(l1l1l1l_opy_):
			l1l111_opy_ = os.path.join(l1l1l1l_opy_, l111l1_opy_)
			if os.path.isfile(l1l111_opy_):
				os.unlink(l1l111_opy_)
		for l111l1_opy_ in os.listdir(l1lll11_opy_):
			l1l111_opy_ = os.path.join(l1lll11_opy_, l111l1_opy_)
			if os.path.isfile(l1l111_opy_):
				os.unlink(l1l111_opy_)
		for l111l1_opy_ in os.listdir(l1ll1ll_opy_):
			l1l111_opy_ = os.path.join(l1ll1ll_opy_, l111l1_opy_)
			if os.path.isfile(l1l111_opy_):
				os.unlink(l1l111_opy_)
		for l111l1_opy_ in os.listdir(l1ll_opy_):
			l1l111_opy_ = os.path.join(l1ll_opy_, l111l1_opy_)
			if os.path.isfile(l1l111_opy_):
				os.unlink(l1l111_opy_)
		for l111l1_opy_ in os.listdir(l1l_opy_):
			l1l111_opy_ = os.path.join(l1l_opy_, l111l1_opy_)
			if os.path.isfile(l1l111_opy_):
				os.unlink(l1l111_opy_)
		for l111l1_opy_ in os.listdir(l11_opy_):
			l1l111_opy_ = os.path.join(l11_opy_, l111l1_opy_)
			if os.path.isfile(l1l111_opy_):
				os.unlink(l1l111_opy_)
		for l111l1_opy_ in os.listdir(l11l_opy_):
			l1l111_opy_ = os.path.join(l11l_opy_, l111l1_opy_)
			if os.path.isfile(l1l111_opy_):
				os.unlink(l1l111_opy_)
		for l111l1_opy_ in os.listdir(l111_opy_):
			l1l111_opy_ = os.path.join(l111_opy_, l111l1_opy_)
			if os.path.isfile(l1l111_opy_):
				os.unlink(l1l111_opy_)
		for l111l1_opy_ in os.listdir(l1l1_opy_):
			l1l111_opy_ = os.path.join(l1l1_opy_, l111l1_opy_)
			if os.path.isfile(l1l111_opy_):
				os.unlink(l1l111_opy_)
		for l111l1_opy_ in os.listdir(l1l11_opy_):
			l1l111_opy_ = os.path.join(l1l11_opy_, l111l1_opy_)
			if os.path.isfile(l1l111_opy_):
				os.unlink(l1l111_opy_)
		l11111_opy_ = os.path.join(xbmc.translatePath(l1ll11_opy_ (u"ࠫࡸࡶࡥࡤ࡫ࡤࡰ࠿࠵࠯ࡩࡱࡰࡩࠬࠕ")), l1ll11_opy_ (u"ࠬࡩࡡࡤࡪࡨࠫࠖ"))
		if os.path.exists(l11111_opy_)==True:
			for root, dirs, l11ll1_opy_ in os.walk(l11111_opy_):
				l1l1ll_opy_ = 0
				l1l1ll_opy_ += len(l11ll1_opy_)
				if l1l1ll_opy_ > 0:
						for f in l11ll1_opy_:
							try:
								os.unlink(os.path.join(root, f))
							except:
								pass
						for d in dirs:
							try:
								shutil.rmtree(os.path.join(root, d))
							except:
								pass
				else:
					pass
		if xbmc.getCondVisibility(l1ll11_opy_ (u"࠭ࡳࡺࡵࡷࡩࡲ࠴ࡰ࡭ࡣࡷࡪࡴࡸ࡭࠯ࡃࡗ࡚࠷࠭ࠗ")):
			l1111l_opy_ = os.path.join(l1ll11_opy_ (u"ࠧ࠰ࡲࡵ࡭ࡻࡧࡴࡦ࠱ࡹࡥࡷ࠵࡭ࡰࡤ࡬ࡰࡪ࠵ࡌࡪࡤࡵࡥࡷࡿ࠯ࡄࡣࡦ࡬ࡪࡹ࠯ࡂࡲࡳࡰࡪ࡚ࡖ࠰ࡘ࡬ࡨࡪࡵ࠯ࠨ࠘"), l1ll11_opy_ (u"ࠨࡑࡷ࡬ࡪࡸࠧ࠙"))
			for root, dirs, l11ll1_opy_ in os.walk(l1111l_opy_):
				l1l1ll_opy_ = 0
				l1l1ll_opy_ += len(l11ll1_opy_)
				if l1l1ll_opy_ > 0:
						for f in l11ll1_opy_:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
				else:
					pass
			l1lllll_opy_ = os.path.join(l1ll11_opy_ (u"ࠩ࠲ࡴࡷ࡯ࡶࡢࡶࡨ࠳ࡻࡧࡲ࠰࡯ࡲࡦ࡮ࡲࡥ࠰ࡎ࡬ࡦࡷࡧࡲࡺ࠱ࡆࡥࡨ࡮ࡥࡴ࠱ࡄࡴࡵࡲࡥࡕࡘ࠲࡚࡮ࡪࡥࡰ࠱ࠪࠚ"), l1ll11_opy_ (u"ࠪࡐࡴࡩࡡ࡭ࡃࡱࡨࡗ࡫࡮ࡵࡣ࡯ࠫࠛ"))
			for root, dirs, l11ll1_opy_ in os.walk(l1lllll_opy_):
				l1l1ll_opy_ = 0
				l1l1ll_opy_ += len(l11ll1_opy_)
				if l1l1ll_opy_ > 0:
						for f in l11ll1_opy_:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
				else:
					pass
		l11ll11_opy_ = os.path.join(xbmc.translatePath(l1ll11_opy_ (u"ࠫࡸࡶࡥࡤ࡫ࡤࡰ࠿࠵࠯ࡱࡴࡲࡪ࡮ࡲࡥ࠰ࡣࡧࡨࡴࡴ࡟ࡥࡣࡷࡥ࠴ࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡼ࡮ࡡࡵࡶ࡫ࡩ࡫ࡻࡲ࡬࠱ࡦࡥࡨ࡮ࡥࠨࠜ")), l1ll11_opy_ (u"ࠬ࠭ࠝ"))
		if os.path.exists(l11ll11_opy_)==True:
			for root, dirs, l11ll1_opy_ in os.walk(l11ll11_opy_):
				l1l1ll_opy_ = 0
				l1l1ll_opy_ += len(l11ll1_opy_)
				if l1l1ll_opy_ > 0:
						for f in l11ll1_opy_:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
				else:
					pass
		l1lll1_opy_= os.path.join(xbmc.translatePath(l1ll11_opy_ (u"࠭ࡳࡱࡧࡦ࡭ࡦࡲ࠺࠰࠱ࡳࡶࡴ࡬ࡩ࡭ࡧ࠲ࡥࡩࡪ࡯࡯ࡡࡧࡥࡹࡧ࠯ࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴࠴ࡰࡦ࠲ࡧࡦࡩࡨࡦࠩࠞ")), l1ll11_opy_ (u"ࠧࠨࠟ"))
		if os.path.exists(l1lll1_opy_)==True:
			for root, dirs, l11ll1_opy_ in os.walk(l1lll1_opy_):
				l1l1ll_opy_ = 0
				l1l1ll_opy_ += len(l11ll1_opy_)
				if l1l1ll_opy_ > 0:
						for f in l11ll1_opy_:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
				else:
					pass
		l11l11_opy_= os.path.join(xbmc.translatePath(l1ll11_opy_ (u"ࠨࡵࡳࡩࡨ࡯ࡡ࡭࠼࠲࠳ࡵࡸ࡯ࡧ࡫࡯ࡩ࠴ࡧࡤࡥࡱࡱࡣࡩࡧࡴࡢ࠱ࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯࡫ࡳࡰࡦࡿࡥࡳ࠱࡬ࡴࡱࡧࡹࡦࡴࡢ࡬ࡹࡺࡰࡠࡥࡤࡧ࡭࡫ࠧࠠ")), l1ll11_opy_ (u"ࠩࠪࠡ"))
		if os.path.exists(l11l11_opy_)==True:
			for root, dirs, l11ll1_opy_ in os.walk(l11l11_opy_):
				l1l1ll_opy_ = 0
				l1l1ll_opy_ += len(l11ll1_opy_)
				if l1l1ll_opy_ > 0:
						for f in l11ll1_opy_:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
				else:
					pass
		l1ll1_opy_ = os.path.join(xbmc.translatePath(l1ll11_opy_ (u"ࠪࡷࡵ࡫ࡣࡪࡣ࡯࠾࠴࠵ࡰࡳࡱࡩ࡭ࡱ࡫࠯ࡢࡦࡧࡳࡳࡥࡤࡢࡶࡤ࠳ࡸࡩࡲࡪࡲࡷ࠲ࡲࡵࡤࡶ࡮ࡨ࠲ࡸ࡯࡭ࡱ࡮ࡨ࠲ࡩࡵࡷ࡯࡮ࡲࡥࡩ࡫ࡲࠨࠢ")), l1ll11_opy_ (u"ࠫࠬࠣ"))
		if os.path.exists(l1ll1_opy_)==True:
			for root, dirs, l11ll1_opy_ in os.walk(l1ll1_opy_):
				l1l1ll_opy_ = 0
				l1l1ll_opy_ += len(l11ll1_opy_)
				if l1l1ll_opy_ > 0:
						for f in l11ll1_opy_:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
				else:
					pass
		l1l11l_opy_ = os.path.join(xbmc.translatePath(l1ll11_opy_ (u"ࠬࡹࡰࡦࡥ࡬ࡥࡱࡀ࠯࠰ࡲࡵࡳ࡫࡯࡬ࡦ࠱ࡤࡨࡩࡵ࡮ࡠࡦࡤࡸࡦ࠵ࡰ࡭ࡷࡪ࡭ࡳ࠴ࡶࡪࡦࡨࡳ࠳࡯ࡴࡷ࠱ࡌࡱࡦ࡭ࡥࡴࠩࠤ")), l1ll11_opy_ (u"࠭ࠧࠥ"))
		if os.path.exists(l1l11l_opy_)==True:
			for root, dirs, l11ll1_opy_ in os.walk(l1l11l_opy_):
				l1l1ll_opy_ = 0
				l1l1ll_opy_ += len(l11ll1_opy_)
				if l1l1ll_opy_ > 0:
						for f in l11ll1_opy_:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
				else:
					pass
		l1111_opy_ = os.path.join(xbmc.translatePath(l1ll11_opy_ (u"ࠧࡴࡲࡨࡧ࡮ࡧ࡬࠻࠱࠲ࡴࡷࡵࡦࡪ࡮ࡨ࠳ࡦࡪࡤࡰࡰࡢࡨࡦࡺࡡ࠰ࡲ࡯ࡹ࡬࡯࡮࠯ࡸ࡬ࡨࡪࡵ࠮࡮ࡱࡹ࡭ࡪࡹ࠴࡮ࡧ࠲ࡧࡦࡩࡨࡦࠩࠦ")), l1ll11_opy_ (u"ࠨࠩࠧ"))
		if os.path.exists(l1l11l_opy_)==True:
			for root, dirs, l11ll1_opy_ in os.walk(l1111_opy_):
				l1l1ll_opy_ = 0
				l1l1ll_opy_ += len(l11ll1_opy_)
				if l1l1ll_opy_ > 0:
						for f in l11ll1_opy_:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
				else:
					pass
		l1l1111_opy_ = os.path.join(xbmc.translatePath(l1ll11_opy_ (u"ࠩࡶࡴࡪࡩࡩࡢ࡮࠽࠳࠴ࡶࡲࡰࡨ࡬ࡰࡪ࠵ࡡࡥࡦࡲࡲࡤࡪࡡࡵࡣ࠲ࡴࡱࡻࡧࡪࡰ࠱ࡺ࡮ࡪࡥࡰ࠰ࡳ࡬ࡸࡺࡲࡦࡣࡰࡷ࠴ࡉࡡࡤࡪࡨࠫࠨ")), l1ll11_opy_ (u"ࠪࠫࠩ"))
		if os.path.exists(l1l11l_opy_)==True:
			for root, dirs, l11ll1_opy_ in os.walk(l1l1111_opy_):
				l1l1ll_opy_ = 0
				l1l1ll_opy_ += len(l11ll1_opy_)
				if l1l1ll_opy_ > 0:
						for f in l11ll1_opy_:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
				else:
					pass
		l1l1l_opy_ = os.path.join(xbmc.translatePath(l1ll11_opy_ (u"ࠫࡸࡶࡥࡤ࡫ࡤࡰ࠿࠵࠯ࡱࡴࡲࡪ࡮ࡲࡥ࠰ࡣࡧࡨࡴࡴ࡟ࡥࡣࡷࡥ࠴ࡶ࡬ࡶࡩ࡬ࡲ࠳ࡼࡩࡥࡧࡲ࠲ࡸࡶ࡯ࡵ࡫ࡷࡹࡧ࡫࠯ࡤࡣࡦ࡬ࡪ࠭ࠪ")), l1ll11_opy_ (u"ࠬ࠭ࠫ"))
		if os.path.exists(l1l11l_opy_)==True:
			for root, dirs, l11ll1_opy_ in os.walk(l1l1l_opy_):
				l1l1ll_opy_ = 0
				l1l1ll_opy_ += len(l11ll1_opy_)
				if l1l1ll_opy_ > 0:
						for f in l11ll1_opy_:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
				else:
					pass
		l11l1l1_opy_ = os.path.join(xbmc.translatePath(l1ll11_opy_ (u"࠭ࡳࡱࡧࡦ࡭ࡦࡲ࠺࠰࠱ࡳࡶࡴ࡬ࡩ࡭ࡧ࠲ࡥࡩࡪ࡯࡯ࡡࡧࡥࡹࡧ࠯ࡱ࡮ࡸ࡫࡮ࡴ࠮ࡷ࡫ࡧࡩࡴ࠴ࡳࡶࡲࡨࡶࡨࡧࡲࡵࡱࡲࡲࡸ࠵ࡣࡢࡥ࡫ࡩࠬࠬ")), l1ll11_opy_ (u"ࠧࠨ࠭"))
		if os.path.exists(l1l11l_opy_)==True:
			for root, dirs, l11ll1_opy_ in os.walk(l11l1l1_opy_):
				l1l1ll_opy_ = 0
				l1l1ll_opy_ += len(l11ll1_opy_)
				if l1l1ll_opy_ > 0:
						for f in l11ll1_opy_:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
				else:
					pass
		l111ll_opy_ = os.path.join(xbmc.translatePath(l1ll11_opy_ (u"ࠨࡵࡳࡩࡨ࡯ࡡ࡭࠼࠲࠳ࡵࡸ࡯ࡧ࡫࡯ࡩ࠴ࡧࡤࡥࡱࡱࡣࡩࡧࡴࡢ࠱ࡳࡰࡺ࡭ࡩ࡯࠰ࡹ࡭ࡩ࡫࡯࠯ࡶࡹࡳࡳࡲࡩ࡯ࡧ࠱ࡧࡨ࠵ࡣࡢࡥ࡫ࡩࠬ࠮")), l1ll11_opy_ (u"ࠩࠪ࠯"))
		if os.path.exists(l1l11l_opy_)==True:
			for root, dirs, l11ll1_opy_ in os.walk(l111ll_opy_):
				l1l1ll_opy_ = 0
				l1l1ll_opy_ += len(l11ll1_opy_)
				if l1l1ll_opy_ > 0:
						for f in l11ll1_opy_:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
				else:
					pass
		l11lll1_opy_ = os.path.join(xbmc.translatePath(l1ll11_opy_ (u"ࠪࡷࡵ࡫ࡣࡪࡣ࡯࠾࠴࠵ࡰࡳࡱࡩ࡭ࡱ࡫࠯ࡢࡦࡧࡳࡳࡥࡤࡢࡶࡤ࠳ࡵࡲࡵࡨ࡫ࡱ࠲ࡻ࡯ࡤࡦࡱ࠱ࡽࡴࡻࡴࡶࡤࡨ࠳ࡰࡵࡤࡪࡱࡱࠫ࠰")), l1ll11_opy_ (u"ࠫࠬ࠱"))
		if os.path.exists(l1l11l_opy_)==True:
			for root, dirs, l11ll1_opy_ in os.walk(l11lll1_opy_):
				l1l1ll_opy_ = 0
				l1l1ll_opy_ += len(l11ll1_opy_)
				if l1l1ll_opy_ > 0:
						for f in l11ll1_opy_:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
				else:
					pass
		l1l111l_opy_ = os.path.join(xbmc.translatePath(l1ll11_opy_ (u"ࠬࡹࡰࡦࡥ࡬ࡥࡱࡀ࠯࠰ࡪࡲࡱࡪ࠵ࡴࡦ࡯ࡳࠫ࠲")), l1ll11_opy_ (u"࠭ࠧ࠳"))
		if os.path.exists(l1l111l_opy_)==True:
			for root, dirs, l11ll1_opy_ in os.walk(l1l111l_opy_):
				l1l1ll_opy_ = 0
				l1l1ll_opy_ += len(l11ll1_opy_)
				if l1l1ll_opy_ > 0:
						for f in l11ll1_opy_:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))