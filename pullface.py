# imports
import face_recognition
# for image manipulation
from PIL import Image

# we are pulling faces from a group photo
# load image
image = face_recognition.load_image_file('./img/groups/team1.jpg')

# find face locations
image_face_locations = face_recognition.face_locations(image)

# iterate thru each face location in the pic
for image_face_location in image_face_locations:

    # get the values from each face loc
    top,right,bottom,left = image_face_location

    # make an array using the values
    face_image = image[top:bottom, left:right]

    # using PIL Image -- turn the array into an image
    pil_image = Image.fromarray(face_image)

    # Show the image
    pil_image.show()

    # save the image - since its a loop ensure they dont overwrite
    pil_image.save(f'{top}.jpg')