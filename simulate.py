import pybullet as p
import time
import numpy as np
import pybullet_data
import pyrosim.pyrosim as prs
import matplotlib.pyplot as plt
physicsClient = p.connect(p.GUI)
p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# set gravity to 9.81 in Z direction

p.setGravity(0,0,-9.81)

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("Robot2.urdf")
duration = 100000
x1 = np.linspace(0,100*2*np.pi, duration)
x2 = np.linspace(0,100*2*np.pi, duration)
plt.plot(x1,'r-',)
# plt.plot(x2,'b-')
plt.xlabel("time")
plt.ylabel("input signal")
plt.show()
# y1 = x1%(2*np.pi)-np.pi
# y2 = x2%(2*np.pi)-np.pi



prs.Prepare_To_Simulate(robotId)

for t in range(duration):
    prs.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Body_Lwheel',
            controlMode = p.POSITION_CONTROL, targetPosition = x1[t],maxForce = 50)
    #contactPoints = p.getContactPoints()
    # if contactPoints:
    #    print("Collision detected!")
    prs.Set_Motor_For_Joint(bodyIndex = robotId, jointName = b'Body_Rwheel',
            controlMode = p.POSITION_CONTROL, targetPosition = x2[t],maxForce = 50)
    p.stepSimulation()
    time.sleep(1/500)
    # if contactPoints:
    #     print("Collision detected!")
    #     continue
    

p.disconnect()




