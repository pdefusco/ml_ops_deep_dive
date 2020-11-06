import os
from pprint import pprint

thecurl = """curl 'https://demo-aws-1-dl-master0.demo-aws.ylcu-atmi.cloudera.site/demo-aws-1-dl/cdp-proxy/atlas/api/atlas/v2/search/basic' \
  -H 'Connection: keep-alive' \
  -H 'Accept: application/json, text/javascript, */*; q=0.01' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'X-XSRF-HEADER: ""' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://demo-aws-1-dl-master0.demo-aws.ylcu-atmi.cloudera.site' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://demo-aws-1-dl-master0.demo-aws.ylcu-atmi.cloudera.site/demo-aws-1-dl/cdp-proxy/atlas/index.html' \
  -H 'Accept-Language: en-US,en;q=0.9,it;q=0.8' \
  -H 'Cookie: _ga=GA1.3.1240983158.1598492987; RANGERADMINSESSIONID=7410C851F33EA9BF83BB194E4716C740; SESSION=5c0d9557-fd9c-4d52-8df7-e148fcfcab7a; _gid=GA1.3.42985451.1603488512; hadoop-jwt=eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJwYXVsZGVmdXNjbyIsImlzcyI6IktOT1hTU08iLCJleHAiOjE2MDM1NzgwOTMsImtub3guaWQiOiJkYjkzZWNlNy0xMjg0LTQwZDAtYWNiOS0yODEwZTM5ODY0MWYifQ.ejJJJL8305ikEJgOwK766Z6Qobk9wzOfI4SYZ7M2x9gJ4euvrU98qr6fgy-uXpaPj5iA79WSDF_jSSNHuiUW_qmcR-_z7QDXGyLMmJtqfKYNAcxsoOTX-Q4Q_-xXFVYF1zUBzT75hsMPWdTPuylN1QCfXkS5AhnvWxFlOxYqRSRayLiDf-8oxmD-DFXePGX-cha9W_uCOwou9R6-FtSSxLPbOZqRkcQYNtmzy3PuiIaF7vGeb1Xj1X5ismDvexCE_zwmQ4pNznuhwMnlEJ1q3S-UNhNe7Et921QSRjNSTrw4uYdzLbh3RWkytw1tF37ccvgyZwIfGXfgevg8FUTrYQ; ATLASSESSIONID=node01lm5471ka8d4elkb4dt7s5mj411842094.node0' \
  --data-binary '{"excludeDeletedEntities":true,"includeSubClassifications":true,"includeSubTypes":true,"includeClassificationAttributes":true,"entityFilters":null,"tagFilters":null,"attributes":[],"limit":25,"offset":0,"typeName":"hive_table","classification":null,"termName":null}' \
  --compressed"""


#print(os.system(thecurl))


pprint(os.system(thecurl))