import os
import sys
import time
import re
import gc
import ConfigParser
from threading import Thread

from sites.ThePirateBay import *
from sites.KickAssTorrents import *

# load the configuration ( database )
config = ConfigParser.RawConfigParser()
config.read('./config/database.cfg')

db_info = [
			config.get( 'database', 'host' ),
			config.get( 'database', 'port' ),
			config.get( 'database', 'user' ),
			config.get( 'database', 'passw' ),
			config.get( 'database', 'name' ),
			]

sites =	[ 
			# music
			[ ThePirateBay, [ "http://thepiratebay.org/browse/101/TPAGE/3" ] ],
			[ ThePirateBay, [ "http://thepiratebay.org/browse/102/TPAGE/3" ] ],
			[ ThePirateBay, [ "http://thepiratebay.org/browse/103/TPAGE/3" ] ],
			[ ThePirateBay, [ "http://thepiratebay.org/browse/104/TPAGE/3" ] ], 
			[ ThePirateBay, [ "http://thepiratebay.org/browse/199/TPAGE/3" ] ], 
			# music
			[ KickAssTorrents, [ "http://www.kickasstorrents.com/music/TPAGE/" ] ], 
			#[ KickAssTorrents, [ "http://www.kickasstorrents.com/music/tag/70s/TPAGE/" ] ], 
			#[ KickAssTorrents, [ "http://www.kickasstorrents.com/music/tag/80s/TPAGE/" ] ], 
			#[ KickAssTorrents, [ "http://www.kickasstorrents.com/music/tag/90s/TPAGE/" ] ], 
			#[ KickAssTorrents, [ "http://www.kickasstorrents.com/music/tag/alternative/TPAGE/" ] ], 
			#[ KickAssTorrents, [ "http://www.kickasstorrents.com/music/tag/alternative-rock/TPAGE/" ] ], 
			#[ KickAssTorrents, [ "http://www.kickasstorrents.com/music/tag/ambient/TPAGE/" ] ], 
			#[ KickAssTorrents, [ "http://www.kickasstorrents.com/music/tag/blues/TPAGE/" ] ], 
			#[ KickAssTorrents, [ "http://www.kickasstorrents.com/music/tag/british/TPAGE/" ] ], 
			#[ KickAssTorrents, [ "http://www.kickasstorrents.com/music/tag/classic-rock/TPAGE/" ] ], 
			#[ KickAssTorrents, [ "http://www.kickasstorrents.com/music/tag/country/TPAGE/" ] ], 
			#[ KickAssTorrents, [ "http://www.kickasstorrents.com/music/tag/dance/TPAGE/" ] ], 
			#[ KickAssTorrents, [ "http://www.kickasstorrents.com/music/tag/death-metal/TPAGE/" ] ], 
			#[ KickAssTorrents, [ "http://www.kickasstorrents.com/music/tag/electro-house/TPAGE/" ] ], 
			#[ KickAssTorrents, [ "http://www.kickasstorrents.com/music/tag/electronic/TPAGE/" ] ], 
			#[ KickAssTorrents, [ "http://www.kickasstorrents.com/music/tag/electronica/TPAGE/" ] ], 
			#[ KickAssTorrents, [ "http://www.kickasstorrents.com/music/tag/female-vocalists/TPAGE/" ] ], 
			#[ KickAssTorrents, [ "http://www.kickasstorrents.com/music/tag/folk/TPAGE/" ] ], 
			#[ KickAssTorrents, [ "http://www.kickasstorrents.com/music/tag/funk/TPAGE/" ] ], 
			#[ KickAssTorrents, [ "http://www.kickasstorrents.com/music/tag/hard-rock/TPAGE/" ] ], 
			#get more later -_-''
		]

count = 0
for site in sites:
	site[0]( db_info, count, site[1][0] ).start()
	time.sleep( random.randint( 0, 5 ) )
	count = count + 1
count = count - 1