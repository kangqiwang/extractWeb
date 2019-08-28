from boilerpipe.extract import Extractor

URL='https://www.oshkosh.com/oshkosh-kid-boy-shoes?page=3'

extractor = Extractor(extractor='ArticleExtractor', url=URL)

print (extractor.getText())
