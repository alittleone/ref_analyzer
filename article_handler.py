import urllib2
import lxml.html
#from lxml import etree

url = 'http://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B6T7F-4V42JC3-1&_user=10&_coverDate=05%2F31%2F2009&_alid=988199744&_rdoc=1&_fmt=high&_orig=mlkt&_cdi=5057&_st=17&_docanchor=&_ct=20&_acct=C000050221&_version=1&_urlVersion=0&_userid=10&md5=00a3d8ed74eb23326f723bd614a7aa4a'
req = urllib2.Request(url)
req.add_header("User-Agent", 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11')
resps = urllib2.urlopen(req)

html = resps.read()
doc = lxml.html.fromstring(html) # lxml.html.parse(resps)

titleElement = doc.find_class('articleTitle')[0]
articleTitle = unicode(titleElement.text_content()).replace('\n', '')

authorsElement = doc.get_element_by_id('authorsAnchors')
ps = authorsElement.cssselect('strong>p')[0]
authorInfos = [unicode(x).replace(' and ', '').replace(', ', '') for x in ps.itertext() if x != ', ']

