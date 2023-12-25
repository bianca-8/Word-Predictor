from pygame import *
init()
SIZE = (400,600)
# Setup your own screen size
screen = display.set_mode(SIZE)

#Colours
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (176,224,230)

#fonts
buttonFont = font.SysFont("Times New Roman", 14) #font of level 2 and 3 buttons
myFont = font.SysFont("Times New Roman", 20) #search bar and dictionary font
threeFont = font.SysFont("Times New Roman", 30) #3 word font

#variables
file = open("dict.txt", "r")
textList = []
occurence = []
words = []
letter = ""
fullWords = ""
allWords = []
totalTimes = []
button = ""

title = myFont.render("", 1, (BLACK))
occurenceWord = myFont.render("", 1, (BLACK))
display1 = myFont.render("", 1, (BLACK))
display2 = myFont.render("", 1, (BLACK))
letters = myFont.render(letter, 1, (BLACK))

#background
def background():
  draw.rect(screen,WHITE,(0,0,400,600)) #White background
  draw.rect(screen,BLUE,(10,10,380,30)) #Search bar
  draw.rect(screen,BLUE,(10,50,380,190)) #Displays 3 words
  draw.line(screen,BLACK,(10,110),(389,110)) #First separator line
  draw.line(screen,BLACK,(10,180),(389,180)) #Second separator line
  draw.rect(screen,BLUE,(10,300,380,180)) #Dictionary
  draw.rect(screen,BLUE,(10,250,185,40)) #Level 2 Click - Indv Words Read (Left button)
  draw.rect(screen,BLUE,(205,250,185,40)) #Level 3 Click - All Words (Right button)
  screen.blit(letters,(13,10,375,30)) #puts typed words on screen

while True:
  text = file.readline() #reads each word in the file
  text = text.rstrip("\n") #takes away "\n"

  if text == "": #breaks when there are no more words to add
    break
    
  if textList.count(text) < 1: #only 1 occurence
    textList.append(text) #adds words to list
    occurence.append(1) #adds 1 occurence to the # of occurences list
  else: #word is already in the dictionary
    place = textList.index(text)
    occurence[place] += 1 #add 1 to the occurences list

running = True
while running:
  counter = 0
  add = 0
  add2 = 0
  add3 = 0
  add4 = 0
  add5 = 0
  
  for e in event.get():      
    if e.type == QUIT:
      running = False

    if e.type == MOUSEBUTTONDOWN: #mouse clicked
      if e.pos[0] >= 10 and e.pos[0] <= 195 and e.pos[1] >= 250 and e.pos[1] <= 290: #left button
        title = myFont.render("Individual words read:", 1, (BLACK))
        occurenceWord = myFont.render(str(len(occurence)), 1, (BLACK))
        button = 1
      if e.pos[0] >= 205 and e.pos[0] <= 390 and e.pos[1] >= 250 and e.pos[1] <= 290: #right button
        count = 0
        allWords = []
        totalTimes = []
        for digits in occurence:
          allWords.append(textList[count])
          totalTimes.append(digits)
          count += 1
          button = 2
    
    if e.type == KEYDOWN: #User types
      button = 0
      count = 0
      fullWords = []
      words = []
      
      if e.key == K_BACKSPACE: #deletes letter
        if len(letter) > 0:
          letter = letter[:-1]
      else:
        letter += e.unicode
      
      if e.key == K_RETURN: #enter pressed - adds word to dictionary if doesn't exist
        letter = letter[:-1] #takes away the new line
        if textList.count(letter) == 0: #checks if word exists in file already
          aFile = open("dict.txt", "a") #adds word to file if press enter
          aFile.write("\n" + letter)
          textList.append(letter)
          occurence.append(1)
          aFile.close()

      for digits in occurence:
        button = 0
        times = digits
        word = textList[count]

        if letter == word[:len(letter)]: #compares typed letters to words in dictionary
          words.append([times,word])
          words.sort(reverse = True) #puts words in order by occurence
          fullWords = words #All words starting with letter

        if fullWords == []:
            button = -1
          
        count += 1
      
      while len(words) > 3: #Finds top 3 occuring words starting with letter
        words = words[:-1]
      
      if len(letter) == 0: #nothing is typed
        button = -1
        
      letters = myFont.render(letter, 1, BLACK)

  background() 
  if button == 1: #Indiv Words Read (left button)
    screen.blit(title,(15,305,380,180))
    screen.blit(occurenceWord,(15,330,380,180))
  
  elif button == 2: #All words (right button)
    draw.line(screen,BLACK,(200,300),(200,479)) #Dictionary Separator Line
    
    for chr in allWords:
      indvWords = myFont.render(allWords[counter], 1, (BLACK)) #all individual words in dictionary
      totalOccurences = myFont.render(str((totalTimes)[counter]), 1, (BLACK)) #total number of occurences
      if add <= 140: #moves words to right if at the bottom of the box
        screen.blit(indvWords,(15,305+add,380,180))
        screen.blit(totalOccurences,(175,305+add,380,180))
      else:
        screen.blit(indvWords,(205,305+add4,380,180))
        screen.blit(totalOccurences,(360,305+add4,380,180))
        add4 += 20
      counter += 1
      add += 20
  
  elif button == 0: #typed words
    draw.line(screen,BLACK,(200,300),(200,479)) #Dict Line
    
    for amount in fullWords: #All words starting with the letter and # of occurences (level 4)
      display1 = myFont.render(str(amount[1]), 1, (BLACK)) #writes words
      display2 = myFont.render(str(amount[0]), 1, (BLACK)) #writes number of occurences
      if add2 <= 140: #moves words to right if at the bottom of the box
        screen.blit(display1,(15,300+add2,380,180))
        screen.blit(display2,(175,305+add2,380,180))
      else:
        screen.blit(display1,(205,300+add5,380,180))
        screen.blit(display2,(360,305+add5,380,180))
        add5 += 20
      add2 += 20

    for characters in words: #writes top 3 words occuring and numbers (level 4+)
      display3 = threeFont.render(str(characters[1]), 1, (BLACK)) #writes top 3 words occuring 
      display4 = threeFont.render(str(characters[0]), 1, (BLACK)) #writes top 3 # of occurences
      screen.blit(display3,(15,60+add3,100,170))
      screen.blit(display4,(340,60+add3,20,170))
      add3 += 65
      
  elif button == -1: #nothing is typed and no buttons clicked
    background()
      
  type = buttonFont.render("Indiv Words Read", 1, (BLACK)) #Level 2 Writing
  screen.blit(type,(40,260,185,40))
  type = buttonFont.render("All Words", 1, (BLACK)) #Level 3 Writing
  screen.blit(type,(255,260,185,40))
  display.update()
  
file.close()
quit()
