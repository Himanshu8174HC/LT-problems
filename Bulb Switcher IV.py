flag = 0  
ans = 0

		for i in target:
        if int(i)!=flag:
        flag = not flag         #######if we change ith index all the index next to i will also change
        ans+=1

		return ans
