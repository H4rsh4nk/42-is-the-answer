
file1 = open(r"C:\Users\nk\Desktop\python\a_an_example.in.txt")
file2 = open(r"C:\Users\nk\Desktop\python\result.txt","w")

n_contributors, n_projects = file1.readline().rstrip().split()
contributors = dict()
projects = dict()
skills = dict()

for i in range(int(n_contributors)):
    temp_contributor, n_skills = file1.readline().rstrip().split()
    contributors[temp_contributor]=dict()
    for j in range(int(n_skills)):
        temp_skill, temp_level = file1.readline().rstrip().split()
        contributors[temp_contributor][temp_skill]=temp_level

for i in range(int(n_projects)):
    name, days, score, deadline, roles = file1.readline().rstrip().split()
    projects[name]=dict()
    for j in range(int(roles)):
        p_skill,p_level = file1.readline().rstrip().split()
        projects[name][p_skill]=p_level




print('contributors: ',contributors)
print('projects: ',projects)

result=dict()

for name in projects.keys():
    temp_contributors=[]
    for skill,level in projects[name].items():
        flag=0
        for contributor_name, skill_list in contributors.items():
            for skill_name,skill_level in skill_list.items():
                if skill_name == skill and skill_level >= level:

                    temp_contributors.append(contributor_name)
                    flag=1
        if not flag:
            break
    if not flag:
        continue
    result[name]=temp_contributors
    # for p_contributor in result[name]:
    #     if contributors[p_contributor][]

print('result: ',result)

    
        
                



