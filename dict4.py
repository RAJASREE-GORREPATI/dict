# Get the values  id	type	name	image.width	image.height	image.url
# Expected Output
'''
{
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "image.url": "images/0001.jpg",
    "image.width": 200,
    "image.height": 200
}
'''
d = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "image":
        {
            "url": "images/0001.jpg",
            "width": 200,
            "height": 200
        },
    "thumbnail":
        {
            "url": "images/thumbnails/0001.jpg",
            "width": 32,
            "height": 32
        }
}
d1={}
for e in d:
    if type(d[e])==str:
        d1[e]=d[e]
    else:
        if e=="image":
            for k in d[e]:
                d1[e+"."+k]=d[e][k]          
print(d1)
    
    
    

