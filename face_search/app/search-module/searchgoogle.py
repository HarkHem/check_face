from googlesearch import search as sr
import re
import itertools
import operator
import time
import random
import urllib.request
from random import randint


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
        search.update({'"'+''.join(col['first_name'])+'" "' + ''.join(col['last_name']) + '" "' + ''.join(col['city']['title']) + '" ':15})
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

    for i in range(1, len(parametr)+1):
        els = [list(x) for x in itertools.combinations(parametr, i)]
        combs.extend(els)
    #count=0
    urling ={}
    for st, v in search.items():
        print(st)
        urls=sr(st, stop=20, pause=1.0,only_standard=True,extra_params={'filter': '0'}, user_agent =  'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)')
        
        #if count % 100 != 0:
        #    time.sleep(random.randint(45,62))
        #else:
        #    time.sleep(random.randint(180,240))

        #count +=1
        
        
        #   time.sleep(random.randint(45, 62))
        y =0
        #blacklist = ["facebook.com","vk.com"]
        #urls = list( k for k in urls if k not in blacklist )
        #time.sleep(random.randint(15, 25))
        for url in urls:
            if url in urling:
                urling.update({url:urling.setdefault(url)+v - v/20*2*y})
            else:
                urling.update({url:v - v/40*2*y})
            y = y+1
 
    x = sorted(urling.items(), key=operator.itemgetter(1), reverse=True)
    k=[]

    for t in x:
        k.append(t[0])

    return k[:10]
