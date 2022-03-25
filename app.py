from flask import Flask, render_template, request, jsonify, json
import numpy as np

app = Flask(__name__)

def findCoordinates(imageDimension, corners):
    rows, columns = imageDimension[0], imageDimension[1] 
    # sort corners first to find bottom left and top right corner
    corners.sort()  
    bL, tR = corners[0], corners[3]  

    # find starting and ending X and Y coordinates where allows columns and rows of image
    x1, x2 = bL[0], tR[0]  
    y1, y2 = bL[1], tR[1]  
    
    # find allowed x and y coordinates of pixels 
    x = np.linspace(x1,x2,columns)
    y = np.linspace(y1,y2,rows)[::-1]

    # find coordinates of every pixel in 3D array
    xx, yy = np.meshgrid(x, y)
    zz= np.stack([xx, yy], axis= -1)
    return zz

@app.route('/', methods = ['POST', 'GET'])
def image():   
    if request.method == 'POST':        
        d = request.form
        imageDimension = int(d['r']), int(d['c'])
        corner1 = float(d['x1']), float(d['y1'])
        corner2 = float(d['x2']), float(d['y2'])
        corner3 = float(d['x3']), float(d['y3'])
        corner4 = float(d['x4']), float(d['y4'])
        corners = [corner1, corner2, corner3, corner4]
        
        zz = np.round(findCoordinates(imageDimension, corners), 2)        
        solution = zz.tolist()    
        return render_template('image.html', solution=solution, imageDimension=imageDimension, corners=corners)

    else:
        return render_template('image.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')