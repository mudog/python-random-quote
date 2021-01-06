import random  #random is imported from built-in python module
def centrala():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")   #f is a variable defined as the contents of the quotes.txt
  quotes = f.readlines()
  """quotes is a variable defined by the readlines() method done on the
f variable or object as defined earlier"""
  f.close()
  
  last = len(quotes) -1 #len 
  rnd= random.randint(0, last)
  rnd2= random.randint(0, last)
  #print(quotes[-1])
  print(quotes[rnd]+"and "+quotes[rnd2])
  
if __name__== "__main__":
  centrala()
