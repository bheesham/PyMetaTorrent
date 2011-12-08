import gc
import time
import ConfigParser
import bson
import threading

from includes.functions import *
from includes.database import *

# load the configuration ( database )
config = ConfigParser.RawConfigParser()

config.read('./config/database.cfg')
config.read('./config/bot.cfg')

db_info = [
			config.get( 'database', 'host' ),
			config.get( 'database', 'port' ),
			config.get( 'database', 'user' ),
			config.get( 'database', 'passw' ),
			config.get( 'database', 'name' ),
			]

max_threads = int( config.get( 'bot', 'max_threads' ) )

db = database()
db = db.connect( db_info )

infinite = 1

while infinite == 1:
	count = 0
	threads = []
	rows = db.to_crawl.find( { "hash": 0 } ).limit( max_threads )
	if rows.count( 1 ) < max_threads:
		print "sleeping"
		time.sleep( 120 )
	else:
		for i in range( rows.count( 1 ) - 1  ):
			thread = get_site( rows[i]['site'] )( db_info, rows[i]['info_url'] )
			threads.append( thread )
			thread.start()
		for thread in threads:
			count = count + 1
			thread.join()
	gc.collect()