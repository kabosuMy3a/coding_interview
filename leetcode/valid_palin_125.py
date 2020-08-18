class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        ### Using List ###
        #palin  = []
        ### Using Deque
        #palin: Deque = collections.deque()
        
        ### PreProcessing ### 
        #for alnum in s :
        #    if str.isalnum(alnum):
        #        palin.append(alnum.lower())
        
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]
    
        #while len(palin) > 1 :
        #    if palin.popleft() != palin.pop():
        #        return False
        #return True
    
        
        ### Decision 1 ####
        #nilap = list(reversed(palin))
        #return nilap == palin
        
        ### Decision 2 ####
        #while len(palin) > 1 :
        #    if palin.pop(0) != palin.pop():
        #        return False
        #return True