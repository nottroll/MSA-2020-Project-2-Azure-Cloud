import urllib.request
url = 'https://data.nsw.gov.au/data/api/3/action/datastore_search?resource_id=2776dbb8-f807-4fb2-b1ed-184a6fc2c8aa&limit=5'  
fileobj = urllib.request.urlopen(url)
print(fileobj.read())