#code to deal with XML

import xml.etree.ElementTree as ET   #alias - a shortform
data = '''<person>
             <name>Chuck</name>
             <phone type="intl"> +1 734 303 4456
             </phone>
             <email hide="yes"/>
          </person>'''

tree =  ET.fromstring(data)   #this can blow. protect it with try/except
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
