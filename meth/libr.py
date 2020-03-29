import random
def match(df):
    	x=random.randrange(len(df)-1)
    	y=random.randrange(len(df)-1)
    	z=random.randrange(len(df)-1)
    	while y==x:
    	    y+=1
    	while z==x or z==y:
    	    z+=1
    	return [x,y,z]

def additional(days,i,food_items):
    	return (k for k in [x for x in list(set(range(len(food_items)-1))-set(days[i]))] if k not in days[i-1])
