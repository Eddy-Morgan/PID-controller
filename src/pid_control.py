

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

    def fb_controller(self, time):
        [qd,qdotd] = self.trajectory(time) #get desired angle and desired velocity
        q = self.senseAngle() # sense actual joint angle
        qdot = (q - self.qprev)/self.dt

        e = qd - q
        edot = qdotd - qdot

        eint = eint + e*self.dt #integral error
        tau = self.kp*e + self.kd*edot + self.ki*eint
        self.qprev = q
        return tau

    def ff_controller(self, time):
        [qd,qdotd,qdotdotd] = self.trajectory(time) #get desired angle and desired velocity
        tau = self.Mtilde(qd)*qdotdotd + self.htilde(qd, qdotd)
        return tau

    def ff_fb_controller(self,time):
        [qd,qdotd,qdotdotd] = self.trajectory(time) #get desired angle and desired velocity
        q = self.senseAngle() # sense actual joint angle
        qdot = (q - self.qprev)/self.dt
        ff_acc = qdotdotd

        e = qd - q
        edot = qdotd - qdot
        eint = eint + e*self.dt #integral error
        fb_acc = self.kp*e + self.kd*edot + self.ki*eint
        tau = self.Mtilde(q)*(ff_acc+fb_acc) + self.htilde(q, qdot)

        self.qprev = q
        return tau

    def Mtilde(self, qd): 
        # inertia model
        pass

    def htilde(self, qd, qdotd):
        # dynamics that depends nonlinearly on the state
        pass
    
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

