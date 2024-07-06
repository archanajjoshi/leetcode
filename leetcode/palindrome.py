class palindromeSolution:
    def palindrome(self, x) -> bool:
        pal = str(x)
        for i in (range((len(pal)/2) + (len(pal)%2)):
                  j = len(pal)-1-i
                  if pal[i] != pal[j]:
                    return False
        return True
