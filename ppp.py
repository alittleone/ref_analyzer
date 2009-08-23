#coding=utf-8
import codecs, sys, urllib2, os
from BeautifulSoup import BeautifulSoup, SoupStrainer
from cPAMIE import PAMIE

idx = 0

streamWriter = codecs.lookup('utf-8')[-1]
sys.stdout = streamWriter(sys.stdout)

def FormatHtml(f, idx):
	#results = d.find(id='bodyMainResults')
	resultDiv = SoupStrainer('div', id='bodyMainResults')
	res = BeautifulSoup(f, parseOnlyThese=resultDiv)

	#tables = res.findChildren('table', attrs={'class':'resultRow'})
	tables = res.contents[0]
	#tables = res.findChildren('table', attrs={'cellspacing':'0','cellpadding':'10'})

	for tab in tables:
		a = tab.find('a')
		link = a['href']
		span = a.findChild('span')
		#print span.contents
		#article = span.contents[0]  
		article = ' '.join([s.string for s in span.contents])
		iList = tab.findAll('i')
		journal = iList[0].contents[0]
		volumn = iList[1].contents[0]
		pubDate = iList[2].contents[0]
		pages = iList[3].contents[0]
		tds = [td for td in tab.contents[0]]
		td1 = tds[1]
		author = td1.contents[10]
		idx = idx + 1
	#	print author
		print "[", idx, "]", "\n\t", article, "\n\t", author, "\n\t", journal, "\n\t", volumn, "\n"
	
	print "FETCH page, to ", idx
	return idx

"""
url = 'c:\\python25\web.html'
ie = PAMIE()
ie.navigate(url)
FormatHtml(ie.outerHTML())

"""

#url = 'http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&refSource=search&_st=13&count=739&_chunk=2&PREV_LIST=1&NEXT_LIST=3&view=c&md5=e528e094dcc02c469caa87884e42fb84&_ArticleListID=987492397&sisr_search=&next=next+page&sisrterm='

url = 'http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=list&_ArticleListID=987492397&_st=13&_acct=C000050221&_version=1&_urlVersion=0&_userid=10&md5=07b2ce065d4fbefa373c5267ca144469'


counter = 0
#FormatHtml(ie.outerHTML(), counter)

if not os.path.exists("urls.txt"):
	urlFile = open("urls.txt", 'w')
	urlFile.write(url + "\n")
	
	ie = PAMIE()
	ie.navigate(url)

	urls = [url]

	while ie.buttonClick('next'):
		url = ie.locationURL()
		print "NEXT page: ", url
		urlFile.write(url + "\n")
		urls.append(url)
		
	urlFile.close()
	print "IE operator OVER"
else:
	urlFile = open("urls.txt", 'r')
	urls = [url for url in urlFile]
	
oriurl = 'http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=list&_ArticleListID=987492397&_st=13&_acct=C000050221&_version=1&_urlVersion=0&_userid=10&md5=07b2ce065d4fbefa373c5267ca144469'
	
for url in urls:
	print url
	req = urllib2.Request(url)
	mycookie = "EUID=d46adf9a-49d1-11de-ae49-00000aac490b; MIAMISESSION=96c0b98e-8fbe-11de-a27c-00008a0c5905:3428468909; MIAMIAUTH=e43abfa71bb8b07f0f9f31f4571d6ec7a04561337915b0a4988e765cf95615ae933f95e3ce895a7a0234b0ae4216a3e5b01ae98d9403bf0ef9ba77ba045005caaadeab82edc85b9a043ae339764fc28665728e33f7ff6517ea6225d183c9d96988d5396ce88a676c7d16c57ed03dd64f960a66b94f7a2fafb8d6e6429d8009de9458dbda9f1c56c473cf04defb0c8b516db54d6c7292e20581771cf7638504553640cb533b3320f7c7b2fdd0cf09e580b05223b248e0d4bcad4db83fd0e3c4d54ac91b476280c405a1de1d430c231c6ca021df1bbf9da01c; TARGET_URL=fcf74dd786744d87fbaaaf8652a764ab4a79b0d3ed681139e91069237606310567c0829015f2c9dd1e7f53b901efb3085634c77790407f6a59cf4b8b43fd52f88c47c65abba081f79ab6d2158c12cde9da364f1b55655d259627887553eebe1eab46e0705dbd83d591ce0cf1927531e8f00d25debb1075906f206de4398bb371d2d82503c0f4e06fb545563925e00da48acfb4a69fa814db74d14598c659061c81a4f2fa9ed6ae424f8687a36ca66fd26e8825017f5c39989dae44d87f94461faa8e1cb2a8c2981d9e35230d7be813036864cd4dafc7b3fa4b50c33cbab88e4c0fc888e5f0315ae0; BROWSER_SUPPORTS_COOKIES=1"
	req.add_header("Host", "www.sciencedirect.com")
	req.add_header("User-Agent", 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11')
	req.add_header("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")
	req.add_header("Accept-Language", "zh-cn")
	req.add_header("Accept-Encoding", "gzip,deflate")
	req.add_header("Accept-Charset", "gb2312,utf-8;q=0.7,*;q=0.7")

	req.add_header("Keep-Alive", "300")
	req.add_header("Connection", 'keep-alive')
	req.add_header("Cookie", mycookie)
	req.add_header("If-Modified-Since", "Sunday, 23 Aug 2009 09:19:05 GMT")

	f = urllib2.urlopen(req)

	counter = FormatHtml(f, counter)
	



