arr= [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,48,49,50,51,52,53,54,55,56,57,95,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
x = 7 # number of input characters minus one. For example, if 6 input characters then x should be 5

def calc(input1): #function that contains the calculation procedure
  v3 = 0
  for i in input1: #input1 is an array of selected characters
      v3 = v3*62
      if i > 64 and i <= 90:
        v3 = v3 + i - 65
      if i > 96 and i <= 122:
        v3 = v3 + i - 71
      if i > 47 and i <= 57:
        v3 = v3 + i + 4
  
  if v3 == 21380291284888: # v3 is the value to match after the calculation above 
    print('Got key ' + str(v3) + ':',end='') #remove print functions for faster speed
    print(input1)
    exit(0)
  if v3 != 21380291284888:
    print('wrong key' + str(v3) + ':',end='')  #remove print functions for faster speed
    print(input1) 

def recur_func(n,s,file1):
  if n != 0:
    for i in arr:
      recur_func(n-1,s+chr(i),file1)

  elif n == 0:
    for i in arr:
      char_string = (s+chr(i))
      calc([ord(x) for x in char_string]) #put input digits in an array and call the calc function
      #file1.write(char_string)  #write attempted digits to file
      #file1.write('\n')
      
def main():
    #file1 = open("myfile2.txt", "w+") #write attempted digits to file
    recur_func(x,'', file1) #1st argument is the number of number of characters to be tested at the same time.
    print('key not found')

if __name__ == "__main__":
    main()


#Sample loop when x = 1

#n = 1 s = ''
#n = 0 s = 'A' - char_string = 'AA' to 'AZ'

#n = 1 s = ''
#n = 0 s = 'B' - char_string = 'BA' to 'BZ'

#n = 1 s = ''
#n = 0 s = 'C' - char_string = 'CA' to 'CZ'

#n = 1 s = ''
#n = 0 s = 'D' - char_string = 'DA' to 'DZ'

#...