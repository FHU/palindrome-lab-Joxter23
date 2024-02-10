#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
      word = word.lower()
      if word[-1] == word[0] and word.isspace() == False:
        return True
      else:
          return False

if __name__ == '__main__': 
    word = input()
    print(palindrome(word))
