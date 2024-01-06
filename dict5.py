# Expected Output
'''
{
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "image.url": "images/0001.jpg",
    "image.width": 200,
    "image.height": 200,
    "thumbnail.url": "images/thumbnails/0001.jpg",
    "thumbnail.width": 32,
    "thumbnail.height": 32
   
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
new_d={}
for k in d:
    if type(d[k])==str:
        new_d[k]=d[k]
    else:
        for s in d[k]:
            new_d[k+"."+s]=d[k][s]
print(new_d)
            
