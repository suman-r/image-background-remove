from flask import Flask, render_template, request
from PIL import Image, ImageOps
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        # Get the uploaded file
        file = request.files['image']
        
        # Open the image with PIL
        image = Image.open(file.stream)
        
        # Remove the image background
        # (You'll need to replace this with your own image processing code)
        image = remove_background(image)
        
        # Convert the image to a format that can be displayed in HTML
        image_data = np.array(image)
        image_data = image_data.tobytes()
        image_src = 'data:image/png;base64,' + base64.b64encode(image_data).decode('ascii')
        
        # Render the HTML template with the processed image
        return render_template('result.html', image_src=image_src)
    
    # If the request method is GET, render the upload form
    return render_template('upload.html')

def remove_background(image):
    # This is where you would put your image processing code
    # to remove the image background
    # For example:
    image = ImageOps.invert(image)
    return image

if __name__ == '__main__':
    app.run(debug=True)
