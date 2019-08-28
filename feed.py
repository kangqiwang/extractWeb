import feedparser

FEED_URL='https://www.oshkosh.com/oshkosh-kid-boy-shoes?page=6'

fp = feedparser.parse(FEED_URL)

for e in fp.entries:
    print (e.title)
    print (e.links[0].href)
    print (e.content[0].value)
