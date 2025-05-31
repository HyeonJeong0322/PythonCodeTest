def solution(s):
    answer = len(s)
    
    for i in range(1, int(len(s)/2)+1):
        tmp = ""
        arr = [s[j:j+i] for j in range(0, len(s), i)]
        print(arr)
        
        p = 0
        while p < len(arr):
            cnt = 1
            
            while p+1<len(arr) and arr[p]==arr[p+1]: 
                cnt+=1
                p+=1

            if cnt>1: 
                tmp+=str(cnt)+arr[p]  
            else: 
                tmp+=arr[p]
            p+=1
        
        len_tmp = len(tmp)
        if answer>len_tmp: answer = len_tmp
        
    

    
    return answer




s = input()
print(solution(s))