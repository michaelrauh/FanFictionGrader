import urllib2
links = []
favs = []
names=[]
dates =[]
def tothe (x):
    return x**1.28
for i in map(tothe,range(1,2000)):
    i = int(i)
    page_links = []
    page_favs = []
    page_names = []
    page_dates = []
    print(i)
    response = urllib2.urlopen('http://www.fanfiction.net/book/Harry-Potter/?&srt=4&lan=1&r=10&p=' + str(i))
    html = response.read()
    words = html.split()
    words2=html.split('>')
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
    for word in range (0,len(words)-1):
        if words[word].find('Updated:') != -1:
            temp = words[word+1].split('-')
            for i in range (0,len (temp)):
                if len(temp[i]) < 2:
                    temp[i] = '0' + temp[i]
            temp = ''.join(temp)
            if temp[-2:] != 99:
                temp = str(temp[:-2]) + str(20) + str(temp[-2:])
            else:
                temp = str(temp[:-2]) + str(19) + str(temp[-2:])
            page_dates.append(temp)
    for word in range (0,len(words2)):
        if words2[word].find('href="/u')!=-1:
            temp = words2[word+1]
            page_names.append(temp[:temp.find('<')])
    if len(page_links) == len(page_favs) == len(page_names) == len(page_dates): # sometimes formatting on links is weird and one is skipped. If this happens the page is thrown out
        links += page_links
        favs += page_favs
        names += page_names
        dates += page_dates
f = open("links.txt",'w')
for link in links:
    f.write(link)
    f.write('\n')
f.close()
f = open("names.txt",'w')
for j in range (0,len(favs)):
    f.write(favs[j])
    f.write('\n')
    f.write(names[j])
    f.write('-')
    f.write(dates[j])
    f.write('\n')
f.close()
