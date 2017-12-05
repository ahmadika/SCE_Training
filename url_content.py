import html2text

import requests

searchTerms = ["definitions", "ocean", "guide"]
ngram = searchTerms[1]
print(ngram)
#Make the proxy settings, if your access is through a proxy server

#reading 12 opened urls
urls = open('urls.txt', 'r')
urlList=[]
for line in urls:
    urlList.append(line)
urls.close()

i=1
for url in urlList:
    res = requests.get(url,timeout=10.0 )
    html = res.text

    #Converting html content to lowercase
    html = html.lower()

    counter = 0
    ocean = False
    rel =''

    if ngram in html:
        for term in searchTerms:
            if term in html:
                counter+=1
                #print (str(counter))
        if counter/len(searchTerms) >= 0.7:
            rel = 'High Relevant'
        elif counter/len(searchTerms) >= 0.30:
            rel = 'Relevant'
        else:
            rel = 'Not Relevant'
    else:
        rel = "Not Relevant"
    print(str(i) + "- "+rel)
    i+=1


