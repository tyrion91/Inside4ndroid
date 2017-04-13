
import time
import xbmc
import os
import xbmcgui
import xbmcaddon

addon_id = 'plugin.video.ecgmovies'
addon       = xbmcaddon.Addon()
selfAddon = xbmcaddon.Addon(id=addon_id)


def CleanUP():
		xbmc_cache_path = os.path.join(xbmc.translatePath('special://home'), 'cache')
		if os.path.exists(xbmc_cache_path)==True:	
			for root, dirs, files in os.walk(xbmc_cache_path):
				file_count = 0
				file_count += len(files)
		
				if file_count > 0:
						for f in files:
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
		if xbmc.getCondVisibility('system.platform.ATV2'):
			atv2_cache_a = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'Other')
		
			for root, dirs, files in os.walk(atv2_cache_a):
				file_count = 0
				file_count += len(files)
		
				if file_count > 0:
						for f in files:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
						
				else:
					pass
			atv2_cache_b = os.path.join('/private/var/mobile/Library/Caches/AppleTV/Video/', 'LocalAndRental')
		
			for root, dirs, files in os.walk(atv2_cache_b):
				file_count = 0
				file_count += len(files)
		
				if file_count > 0:
						for f in files:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
						
				else:
					pass
							 
		wtf_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.whatthefurk/cache'), '')
		if os.path.exists(wtf_cache_path)==True:	
			for root, dirs, files in os.walk(wtf_cache_path):
				file_count = 0
				file_count += len(files)
		
				if file_count > 0:
						for f in files:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))

				else:
					pass
				
		channel4_cache_path= os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.4od/cache'), '')
		if os.path.exists(channel4_cache_path)==True:	
			for root, dirs, files in os.walk(channel4_cache_path):
				file_count = 0
				file_count += len(files)
		
				if file_count > 0:
						for f in files:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
						
				else:
					pass
				
		iplayer_cache_path= os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.iplayer/iplayer_http_cache'), '')
		if os.path.exists(iplayer_cache_path)==True:	
			for root, dirs, files in os.walk(iplayer_cache_path):
				file_count = 0
				file_count += len(files)
		
				if file_count > 0:
						for f in files:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
						
				else:
					pass
				
				
		downloader_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/script.module.simple.downloader'), '')
		if os.path.exists(downloader_cache_path)==True:	
			for root, dirs, files in os.walk(downloader_cache_path):
				file_count = 0
				file_count += len(files)
		
				if file_count > 0:
						for f in files:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
						
				else:
					pass
				
		itv_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.itv/Images'), '')
		if os.path.exists(itv_cache_path)==True:	
			for root, dirs, files in os.walk(itv_cache_path):
				file_count = 0
				file_count += len(files)
		
				if file_count > 0:
						for f in files:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
						
				else:
					pass
	
		m4me_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.movies4me/cache'), '')
		if os.path.exists(itv_cache_path)==True:	
			for root, dirs, files in os.walk(m4me_cache_path):
				file_count = 0
				file_count += len(files)
		
				if file_count > 0:
						for f in files:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
						
				else:
					pass

		phoenix_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.phstreams/Cache'), '')
		if os.path.exists(itv_cache_path)==True:	
			for root, dirs, files in os.walk(phoenix_cache_path):
				file_count = 0
				file_count += len(files)
		
				if file_count > 0:
						for f in files:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
						
				else:
					pass

		ytmusic_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.spotitube/cache'), '')
		if os.path.exists(itv_cache_path)==True:	
			for root, dirs, files in os.walk(ytmusic_cache_path):
				file_count = 0
				file_count += len(files)
		
				if file_count > 0:
						for f in files:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
						
				else:
					pass

		supercartoons_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.supercartoons/cache'), '')
		if os.path.exists(itv_cache_path)==True:	
			for root, dirs, files in os.walk(supercartoons_cache_path):
				file_count = 0
				file_count += len(files)
		
				if file_count > 0:
						for f in files:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
						
				else:
					pass

		tvonline_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.tvonline.cc/cache'), '')
		if os.path.exists(itv_cache_path)==True:	
			for root, dirs, files in os.walk(tvonline_cache_path):
				file_count = 0
				file_count += len(files)
		
				if file_count > 0:
						for f in files:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
						
				else:
					pass

		youtube_cache_path = os.path.join(xbmc.translatePath('special://profile/addon_data/plugin.video.youtube/kodion'), '')
		if os.path.exists(itv_cache_path)==True:	
			for root, dirs, files in os.walk(youtube_cache_path):
				file_count = 0
				file_count += len(files)
		
				if file_count > 0:
						for f in files:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))
						
				else:
					pass

		temp_cache_path = os.path.join(xbmc.translatePath('special://home/temp'), '')
		if os.path.exists(temp_cache_path)==True:	
			for root, dirs, files in os.walk(temp_cache_path):
				file_count = 0
				file_count += len(files)
	   
				if file_count > 0:
						for f in files:
							os.unlink(os.path.join(root, f))
						for d in dirs:
							shutil.rmtree(os.path.join(root, d))

def Clear_P():
		xbmc_pack_path = os.path.join(xbmc.translatePath('special://home'), 'addons', 'packages')
		if os.path.exists(xbmc_pack_path)==True:	
			for root, dirs, files in os.walk(xbmc_pack_path):
				file_count = 0
				file_count += len(files)
		
				if file_count > 0:
						for f in files:
							try:
								os.unlink(os.path.join(root, f))
							except:
								pass
						for d in dirs:
							try:
								shutil.rmtree(os.path.join(root, d))
							except:
								pass
	