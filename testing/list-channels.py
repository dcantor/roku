from xml.dom import minidom
import requests



r = requests.get('http://192.168.50.70:8060/query/apps')
mydoc = minidom.parseString(r.content)
print mydoc
items = mydoc.getElementsByTagName('app')

# all items data
print('\nAll item data:')
for elem in items:
    print(elem.firstChild.data)