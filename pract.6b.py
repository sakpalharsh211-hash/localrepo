import geometry
def pointyshapevolume(x,y,squareBase):
    if squareBase:
        base=geometry.squarearea(x)


    else:
        base=geometry.circlearea(x)
    return y*base/3.0
#print(dir(geometry))
print(pointyshapevolume(4,2,True))
print(pointyshapevolume(4,2,False))
