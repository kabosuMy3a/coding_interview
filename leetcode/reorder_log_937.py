class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
    
        reordered_logs = []
        temp = []
        temp2 = []

        for log in logs :
            s_idx = log.find(' ')
            
            identifier= log[:s_idx]
            message = log[s_idx:]
            if(message[1].isalpha()):
                temp.append([identifier, message])
            else:
                temp2.append(log)
        
        temp = sorted(temp, key= lambda message: (message[1], message[0]))
        
        for i in temp :
            reordered_logs.append(i[0]+i[1])
        reordered_logs += temp2
        
        return reordered_logs
                    