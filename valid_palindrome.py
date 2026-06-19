class valid:
    def palindrome(s):
    
      s = s.lower()
      s = "".join(filter(str.isalnum, s))
      reversed_str = "".join(reversed(s))
      if s == reversed_str:
          return True
      else:
          return False
