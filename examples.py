#A fractal generator v3 - Example Sheet
#by Jim Johnston - jimmy.johnston@gmail.com copyright 2020
#Created 2-20-20

from afractalgenerator_v3_3 import *
#Note: afractalgenerator is dependent upon the python math library (internal) and my graphics library, fractalgraphics.py (external)

####################
##### Examples #####
####################

#Note: remove hashtag to uncomment

##### affine maps instructions #####
#sierpinski = [affine(.5,.5,0,0,0,0),affine(.5,.5,0,0,0,.5),affine(.5,.5,-90,-90,.5,.5)]
sierpinski = [affine(.5,.5,0,0,0,0),affine(.5,.5,0,0,0,.5),affine(.5,.5,0,0,.5,0)]
kochcurve = [affine(1/3,1/3,0,0,0,0),affine(1/3,1/3,60,60,1/3,0),affine(1/3,1/3,-60,-60,1/2,(1/2)*1/sqrt(3)),affine(1/3,1/3,0,0,2/3,0)]
##########

##### Heebgb instructions #####
sierpinskigb_flavor1 = ['-left','-right','-down','-up']
sierpinskigb_flavor2 = ['up','up','right','blank']
sierpinskigb = ['up','up','up','blank']
xaviersfractal = ['left','up','up','left']
fractaldesign1 = ['down','left','up','right','up','right','up','left','down'] #find out why bottom left corner looks wrong
fractaldesign3 = ['left','left','left','right','blank','left','right','right','right']
fractaldesign5 = ['down','up','down','up','down','up','down','down','down','up','down','left','down','right','down','up','down','up','down','up','down','up','down','up','down']
##########

##### Heebgb color mappings #####
colormap2x2_0 = ['black','black','black','black']
colormap2x2_1 = ['blue','red','green','yellow']
colormap3x3_1 = ['blue','green','red','blue','green','red','blue','green','red']
colormap3x3_2 = ['red','red','red','green','yellow','red','green','green','green']
colormap5x5_1 = ['green','red','green','red','green','red','yellow','red','yellow','red','green','red','green','red','green','red','yellow','red','yellow','red','green','red','green','red','green']
colormap5x5_2 = ['green','red','green','red','green','red','yellow','green','yellow','red','green','blue','green','yellow','green','red','yellow','red','yellow','orange','green','red','green','red','green']
##########
#TESTING#
#drawIFS(sierpinski,1,seed="MrFace",filename="static/images/user-generated/example1a.jpg") #method=affine by default
#drawIFS(sierpinski,2,seed="MrFace",filename="static/images/user-generated/example1b.jpg") #method=affine by default
drawIFS(sierpinski,3,seed="MrFace",filename="static/images/user-generated/example1c.jpg") #method=affine by default
drawIFS(sierpinski,3,seed="MrFace",method="affine",filename="static/images/user-generated/example2.jpg") #method=affine by default
drawIFS(sierpinski,3,seed="Square",filename="static/images/user-generated/example3.jpg",size=(500,500)) #method=affine by default
drawIFS(sierpinskigb,1,method="HeeBGB",seed="Square",filename="static/images/user-generated/example4.jpg")
drawIFS(sierpinskigb,1,method="HeeBGBcolor",seed="Square",colormap=colormap2x2_1,filename="static/images/user-generated/example5.jpg")
drawIFS(sierpinskigb,1,method="HeeBGB",filename="static/images/user-generated/example6.jpg")
drawIFS(sierpinskigb,1,method="HeeBGBcolor",colormap=colormap2x2_1,filename="static/images/user-generated/example7a.jpg")
drawIFS(sierpinskigb,2,method="HeeBGBcolor",colormap=colormap2x2_1,filename="static/images/user-generated/example7b.jpg")
drawIFS(sierpinskigb,3,method="HeeBGBcolor",colormap=colormap2x2_1,filename="static/images/user-generated/example7c.jpg")
drawIFS(sierpinskigb,2,method="HeeBGB",seed="MrFace",filename="static/images/user-generated/example8.jpg")
drawIFS(kochcurve,3,seed="Line",filename="static/images/user-generated/example9.jpg")
drawIFS(sierpinskigb,1,method="HeeBGBcolor",seed="MrFace",colormap=colormap2x2_1,filename="static/images/user-generated/example10.jpg")
drawIFS(sierpinskigb_flavor2,2,method="HeeBGBcolor",seed="MrFace",colormap=colormap2x2_1,filename="static/images/user-generated/example11.jpg")

''' Print Jobs - where the fractals are constructed and saved as JPEG images '''
######################
#### Geometry - 21st Century
######################
#drawIFS(sierpinski,1,seed="MrFace",filename="static/images/user-generated/example1.jpg")
#drawIFS(sierpinski,3,seed="MrFace",filename="static/images/user-generated/example2.jpg")
#drawIFS(sierpinskigb,3,method="HeeBGB",seed="MrFace",filename="static/images/user-generated/example3.jpg")
#drawIFS(sierpinskigb,8,method="HeeBGB",seed="Square",filename="static/images/user-generated/example4.jpg")
#drawIFS(sierpinskigb,1,method="HeeBGB",seed="Square",colormap=colormap2x2_1,filename="static/images/user-generated/example5.jpg")
#drawIFS(kochcurve,3,seed="Line",filename="static/images/user-generated/example6.jpg")
#drawIFS(xaviersfractal,1,method="HeeBGB",seed="Square",colormap=colormap2x2_1,filename="static/images/user-generated/example7.jpg")
#drawIFS(xaviersfractal,5,method="HeeBGB",seed="Square",colormap=colormap2x2_1,filename="static/images/user-generated/example8.jpg")
#drawIFS(xaviersfractal,8,method="HeeBGB",seed="Square",colormap=colormap2x2_1,filename="static/images/user-generated/example9.jpg")
#drawIFS(fractaldesign3,4,method="HeeBGB",seed="Square",colormap=colormap3x3_2,filename="static/images/user-generated/example10.jpg")


######################
#### function drawIFS: affine maps, iterations, initial object (MrFace/Square), filename.jpg
######################
#drawIFS(sierpinski,1,"MrFace","static/images/user-generated/sierpinski-mrface-1.jpg")
#drawIFS(sierpinski,2,"MrFace","static/images/user-generated/sierpinski-mrface-2.jpg")
#drawIFS(sierpinski,5,"MrFace","static/images/user-generated/sierpinski-mrface-3.jpg")
#drawIFS(sierpinski,13,"Square","static/images/user-generated/sierpinski-square-12.jpg",(16000,16000))
#drawIFS(kochcurve,1,"MrFace","static/images/user-generated/kochcurve-mrface-1.jpg")
#drawIFS(kochcurve,2,"MrFace","static/images/user-generated/kochcurve-mrface-2.jpg")
#drawIFS(kochcurve,1,"Line","static/images/user-generated/kochcurve-line-1.jpg")
#drawIFS(kochcurve,2,"Line","static/images/user-generated/kochcurve-line-2.jpg")
#drawIFS(kochcurve,4,"Line","static/images/user-generated/kochcurve-line-4.jpg")
#drawIFS(kochcurve,5,"Line","static/images/user-generated/kochcurve-line-5.jpg")
#drawIFS(kochcurve,6,"Line","static/images/user-generated/kochcurve-line-6.jpg")
######################
#### function drawHeebgbColor: Heebgb instructions, color map, iterations, filename
######################
#drawHeebgbColor(sierpinskigb,colormap2x2_1,1,"images/user-generated/sierpinskiHeeBGB-1.jpg")
#drawHeebgbColor(sierpinskigb,colormap2x2_1,2,"images/user-generated/sierpinskiHeeBGB-2.jpg")
#drawHeebgbColor(sierpinskigb,colormap2x2_0,13,"static/images/user-generated/sierpinskiHeeBGB-10-large.jpg",(13000,13000))
#drawHeebgbColor(sierpinskigb_flavor1,colormap2x2_1,1,"images/user-generated/sierpinski_flavor1_HeeBGB-1.jpg")
#drawHeebgbColor(sierpinskigb_flavor1,colormap2x2_1,7,"images/user-generated/sierpinski_flavor1_HeeBGB-7.jpg")
#drawHeebgbColor(xaviersfractal,colormap2x2_1,1,"static/images/user-generated/xavier-1.jpg")
#drawHeebgbColor(xaviersfractal,colormap2x2_1,5,"static/images/user-generated/xavier-5.jpg")
#drawHeebgbColor(xaviersfractal,colormap2x2_1,7,"images/user-generated/xavier-7.jpg")
#drawHeebgbColor(xaviersfractal,colormap2x2_1,10,"static/images/collections/xavier/xavier-8-large.jpg",(16384,16384))#beware! 54MB file
#drawHeebgbColor(fractaldesign3,colormap3x3_2,4,"images/user-generated/christmaswreath-4.jpg")#christmas wreath
#drawHeebgbColor(fractaldesign5,colormap5x5_2,1,"images/user-generated/fd5_2-1.jpg") #sunshine
#drawHeebgbColor(fractaldesign5,colormap5x5_2,3,"images/user-generated/fd5_2-3.jpg") #sunshine
#drawHeebgbColor(fractaldesign5,colormap5x5_2,4,"images/user-generated/fd5_2-4.jpg") #sunshine
#drawHeebgbColor(fractaldesign5,colormap5x5_1,1,"images/user-generated/fd5_1-1.jpg") #southwest
#drawHeebgbColor(fractaldesign5,colormap5x5_1,3,"images/user-generated/fd5_1-3.jpg") #southwest
#drawHeebgbColor(fractaldesign5,colormap5x5_1,2,"static/images/user-generated/fd5_1-4.jpg") #southwest
######################
#### function drawHeebgb + more drawHeebgbColor related fractals
######################
#drawHeebgb(fractaldesign1,1,"MrFace","images/user-generated/fd1_1mrface.jpg")
#drawHeebgb(fractaldesign1,2,"MrFace","images/user-generated/fd1_2mrface.jpg")
#drawHeebgbColor(fractaldesign1,colormap3x3_1,1,"images/user-generated/fd1_1color.jpg")
#drawHeebgbColor(fractaldesign1,colormap3x3_1,4,"images/user-generated/fd1_4color.jpg")
#drawHeebgbColor(fractaldesign1,colormap3x3_1,5,"images/user-generated/fd1_5color.jpg")
print('success')


