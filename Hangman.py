import random
word_list = ["rib","distribute","timber","junior","argument","curve","lump","last","start","guide","lake","indoor","unpleasant","cemetery","sting"]
mydict={}
word=random.choice(word_list)
start=[]
end = False
for i in range(len(word)):
  start.append("_")
  if word[i] in mydict:
    mydict[word[i]].append(i)
  else:
    mydict[word[i]]=[i]
print(start)
guess_count=0
while guess_count <3 :
  guess=input(str("Guess the Letter: "))
  if guess in mydict:
    for index in mydict[guess]:
      start[index]=guess
    print(start)
    if "_" not in start:
      print("You Won ! The word was "+word)
      end = True
      break
  else:
    guess_count+=1
    print("You have "+str(3-guess_count)+" tries left")
if end == False:
  print("Game Over ! The word was "+word)

  