from fluentJoints import FluentJoints

class FluentArms():

    # init method
    def __init__(self, fluentNao, elbows, wrists, hands):
        
        self.elbows = elbows
        self.wrists = wrists
        self.hands = hands

        # jobs for threading
        self.fluentNao = fluentNao
        self.joints = fluentNao.joints
        self.chains = fluentNao.chains
        self.log = fluentNao.log

    def go(self):
        self.fluentNao.go()
        
    ###################################
    # Forward
    ###################################
    def forward(self, duration=0, offset=0):   
        self.rForward(duration, offset)
        self.lForward(duration, offset)
        return self;

    def lForward(self, duration=0, offset=0):
        duration = self.fluentNao.determineDuration(duration)       
        angle = 0 + offset
        self.fluentNao.moveWithDegreesAndDuration(self.joints.LArm.LShoulderPitch, angle, duration)
        self.fluentNao.moveWithDegreesAndDuration(self.joints.LArm.LShoulderRoll, 0, duration)

        return self;
        
    def rForward(self, duration=0, offset=0):
        duration = self.fluentNao.determineDuration(duration)  
        angle = 0 + offset
        self.fluentNao.moveWithDegreesAndDuration(self.joints.RArm.RShoulderPitch, angle, duration)
        self.fluentNao.moveWithDegreesAndDuration(self.joints.RArm.RShoulderRoll, 0, duration)
        return self;

    ###################################
    # Out
    ###################################
    def out(self, duration=0, offset=0):     
        self.rOut(duration, offset)
        self.lOut(duration, offset)
        return self;

    def lOut(self, duration=0, offset=0):     
        duration = self.fluentNao.determineDuration(duration)  
        angle = 90 + offset
        self.fluentNao.moveWithDegreesAndDuration(self.joints.LArm.LShoulderRoll, angle, duration)
        self.fluentNao.moveWithDegreesAndDuration(self.joints.LArm.LShoulderPitch, 0, duration)
        return self;
        
    def rOut(self, duration=0, offset=0):
        duration = self.fluentNao.determineDuration(duration)  
        angle = -90 - offset
        self.fluentNao.moveWithDegreesAndDuration(self.joints.RArm.RShoulderRoll, angle, duration)
        self.fluentNao.moveWithDegreesAndDuration(self.joints.RArm.RShoulderPitch, 0, duration)
        return self;

    ###################################
    # Up
    ###################################
    def up(self, duration=0, offset=0):     
        self.rUp(duration, offset)
        self.lUp(duration, offset)
        return self;

    def lUp(self, duration=0, offset=0):
        duration = self.fluentNao.determineDuration(duration)    
        angle = -90 - offset
        self.fluentNao.moveWithDegreesAndDuration(self.joints.LArm.LShoulderPitch, angle, duration)
        self.fluentNao.moveWithDegreesAndDuration(self.joints.LArm.LShoulderRoll, 0, duration)
        return self;
        
    def rUp(self, duration=0, offset=0):
        duration = self.fluentNao.determineDuration(duration)   
        angle = -90 - offset
        self.fluentNao.moveWithDegreesAndDuration(self.joints.RArm.RShoulderPitch, angle, duration) 
        self.fluentNao.moveWithDegreesAndDuration(self.joints.RArm.RShoulderRoll, 0, duration)
        return self;

    ###################################
    # Down
    ###################################
    def down(self, duration=0, offset=0):     
        self.rDown(duration, offset)
        self.lDown(duration, offset)
        return self;

    def lDown(self, duration=0, offset=0):
        duration = self.fluentNao.determineDuration(duration)   
        angle = 90 + offset
        self.fluentNao.moveWithDegreesAndDuration(self.joints.LArm.LShoulderPitch, angle, duration)
        self.fluentNao.moveWithDegreesAndDuration(self.joints.LArm.LShoulderRoll, 0, duration)
        return self;
        
    def rDown(self, duration=0, offset=0):
        duration = self.fluentNao.determineDuration(duration)   
        angle = 90 + offset
        self.fluentNao.moveWithDegreesAndDuration(self.joints.RArm.RShoulderPitch, angle, duration) 
        self.fluentNao.moveWithDegreesAndDuration(self.joints.RArm.RShoulderRoll, 0, duration)
        return self;


    ###################################
    # Back
    ###################################
    def back(self, duration=0, offset=0):     
        self.rBack(duration, offset)
        self.lBack(duration, offset)
        return self;

    def lBack(self, duration=0, offset=0):
        duration = self.fluentNao.determineDuration(duration)  
        angle = 119.5 + offset
        self.fluentNao.moveWithDegreesAndDuration(self.joints.LArm.LShoulderPitch, angle, duration)
        self.fluentNao.moveWithDegreesAndDuration(self.joints.LArm.LShoulderRoll, 0, duration)
        return self;
        
    def rBack(self, duration=0, offset=0):
        duration = self.fluentNao.determineDuration(duration)  
        angle = 119.5 + offset
        self.fluentNao.moveWithDegreesAndDuration(self.joints.RArm.RShoulderPitch, angle, duration) 
        self.fluentNao.moveWithDegreesAndDuration(self.joints.RArm.RShoulderRoll, 0, duration)
        return self;