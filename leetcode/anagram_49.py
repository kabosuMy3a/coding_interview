class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #ann = []
        #for word in strs :
        #    init_flag = False
        #    sorted_char = sorted(word)
        #    for x in ann :
        #        if sorted_char in x :
        #            x.append(word)
        #            init_flag = True
        #    if init_flag == False:
        #        ann.append([sorted(word),word])
        #    
        #for x in ann :
        #    del x[0]
        #    
        #return ann
        
        ann = collections.defaultdict(list)
        ##default value is []
        for word in strs:
            ann[''.join(sorted(word))].append(word)
        
        return ann.values()