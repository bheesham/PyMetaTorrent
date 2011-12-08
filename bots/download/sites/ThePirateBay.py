import re
import gc
import hashlib
import threading

from includes.functions import *
from includes.database import *
from includes.bencode import *

class ThePirateBay( threading.Thread ):
	def __init__( self, db_info, url ):
		threading.Thread.__init__( self )
		
		self.dbc = database()
		self.dbc = self.dbc.connect( db_info )
		self.db = database()
		
		self.download_url_pattern = re.compile( r'<a href="http://([a-zA-Z0-9\_\-\(\)/\.\[\]]+).TPB.torrent" title="', re.I )
		
		self.url = url

	def run( self ):
		page = get_page( self.url )
		if page != 0:
			matches = self.download_url_pattern.findall( page )
			if len( matches ) > 0:
				torrent_url = "http://" + matches[0] + "TPB.torrent"
				torrent_contents = get_page( torrent_url )				
				if torrent_contents != 0:
					torrent_contents = bdecode( torrent_contents )
					self.db.set_torrent_info( self.dbc, self.url, torrent_contents )
				else:
					pass
					#self.db.torrent_404( self.dbc, self.url )
		else:
			pass
			#self.db.torrent_404( self.dbc, self.url )
		return None