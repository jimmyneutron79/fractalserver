#fractalgraphics.py

'''
#####Example Usage ########
win = GraphImage(500,500)
win.Polygon((100,100),(400,100),(400,400),(100,400),"blue")
win.Rectangle((100,100),(200,200),"red")
win.Circle((250,250),50,setColor="red")
win.Line((0,0),(500,500),setColor="red")
win.savejpg('fractalgraphicstest.jpg')
win.cls()
win.savejpg('fractalgraphictest2.jpg')
############################
'''

from PIL import Image, ImageDraw
import sys

def colorcode(colortxt):
	if colortxt=="red":
		return((255,0,0))
	elif colortxt=="blue":
		return((0,0,255))
	elif colortxt=="green":
		return((0,255,0))
	elif colortxt=="yellow":
		return((255,255,0))
	elif colortxt=="white":
		return((255,255,255))
	elif colortxt=="black":
		return((0,0,0))
	elif colortxt=="grey":
		return((128,128,128))
	elif colortxt=="orange":
		return((255,165,0))
	else:
		return((128,128,128))

class GraphImage():

	def __init__(self, width=500, height=500,background="black"):
		self.width = width
		self.height = height
		if width<height:
			self.size = width
		else:
			self.size = height
		self.background = colorcode("white")
		self.im = Image.new('RGB',(width,height),self.background)
		self.items = []
		self.drawim = ImageDraw.Draw(self.im)
		
	def updateimage(self,shape):
		#### it works but is not in use at this time
		self.items.append(shape)
		return self.items
		
	def savejpg(self,filename):
		try:
			self.im.save(filename,quality=95)
		except ValueError:
			return(0)
		return(1)
		
	def Rectangle(self,XY1,XY2,setColor=None,setOutlineColor=None):
		if setOutlineColor==None:
			setOutlineColor=setColor
		self.drawim.rectangle((XY1[0],XY1[1],XY2[0],XY2[1]), fill=colorcode(setColor), outline=colorcode(setOutlineColor))
		
	def Polygon(self,XY1,XY2,XY3,XY4,setColor=None,setOutlineColor=None):
		if setOutlineColor==None:
			setOutlineColor=setColor
		self.drawim.polygon((XY1,XY2,XY3,XY4),fill=colorcode(setColor),outline=colorcode(setOutlineColor))
		
	def Point(self,XY, setColor=None):
		self.drawim.point((),fill=colorcode(setColor))
		
	def Circle(self,XY,radius,setColor=None,setOutlineColor=None):
		if setOutlineColor==None:
			setOutlineColor=setColor
		self.drawim.ellipse((XY[0]-radius,XY[1]-radius,XY[0]+radius,XY[1]+radius),fill=colorcode(setColor),outline=colorcode(setOutlineColor))
		
	def Line(self,XY1,XY2,setColor=None):
		self.drawim.line((XY1[0],XY1[1],XY2[0],XY2[1]),fill=colorcode(setColor),width=1)
		
	def cls(self):
		#self.Rectangle(0,0,self.width,self.height,"white")
		self.im=Image.new('RGB',(self.width,self.height),colorcode("white"))
		
		

'''
def GraphImage(width,height):

	im = Image.new('RGB', (width,height), (255,0,0,0))
	draw = ImageDraw.Draw(im)
	#draw.ellipse([(100,100),(400,400)],fill=None)
	#im.save("test.png", "PNG")
	
	draw.ellipse([(100, 100), (200, 200)], fill=(255, 0, 0), outline=(0, 0, 0))
	draw.rectangle((200, 100, 300, 200), fill=(0, 192, 192), outline=(255, 255, 255))
	draw.line((350, 200, 450, 100), fill=(255, 255, 0), width=10)

	im.save('pillow_imagedraw.jpg', quality=95)
	
GraphImage(500,500)
print("ok")
'''

