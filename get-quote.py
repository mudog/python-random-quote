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

  f= open("quotes.txt","a+")
  f.write("%s" % ("\nNew line added"))
  f.close
  print(quotes[last])
def centralb():
    print("This will print", end=' ')
    print("without", end=' ')
    print("newline")  #by default the print() function has \n defined in its end parameter which adds a newline
    #print (*objects, sep= ' ', end='\n, file=sys.stdout, flush=False)

    f= open("nogaps.txt")
    nogap= f.readlines()
    f.close

    for a in range(len(nogap)):
        print(nogap[a], end=' ')
        
    print("End.")
if __name__== "__main__":
  centrala()
  centralb()
