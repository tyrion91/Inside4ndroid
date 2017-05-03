# -*- coding: utf-8 -*- 

import sys,xbmc,xbmcplugin
from common import Addon


def setView(addon_id, content, viewType):

        addon = Addon(addon_id, sys.argv)

        if content:

                xbmcplugin.setContent(int(sys.argv[1]), content)

        if addon.get_setting('auto-view') == 'true':

                addon.log(addon.get_setting(viewType))

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

                elif addon.get_setting(viewType) == 'List':
                        VT = '50'

                elif addon.get_setting(viewType) == 'Default Menu View':
                        VT = addon.get_setting('default-view1')

                elif addon.get_setting(viewType) == 'Default TV Shows View':
                        VT = addon.get_setting('default-view2')

                elif addon.get_setting(viewType) == 'Default Episodes View':
                        VT = addon.get_setting('default-view3')

                elif addon.get_setting(viewType) == 'Default Movies View':
                        VT = addon.get_setting('default-view4')

                elif addon.get_setting(viewType) == 'Default Docs View':
                        VT = addon.get_setting('default-view5')

                elif addon.get_setting(viewType) == 'Default Cartoons View':
                        VT = addon.get_setting('default-view6')

                elif addon.get_setting(viewType) == 'Default Anime View':
                        VT = addon.get_setting('default-view7')

                addon.log(viewType)
                addon.log(VT)

                xbmc.executebuiltin("Container.SetViewMode(%s)" % ( int(VT) ) )

        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_UNSORTED )
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_LABEL )
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RATING )
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_DATE )
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_PROGRAM_COUNT )
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_VIDEO_RUNTIME )
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_GENRE )
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), sortMethod=xbmcplugin.SORT_METHOD_MPAA_RATING )