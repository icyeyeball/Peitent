import jieba
import sys
result = [1,3,5,7,9,2,4,6,8,10]
'''
for i in range(0,len(result)-1):
    for j in range(0,len(result)-1-i): 
        if result[j] < result[j+1]:
            tmp = result[j]
            result[j]= result[j+1]
            result[j+1] = tmp
print(result)         
'''
'''
input = sys.argv[1]
seg_list = jieba.cut(input, cut_all=False)

print(" ".join(seg_list))
'''
result = [1,3,5,7,9]
for i in range(0,len(result)-1):
    print("i = "+str(i))
    for j in range(0,len(result)-1-i):
        print("j = "+str(j))
        if result[j] < result[j+1]:
            tmp = result[j]
            result[j]= result[j+1]
            result[j+1] = tmp
            print(result)
            
print(result)            