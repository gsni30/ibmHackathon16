import os
import requests
import json
# We'll render HTML templates and access data sent by POST
# using the request object from flask. Redirect and url_for
# will be used to redirect the user once the upload is done
# and send_from_directory will help us to send/show on the
# browser the file that the user just uploaded
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename

from os.path import join, dirname
from os import environ
from watson_developer_cloud import VisualRecognitionV3



# Initialize the Flask application
app = Flask(__name__)
summerWardrobe=[]
winterWardrobe=[]
# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/')
def index():
    return render_template('index.html')


# Route that will process the file upload
@app.route('/upload', methods=['POST'])
def upload():
    # Get the name of the uploaded file
    file1 = request.files['file1']
    file2 = request.files['file2']
    file3 = request.files['file3']
    file4 = request.files['file4']
    
    # Check if the file is one of the allowed types/extensions
    if file1 and allowed_file(file1.filename):#and file2 and file3 and file4 and allowed_file(file1.filename) and allowed_file(file2.filename) and allowed_file(file3.filename) and allowed_file(file4.filename):
        # Make the filename safe, remove unsupported chars
		print "sdfnjsdf"
		filename1 = secure_filename(file1.filename)
		filename2 = secure_filename(file2.filename)
		filename3 = secure_filename(file3.filename)
		filename4 = secure_filename(file4.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
		file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
		file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))
		file3.save(os.path.join(app.config['UPLOAD_FOLDER'], filename3))
		file4.save(os.path.join(app.config['UPLOAD_FOLDER'], filename4))
		filenames= [filename1, filename2, filename3, filename4]
        # Redirect the user to the uploaded_file route, which
        # will basicaly show on the browser the uploaded file
		visual_recognition = VisualRecognitionV3('2016-05-20', api_key='f11faf136164665418a93df1b6037bc4e5c4cc7e')
	# with open("/uploads/"+str(filename)) as image_file:
	# print (json.dumps(visual_recognition.classify(images_file="/uploads/"+str(filename), threshold=0, classifier_ids=['Summer_Winter_1816597639']), indent=2))
	# return send_from_directory(app.config['UPLOAD_FOLDER'],
    
		with open(join(dirname(__file__), '/uploads/'+str(filename1)), 'rb') as image_file:
			f1= visual_recognition.classify(images_file=image_file, threshold=0, classifier_ids=['Summer_Winter_1816597639'])
			print json.dumps(f1,indent=2)
			x0=f1['images']
			x1= x0[0]
			x2= x1['classifiers']
			x3= x2[0]
			x4= x3['classes']
			x5= x4[0]
			score= x5['score']
			if score>0.5:
				summerWardrobe.append(str(filename1))
			else:
				winterWardrobe.append(str(filename1))
		
		with open(join(dirname(__file__), '/uploads/'+str(filename2)), 'rb') as image_file:
			f2= visual_recognition.classify(images_file=image_file, threshold=0, classifier_ids=['Summer_Winter_1816597639'])
			x0=f2['images']
			x1= x0[0]
			x2= x1['classifiers']
			x3= x2[0]
			x4= x3['classes']
			x5= x4[0]
			score= x5['score']
			if score>0.5:
				summerWardrobe.append(str(filename2))
			else:
				winterWardrobe.append(str(filename2))
		
		with open(join(dirname(__file__), '/uploads/'+str(filename3)), 'rb') as image_file:
			f3= visual_recognition.classify(images_file=image_file, threshold=0, classifier_ids=['Summer_Winter_1816597639'])
			x0=f3['images']
			x1= x0[0]
			x2= x1['classifiers']
			x3= x2[0]
			x4= x3['classes']
			x5= x4[0]
			score= x5['score']
			if score>0.5:
				summerWardrobe.append(str(filename3))
			else:
				winterWardrobe.append(str(filename3))
	
		with open(join(dirname(__file__), '/uploads/'+str(filename4)), 'rb') as image_file:
			f4= visual_recognition.classify(images_file=image_file, threshold=0, classifier_ids=['Summer_Winter_1816597639'])
			x0=f4['images']
			x1= x0[0]
			x2= x1['classifiers']
			x3= x2[0]
			x4= x3['classes']
			x5= x4[0]
			score= x5['score']
			if score>0.5:
				summerWardrobe.append(str(filename4))
			else:
				winterWardrobe.append(str(filename4))
			# return redirect(url_for('uploaded_file', filename1=filename1, filename2= filename2, filename3= filename3, filename4= filename4))
		return render_template('city.html')	
# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload

# ')
@app.route('/uploads/<filename1>/<filename2>/<filename3>/<filename4>')
def uploaded_file(filename1,filename2, filename3, filename4):
	visual_recognition = VisualRecognitionV3('2016-05-20', api_key='f11faf136164665418a93df1b6037bc4e5c4cc7e')
	# with open("/uploads/"+str(filename)) as image_file:
	# print (json.dumps(visual_recognition.classify(images_file="/uploads/"+str(filename), threshold=0, classifier_ids=['Summer_Winter_1816597639']), indent=2))
	# return send_from_directory(app.config['UPLOAD_FOLDER'],
    
	with open(join(dirname(__file__), '/uploads/'+str(filename1)), 'rb') as image_file:
		f1= visual_recognition.classify(images_file=image_file, threshold=0, classifier_ids=['Summer_Winter_1816597639'])
		print json.dumps(f1,indent=2)
		x0=f1['images']
		x1= x0[0]
		x2= x1['classifiers']
		x3= x2[0]
		x4= x3['classes']
		x5= x4[0]
		score= x5['score']
		if score>0.5:
			summerWardrobe.append(str(filename1))
		else:
			winterWardrobe.append(str(filename1))
		
	with open(join(dirname(__file__), '/uploads/'+str(filename2)), 'rb') as image_file:
		f2= visual_recognition.classify(images_file=image_file, threshold=0, classifier_ids=['Summer_Winter_1816597639'])
		x0=f2['images']
		x1= x0[0]
		x2= x1['classifiers']
		x3= x2[0]
		x4= x3['classes']
		x5= x4[0]
		score= x5['score']
		if score>0.5:
			summerWardrobe.append(str(filename2))
		else:
			winterWardrobe.append(str(filename2))
		
	with open(join(dirname(__file__), '/uploads/'+str(filename3)), 'rb') as image_file:
		f3= visual_recognition.classify(images_file=image_file, threshold=0, classifier_ids=['Summer_Winter_1816597639'])
		x0=f3['images']
		x1= x0[0]
		x2= x1['classifiers']
		x3= x2[0]
		x4= x3['classes']
		x5= x4[0]
		score= x5['score']
		if score>0.5:
			summerWardrobe.append(str(filename3))
		else:
			winterWardrobe.append(str(filename3))
	
	with open(join(dirname(__file__), '/uploads/'+str(filename4)), 'rb') as image_file:
		f4= visual_recognition.classify(images_file=image_file, threshold=0, classifier_ids=['Summer_Winter_1816597639'])
		x0=f4['images']
		x1= x0[0]
		x2= x1['classifiers']
		x3= x2[0]
		x4= x3['classes']
		x5= x4[0]
		score= x5['score']
		if score>0.5:
			summerWardrobe.append(str(filename4))
		else:
			winterWardrobe.append(str(filename4))
			
	
	
@app.route('/take_city', methods=['POST'])
def weather():
	# Get the name of the uploaded file
	file = request.form['city']
	r = requests.post('http://api.openweathermap.org/data/2.5/forecast/city?q='+file+'&APPID=03e1355b70f3610690ba062f57e78103')
	# print r.json()
	s= r.json()
	s1= s['list']
	s2= s1[0]
	s3= s2['main']
	temp= s3['temp']
	weather=''
	if temp>293:
		weather='summer'
	else:
		weather='winter'
		
	print weather
	return redirect(url_for('show_images',message=weather))
	
@app.route('/showwardrobe')	
def show_images():
	if request.args['message']=='summer':
		if len(summerWardrobe)!=0:
			s=''
			for i in summerWardrobe:
				s= s+'<img src="uploads/'+i+'"/> <br/>'
			return s
		else:
			return ('No summer cloths in wardrobe')
	else:
		if len(winterWardrobe)!=0:
			s= ''
			for i in winterWardrobe:
				s= s+'<img src="uploads/'+i+'"/> <br/>'
			return s
		else:
			return ('No winter cloths in wardrobe')
if __name__ == '__main__':
    app.run(
        
        port=int("8090"),
        debug=True
    )
