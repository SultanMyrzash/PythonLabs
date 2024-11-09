# 1.1
sozder = "Pulp Fiction"
slist = []
for i in sozder:
    slist.append(i.lower())
print(slist)

# 1.2
slist = [('p', 2), ('u', 1), ('l', 1), (' ', 1), ('f', 1), ('i', 2), ('c', 1), ('t', 1), ('o', 1), ('n', 1)]
vowels = ["a","e","i","o","u"]
cons = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
list_vow = []
list_cons = []
list_sym = []

for i in slist:
    if i[0] in vowels:
        list_vow.append(i)
    elif i[0] in cons:
        list_cons.append(i)
    else:
        list_sym.append(i)
print(list_vow)
print(list_cons)
print(list_sym)

# 2.1
st_scores = {'name':'Adam', 'assignments' : [82, 56, 44, 30], 'labs' : [78.20, 77.20], 'tests' : [78, 77]}
print(st_scores)

# 2.2
activities = 0
for value in st_scores.values():
    if type(value) == list:
        activities += len(value)
submission_check = {st_scores['name'] : activities}
print(submission_check)

# 2.3
def average(a):
    sum = 0
    for san in a:
        sum += san
    return sum/len(a)

fgrade = 0
if activities > 6:
    fgrade = 0.3*average(st_scores['assignments']) + 0.5*average(st_scores['labs']) + 0.2*average(st_scores['tests'])
    print(fgrade)

# 2.4
st_scores['final_grade'] = fgrade
print(st_scores)