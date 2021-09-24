'''Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba' '''

def front_back(str):
  if (len(str)>= 3):
    firstChar = str[0]
    lastChar = str[-1]
    newString = lastChar + str[1:-1] + firstChar
    return newString
  else:
    return str[::-1]
  
