# coding: UTF-8
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