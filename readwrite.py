
def main():
    
#file_object  = open("filename", "mode")
      """modes include:
w+ = writes/creates files + reads
a+ = appends to file
'r' 	This is the default mode. It Opens file for reading.
'w' 	This Mode Opens file for writing.
If file does not exist, it creates a new file.
If file exists it truncates the file.
'x' 	Creates a new file. If file already exists, the operation fails.
'a' 	Open file in append mode.
If file does not exist, it creates a new file.
't' 	This is the default mode. It opens in text mode.
'b' 	This opens in binary mode.
'+' 	This will open a file for reading and writing (updating)
"""
      w = open("readwrite.txt","w+")
      w.write("This text file is being written through Python\n")
      for i in range(3):
        w.write("Appended line %d\r\n" % (i+1)) #the %d formats the integer for display, \r\n add lines for windows display
        #The string modulo format is an older style. Syntax: <format_string> % <values>
        #It is completely different from arithmetic modulo but called modulo because of common % sign
        #<format_string> is composed of conversion specifiers : %[<flags>][<width>][.<precision>]<type>
        #in the example %d is the conversion type for decimal integer and converts i to display as integer
        #see https://realpython.com/python-input-output/#the-string-modulo-operator for other conversion types
        
  

  
if __name__=="__main__":
    main()
