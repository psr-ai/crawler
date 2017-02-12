from crawler import Crawler

crawler = Crawler()

flipkart_url = "https://www.flipkart.com/search?q=iphone%207&as=on&as-show=on&otracker=start&as-pos=2_q_iph"
amazon_url = "http://www.amazon.in/s/ref=nb_sb_ss_i_4_6?url=search-alias%3Daps&field-keywords=iphone+7&sprefix=iphone%2Caps%2C284&crid=ZNKHKONNIHBA"

crawler.auto_crawl(flipkart_url)

