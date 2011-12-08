from pymongo import Connection
import bson

class database:
	def connect( self, db_info ):
		# host, port, user, pass, name
		con_string = '{2}:{3}@{0}:{1}'.format( db_info[0], db_info[1], db_info[2], db_info[3] )
		con = Connection( con_string )
		db = con[db_info[4]]
		return db
	def torrent_exists( self, db, url ):
		info_url = bson.son.SON( { "info_url": url } )
		found = db.to_crawl.find( info_url ).count()
		if found == 0:
			return 0
		else:
			return 1
	def torrent_insert( self, db, site, urls ):
		for url in urls:
			query = bson.son.SON( {
								"site": site,
								"info_url": url,
								"hash": 0
			} )
			db.to_crawl.insert( query )
		return 1