crew_members = ['nini ochigava','luka gamreklidze','leqso pataraia','mate shotaia','niko kutateladze','nikolas bobokhidze']

my_name = "nini ochigava"

for i in range (len(crew_members) - 1, -1, -1):
    if len(my_name) == len(crew_members[i]):
        crew_members.pop(i)

print(crew_members)