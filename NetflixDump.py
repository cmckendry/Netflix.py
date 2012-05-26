from Netflix import *
import getopt
import time 
import sys

APP_NAME   = ''
API_KEY    = ''
API_SECRET = ''
CALLBACK   = ''

if __name__ == '__main__':
	netflixClient = NetflixClient(APP_NAME, API_KEY, API_SECRET, CALLBACK, False)
	netflixCatalog = NetflixCatalog(netflixClient)
	completeNetflixCatalog = netflixCatalog.getCatalog()
	if len(sys.argv) >= 2:
		filepath = sys.argv[1]
		file = open(filepath,'w')
		file.write(completeNetflixCatalog)
		file.close()
	else:
		print completeNetflixCatalog