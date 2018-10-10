import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
import face_recognition
import math
image = face_recognition.load_image_file("../unknown_pictures/test3.jpg")
face_locations = face_recognition.face_locations(image)


	

im = np.array(Image.open('../unknown_pictures/test3.jpg'), dtype=np.uint8)

# Create figure and axes
fig,ax = plt.subplots(1)

# Display the image
ax.imshow(im)

for i in face_locations:
# Create a Rectangle patch
	rect = patches.Rectangle((i[1],i[0]), - math.fabs(i[1]-i[3]), math.fabs(i[0]-i[2]),linewidth=1,edgecolor='r',facecolor='none')

# Add the patch to the Axes
	ax.add_patch(rect)

plt.show()
