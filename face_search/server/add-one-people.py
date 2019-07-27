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

login = ''
password =''
vk_id = ''
session  = vk.AuthSession(app_id = vk_id, user_login = login, user_password = password)
vkapi = vk.API(session, v= 5.87)

if len(sys.argv) < 2:
    print ("error")
    exit(1)
id = sys.argv[1]
print (id)
t = vkapi.users.get(user_ids = id , fields='domain, photo_200_orig')


if not os.path.exists("./.faces"):
    os.mkdir("./.faces")

for ter in t:
    p = requests.get(ter['photo_200_orig'])
    path = "".join(['./.faces/' ,str(ter['domain']),':', ter['first_name'] , '_' , ter['last_name'] , '.jpg'])
    out = open(path, "wb")
    out.write(p.content)
    out.close()
    face_detector = dlib.get_frontal_face_detector()
    image = cv2.imread(path)
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
    db.close()
    os.remove(path)
#        cv2.imwrite("./.faces/aligned_face_{}_{}_crop.jpg".format(path.replace('/', '_'), i), crop)




