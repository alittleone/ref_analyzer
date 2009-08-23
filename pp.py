#coding=utf-8
import codecs, sys, urllib2
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
        #tables = res.contents[0]
        tables = res.findChildren('table', attrs={'cellspacing':'0','cellpadding':'10'})

        for tab in tables:
                a = tab.find('a')
                link = a['href']
                span = a.findChild('span')
                #print span.contents
                #article = span.contents[0]  
                article = ' '.join([s.string for s in span.contents if s.string])
                iList = tab.findAll('i')
                journal = iList[0].contents[0]
                volumn = iList[1].contents[0]
                pubDate = iList[2].contents[0]
                pages = iList[3].contents[0]
                tds = [td for td in tab.contents]
                item = tds[1].find('td', attrs={'align':'left','width':'95%','colspan':'2'})
                author = item.contents[10]
                #td1 = tds[1]
                #author = td1.contents[10]
                ie = PAMIE()
                ie.navigate(link)
                ie.linkClick('References')
                #ie.quit()
                idx += 1
                print "[", idx, "]", "\n\t", link, "\n\t", article, "\n\t", author, "\n\t", journal, "\n\t", volumn, "\n\t", pages, "\n"
                #print "[", idx, "]", "\n\t", article, "\n\t", journal, "\n\t", volumn, "\n\t", pages, "\n"
        print "FETCH page, to ", idx
        return idx

"""
url = 'c:\\python25\web.html'
ie = PAMIE()
ie.navigate(url)
FormatHtml(ie.outerHTML())

"""

#url = 'http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=tag&refSource=search&_st=13&count=739&_chunk=2&PREV_LIST=1&NEXT_LIST=3&view=c&md5=e528e094dcc02c469caa87884e42fb84&_ArticleListID=987492397&sisr_search=&next=next+page&sisrterm='

url = 'http://www.sciencedirect.com/science?_ob=ArticleListURL&_method=list&_ArticleListID=988199744&_st=17&_acct=C000050221&_version=1&_urlVersion=0&_userid=10&md5=49b6cf8f710c22f40e5ca2c9b0517312'

ie = PAMIE()
ie.navigate(url)

counter = 0
FormatHtml(ie.outerHTML(), counter)

#urls = [url]
while ie.buttonClick('next'):
#       url = ie.locationURL()
#       print "NEXT page: ", url
#       urls.append(url)
        counter = FormatHtml(ie.outerHTML(), counter)
                
#for url in urls:
#       print url
#       req = urllib2.Request(url)
#       req.add_header("User-Agent", 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11')
#
#       f = urllib2.urlopen(req)
#
#       counter = FormatHtml(f, counter)
        



