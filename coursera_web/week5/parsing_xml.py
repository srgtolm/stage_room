__author__ = 'srgtolm'

import xml.etree.ElementTree as ET
input ='''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="22">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>
'''
stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print 'User count:', len(lst)
for item in lst:
    print 'Name', item.find('name').text
    print 'ID', item.find('id').text
    print 'Att', item.get('x')





