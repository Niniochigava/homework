import random

crew_member = ['nini ochigava','mariam revishvili','luka telia','luka gamreklidze','leqso pataraia','lazare gogoberidze','mate shotadze','niko kutateladze','nikolas bobokhidze','tornike karelidze','erekle gochitashvili']
 
choice  = random.choice(crew_member)
choice2 = (choice + ' ' + ' is cool')
choice3 = (choice + ' ' + 'stadies good')
if choice.endswith('i'):
    print(choice3)
else:
    print(choice2)