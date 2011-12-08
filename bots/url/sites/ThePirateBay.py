import random
import time
import re
import gc
from threading import Thread

from includes.functions import *
from includes.database import *

class ThePirateBay( Thread ):
	def __init__( self, db_info, id, url_structure ):
		
		# initiate the thread
		Thread.__init__(self)
		
		# set the thread ID
		self.id = id
		
		# save the database connection and the class
		self.dbc = database()
		self.dbc = self.dbc.connect( db_info )
		self.db = database()
		
		# compile and save a regular expression that will match the torrent information URL
		self.torrent_url_pattern = re.compile( r'<div class="detName"><a href="([a-zA-Z0-9\_\-\(\)/\.\[\]]+)"', re.I )
		
		# save the page url structure ( e.g. http://thepiratebay.org/browse/101/TPAGE/3 )
		self.url_structure = url_structure
		
		# set the current page as the first page
		self.first_page()
		
		# pages to parse before we set this to sleep to stop the program
		self.max_parse = 100
		self.num_parsed = 0
		
	def run( self ):
		infinite = 1
		while infinite == 1:
			gc.collect()
			# parse the current page
			parsed = self.parse_page( self.current_page_url )
			print "{0} - {1}: {2}".format( self.id, self.current_page, len( parsed ) )
			self.num_parsed = self.num_parsed + 1
			if parsed == None:
				self.first_page()
				print "{0} sleeping...".format( self.id )
				time.sleep( 1800 )
			else:
				self.db.torrent_insert( self.dbc, "ThePirateBay", parsed )
				self.next_page()
				time.sleep( random.randint( 0, 5 ) )

	def parse_page( self, page_url ):
		ret = []
		page_source = get_page( page_url )
		matches = self.torrent_url_pattern.findall( page_source )
		if len( matches ) > 0:
			for part_url in matches:
				torrent_url = 'http://www.thepiratebay.org' + part_url
				if self.db.torrent_exists( self.dbc, torrent_url ) == 0:
					ret.append( torrent_url )
			return ret
		else:
			return None

	def first_page( self ):
		self.current_page_url = self.url_structure.replace( 'TPAGE', str( 0 ) );
		self.current_page = 0
		return 1

	def next_page( self ):
		self.current_page = self.current_page + 1
		self.current_page_url = self.url_structure.replace( 'TPAGE', str( self.current_page ) );
		return 1