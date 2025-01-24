from math import sqrt

class point :
     def __init__(self, x, y):
        self.x = x
        self.y = y

def xd(p1,p2):
    return (p2.x-p1.x)

def yd(p1,p2):
    return p2.y-p1.y

def dist(l:list[point]):
    return distance(l[0],l[1])

def distance(p1:point,p2:point):
    return sqrt((xd(p1,p2)**2)+(yd(p1,p2)**2))

def bruteForce(P:list, n):
    mdp = [point(0,0),point(1000,1000)]
    
    for i in range(n-1):
        for j in range(i+1, n):
            #print(i,j, len(P))
            if distance(P[i], P[j]) < distance(mdp[0],mdp[1]):
                mdp =[P[i], P[j]]
    return (mdp[0],mdp[1])

def strip(strip, size, d):
    min_dist = d
    points=[point(0,0),point(1000,1000)]
    strip = sorted(strip, key=lambda point: point.y)
 
    for i in range(size-1):
        for j in range(i+1, size):
            if (strip[j].y - strip[i].y) >= min_dist:
                break
            if distance(strip[i], strip[j]) <min_dist:
                min_dist = distance(strip[i], strip[j])
                points=[strip[i], strip[j]]
    return (points[0],points[1]) 
def closest(points , n):
    
    if n<4 :
        return bruteForce(points , n)
    else:
        mid=n//2
        mp=points[mid]
        l1 = list(closest(points[:mid],mid))
        l2 = list(closest(points[mid:],n-mid))
        d=min(dist(l1),dist(l2))
        s = []
        for i in range(n):
            if abs(points[i].x - mp.x) < d:
                s.append(points[i])
        l3=list(strip(s,len(s),d))
        mini=sorted([l1,l2,l3],key=dist )
        return (mini[0][0],mini[0][1])
        

if __name__ == "__main__":
    n=int(input())
    points=[]
    for i in range(n):
        x,y=map(int,input().split())
        points.append(point(x,y)) 
    points=sorted(points,key=lambda point:point.x) 
    p1,p2 =closest(points,n)
    print(p1.x,p1.y,sep=" ")
    print(p2.x,p2.y,sep=" ")