import urllib

# change the user agent
class AppURLopener( urllib.FancyURLopener ):
	version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.98 Safari/534.13' # google chrome
urllib._urlopener = AppURLopener()

def get_page( url ):
	client = urllib.urlopen( url )
	page_html = client.read()
	if client.code != 200: return 0
	return page_html