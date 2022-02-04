
#file1 = input file     file2=output file
file1 = open(r"C:\Users\nk\Desktop\python\a_an_example.in.txt")
file2 = open(r"C:\Users\nk\Desktop\python\example.txt","w")

#data structures to store the input
customer =dict()
item = dict()

cases = int(file1.readline())

#iterate over each customer
for i in range(cases):
    likes = file1.readline().rstrip().split()[1:]
    dislikes = file1.readline().rstrip().split()[1:]
    
    #store likes and dislikes of that customer
    customer[i+1]=[likes,dislikes]

    #for each liked item, store that customer(that is, i+1) in item dictionary item[][0]
    for val in likes:
        if val in item:
            item[val][0].append(i+1)
        else:
            item[val]=[[i+1],[]]
    
    #for each disliked item, store that customer(that is, i+1) in item dictionary item[][1]
    for val in dislikes:
        if val in item:
            item[val][1].append(i+1)
        else:
            item[val]=[[],[i+1]]

#main conflict matrix to represent all the incompatible customers
conflict=dict()
conflict_size=dict()

#go through each customer, creating a list of conflicts for that customer
for person in customer:
    conflict[person]=set()
    
    #compare this customer's disliked items against liked items of all the other customers
    for disliked_item in customer[person][1]:
        for val in item[disliked_item][0]:
            if val != person:
                conflict[person].add(val)
                
    #compare this customer's liked items against disliked items of all the other customers
    for liked_item in customer[person][0]:
        for val in item[liked_item][1]:
            if val!= person:
                conflict[person].add(val)
    
    #store the number of conflicts for each customer
    conflict_size[person]=len(conflict[person])


print('conflict matrix',conflict)
print('conflict_size',conflict_size)


#main algo to calculate the result which is a list of all compatible customers
result=[]
while(conflict_size):
    min_val=10000

    #find the customer with minimum conflicts
    for k,v in conflict_size.items():
        if v < min_val:
            min_val=v
            min_key=k
    #add that customer to the result
    result.append(min_key)

    #delete that customer from the conflict matrix
    del conflict_size[min_key]

    #remove all the customers that had a conflict with the added customer, as they
    #cannot be in the result anymore
    for cust in conflict[min_key]:
        flag=conflict_size.pop(cust,-1)

        #For all the customers that were just removed, remove their effect on the result of the customers
        #If any other customers had a conflict with the removed ones, reduce that number
        if flag!=-1:
            for temp_cust in conflict[cust]:
                if temp_cust in conflict_size.keys():
                    conflict_size[temp_cust]-=1
    

#Now that we have all the customers in result, check which ingredients they want and that is the answer
ingredients = set()
for cust in result:
    for ingredient in customer[cust][0]:
        ingredients.add(ingredient) 

#store the final result (count & ingredients) in the output file
count = len(ingredients)
print(count,' '.join(ingredients),file=file2)
print('this is the final answer',result)

#close the files
file1.close()
file2.close()





#recursive approach -- optimal solution -- IGNORE
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
