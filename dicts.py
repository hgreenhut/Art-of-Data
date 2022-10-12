story = { 
 "title": "Invisible Planets", 
 "author": "Hao Jingfang", 
 "published": 2013 
} 

#story["words"] = 6359

#print(story)

#story["title"] = "Folding Beijing"
#print(story["title"])

#story["translator"] = "Ken Liu"
#print(story)

#del story['published']
#print (story)

#for x in story: 
 #print(story[x]) 

for (k,v) in story.items(): 
 print(k) 
 print(v) 




def count(x):
    dict = {}
    for i in x:
        dict[i] = x.count(i)
    return dict


print(count([4,5,4,4]))

        
