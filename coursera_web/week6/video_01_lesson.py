__author__ = 'srgtolm'

import json

data = '''{
"name": "Chuck",
"phone" : {
    "type" : "intl",
    "number" : "intl",
     "number" : " 8 953 702 xx 11"
     },
     "email" : { "hide" : "yes"
     }
}'''

info = json.loads(data)
print 'Name:',info["name"]
print 'Hide', info["email"]["hide"]
