#FILENAME: afractalgenerator_v3.py
#AUTHOR: Jim Johnston - jimmy.johnston@gmail.com (C)2019-2020
#CREATED: 12-19-2019
#LAST MODIFIED: 2-27-2020
#DESC: A library that generates two styles of fractals IFS/HeeBGB (a flavored IFS) in black & white and color
#RESOURCES: see examples.py on usage
#VERSION: 3.3
#NOTES: This version works and is first version that only relies on drawIFS function, next version code will be condensed.
#PRODUCTION LEVEL: Ready

from fractalgraphics import *
from math import cos,sin,pi,radians,sqrt

def affine(r,s,theta,phi,e,f):
	#AFFINE object expects 6 inputs written as affine(r,s,theta,phi,e,f)
	#r,s:-> scales both the x and y-axis such that 0<r<1 and 0<s<1
	#theta,phi:-> component rotations in degrees
	#e,f:-> vertical and horizontal transformations such that 0<e<1 and 0<f<1
	#returns an affine contraction map in the form [[r*cos(theta),-s*sin(phi),e], [r*sin(theta),s*cos(phi),f]]
	
	theta = radians(theta) #convert degrees to radians
	phi = radians(phi)
	#X = [r*cos(theta),-s*sin(phi),e] #note: *pi is included to transform the image to position correctly on a computer screen
	#Y = [r*sin(phi),s*cos(theta),f]
	X = [r*cos(phi),-s*sin(theta),e] #note: *pi is included to transform the image to position correctly on a computer screen
	Y = [r*sin(phi),s*cos(theta),f]
	return([X,Y])
	
def affinecolor(r,s,theta,phi,e,f,color):
	#AFFINECOLOR object expects 7 inputs see AFFINE for first 6 inputs
	#color:->each affine mapping is assigned a color, this function embeds the color into the affine mapping as a third component
	#returns an affine contraction map in the form [[r*cos(theta),-s*sin(phi),e], [r*sin(theta),s*cos(phi),f], color]
	a = affine(r,s,theta,phi,e,f)
	a.append(color)
	return(a)
	
def transform(shapeobject,win,color="on"):
	#TRANSFORM function that takes in a shape (set of points that define it) and transforms it by 90 degrees to display properly on screen	
	transformedpoints = []
	angularshift = 90
	size = win.size-1
	i=1 #used for print testing only, delete
	for points in shapeobject: 
		tsetofpoints = []
		for point in points:
			X = point[0]
			Y = point[1]
			newX = 1*size*X
			#newX = size*X
			newY = -1*size*Y+size
			#newY = size*Y
			if color=="on":
				Z = point[2] #color field
				tsetofpoints.append([newX,newY,Z])
			else:
				tsetofpoints.append([newX,newY])
		i+=1
		transformedpoints.append(tsetofpoints)
	return(transformedpoints)	
	
def MrFace():
	#pointwise defintion of Mr Face object. 
	#MRFACE[0] and MRFACE[1] define polygon points that draw the square body
	#MRFACE[2] defines the center of the open eye and the point on circular eye at the 3 o'clock position
	#MRFACE[3] defines the end points of the closed eye
	#MRFACE[4] defines the end points of the mouth
	#returns the set of points that define Mr Face
	
	MRFACE = [[[0,0],[0,1]], [[1,1],[1,0]], [[1/3,2/3],[1/2,2/3]], [[7/12,2/3],[3/4,2/3]], [[1/4,1/4],[3/4,1/4]]]
	return(MRFACE)
	
def MrSquare():
	#pointwise definition of Mr Square object. Mr Square is Mr Face without any facial features.
	#MRSQUARE[0] and MRSQUARE[1] define polygon points that draw the square body
	#returns the set of points that define Mr Square
	
	MRSQUARE = [[[0,0],[0,1]],[[1,1],[1,0]]]
	return(MRSQUARE)
	
def MrsLine():
	#pointwise definition of Mrs Line object. 
	#MRSLINE[0] and MRSLINE[1] define end points that draw the line
	#returns the set of points that define Mrs Line
	
	MRSLINE = [[[0,0],[1,0]]]
	return(MRSLINE)
	
def _drawMrFace(MRFACE,win):
	#not to be called directly
	#inputs a single set of points that defines Mr Face object and a window to draw on
	#converts the set of points into graphics.py objects (Polygon, Circle, Line) and draws them to the window 
	#see MrFace() for a better understanding of the input points
	
	##mr face body
	win.Polygon((MRFACE[0][0][0],MRFACE[0][0][1]),(MRFACE[0][1][0],MRFACE[0][1][1]),(MRFACE[1][0][0],MRFACE[1][0][1]),(MRFACE[1][1][0],MRFACE[1][1][1]),"white","black")
	##mr face open eye
	win.Circle((MRFACE[2][0][0],MRFACE[2][0][1]),sqrt((MRFACE[2][0][0]-MRFACE[2][1][0])**2 + (MRFACE[2][0][1]-MRFACE[2][1][1])**2),"white","black")
	##mr face closed eye
	win.Line((MRFACE[3][0][0],MRFACE[3][0][1]),(MRFACE[3][1][0],MRFACE[3][1][1]))
	##mr face mouth
	win.Line((MRFACE[4][0][0],MRFACE[4][0][1]),(MRFACE[4][1][0],MRFACE[4][1][1]))
	
def _drawMrFaceColor(MRFACE,win):
	#not to be called directly
	#inputs a single set of points that defines Mr Face object and a window to draw on
	#converts the set of points into graphics.py objects (Polygon, Circle, Line) and draws them to the window 
	#see MrFace() for a better understanding of the input points
	
	##mr face body
	win.Polygon((MRFACE[0][0][0],MRFACE[0][0][1]),(MRFACE[0][1][0],MRFACE[0][1][1]),(MRFACE[1][0][0],MRFACE[1][0][1]),(MRFACE[1][1][0],MRFACE[1][1][1]),MRFACE[0][0][2],"black")
	##mr face open eye
	win.Circle((MRFACE[2][0][0],MRFACE[2][0][1]),sqrt((MRFACE[2][0][0]-MRFACE[2][1][0])**2 + (MRFACE[2][0][1]-MRFACE[2][1][1])**2),MRFACE[0][0][2],"black")
	##mr face closed eye
	win.Line((MRFACE[3][0][0],MRFACE[3][0][1]),(MRFACE[3][1][0],MRFACE[3][1][1]))
	##mr face mouth
	win.Line((MRFACE[4][0][0],MRFACE[4][0][1]),(MRFACE[4][1][0],MRFACE[4][1][1]))

def _drawSquare(MRSQUARE,win):
	#not to be called directly
	#inputs a single set of points that defines Mr Square object and a window to draw on
	#converts the set of points into graphics.py polygon object and draws it to the window 
	#see MrSquare() for a better understanding of the input points
	
	#mr body 
	win.Polygon((MRSQUARE[0][0][0],MRSQUARE[0][0][1]),(MRSQUARE[0][1][0],MRSQUARE[0][1][1]),(MRSQUARE[1][0][0],MRSQUARE[1][0][1]),(MRSQUARE[1][1][0],MRSQUARE[1][1][1]),"white","black")
	
def _drawMrSquareColor(MRSQUARE,win):
	#not to be called directly
	#mrs body
	win.Polygon((MRSQUARE[0][0][0],MRSQUARE[0][0][1]),(MRSQUARE[0][1][0],MRSQUARE[0][1][1]),(MRSQUARE[1][0][0],MRSQUARE[1][0][1]),(MRSQUARE[1][1][0],MRSQUARE[1][1][1]),MRSQUARE[0][0][2])
	
def _drawLine(aLine,win):
	#not to be called directly
	#inputs a single set of points that defines a Line object and a window to draw on
	#converts the set of points into graphics.py line object and draws it to the window 
	
	win.Line((aLine[0][0][0],aLine[0][0][1]),(aLine[0][1][0],aLine[0][1][1]))
	
	
def _drawPoint(aPoint,win,setColor="black"):
	#not to be called directly
	#inputs a single set of points that defines a Point object and a window to draw on
	#converts the set of points into graphics.py Point object and draws it to the window 
	
	win.Point((aPoint[0][0][0],aPoint[0][0][1]),setColor)
	#aPoint_point = Point(aPoint[0][0][0],aPoint[0][0][1])
	#aPoint_point.draw(win)
	
def defaultcolormap(num_of_colors):
	colormap = ['black' for i in range(num_of_colors)]
	return(colormap)
	
def mapcolormaptoaffinemap(affinemaps,colormaps):
	#if "bw" not in colormaps:
	i = 0
	while i<len(affinemaps):
		affinemaps[i].append(colormaps[i])
		i+=1
	#print(affinemaps)
	return(affinemaps)
		
def convertHeeBGBtoAffine(instructions,colormap=None):
	num_of_instructions = len(instructions)
	#####error check######
	if int(sqrt(num_of_instructions))!=sqrt(num_of_instructions):
		print("error:202 - check that the number of affine maps sent to drawHeebgb is a square number")
		return("input error, the number of instructions should be a squared integer")
	#####
	
	num_of_rows = num_of_cols = sqrt(num_of_instructions)
	affinemaps = []
	##### convert heebgb instructions into affine map definitions #####
	for i in range(num_of_instructions):
		row = i//num_of_rows
		col = i%num_of_cols
		if instructions[i]=="up": 
			r = 1/num_of_cols
			s = 1/num_of_rows
			theta = 0
			phi = 0
			e = r*col
			f = s*row
			#affinemaps.append(affine(r,s,theta,phi,e,f))
			if colormap==None:
				affinemaps.append(affine(r,s,theta,phi,e,f))
			else:
				aff = affine(r,s,theta,phi,e,f)
				aff.append(colormap[i])
				affinemaps.append(aff)
		elif instructions[i]=="left":
			r = 1/num_of_cols
			s = 1/num_of_rows
			theta = 90
			phi = 90
			e = r*col+r
			f = s*row
			#affinemaps.append(affine(r,s,theta,phi,e,f))
			if colormap==None:
				affinemaps.append(affine(r,s,theta,phi,e,f))
			else:
				aff = affine(r,s,theta,phi,e,f)
				aff.append(colormap[i])
				affinemaps.append(aff)
		elif instructions[i]=="right":
			r = 1/num_of_cols
			s = 1/num_of_rows
			theta = -90
			phi = -90
			e = r*col
			f = s*row+s
			#affinemaps.append(affine(r,s,theta,phi,e,f))
			if colormap==None:
				affinemaps.append(affine(r,s,theta,phi,e,f))
			else:
				aff = affine(r,s,theta,phi,e,f)
				aff.append(colormap[i])
				affinemaps.append(aff)
		elif instructions[i]=="down":
			r = 1/num_of_cols
			s = 1/num_of_rows
			theta = 0
			phi = 0
			e = r*col
			f = s*row+s
			#affinemaps.append(affine(r,-s,theta,phi,e,f))
			if colormap==None:
				affinemaps.append(affine(r,-s,theta,phi,e,f))
			else:
				aff = affine(r,-s,theta,phi,e,f)
				aff.append(colormap[i])
				affinemaps.append(aff)
		elif instructions[i]=="-up":
			r = 1/num_of_cols
			s = 1/num_of_rows
			theta = 0
			phi = 0
			e = r*col+r
			f = s*row
			#affinemaps.append(affine(-r,s,theta,phi,e,f))
			if colormap==None:
				affinemaps.append(affine(-r,s,theta,phi,e,f))
			else:
				aff = affine(-r,s,theta,phi,e,f)
				aff.append(colormap[i])
				affinemaps.append(aff)
		elif instructions[i]=="-left":
			r = 1/num_of_cols
			s = 1/num_of_rows
			theta = 90
			phi = 90
			e = r*col+r
			f = s*row+s
			#affinemaps.append(affine(-r,s,theta,phi,e,f))
			if colormap==None:
				affinemaps.append(affine(-r,s,theta,phi,e,f))
			else:
				aff = affine(-r,s,theta,phi,e,f)
				aff.append(colormap[i])
				affinemaps.append(aff)
		elif instructions[i]=="-right":
			r = 1/num_of_cols
			s = 1/num_of_rows
			theta = -90
			phi = -90
			e = r*col
			f = s*row
			#affinemaps.append(affine(-r,s,theta,phi,e,f))
			if colormap==None:
				affinemaps.append(affine(-r,s,theta,phi,e,f))
			else:
				aff = affine(-r,s,theta,phi,e,f)
				aff.append(colormap[i])
				affinemaps.append(aff)
		elif instructions[i]=="-down":
			r = 1/num_of_cols
			s = 1/num_of_rows
			theta = 180
			phi = 180
			e = r*col+r
			f = s*row+s
			if colormap==None:
				affinemaps.append(affine(r,s,theta,phi,e,f))
			else:
				aff = affine(r,s,theta,phi,e,f)
				aff.append(colormap[i])
				affinemaps.append(aff)
		#print(affinemaps)
		
	return(affinemaps)		
	
def drawIFS(listofmaps,maxiter,**kwargs):
	#drawIFS is an Iterated Function System generator
	#drawIFS accepts three inputs: listofmaps, maxiter and seeds
	#listofmaps is a list of affine contraction mappings
	#maxiter is the amount of iterations you would like the IFS to run
	#seeds must be any of the following: "MrFace", "Line", "Square", "Point" (default)
	#returns a GUI image of resulting fractal at a specific iteration
	
	###### Gather data from optional arguments ########
	args = dict(**kwargs)
	if 'seed' in args:
		seed = args['seed']
	else:
		seed = "Square"
		
	if 'size' in args:
		size = args['size']
	else:
		size=(1000,1000)
		
	if 'colormap' in args:
		colormap = args['colormap']
	else:
		colormap = None#defaultcolormap(len(listofmaps))
		#print(colormap,len(colormap)) #delete when done using
		
	if 'filename' in args:
		filename = args['filename']
	else:
		filename = None
		
	if 'method' in args:
		method = args['method']
	else:
		method = "affine"
	##########################
	
	
	##### user directed settings #####
	if seed=="MrFace":
		currentdomain = [MrFace()] #starting domain is a set of points in R^2:[0,1]x[0,1] that define Mr Face object
		num_of_body_parts = 5 #see MrFace()
	elif seed=="Line":
		currentdomain = [MrsLine()] #starting domain is single line y=0 such that x in [0,1]
		num_of_body_parts = 1 #see MrsLine(
	elif seed=="Square":
		currentdomain = [MrSquare()] #starting domain is a set of points in R^2:[0,1]x[0,1] that define Mr Square object
		num_of_body_parts = 2 #see MrSquare()
	else: #currently everything else is set to Square object
		#currentdomain = [[[[0,0],[0,0]]]]; #starting domain is single point at origin, programmer note: the structure of this point is not ideal but is written to accommodate the other methods employed
		#num_of_body_parts = 1
		seed=="Square"
		currentdomain = [MrSquare()] #starting domain is a set of points in R^2:[0,1]x[0,1] that define Mr Square object
		num_of_body_parts = 2 #see MrSquare()
			
	if method=="HeeBGB":
		listofmaps = convertHeeBGBtoAffine(listofmaps)
		#listofmaps = mapcolormaptoaffinemap(listofmaps,colormap)
	elif method=="HeeBGBcolor":
		#print(listofmaps)
		listofmaps = convertHeeBGBtoAffine(listofmaps,colormap)
		#print(listofmaps)
	
	##########
	
	##### graphics settings #####
	win = GraphImage(size[0],size[1]) #creates an image instance to digitally draw on; window default size is 500x500, default background is white
	#############################
	
	num_of_affinemaps = len(listofmaps) #number of affine maps/instructions
	
	if 'colormap' in args:
		#jimmy you clean up this mess - you complete one iteration so you can map colors at the same time, which is unneeded now that you have a function that does the mapping automatically
		#you then have a whole nother set of for loops that iterate the remaining operations, toooooo much
		num_of_points = len(currentdomain)
		futuredomain = [] #a storage variable
		for mapnumber in range(num_of_affinemaps):
			for p in range(num_of_points):
				newobject = []
				for z in range(num_of_body_parts): 
					#apply affine mapping to current set of points (x,y) where currentdomain[p][z] is a specific point
					x1 = listofmaps[mapnumber][0][0]*currentdomain[p][z][0][0]+listofmaps[mapnumber][0][1]*currentdomain[p][z][0][1]+listofmaps[mapnumber][0][2]
					y1 = listofmaps[mapnumber][1][0]*currentdomain[p][z][0][0]+listofmaps[mapnumber][1][1]*currentdomain[p][z][0][1]+listofmaps[mapnumber][1][2]
					x2 = listofmaps[mapnumber][0][0]*currentdomain[p][z][1][0]+listofmaps[mapnumber][0][1]*currentdomain[p][z][1][1]+listofmaps[mapnumber][0][2]
					y2 = listofmaps[mapnumber][1][0]*currentdomain[p][z][1][0]+listofmaps[mapnumber][1][1]*currentdomain[p][z][1][1]+listofmaps[mapnumber][1][2]
					if method=="HeeBGBcolor":
						newobject.append([[x1,y1,listofmaps[mapnumber][2]],[x2,y2,listofmaps[mapnumber][2]]]) #add point to the set that defines an object (think MrFace)
					else:
						newobject.append([[x1,y1],[x2,y2]]) #add point to the set that defines an object (think MrFace)
				futuredomain.append(newobject)	#once the object has been completely transformed it is added to the set of objects that define this iteration
		currentdomain = futuredomain #the next iteration will apply affine mappings to this set of objects
		
		for j in range(maxiter-1): #was maxiter-1 2.26.2020
			num_of_points = len(currentdomain)
			futuredomain = [] #a storage variable
			for p in range(num_of_points):
				for mapnumber in range(num_of_affinemaps):
					newmrsquare = []
					for z in range(num_of_body_parts): #1 body parts where the body part is a polygon of 4 points
						#apply mapping to current body part
						x1 = listofmaps[mapnumber][0][0]*currentdomain[p][z][0][0]+listofmaps[mapnumber][0][1]*currentdomain[p][z][0][1]+listofmaps[mapnumber][0][2]
						y1 = listofmaps[mapnumber][1][0]*currentdomain[p][z][0][0]+listofmaps[mapnumber][1][1]*currentdomain[p][z][0][1]+listofmaps[mapnumber][1][2]
						x2 = listofmaps[mapnumber][0][0]*currentdomain[p][z][1][0]+listofmaps[mapnumber][0][1]*currentdomain[p][z][1][1]+listofmaps[mapnumber][0][2]
						y2 = listofmaps[mapnumber][1][0]*currentdomain[p][z][1][0]+listofmaps[mapnumber][1][1]*currentdomain[p][z][1][1]+listofmaps[mapnumber][1][2]
						newmrsquare.append([[x1,y1,currentdomain[p][z][0][2]],[x2,y2,currentdomain[p][z][0][2]]])
					futuredomain.append(newmrsquare)
					
			currentdomain = futuredomain
	else: #black & white fractal
		for j in range(maxiter):
			num_of_points = len(currentdomain)
			futuredomain = [] #a storage variable
			for mapnumber in range(num_of_affinemaps):
				for p in range(num_of_points):
					newobject = []
					for z in range(num_of_body_parts): 
						#apply affine mapping to current set of points (x,y) where currentdomain[p][z] is a specific point
						x1 = listofmaps[mapnumber][0][0]*currentdomain[p][z][0][0]+listofmaps[mapnumber][0][1]*currentdomain[p][z][0][1]+listofmaps[mapnumber][0][2]
						y1 = listofmaps[mapnumber][1][0]*currentdomain[p][z][0][0]+listofmaps[mapnumber][1][1]*currentdomain[p][z][0][1]+listofmaps[mapnumber][1][2]
						x2 = listofmaps[mapnumber][0][0]*currentdomain[p][z][1][0]+listofmaps[mapnumber][0][1]*currentdomain[p][z][1][1]+listofmaps[mapnumber][0][2]
						y2 = listofmaps[mapnumber][1][0]*currentdomain[p][z][1][0]+listofmaps[mapnumber][1][1]*currentdomain[p][z][1][1]+listofmaps[mapnumber][1][2]
						newobject.append([[x1,y1],[x2,y2]]) #add point to the set that defines an object (think MrFace)
					futuredomain.append(newobject)	#once the object has been completely transformed it is added to the set of objects that define this iteration
			currentdomain = futuredomain #the next iteration will apply affine mappings to this set of objects
		
	if colormap==None:
		if seed=="MrFace":
			for m in currentdomain:
				MRFACE = transform(m,win,color="off") #prepares object to fit the dimension and position of a digital image
				_drawMrFace(MRFACE,win)
		elif seed=="Line":
			for m in currentdomain:
				LINE = transform(m,win,color="off")
				_drawLine(LINE,win)
		elif seed=="Square":
			for m in currentdomain:
				SQUARE = transform(m,win,color="off")
				_drawSquare(SQUARE,win)
		else: #everything else is set to Point method
			for m in currentdomain:
				#doesn't seem to work
				POINT = transform(m,win,color="off")
				_drawPoint(POINT,win)
	else:
		if seed=="Square":
			for m in currentdomain:
				SQUARE = transform(m,win,color="on")
				_drawMrSquareColor(SQUARE,win)
		elif seed=="MrFace":
			for m in currentdomain:
				MRFACE = transform(m,win,color="on")
				_drawMrFaceColor(MRFACE,win)
	status = win.savejpg(filename)
	return(status)
'''	
def drawColorIFS(listofmaps,maxiter,filename,size=(1000,1000)):
	currentdomain = [MrSquare()] #starting domain is single point at origin
	num_of_affinemaps = len(listofmaps) #number of affine maps
	
	#####graphics#####
	win = GraphImage(size[0],size[1]) #default background is white
	#win.setCoords(-1/5,-1/5,6/5,6/5) #call when this code is finally written
	##################
	
	#####map color to point#####
	num_of_points = len(currentdomain)
	futuredomain = [] #a storage variable
	for p in range(num_of_points):
		for mapnumber in range(num_of_affinemaps):
			newmrsquare = []
			for z in range(2): #1 body parts where the body part is a polygon of 4 points
				#apply mapping to current body part
				x1 = listofmaps[mapnumber][0][0]*currentdomain[p][z][0][0]+listofmaps[mapnumber][0][1]*currentdomain[p][z][0][1]+listofmaps[mapnumber][0][2]
				y1 = listofmaps[mapnumber][1][0]*currentdomain[p][z][0][0]+listofmaps[mapnumber][1][1]*currentdomain[p][z][0][1]+listofmaps[mapnumber][1][2]
				x2 = listofmaps[mapnumber][0][0]*currentdomain[p][z][1][0]+listofmaps[mapnumber][0][1]*currentdomain[p][z][1][1]+listofmaps[mapnumber][0][2]
				y2 = listofmaps[mapnumber][1][0]*currentdomain[p][z][1][0]+listofmaps[mapnumber][1][1]*currentdomain[p][z][1][1]+listofmaps[mapnumber][1][2]
				newmrsquare.append([[x1,y1,listofmaps[mapnumber][2]],[x2,y2,listofmaps[mapnumber][2]]])
			futuredomain.append(newmrsquare)
	currentdomain = futuredomain
	##########
	
	for j in range(maxiter-1):
		num_of_points = len(currentdomain)
		futuredomain = [] #a storage variable
		for p in range(num_of_points):
			for mapnumber in range(num_of_affinemaps):
				newmrsquare = []
				for z in range(2): #1 body parts where the body part is a polygon of 4 points
					#apply mapping to current body part
					x1 = listofmaps[mapnumber][0][0]*currentdomain[p][z][0][0]+listofmaps[mapnumber][0][1]*currentdomain[p][z][0][1]+listofmaps[mapnumber][0][2]
					y1 = listofmaps[mapnumber][1][0]*currentdomain[p][z][0][0]+listofmaps[mapnumber][1][1]*currentdomain[p][z][0][1]+listofmaps[mapnumber][1][2]
					x2 = listofmaps[mapnumber][0][0]*currentdomain[p][z][1][0]+listofmaps[mapnumber][0][1]*currentdomain[p][z][1][1]+listofmaps[mapnumber][0][2]
					y2 = listofmaps[mapnumber][1][0]*currentdomain[p][z][1][0]+listofmaps[mapnumber][1][1]*currentdomain[p][z][1][1]+listofmaps[mapnumber][1][2]
					newmrsquare.append([[x1,y1,currentdomain[p][z][0][2]],[x2,y2,currentdomain[p][z][0][2]]])
				futuredomain.append(newmrsquare)
				
		currentdomain = futuredomain

	for m in currentdomain:
		MRSQUARE = transform(m,win) #prepares object to fit the dimension and position of a digital image
		_drawMrSquareColor(MRSQUARE,win)
	
	status = win.savejpg(filename)
	return(status)
	
def drawHeebgb(instructions,maxiter,seed,filename,size=(1000,1000)):
	num_of_instructions = len(instructions)
	#####error check######
	if int(sqrt(num_of_instructions))!=sqrt(num_of_instructions):
		print("error:202 - check that the number of affine maps sent to drawHeebgb is a square number")
		return("input error, the number of instructions should be a squared integer")
	#####
	
	num_of_rows = num_of_cols = sqrt(num_of_instructions)
	affinemaps = []
	##### convert heebgb instructions into affine map definitions #####
	for i in range(num_of_instructions):
		row = i//num_of_rows
		col = i%num_of_cols
		if instructions[i]=="up": 
			r = 1/num_of_cols
			s = 1/num_of_rows
			theta = 0
			phi = 0
			e = r*col
			f = s*row
			affinemaps.append(affine(r,s,theta,phi,e,f))
		elif instructions[i]=="left":
			r = 1/num_of_cols
			s = 1/num_of_rows
			theta = 90
			phi = 90
			e = r*col+r
			f = s*row
			affinemaps.append(affine(r,s,theta,phi,e,f))
		elif instructions[i]=="right":
			r = 1/num_of_cols
			s = 1/num_of_rows
			theta = -90
			phi = -90
			e = r*col
			f = s*row+s
			affinemaps.append(affine(r,s,theta,phi,e,f))
		elif instructions[i]=="down":
			r = 1/num_of_cols
			s = 1/num_of_rows
			theta = 0
			phi = 0
			e = r*col
			f = s*row+s
			affinemaps.append(affine(r,-s,theta,phi,e,f))
		elif instructions[i]=="-up":
			r = 1/num_of_cols
			s = 1/num_of_rows
			theta = 0
			phi = 0
			e = r*col+r
			f = s*row
			affinemaps.append(affine(-r,s,theta,phi,e,f))
		elif instructions[i]=="-left":
			r = 1/num_of_cols
			s = 1/num_of_rows
			theta = 90
			phi = 90
			e = r*col+r
			f = s*row+s
			affinemaps.append(affine(-r,s,theta,phi,e,f))
		elif instructions[i]=="-right":
			r = 1/num_of_cols
			s = 1/num_of_rows
			theta = -90
			phi = -90
			e = r*col
			f = s*row
			affinemaps.append(affine(-r,s,theta,phi,e,f))
		elif instructions[i]=="-down":
			r = 1/num_of_cols
			s = 1/num_of_rows
			theta = 180
			phi = 180
			e = r*col+r
			f = s*row+s
			affinemaps.append(affine(r,s,theta,phi,e,f))
		#####
		
	return(drawIFS(affinemaps,maxiter,seed,filename,size)) #now that instructions have been converted, call drawIFS 
	
def drawHeebgbColor(instructions,colormap,maxiter,filename,size=(1000,1000)):
	#instructions,maxiter,filename,size
	num_of_instructions = len(instructions)
	#####error check######
	if num_of_instructions!=len(colormap):
		print("Error number of affine maps does not equal the number of color maps")
		return(0)
	if int(sqrt(num_of_instructions))!=sqrt(num_of_instructions):
		print("input error, the number of instructions should be a squared integer")
		return()
	##########
	
	num_of_rows = num_of_cols = sqrt(num_of_instructions)
	affinemaps = []
	
	for i in range(num_of_instructions):
		row = i//num_of_rows
		col = i%num_of_cols
		if instructions[i]=="up":
			r = 1/num_of_cols
			s = 1/num_of_rows
			theta = 0
			phi = 0
			e = r*col
			f = s*row
			affinemaps.append(affinecolor(r,s,theta,phi,e,f,colormap[i]))
		elif instructions[i]=="right":
			r = 1/num_of_cols
			s = 1/num_of_rows
			theta = -90
			phi = -90
			e = r*col
			f = s*row+s
			affinemaps.append(affinecolor(r,s,theta,phi,e,f,colormap[i]))
		elif instructions[i]=="left":
			r = 1/num_of_cols
			s = 1/num_of_rows
			theta = 90
			phi = 90
			e = r*col+r
			f = s*row
			affinemaps.append(affinecolor(r,s,theta,phi,e,f,colormap[i]))
		elif instructions[i]=="down":
			r = 1/num_of_cols
			s = 1/num_of_rows 
			theta = 0
			phi = 0
			e = r*col
			f = s*row+s
			affinemaps.append(affinecolor(r,-s,theta,phi,e,f,colormap[i]))
		elif instructions[i]=="-up":
			r = 1/num_of_cols
			s = 1/num_of_rows
			theta = 0
			phi = 0
			e = r*col+r
			f = s*row
			affinemaps.append(affinecolor(-r,s,theta,phi,e,f,colormap[i]))
		elif instructions[i]=="-left":
			r = 1/num_of_cols
			s = 1/num_of_rows
			theta = 90
			phi = 90
			e = r*col+r
			f = s*row+s
			affinemaps.append(affinecolor(-r,s,theta,phi,e,f,colormap[i]))
		elif instructions[i]=="-right":
			r = 1/num_of_cols
			s = 1/num_of_rows
			theta = -90
			phi = -90
			e = r*col
			f = s*row
			affinemaps.append(affinecolor(-r,s,theta,phi,e,f,colormap[i]))
		elif instructions[i]=="-down":
			r = 1/num_of_cols
			s = 1/num_of_rows
			theta = 180
			phi = 180
			e = r*col+r
			f = s*row+s
			affinemaps.append(affinecolor(r,s,theta,phi,e,f,colormap[i]))
	
	return(drawColorIFS(affinemaps,maxiter,filename,size))
'''

