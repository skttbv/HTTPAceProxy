# -*- coding: utf-8 -*-
'''
af1c1onados Playlist Plugin configuration file
'''
import os

# Proxy settings
proxies = {}

# URL for the JSON playlist catalog
url = 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/AcEStREAM%20iDs.w3u'

# Resolve current subgroup shorteners to raw URLs directly.
# This avoids VPN/rate-limit issues with cutt.ly/urlfy/n9/smurl.
urlaliases = {
    'https://cutt.ly/ctbwFuKv': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/01.%20Dazn.w3u',
    'https://cutt.ly/TtQOyZkg': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/02.%20EuroSport.w3u',
    'https://cutt.ly/UtR8TMTN': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/03.%20Dazn%20F1.w3u',
    'https://urlfy.org/S9KnTq8': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/04.%20Liga%20HyperMotion.w3u',
    'https://cutt.ly/KtbwJsMV': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/05.0%20Liga%20EA%20Sport.w3u',
    'https://cutt.ly/MtbwZ4Pk': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/06.%20Liga%20de%20Campeones.w3u',
    'https://smurl.es/1gXrwn': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/07.%20Movistar%20Plus.w3u',
    'https://cutt.ly/8tQOtEXz': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/08.%20Movistar%20Deportes.w3u',
    'https://urlfy.org/SjAtOHH': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/09.%20Movistar.Ellas.w3u',
    'https://cutt.ly/BtbwCk67': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/10.%20Movistar.Vamos.w3u',
    'https://n9.cl/zxk3c': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/11.%20ACB.Eventos',
    'https://smurl.es/1gY6es': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/12.%20Canales%20Espa%C3%B1a.w3u',
    'https://urlfy.org/IIo5hfE': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/13.%20Copa%20del%20Rey.w3u',
    'https://cutt.ly/QtbwVXec': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/14.%20Movistar.w3u',
    'https://smurl.es/1gZm3a': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/15.%20Movistar.Golf.w3u',
    'https://n9.cl/n4aeay': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/16.%20Tenis%20Channel.w3u',
    'https://urlfy.org/IzdOsmu': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/17.%20Sport%20TV.w3u',
    'https://cutt.ly/ntn8ehAC': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/18.%20Ppvp.w3u',
    'https://cutt.ly/itm87Ku3': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/19.%20Espn.w3u',
    'https://cutt.ly/Ltn38cB6': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/20.%20BT.Sport.Uk.w3u',
    'https://urlfy.org/j2Wh47G': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/21.%20Sky.Sport.UK.w3u',
    'https://cutt.ly/6tn39HDY': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/22.%20Viaplay.Sport.UK.w3u',
    'https://urlfy.org/h8lfLnx': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/23.%20Bein.Sport.w3u',
    'https://cutt.ly/Ttn39oLr': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/24.%20Eleven.Sport.w3u',
    'https://n9.cl/vj46d0': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/25.%20Extreme.Sport.w3u',
    'https://cutt.ly/wtn8q3vs': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/26.%20EuroSport.360.w3u',
    'https://smurl.es/1qegGO': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/refs/heads/main/27.%20Red.Bull.w3u',
    'https://github.com/af1Series1/Tritolgia/blob/main/28.%20Ufc.w3u': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/main/28.%20Ufc.w3u',
    'https://cutt.ly/ztn37rRI': 'https://raw.githubusercontent.com/af1Series1/Tritolgia/main/29.%20Nba.USA.w3u',
}

# Download playlist every N minutes
updateevery = 60

# TV Guide URL
tvgurl = 'https://raw.githubusercontent.com/davidmuma/EPG_dobleM/master/guiatv_sincolor0.xml.gz'

# Shift the TV Guide time
tvgshift = 0

# Playlist Headers
m3uheadertemplate = u'#EXTM3U url-tvg="{}" tvg-shift={} deinterlace=1 m3uautoload=1 cache=1000\n'.format(tvgurl, tvgshift)

# Channel template
m3uchanneltemplate = u'#EXTINF:-1 group-title="{group}" tvg-name="{tvg}" tvg-id="{tvgid}" tvg-logo="{logo}",{name}\n#EXTGRP:{group}\n{url}\n'
