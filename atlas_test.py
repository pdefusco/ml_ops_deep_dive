import atlasclient
endpoint = "https://demo-aws-1-dl-master0.demo-aws.ylcu-atmi.cloudera.site/demo-aws-1-dl/cdp-proxy-api/atlas/api/atlas/"

from atlasclient.client import Atlas
client = Atlas(endpoint, port='', username='pauldefusco', password='ColliAlbani1987@')

params = {'attrName': 'name'}
search_results = client.search_basic(**params)

for s in search_results:
    print(s._name)