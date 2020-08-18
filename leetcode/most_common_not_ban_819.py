class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        #paragraph = re.sub('[^\w\s]'," ", paragraph)
        #paragraph = paragraph.lower() 
        #words = paragraph.split() 
        #words = [x for x in words if x not in banned]
        
        ## 위에 코드가 나은듯
        words = [ word for word in re.sub('[^\w]',' ', paragraph).lower().split()
                    if word not in banned]
        
        
        counter = collections.Counter(words)  
        return counter.most_common(1)[0][0]
        