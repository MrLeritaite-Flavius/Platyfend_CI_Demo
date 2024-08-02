import os
from flask import Blueprint, request
from werkzeug.utils import secure_filename

file_upload_blueprint = Blueprint('welcome', __name__)
UPLOAD_FOLDER = "C:\\uploads"


@file_upload_blueprint.route('/upload-meme', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(UPLOAD_FOLDER, filename))

        return 'Meme uploaded successfully'
    else:
        return '''
            <html>
               <body>
                  <form  method = "POST" enctype = "multipart/form-data">
                     <input type = "file" name = "file" />
                     <input type = "submit"/>
                  </form>   
               </body>
            </html>
        '''
