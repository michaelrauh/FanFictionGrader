import urllib2
links = []
for i in range(0,3000):
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
                links.append("http://www.fanfiction.net" + word)       
links = list(set(links))
f = open("goodlinks.txt",'w')
for link in links:
    f.write(link)
    f.write('\n')
f.close()
