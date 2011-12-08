from pymongo import Connection
import bson

class database:
	def connect( self, db_info ):
		# host, port, user, pass, name
		con_string = '{2}:{3}@{0}:{1}'.format( db_info[0], db_info[1], db_info[2], db_info[3] )
		con = Connection( con_string )
		db = con[db_info[4]]
		return db
	def torrent_404( self, db, url ):
		hash_404 = bson.son.SON( { "$set": { "hash": 404 } } )
		info_url = bson.son.SON( { "info_url": url } )
		db.to_crawl.update( info_url, hash_404 )
		return 1
	def set_torrent_info( self, db, info_url, contents ):
		hash = hashlib.sha1( bencode( contents['info'] ) ).hexdigest()
		
		# update to_crawl
		update_info_url = bson.son.SON( { "info_url": info_url } )
		update_torrent_hash = bson.son.SON( { "$set": { "hash": hash } } )
		db.to_crawl.update( update_info_url, update_torrent_hash )
		
		# does this torrent already exist?
		exist_hash = bson.son.SON( { "hash": hash } )
		found = db.to_crawl.find( exist_hash ).count()
		if found == 0:
			add_info_url = [ info_url ]
			add_announces = []
			add_announces.append( contents['announce'] )
			for a in contents['announce-list']:
				add_announces.append( a )
			add_first_seen = contents['creation date']
			add_create_torrent = 0
			add_info = bson.son.SON( { 
										"hash": hash,
										"info_urls": add_info_url,
										"announces": add_announces,
										"first-seen": add_first_seen,
										"create_torrent": add_create_torrent
										} )
			db.to_info.insert( add_info )
			pass
		else:
			# existing torrent
			# add new info_url
			# add to announce-list
			# check to see if this torrent was created before
			# reset the create-torrent key?
			pass
		return 1