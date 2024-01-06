# Expected Output
'''
topping_data = {"ids": ["5001","5002", "5005", "5007", "5006", "5003", "5004"],
                "types" ["None", "Glazed", "Sugar", "Powdered Sugar","Chocolate with Sprinkles", "Chocolate", "Maple" ]}
'''
d = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "batters":{
        "batter":
            [
                { "id": "1001", "type": "Regular" },
                { "id": "1002", "type": "Chocolate" },
                { "id": "1003", "type": "Blueberry" },
                { "id": "1004", "type": "Devil's Food" }
            ]
    },
    "topping":
        [
            { "id": "5001", "type": "None" },
            { "id": "5002", "type": "Glazed" },
            { "id": "5005", "type": "Sugar" },
            { "id": "5007", "type": "Powdered Sugar" },
            { "id": "5006", "type": "Chocolate with Sprinkles" },
            { "id": "5003", "type": "Chocolate" },
            { "id": "5004", "type": "Maple" }
        ]
}
l1=[]
l2=[]
for k in d:
    if k=="topping":
        r=d[k]
        for e in range(len(r)):
            for l in r[e]:
                if l=="id":
                    l1.append(r[e][l])
                else:
                    l2.append(r[e][l])
d1={"ids":l1,"types":l2}
print(d1)
                    
            
            

