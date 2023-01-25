

class PID():
    def __init__(self,kp, ki, kd , windupMax):
        self.kp = kp
        self.ki = ki
        self.kd = kd

        self.iTerm = 0

        self.tprev = 0

        self.dt = 0.001 #servo cycle time
        self.time = 0
        self.qprev = self.senseAngle() # initial joint angle q
        self.windupMax = windupMax

    def controller(self, time):
        [qd,qdotd] = self.trajectory(time) #get desired angle and desired velocity
        q = self.senseAngle() # sense actual joint angle
        qdot = (q - self.qprev)/self.dt
        q = self.qprev

        e = qd - q
        edot = qdotd - qdot

        eint = eint + e*self.dt #integral error
        tau = self.kp*e + self.kd*edot + self.ki*eint
        self.time = self.time + self.dt
        return tau

        

    
    def antiWindUp(self):
        if self.windupMax != 0:
            if self.iTerm > self.windupMax:
                self.iTerm = self.windupMax
            elif self.iTerm < -self.windupMax:
                self.iTerm = -self.windupMax


    def trajectory(self,time):
        pass

    def senseAngle():
        pass

