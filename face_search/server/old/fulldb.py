import subprocess
import vk
import requests
import psycopg2
import sys
import face_recognition
import dlib
import cv2
import os
import postgresql
import numpy as np
import urllib.request

login = ''
password =''
vk_id = ''
session  = vk.AuthSession(app_id = vk_id, user_login = login, user_password = password)
vkapi = vk.API(session, v= 5.87)
#fr = vkapi.friends.get(user_id =33514885, fields='photo_200_orig, nickname, contac, domain')
#print(fr)
l=0

handle = open("name.txt", "w")
for kol in range(14, 80):
    for se in range(1,2):
        try:
            fr = vkapi.users.search(sort = 0,sex = se, age_from=kol, age_to=kol, count=1000, has_photo=1 , fields='photo_200_orig,nickname, contact, domain', city = 112 )
        except:
            sys.exit()
        i = 0
        t = 0

        if not os.path.exists("./.faces"):
            os.mkdir("./.faces")

#file = open('test/nickname.txt', 'w')
        for ter in fr['items']:
            i=i+1
            l=l+1
   # print(i if (i%100==0) else pass  )
            print ( ter['first_name'] , '_' , ter['last_name'])
        #p = requests.get(ter['photo_200_orig'])
            path = "".join(['./.faces/' ,str(ter['domain']),':', ter['first_name'] , '_' , ter['last_name'] , '.jpg'])
        #out = open(path, "wb")
        #out.write(p.content)
        #out.close()
            face_detector = dlib.get_frontal_face_detector()
            try:
                resp = urllib.request.urlopen(ter['photo_200_orig'])
            except:
                break
            image = np.asarray(bytearray(resp.read()), dtype="uint8")
            image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        #image = cv2.imread(path)
            detected_faces = face_detector(image, 1)
            db = postgresql.open('pq://myuser:password@localhost:5432/mydatabase')
            for i, face_rect in enumerate(detected_faces):
                crop = image[face_rect.top():face_rect.bottom(), face_rect.left():face_rect.right()]
                encodings = face_recognition.face_encodings(crop)
                if (len(encodings) > 0):
                    query = "INSERT INTO vectors (file, vec_low, vec_high) VALUES ('{}', CUBE(array[{}]), CUBE(array[{}]))".format(
                        str(ter['domain']),
                        ','.join(str(s) for s in encodings[0][0:64]),
                        ','.join(str(s) for s in encodings[0][64:128]),
                    )
                    db.execute(query)
                    handle.write(str(ter['domain']))
      #  os.remove(path)
#        cv2.imwrite("./.faces/aligned_face_{}_{}_crop.jpg".format(path.replace('/', '_'), i), crop)

        print('count ', l, ' revision ', kol)
handle.close()
print(l)

