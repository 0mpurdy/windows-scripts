# from https://stackoverflow.com/questions/4489550/how-to-get-an-html-file-using-python
import urllib.request
import re

# https://stackoverflow.com/questions/21842885/python-find-a-substring-in-a-string-and-returning-the-index-of-the-substring
def getChapterText(html, cutoff):
    nextChapIndex1 = html.find(cutoff)
    nextChapIndex2 = html.find(cutoff, nextChapIndex1 + 1)
    print("Cutoff:", nextChapIndex1)
    output = html[nextChapIndex1:nextChapIndex2]
    #print("new output:", output)
    return output

# from https://stackoverflow.com/questions/4489550/how-to-get-an-html-file-using-python
# https://stackoverflow.com/questions/3336549/pythons-urllib2-why-do-i-get-error-403-when-i-urlopen-a-wikipedia-page
def getParagraphs(url, pat, cutoff):
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    sock = urllib.request.urlopen(req)
    output = sock.read().decode('utf-8')
    sock.close()
    output = getChapterText(output, cutoff)
    results = pat.findall(output)
    return results

def printWuxiaPage(url):
    pat = re.compile('<p>.*</p>')
    cutoff = '>Next Chapter<'
    results = getParagraphs(url, pat, cutoff)

    for result in results:
        print(re.sub('<[^>]*>', '', result))
        print()
    
pat = re.compile('<p>.*</p>')
#url = 'https://en.wikipedia.org/wiki/HTTP_403'
url = 'http://www.wuxiaworld.com/col-index/col-volume-1-chapter-2/'
cutoff = '>Next Chapter<'

for i in range(1,4):
    page = 'http://www.wuxiaworld.com/desolate-era-index/de-book-41-chapter-%d/' % i
    print('#', page)
    printWuxiaPage(page)
