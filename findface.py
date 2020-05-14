import face_recognition

# Load the image 
img = face_recognition.load_image_file('./img/groups/team1.jpg')

# find the face locations of each face - list of tuple
img_face_locations = face_recognition.face_locations(img)

# length of the list == no of faces
print(f"There are {len(img_face_locations)} people.")