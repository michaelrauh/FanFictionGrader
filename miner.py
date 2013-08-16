import urllib2
links = []
favs = []
for i in range(1,16830,10):
    page_links = []
    page_favs = []
    print(i)
    response = urllib2.urlopen('http://www.fanfiction.net/book/Harry-Potter/?&srt=4&lan=1&r=10&p=' + str(i))
    html = response.read()
    words = html.split()
    for word in words:
        if word.find('href') != -1 and word.find('/s/') != -1:
            if word[-1] == 'g':
                word = word[6:-6]
            else:
                word = word[6:-12]
            if word[11] == '1' and word[12] =='/':
                page_links.append("http://www.fanfiction.net" + word)
    for word in range (0,len(words)-1):
        if words[word].find('Favs:') != -1:
            page_favs.append(words[word+1])
    if len(page_links) == len(page_favs): # sometimes formatting on links is weird and one is skipped. If this happens the page is thrown out
        links += page_links
        favs += page_favs
f = open("names.txt",'w')
for link in links:
    f.write(link)
    f.write('\n')
f.close()
f = open("favs.txt",'w')
for fav in favs:
    f.write(fav)
    f.write('\n')
f.close()
