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
    story = {}
    for i in x:
        story[i] = len(i)
    return story

print(count(["hello", "hello", "world", "hello"]))
        
