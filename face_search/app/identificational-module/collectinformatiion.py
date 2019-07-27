import subprocess
import vk
import requests
import psycopg2
import sys
import face_recognition
def collect(str):
    login = ''
    password =''
    vk_id = ''
    str=str[7:]
    if str[0:2]=="id":
        str=str[2:]
    print (str)
    session  = vk.AuthSession(app_id = vk_id, user_login = login, user_password = password)
    vkapi = vk.API(session, v= 5.87)
    fr = vkapi.users.get(user_ids =str, fields='first_name,  last_name, nickname, maiden_name, sex,bdate , relation,city,contacts, activities,  career, exports, domain, country, home_town,contacts, site, education, universities, schools ', name_case = 'nom')
    print (fr)
    return(fr[0])
#print (fr[0]['first_name'])
