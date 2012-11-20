from urllib import urlopen
from xml.dom.minidom import parseString
import urllib2

''' Two functions that download the tweets from a twitter account, given as parameter. See documentation of each function.

Please note that the twitter API is subject to changes, which may result in these functions not working properly. Also, the Twitter API is limited to 150 requests per hour

@author: Marius Constantinescu
marius@ipworkshop.ro

'''


'''getStatusesfromPage(url) returns a list of tweets from a given url which accesses the twitter api. for example, if run with the parameter  http://api.twitter.com/1/statuses/user_timeline.xml?screen_name=barackobama&page=1, it returns a list of the most 15 recent tweets of barack obama. Normally, you do not need to call this function, this is already done in the next function.

'''

def getStatusesfromPage(url):
	tw = []
	# download the file:
	fis = urllib2.urlopen(url)
	# convert to string:
	data = fis.read()
	# close file because we dont need it anymore:
	fis.close()
	# parse the xml you downloaded
	dom = parseString(data)
	#out=file('tweets.txt', 'w')
	# retrieve the first xml tag (<tag>data</tag>) that the parser finds with name tagName:
	for e in dom.getElementsByTagName('text'):
		xmlTag = e.toxml().encode('utf-8')
		# strip off the tag (<tag>data</tag>  --->   data):
		xmlData=xmlTag.replace('<text>','').replace('</text>','')
		# print out the xml tag and data in this format: <tag>data</tag>
		#out.write(xmlTag)
		# just print the data
		tw.append(xmlData)
		#out.write(xmlData)
		#out.write('\n')
	#out.close()
	return tw
	 

'''getStatuses(accout,n, path) uses the previous function to write in a file the latest 15*n tweets of the account account. The first parameter specifies the account which is mined (should be string), n is the number of pages which are scanned (integer; 15 tweets/page), path gives the name of the output file (the file's name would be "path_tweets")

'''
	 
def getStatuses(account, n):
	bigListOfTweets = []
	for i in range(n):
		newurl = 'http://api.twitter.com/1/statuses/user_timeline.xml?screen_name=' + account +'&?page=%d'%(i+1)
		print(newurl)
		bigListOfTweets=bigListOfTweets+getStatusesfromPage(newurl)
	out = file(account+'_tweets', 'w')
	out.write("\n".join(bigListOfTweets))
	out.close()
		