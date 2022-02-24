
file1 = open(r"C:\Users\nk\Desktop\python\a_an_example.in.txt")
file2 = open(r"C:\Users\nk\Desktop\python\result.txt","w")

n_contributors, n_projects = file1.readline().rstrip().split()
contributors = dict()
projects = dict()
skills = dict()

for i in range(int(n_contributors)):
    temp_contributor, n_skills = file1.readline().rstrip().split()
    contributors[temp_contributor]=[]
    for j in range(int(n_skills)):
        temp_skill, temp_level = file1.readline().rstrip().split()
        contributors[temp_contributor].append([temp_skill,temp_level])

for i in range(int(n_projects)):
    name, days, score, deadline, roles = file1.readline().rstrip().split()
    projects[name]=[]
    for j in range(int(roles)):
        projects[name].append(file1.readline().rstrip().split())



print('contributors: ',contributors)
print('projects: ',projects)

result=dict()

for name in projects.keys():
    temp_contributors=[]
    for skill,level in projects[name]:
        flag=0
        for contributor_name, skill_list in contributors.items():
            for skill_item in skill_list:
                if skill_item[0] == skill and skill_item[1] >= level:
                    
                    temp_contributors.append(contributor_name)
                    flag=1
        if not flag:
            break
    if not flag:
        continue
    result[name]=temp_contributors

print('result: ',result)

    
        
                



