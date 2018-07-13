from lxml import html
import requests
import  urllib

page = requests.get('http://www.wcoomd.org/en/topics/nomenclature/instrument-and-tools/hs-nomenclature-2017-edition/hs-nomenclature-2017-edition')
tree = html.fromstring(page.content)


for x in xrange(8,175):
	link = tree.xpath('//*[@id="columncontent_3_divMainText"]/table/tbody/tr['+str(x)+']/td[3]/p/a/@href')
	name = tree.xpath('//*[@id="columncontent_3_divMainText"]/table/tbody/tr['+str(x)+']/td[1]/p/text()')


	if len(link) != 0 and len(name) != 0:
		testfile = urllib.URLopener()
		l='http://www.wcoomd.org'+link[0]
		testfile.retrieve(l,'c:\\users\\admin\\Desktop\\ruling\\wco\\Chapter '+name[0]+'.pdf')
		print "File Downloaded " + name[0]