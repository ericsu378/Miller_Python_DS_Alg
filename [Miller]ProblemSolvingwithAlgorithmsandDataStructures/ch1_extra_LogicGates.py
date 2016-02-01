__author__ = 'ESU_2'

# Problem Solving with Algorithms and Data Structures [Online]
# http://interactivepython.org/
# Brad Miller, David Ranum

# 1.7 Logic Gates

# System Diagram

#               Logic Gate
#               /        \
#       Binary Gate      Unary Gate
#       /        \             \
#     AND        OR            NOT

# IS-A relationship (which requires inheritance)
# HAS-A relationships (with no inheritance)


class LogicGate:

    def __init__(self, n):
        self.label = n # name
        self.output = None # output

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


# Each gate input can be either external (user) or from output of aconnected gate
class BinaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self,n) # init parent class constructors
        # init own distinguished data
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")

class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")


class AndGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==0 and b==0:
            return 0
        else:
            return 1


class NotGate(UnaryGate):

    def __init__(self, n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):

        pin = self.getPin()
        if pin == 0:
            return 1
        if pin == 1:
            return 0


# a Connector HAS-A LogicGate (connectors will have instances of LogicGate but are not part of the hierarchy)
# connector ends are referred to as 'fromgate' and 'togate'
class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


# Self Check
# Create a two new gate classes, one called NorGate the other called NandGate.
# NandGates work like AndGates that have a Not attached to the output.
# NorGates work like OrGates that have a Not attached to the output.
#
# Create a series of gates that prove the following equality
# NOT (( A and B) or (C and D)) is that same as NOT( A and B ) and NOT (C and D).
# Make sure to use some of your new gates in the simulation.

class NorGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==0 and b==0:
            return 1
        else:
            return 0


class NandGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 0
        else:
            return 1


def main():

    # Chapter Simulation
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1,g3)
    c2 = Connector(g2,g3)
    c3 = Connector(g3,g4)
    print(g4.getOutput())

    # NOT (( A and B) or (C and D))
    g5 = AndGate("G5")
    g6 = AndGate("G6")
    g7 = NorGate("G7")
    c4 = Connector(g5, g7)
    c5 = Connector(g6, g7)
    print(g7.getOutput())

    # NOT( A and B ) and NOT (C and D)
    g8 = NandGate("G8")
    g9 = NandGate("G9")
    g10 = AndGate("G10")
    c6 = Connector(g8, g10)
    c7 = Connector(g9, g10)
    print(g10.getOutput())

main()