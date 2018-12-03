import numpy as np
data = open("input3").read().splitlines()
#data = "#1 @ 1,3: 4x4\n #2 @ 3,1: 4x4\n#3 @ 5,5: 2x2".splitlines()
claims = []
for claim in data:
    n1 = claim.find("@ ")+2
    n1e = claim.find(",")
    n2 = n1e + 1
    n2e = claim.find(": ")
    n3 = n2e + 2
    n3e = claim.find("x")
    n4 = n3e + 1
    x0 = int(claim[n1:n1e])
    y0 = int(claim[n2:n2e])
    x1 = int(claim[n3:n3e]) + x0
    y1 = int(claim[n4:]) + y0
    claims.append(((x0,y0),(x1,y1)))
fabric = np.zeros((1000,1000))
for claim in claims:
    fabric[claim[0][0]:claim[1][0],claim[0][1]:claim[1][1]] += 1
        
count = len(fabric[np.where(fabric > 1)])
    
print(count)

fabric[:,:] -= 1
for claim in claims:
    if not np.any(fabric[claim[0][0]:claim[1][0],claim[0][1]:claim[1][1]]):
        print(claims.index(claim) + 1)
