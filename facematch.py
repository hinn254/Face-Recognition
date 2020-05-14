import face_recognition

# load known image 
img_of_bill = face_recognition.load_image_file('./img/known/Bill Gates.jpg')

# Known image encodings
bill_face_encodings = face_recognition.face_encodings(img_of_bill)[0]

# load unknown img
img_to_compare = face_recognition.load_image_file('./img/known/Barack Obama.jpg')

# unknown img encoding
img_face_encodings = face_recognition.face_encodings(img_to_compare)[0]

# compare to see if similar - returns a list,the first item in the list is a boolean value
comparison = face_recognition.compare_faces([bill_face_encodings],img_face_encodings)[0]

# if true - match and if false - no match
if comparison:
    print('Image of Bill')

else:
    print('This is not Bill')