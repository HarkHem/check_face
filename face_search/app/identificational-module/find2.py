
import sys
import dlib
import cv2
import face_recognition
import os
import psycopg2
import re

def fin(strk):

    file_name = strk
    face_detector = dlib.get_frontal_face_detector()
    image = cv2.imread(file_name)
    detected_faces = face_detector(image, 1)

#print("Found {} faces in the image file {}".format(len(detected_faces), file_name))

#if not os.path.exists("./.faces"):
#    os.mkdir("./.faces")

    connection_db = psycopg2.connect("user='myuser' password='*******' host='*********' dbname='mydatabase'")
    db=connection_db.cursor()

    for i, face_rect in enumerate(detected_faces):

        crop = image[face_rect.top():face_rect.bottom(), face_rect.left():face_rect.right()]

        encodings = face_recognition.face_encodings(crop)
        threshold = 0.55
        if len(encodings) > 0:
            query = "SELECT file FROM vectors WHERE sqrt(power(CUBE(array[{}]) <-> vec_low, 2) + power(CUBE(array[{}]) <-> vec_high, 2)) <= {} ".format(
                ','.join(str(s) for s in encodings[0][0:63]),
                ','.join(str(s) for s in encodings[0][64:127]),
                threshold,
            ) + \
                "ORDER BY sqrt((CUBE(array[{}]) <-> vec_low) + (CUBE(array[{}]) <-> vec_high)) ASC LIMIT 1".format(
                ','.join(str(s) for s in encodings[0][0:63]),
                ','.join(str(s) for s in encodings[0][63:127]),
            )
            #print(query)
            db.execute(query)
            #print("The number of parts: ", db.rowcount)
            row = db.fetchone()

            while row is not None:
                #print(row)
                result = re.search(r"'(.*?)'", str(row))
                terv = result.group(0)
                terv = terv[1:len(terv)-1]
                print ("vk.com/"+terv)
                db.close()
                if connection_db is not None:
                    connection_db.close()
                return ("vk.com/"+terv)
                row = db.fetchone()

            db.close()
        else:
            #print("No encodings")
            return(None)

    if connection_db is not None:
        connection_db.close()
