import json
from pprint import pprint
def g():
    with open('html.json') as data_file:
        data = json.load(data_file)

    for key in data:
        print('wget http://stars.chromeexperiments.com/detail/'+key.replace(' ','_').lower()+'.html')

def f():
    with open('stars_all.json') as data_file:
        data = json.load(data_file)

    for dat in data['stars']:
        if(dat.get('name')):
            # print dat
            print('wget http://stars.chromeexperiments.com/detail/'+dat['name'].replace(' ','_').lower()+'.html')
# f()
g()
