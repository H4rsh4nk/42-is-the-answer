from copy import deepcopy

""" to be used
def next_choice(conflict_size,next):
    print('entered function')
    print('next ',next)
    print('conflict_size ',conflict_size)
    ans=[]
    if not conflict_size:
        return ans
    copy_conflict=deepcopy(conflict_size)
    
    ans.append(next)
    #print('next value..',next)
    del copy_conflict[next]
    
    for cust in conflict[next]:
        print('cust ',cust)
        flag=copy_conflict.pop(cust,-1)
        if flag!=-1:
            for temp_cust in conflict[cust]:
                if temp_cust in copy_conflict.keys():
                    print('temp_cust ',temp_cust)
                    copy_conflict[temp_cust]-=1
    if not copy_conflict:
        return ans
    min_len = min(copy_conflict.values())
    min_conflicts = [i for i, val in copy_conflict.items() if val == min_len]

    # print('min_len',min_len)
    # print('min_conflicts',min_conflicts)
    # #min_conflicts = sorted(conflict.values(),key=len)

    result = []
    for test in min_conflicts:
        print('before next call..parameters..',copy_conflict,test)
        temp_result= next_choice(copy_conflict,test)
        if len(temp_result) > len(result):
            result=temp_result
    ans.extend(result)
    return ans

"""
    #print('discarded conflict',myconflict)
    #min_len = min(copy_conflict.values(),key=len)
    #print('min_len',min_len)
    #min_conflicts = [i for i, val in copy_conflict.items() if len(val) == len(min_len)]
    #print('next value: ',next,'min_conficts: ',min_conflicts)
    #print('min_conflicts inside function..',min_conflicts)
    # result=[]
    # for val in min_conflicts:
    #     temp = next_choice(copy_conflict,val)
    #     #print('this is temp...',temp)
    #     if len(temp) > len(result):
    #         result = temp
    #         #print('assigned result...',result)
    # #print('outside of for loop...',result)
    # ans.extend(result)
    # #print('this is returning value...',ans)
    # return ans
    


file1 = open(r"C:\Users\nk\Desktop\python\a_an_example.in.txt")
file2 = open(r"C:\Users\nk\Desktop\python\example.txt","w")
customer =dict()
item = dict()
cases = int(file1.readline())
for i in range(cases):
    likes = file1.readline().rstrip().split()[1:]
    dislikes = file1.readline().rstrip().split()[1:]
    #print('likes',likes,'dislikes',dislikes)
    customer[i+1]=[likes,dislikes]
    for val in likes:
        if val in item:
            item[val][0].append(i+1)
        else:
            item[val]=[[i+1],[]]
    for val in dislikes:
        if val in item:
            item[val][1].append(i+1)
        else:
            item[val]=[[],[i+1]]
#print('customer',customer)
#print('item',item)

conflict=dict()
conflict_size=dict()
#print('before',conflict_size)
for person in customer:
    conflict[person]=set()
    for disliked_item in customer[person][1]:
        for val in item[disliked_item][0]:
            if val != person:
                print(disliked_item,val)
                conflict[person].add(val)
    for liked_item in customer[person][0]:
        for val in item[liked_item][1]:
            if val!= person:
                conflict[person].add(val)
    conflict_size[person]=len(conflict[person])
print('conflict matrix',conflict)
print('conflict_size',conflict_size)
result=[]
while(conflict_size):
    min_val=10000
    for k,v in conflict_size.items():
        if v < min_val:
            min_val=v
            min_key=k
    result.append(min_key)
    del conflict_size[min_key]
    for cust in conflict[min_key]:
        #print('cust ',cust)
        flag=conflict_size.pop(cust,-1)
        if flag!=-1:
            for temp_cust in conflict[cust]:
                if temp_cust in conflict_size.keys():
                    #print('temp_cust ',temp_cust)
                    conflict_size[temp_cust]-=1
    


# min_len = min(conflict_size.values())
# min_conflicts = [i for i, val in conflict_size.items() if val == min_len]

# #print('min_len',min_len)
# #print('min_conflicts',min_conflicts)
# #min_conflicts = sorted(conflict.values(),key=len)

# result = []
# for test in min_conflicts:
# #     #print('working on..',val,conflict)
#     temp_result= next_choice(conflict_size,test)
#     if len(temp_result) > len(result):
#         result=temp_result

#print('this is the result: ',result)
ingredients = set()
for cust in result:
    for ingredient in customer[cust][0]:
        ingredients.add(ingredient) 
count = len(ingredients)
print(count,' '.join(ingredients),file=file2)
print('this is the final answer',result)
file1.close()
file2.close()
#print('final list of customers: ',result)
