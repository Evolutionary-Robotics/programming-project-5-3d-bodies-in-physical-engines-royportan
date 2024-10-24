import pyrosim.pyrosim as ps 

# rectangular box with h = 4 w =4 l = 7

l = 4
w = 2
h = 1

l1 = 2
w1 =1
h1 = 2

x0 = 0
y0 = 0
z0 = h/2


xj1 = l
yj1 = w
zj1 = h

xj2 = 0
yj2 = 0
zj2 = 0 

xw1 = 0
yw1 = 0
zw1 = 0

xw2 = 0
yw2 = 0
zw2 = 0


def Create_Robot():
    ps.Start_URDF("Robot1.urdf")
    ps.Send_Cube(name = "link1", pos = [x0,y0,z0], size = [l,w,h])
    ps.Send_Joint(name = "link1_link2",parent = "link1",child ="link2",type = "revolute",position = [x0+l/2,y0,z0+h/2])
    ps.Send_Cube(name = "link2",pos = [l/2 , 0, -h/2],size= [l,w,h])
    ps.End()
def Create_Robot2():
    ps.Start_URDF("Robot2.urdf")
    ps.Send_Cube(name = "Body", pos = [x0,y0,z0], size = [l,w,h])
    ps.Send_Joint(name = "Body_Lwheel", parent= "Body", child="Lwheel",type = "revolute",position = [x0,y0+w/2,z0])
    ps.Send_Cube(name = "Lwheel",pos =[0,w1/2,0],size=[l1,w1,h1])
    ps.Send_Joint(name = "Body_Rwheel", parent= "Body", child="Rwheel",type = "revolute",position = [x0,y0-w/2,z0])
    ps.Send_Cube(name= "Rwheel",pos = [0,-w1/2,0],size=[l1,w1,h1])
Create_Robot2()

