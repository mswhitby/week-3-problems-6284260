def user_input(): 
  input(
    """
    1.vowel check must use only one word at a time
    2.word must not contain any special characters
    3.word must not contain numbers
  
    """
  
    "Please input a word: "
 ) 
  
  return user_input

def txt(user_input):
    for chr in user_input: 
		if "a" in user_input():
		    txt=txt+1
		if "e" in user_input():
		    txt=txt+1
    if "i" in user_input():
		    txt=txt+1
    if "o" in user_input():
	    	txt=txt+1
    if "u" in user_input():
		    txt=txt+1
		 
    return txt
    
    str(txt)
    print("this word has "+txt+" vowels")
    return txt




user_input()
