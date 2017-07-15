import sys
import urllib
import simplejson

apikey= "b75b49844df265a09f419520373f93c0"
SEARCH_BASE = "https://apis.daum.net/search/book"

print(sys.argv)

def search(query, pageno, **args):
    args.update({
        'apikey':apikey,
        'q' : query,
            'result':20,
            'pageno': pageno,
        'output' :'json'
    })

    url = SEARCH_BASE + '?' + urllib.urlencode(args)
    result = simplejson.load(urllib.urlopen(url))
    return result['channel']

query= "business"
pageno = 1
c = search(query,pageno)
json = simplejson.loads(c)


print(json)
