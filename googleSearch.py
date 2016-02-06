import requests, sys, bs4, webbrowser

print "Googling %s..." % (' '.join(sys.argv[1:]))
response = requests.get("http://www.google.com/search?q=%s" % (' '.join(sys.argv[1:])))
response.raise_for_status()

googleSoup = bs4.BeautifulSoup(response.content, "lxml")
links = googleSoup.select('.r > a')

for i in range(min(5, len(links))):
    webbrowser.open('https://www.google.com%s' % links[i].get("href"))