import random

when = ["yesterday","Last night","a long time ago","On 22nd Jan",]
who = ["An elephant","A lion","A girl"," A boy"]
name = ["Ellie","Leo","Aurora","Austin"]
residence = ["A Forest","A Den","New York","London"]
went = ["River","Jungle","University","Cinema"]
happened = ["Made new friends","Caught its prey","learnt to code","ate some popcorn"]
print(random.choice(when) + "," + random.choice(who) + "named" + random.choice(name) + "," +"Who lived in" + random.choice(residence) + "went to the" + random.choice(went) + "and" + random.choice(happened))
