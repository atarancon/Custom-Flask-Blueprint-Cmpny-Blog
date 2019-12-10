import os
from PIL import Image
from flask import url_for,current_app

def add_profile_pic (pic_upload , username):
    filename = pic_upload.filename
    ext_type = filename.split('.')[-1]
    #using username in name of file t store
    #"username.jpg"
    storage_filename = str(username)+'.'+ext_type
    #create special folder
    filepath = os.path.join(current_app.root_path,'static/profile_pics',storage_filename)
    #specific size
    output_size = (200,200)
    #grab image uploaded
    pic = Image.open(pic_upload)
    #resize to thumbnail
    pic.thumbnail(output_size)
    #save in folder
    pic.save(filepath)

    #return new name of profile picture 

    return storage_filename

    

