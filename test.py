import random

class Main:
  def __init__(self,fale,key):
    self.fale = fale
    self.key = key
    self.new_fale = "result.txt"
    self.newList = list()
    self.listResult = []

  def update(self):
    try:
      with open(self.fale , 'r') as newFale:
        text = newFale.read()
        for items in text.split():
          self.newList.append(" ")
          for j in range(len(items)):
            n = ord(items[j])
            self.newList.append(n)
        return self.shif(self.newList)
    except FileNotFoundError:
      return "File error"

  def shif(self,listOrd):
  	number = ""
  	for i in range(len(listOrd)):
  		a  = listOrd[i]
  		if a != " ":
  		for _ in range(0, 20):
  			b = a/2
  			if b <= 0:
  				number += " "
  				break
  			elif int(b) != b:
  				number += "0"
  				a = int(b)
  			else:
  				number += "1"
  				a = b
  		elif a ==" ":
  			self.listResult.append(number)
  			self.listResult.append(" ")
  			number = " "
  	with open(self.new_fale,"a") as fale:
  		fale.write(str(self.listResult))


def main():
  fale = "YOUR_FILE.txt"
  key = random.randint(0,100)
  if fale[-4::] == ".txt" and key > 0:
    main_shif = Main(fale,key)
    main_shif.update()
main()
