from googlesearch import search as sr
import re
import itertools
import operator
import time
import random
import urllib.request
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.parse
from collections import OrderedDict


def globalsearch(col):
    

    
    
    parametr = []
    search={}
    user_id = 'id*'
    whitelist = ["first_name","last_name","maiden_name", "bdate","city"]
    col = dict( (k,v) for k, v in col.items() if v and k in whitelist )
    
    try:       
        search.update({'"'+''.join(col['first_name'])+'" "' + ''.join(col['last_name']) + '"':10})
    except:
        pass
    
    try: 
        search.update({'"'+''.join(col['first_name'])+' ' + ''.join(col['last_name']) + '" "' + ''.join(col['city']['title']) + '" ':15})
    except:
        pass
    
    try: 
        search.update({'"'+''.join(col['first_name'])+'" "' + ''.join(col['last_name']) + '" "' + ''.join(col['maiden_name']) + '" ':23})
    except:
        pass
    
    try: 
        search.update({'"'+''.join(col['first_name'])+' ' + ''.join(col['last_name']) + ' ' + ''.join(col['maiden_name']) + '"':33})
    except:
        pass
    
    try: 
        search.update({'"'+''.join(col['first_name'])+' ' + ''.join(col['last_name']) + ' ' + ''.join(col['city']['title']) + '"':43})
    except:
        pass
    
    try: 
        search.update({'"'+''.join(col['first_name'])+' ' + ''.join(col['last_name']) + ' ' + ''.join(col['city']['title']) + ' ' + ''.join(col['bdate'])  + '"':53})
    except:
        pass
    
#education
    try: 
        search.update({'"'+''.join(col['first_name'])+' ' + ''.join(col['last_name']) + ' ' + ''.join(col['education']['university_name']) +  '"':53})
    except:
        pass

    try: 
        search.update({'"'+''.join(col['first_name'])+' ' + ''.join(col['last_name']) + ' ' + ''.join(col['education']['university_name']) + ' ' + ''.join(col['education']['faculty_name']) +  '"':63})
    except:
        pass
    
    try: 
        search.update({'"'+''.join(col['first_name'])+' ' + ''.join(col['last_name']) + '" "' + ''.join(col['education']['university_name']) +  '"':43})
    except:
        pass
    
#job

    try: 
        search.update({'"'+''.join(col['first_name'])+' ' + ''.join(col['last_name']) + ' ' + ''.join(col['career']['company']) +  '"':53})
    except:
        pass

    
    try: 
        search.update({'"'+''.join(col['first_name'])+' ' + ''.join(col['last_name']) + '" "' + ''.join(col['career']['company']) +  '"':43})
    except:
        pass

#phone
    
    try: 
        search.update({'"'+''.join(col['first_name'])+' ' + ''.join(col['last_name']) + '" "' + ''.join(col['contacts']['mobile_phone']) +  '"':93})
    except:
        pass
    
    try: 
        search.update({'"'+''.join(col['first_name'])+' ' + ''.join(col['last_name']) + '" "' + ''.join(col['contacts']['home_phone'])  +  '"':93})
    except:
        pass
    
#nickname

    try: 
        search.update({'"'+''.join(col['first_name'])+' ' + ''.join(col['last_name']) + '" "' + ''.join(col['nickname'])  +  '"':133})
    except:
        pass
    
    try: 
        search.update({'"'+''.join(col['nickname'])  +  '"':33})
    except:
        pass
    
 
    
    

   
    combs = []
    urling ={}
    for i in range(1, len(parametr)+1):
        els = [list(x) for x in itertools.combinations(parametr, i)]
        combs.extend(els)
    #count=0
    
    for st, v in search.items():
        print(st)
        
        
        
        driver = webdriver.Firefox()
        driver.implicitly_wait(30)
        #driver.maximize_window()

        driver.get("http://www.google.com")

        search_field = driver.find_element_by_name("q")

        search_field.send_keys(st)
        search_field.submit()
        driver.implicitly_wait(10)

        lists= driver.find_elements_by_class_name("r")
        bodyText = driver.find_element_by_tag_name('body').text
        if "Нет результатов для" not in bodyText: 
            print ("Found " + str(len(lists)) + " searches:")
        #i=0
            results = []
            for listitem in lists:
                text = listitem.get_attribute("innerHTML")
                m = re.search('href="(.*?)"', str(text))
                if m:
                    found = m.group(1)
   #print (found)
                    results.append(found)

                #i=i+1
                #if(i>15):
                 #   break
            urls = list(OrderedDict.fromkeys(results))
        else:
           print ("Found 0 searches:")
           urls = []
        driver.close()
        #print(results)
        
        #print(urls)
        #urls = results
        
        
        
        
        #urls=sr(st, stop=20, pause=1.0,only_standard=True,extra_params={'filter': '0'}, user_agent =  'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)')
        

        y =0
        
        for url in urls:
            if url in urling:
                urling.update({url:urling.setdefault(url)+v - v/20*2*y})
            else:
                urling.update({url:v - v/40*2*y})
            y = y+1
    print(urling)
    x = sorted(urling.items(), key=operator.itemgetter(1), reverse=True)
    k=[]

    for t in x:
        k.append(t[0])

    return k[:10]
