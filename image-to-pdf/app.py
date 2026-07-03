import os
from flask import Flask, render_template, request, send_file
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    files=request.files.getlist('images')
    if len(files) == 0:
        return "No files uploaded", 400
    image_paths=[]
    for file in files:  
        path=os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)
        image_paths.append(path)    
    images=[]
    for path in image_paths:
        img=Image.open(path).convert('RGB')
        images.append(img)
    output_pdf=os.path.join(OUTPUT_FOLDER, 'converted.pdf')
    images[0].save(output_pdf, save_all=True, append_images=images[1:])
    return send_file(output_pdf, as_attachment=True)
if __name__ == '__main__':
    app.run(debug=True)