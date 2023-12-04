import js as p5

print('Assignment #8 (Final Project Part B)')
bg=p5.loadImage('bg.png')
font=p5.loadFont('font1.otf')
cs1=p5.loadImage('sheep/sheep11.png')
cs2=p5.loadImage('sheep/sheep12.png')
cs3=p5.loadImage('sheep/sheep21.png')
cs4=p5.loadImage('sheep/sheep22.png')

program_state ='START'


score=0


def setup():
  p5.createCanvas(1000, 397) 
  # p5.noloop()

def draw():
  global program_state, score
  p5.background(255)   
  p5.fill(0)  
  cursor_xy = (int(p5.mouseX), int(p5.mouseY))
  p5.text(cursor_xy, 10, 20)  # cursor (x, y) 
  
  if (program_state == 'START'):
    p5.image(bg,0,0)
    score=0
    if(p5.millis()%1000<500):
      p5.image(cs1,150,250)
    else:
      p5.image(cs2,150,250)

    if(p5.millis()%1000<500):
      p5.image(cs3,700,250)
    else:
      p5.image(cs4,700,250)


    # distance = p5.dist (wolf.x,wolf.y,wstick.x,wstick.y)

    # if (distance<10):
    #   wolf.x= - wolf.x+wolf.speed
      
    
    p5.textFont(font)
    p5.textSize(60)
    p5.text('Sheep Defender', 250, 150)
    p5.textSize(40)
    p5.text('Click to start', 330, 220)

  elif (program_state == 'PLAY'):
    p5.image(bg,0,0)
    sheep.draw()
    sheep.move()
    wolf.draw()
    wolf.move()
    herder1.draw()
    herder1.move()
    wstick.draw()
    wstick.move()
    p5.textSize(25)
    # p5.text('score =', 0,850, 50)
    p5.text('score=', 850,50)
    p5.text(score, 950,50)


  distance = p5.dist (wolf.x,wolf.y,sheep.x,sheep.y)

  # if (distance<10): 
  #   program_state = 'FINISH'

  if (wolf.x>sheep.x): 
    program_state = 'FINISH'
    print('finish')

  
  if (program_state == 'FINISH'):
    p5.image(bg,0,0)
    p5.textSize(60)
    p5.text('Game Over', 320, 200)
    p5.textSize(30)
    p5.text('Press mouse to continue', 300, 250)
    

class Sheep:
  def __init__(self, x=300,y=170):
    self.x = x
    self.y = y
    self.speed = 1
    self.timer = 0
    self.img1 = p5.loadImage('sheep/sheep1.png')
    self.img2 = p5.loadImage('sheep/sheep2.png')
    self.img3 = p5.loadImage('sheep/sheep3.png')
    self.img=p5.loadImage('sheep/sheep.gif')
    # self.img1=p5.loadImage('sheep/lsheepgif.gif')
    
  def draw(self):
    
    p5.image(self.img,self.x,self.y)
    # self.img1=p5.loadImage('sheep/lsheepgif.gif')
    if(p5.millis()%1000<250):
       p5.image(self.img1,self.x,self.y)
    elif(p5.millis()%1000<500):
      p5.image(self.img2,self.x,self.y)
    elif(p5.millis()%1000<750):
      p5.image(self.img3,self.x,self.y)
    else:
      p5.image(self.img2,self.x,self.y)
      
    # if self.x == self.x -self.speed:
    #   p5.image(self.img1,self.x,self.y)
    # else:
    #   p5.image(self.img,self.x,self.y)
    
    


  def move(self):
    if p5.millis() > self.timer + 2000:
      self.speed = -self.speed
      self.timer = p5.millis()
    self.x = self.x + self.speed*p5.random(1, 2)

    # if self.x == self.x + -self.speed:
    #   p5.image(self.img1,self.x,self.y)
    # else:
    #   p5.image(self.img,self.x,self.y)
    
sheep=Sheep()


class Wolf:
    def __init__(self,x= -50,y=150):
      self.speed = 1
      self.x = x
      self.y = y
      self.img = p5.loadImage('wolf.gif')
      self.img1=p5.loadImage('lwolf.gif')

    def draw(self):
      p5.image(self.img,self.x,self.y)
      

    def move(self):
      global my_timer,score
      my_timer=p5.millis()
      
      distance = p5.dist (self.x,self.y,wstick.x,wstick.y)
      # print(distance)
      if (distance< 200): 
        self.speed = -self.speed
        # self.x = self.x - self.speed 
        p5.image(self.img1,self.x,self.y)
        score+=1
      else:
        p5.image(self.img,self.x,self.y)
        
      if (self.x<-200):
        self.speed=-self.speed

      self.x = self.x + self.speed

      if (self.speed == -self.speed):
        p5.image(self.img1,self.x,self.y)

      # if (self.x> wstick.x): 
      #   self.x= - self.x+self.speed
      #   p5.image(self.img1,self.x,self.y)
      #   score+=1
      # else:
      #   self.x = self.x+self.speed

      if (p5.millis()>my_timer+5000):
        self.speed+-0.5
        my_timer=p5.millis()
        print('go faster!...')

    

wolf=Wolf()

class Human: 
    def __init__(self,x=400,y=100):
     self.x = x
     self.y = y
     self.img1 = p5.loadImage('people1.png') #my drawing :)
     self.img2 = p5.loadImage('people2.png') #my drawing :)
     self.img3 =p5.loadImage('lpeople1.png') 
     self.img4 =p5.loadImage('lpeople2.png') 
      
    def draw(self):


      if(p5.keyCode == p5.LEFT_ARROW):
        if(p5.millis()%1000<500):
          p5.image(self.img3,self.x,self.y)
        else:
          p5.image(self.img4,self.x,self.y)

      else:
        if(p5.millis()%1000<500):
          p5.image(self.img1,self.x,self.y)
  
        else:
          p5.image(self.img2,self.x,self.y)
        
    def move(self):
        if (p5.keyIsPressed == True):
          if(p5.keyCode == p5.RIGHT_ARROW):
            self.x+=5
          elif(p5.keyCode == p5.LEFT_ARROW):
            self.x-=5
      
herder1=Human()

class Stick(Human):
    def __init__(self,x=500,y=190):
      self.x = x
      self.y = y
      self.img1 = p5.loadImage('stick.png')
      self.img2 = p5.loadImage('stick1.png')
      self.img3 = p5.loadImage('stick3.png')
      self.img4 = p5.loadImage('stick4.png')
      

    def draw(self):
        
      # if(p5.millis()%1000<500):
      #   p5.image(self.img1,self.x,self.y)
      # else:
      #   # p5.image(self.img2,150,260)
      #   p5.image(self.img2,self.x-110,self.y+98)
      
      if(p5.keyCode == p5.LEFT_ARROW):
        if(p5.millis()%1000<500):
          p5.image(self.img4,self.x+37,self.y+92)
        else:
          p5.image(self.img3,self.x-70,self.y+5)

      else:
        if(p5.millis()%1000<500):
          p5.image(self.img1,self.x,self.y)

        else:
          p5.image(self.img2,self.x-100,self.y+88)

      
    def move(self):
      if (p5.keyIsPressed == True):
        if(p5.keyCode == p5.RIGHT_ARROW):
          self.x+=5
        elif(p5.keyCode == p5.LEFT_ARROW):
          self.x-=5

wstick=Stick()


# event function below need to be included,
# even if they don't do anything

def keyPressed(event):
  pass
  # global program_state
  # print('keyPressed.. ' + str(p5.key))
  # if (p5.keyIsPressed == True):
  #   if(p5.keyCode == p5.UP_ARROW):
  #     program_state = 'START'  
  #   print('change to START..')

def keyReleased(event):
    #print('keyReleased.. ' + str(p5.key))
    pass

def mousePressed(event):
  global program_state
  print('keyPressed.. ' + str(p5.key))
  # if (p5.mouseIsPressed):
  program_state = 'PLAY'
  print('change to PLAY..')

def mouseReleased(event):
  #print('mouseReleased..')
  pass


  
