def user_input(): 
  word = input(
    """
    1.vowel check must use only one word at a time
    2.word must not contain any special characters
    3.word must not contain numbers
  
    """
  
    "Please input a word: "
 ) 
  
  return word

def txt(user_put):
    text=0
    # for char in user_put: 
    if "a" in user_put:
      text=text+1
    if "e" in user_put:
      text=text+1
    if "i" in user_put:
      text=text+1
    if "o" in user_put:
      text=text+1
    if "u" in user_put:
      text=text+1
		    
    text = str(text)
    print("this word has " + text + " vowels")
    return txt



user_put=user_input()
txt(user_put)
