#1. 7
#2. (b^n)-1
#3. 
def totalBill(checkAmount):
  tip = checkAmount*.15
  total = tip + checkAmount
  print total
#4. 
def newPic():
  pic = makeEmptyPicture(200, 200, makeColor(18, 52, 86))
  show(pic)
#5.
def fibSequence(fib):
  d1 = 1
  d2 = 1
  if fib>0:
    print d1
  if fib>1:
    print d2
  for num in range (0, fib):
    v = d1+ d2
    print v
    d1 + d2
    d2 = v
#6. 
def fibList(fib):
  d1 = 1
  d2 = 1
  fibList = []
  if fib>0:
    fibList.append(d1)
  if fib>1:
    fibList.append(d2)
  for num in range (0, fib):
    v = d1+ d2
    fibList.append(v)
    d1 + d2
    d2 = v
  print fibList
#7. 
def Checker():
  pic = makeEmptyPicture(800, 800, white)
  blackPic = makeEmptyPicture(100, 100, black)
  for row in range(0, 8, 2):
    for col in range(1, 8, 2):
      copyInto(blackPic,pic,col*100,row*100)
  for row in range(1, 8, 2):
    for col in range(0, 8, 2):
      copyInto(blackPic,pic,col*100,row*100)
  show(pic)
  
  show(pic)
#8. Creates a checkerboard pattern of 100 by 100 squares alternating black and white.

#9. Function B is not defined globally, and so is called before it is defined. Fixed by deleting the tab in of function B.

#10. sqrt((100-50)^2 + (50 - 10)^2 + (150 - 50)^2) Solution = 118.7

#11.
def removeRed():
  file = pickAFile()
  pic = makePicture(file)
  for p in getPixels(pic):
    setRed(p,0)
  show(pic)

#12. 39, 49, 28

#13. 


def blackOrWhite():
  file = pickAFile()
  pic = makePicture(file)
  for p in getPixels(pic):
    red = getRed(p)
    green = getGreen(p)
    blue = getBlue(p)
    d = sqrt((red*red)+(green*green)+(blue*blue))
    if d > 222:
      setColor(p, white)
    else:
      setColor(p, black)
  show(pic)



#14. 
def drawCircle(pic,diameter):
  for i in range(628):
    x=diameter*cos(2*pi*i/628)+150
    y=diameter*sin(2*pi*i/628)+150
    p=getPixel(pic,int(x),int(y))
    setColor(p,black)
  
#draws a circle at center 150 150 of defined radius.

#15. 

def conCircles():
  pic = makeEmptyPicture(300, 300)
  drawCircle(pic, 100)
  drawCircle(pic, 75)
  drawCircle(pic, 50)
  drawCircle(pic, 25)
  show(pic)
  
#16, Makes a solid red circle of diameter define.

#17. 
def colorCenter(pic,diameter):
  for p in getPixels(pic):
    if sqrt(pow(getX(p)-150,2) + pow(getY(p)-150,2)) < diameter:
      setColor(p,red)
def RedCircles():
  pic = makeEmptyPicture(300, 300)
  drawCircle(pic, 100)
  drawCircle(pic, 75)
  drawCircle(pic, 50)
  drawCircle(pic, 25)
  colorCenter(pic,25)
  show(pic)
  
#18. 
def drawX(pic):
  for p in getPixels(pic):
    for v in range(300):
      p = getPixel(pic, v, v)
      setColor(p, black)
    for v in range(300):
      px = getPixel(pic, v, 299-v)
      setColor(px, black)
      
def RedXCircles():
  pic = makeEmptyPicture(300, 300)
  drawCircle(pic, 100)
  drawCircle(pic, 75)
  drawCircle(pic, 50)
  drawCircle(pic, 25)
  colorCenter(pic,25)
  drawX(pic)
  show(pic)
      
#19.

def RedLinesXCircles():
  pic = makeEmptyPicture(300, 300)
  drawCircle(pic, 100)
  drawCircle(pic, 75)
  drawCircle(pic, 50)
  drawCircle(pic, 25)
  colorCenter(pic,25)
  drawX(pic)
  drawPlus(pic)
  show(pic)

def drawPlus(pic):
  for x in range(150, 151):
    for y in range(0, getHeight(pic)):
      p = getPixel(pic, x, y)
      setColor(p, black)
  for y in range(150, 151):
    for x in range(0, getWidth(pic)):
      p = getPixel(pic, x, y)
      setColor(p, black)

#20. 1,048,576 