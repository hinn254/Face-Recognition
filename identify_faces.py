import face_recognition
from PIL import ImageDraw,Image

# load image
bill_image = face_recognition.load_image_file('./img/known/Bill Gates.jpg')

# face_encodings
bill_face_encodings = face_recognition.face_encodings(bill_image)[0]

# load image
steve_image = face_recognition.load_image_file('./img/known/Steve Jobs.jpg')

# face encodings
steve_face_encodings = face_recognition.face_encodings(steve_image)[0]

known_face_encodings = [
    bill_face_encodings,
    steve_face_encodings
]

known_face_names = [
    'Bill Gates',
    'Steve Jobs'
]

# load image to find identical faces
group_image = face_recognition.load_image_file('./img/groups/bill-steve.jpg')

# face locations
group_face_locations = face_recognition.face_locations(group_image)

# finding each faces encoding
group_face_encodings = face_recognition.face_encodings(group_image, group_face_locations)

# convert to PIL format

pil_image = Image.fromarray(group_image)

# create a PIL draw instance
draw = ImageDraw.Draw(pil_image)

# loop thru faces in group image
for (top,right,bottom,left), face_encoding in zip(group_face_locations, group_face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = 'Unknown Person'

    # if match 
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    
    # Draw Box
    draw.rectangle(((left,top),(right, bottom)),outline=(0,0,0))

    # Draw label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height -10),(right, bottom)),fill=(0,0,0),outline=(0,0,0))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255,255,255,255))

del draw

# Display the image
pil_image.show()

# Save image
pil_image.save('identify.jpg')