__author__ = 'ESU'

# Problem Solving with Algorithms and Data Structures [Online]
# http://interactivepython.org/
# Brad Miller, David Ranum

# 1.13.2 Inheritance: Logic Gates and Circuits

# System Diagram

#               Logic Gate
#               /        \
#       Binary Gate      Unary Gate
#       /        \             \
#     AND        OR            NOT

# IS-A relationship (which requires inheritance)
# HAS-A relationships (with no inheritance)

# Forward Implementation

class LogicGate:

    def __init__(self, name):
        self.label = name # name
        self.output = None # output

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


# Each gate input can be either external (user) or from output of a connected gate
class BinaryGate(LogicGate):

    def __init__(self, name):
        LogicGate.__init__(self, name) # init parent class constructors
        # init own distinguished data
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return self.pinA

    def getPinB(self):
        return self.pinB

    def setPinA(self, value):
        self.pinA = int(value)

    def setPinB(self, value):
        self.pinB = int(value)

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS on this gate")


class UnaryGate(LogicGate):

    def __init__(self, name):
        LogicGate.__init__(self, name)
        self.pin = None

    def getPin(self):
        return self.pin

    def setPin(self, value):
        self.pin = int(value)

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Cannot Connect: NO EMPTY PINS on this gate")


class OrGate(BinaryGate):

    def __init__(self, name):
        BinaryGate.__init__(self, name)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==0 and b==0:
            return 0
        else:
            return 1


class AndGate(BinaryGate):

    def __init__(self, name):
        BinaryGate.__init__(self, name)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0


class NotGate(UnaryGate):

    def __init__(self, name):
        UnaryGate.__init__(self, name)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1


class NorGate(BinaryGate):

    def __init__(self, name):
        BinaryGate.__init__(self, name)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 0 and b == 0:
            return 1
        else:
            return 0


class NandGate(BinaryGate):

    def __init__(self, name):
        BinaryGate.__init__(self, name)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 0
        else:
            return 1


class XOrGate(BinaryGate):

    def __init__(self, name):
        BinaryGate.__init__(self, name)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == b:
            return 0
        else:
            return 1


class XNorGate(BinaryGate):

    def __init__(self, name):
        BinaryGate.__init__(self, name)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == b:
            return 1
        else:
            return 0


# # a Connector HAS-A LogicGate (connectors will have instances of LogicGate but are not part of the hierarchy)
# # connector ends are referred to as 'fromgate' and 'togate'
# class Connector:
#
#     def __init__(self, fgate, tgate):
#         self.fromgate = fgate
#         self.togate = tgate
#
#         tgate.setNextPin(self)
#
#     def getFrom(self):
#         return self.fromgate
#
#     def getTo(self):
#         return self.togate


def HalfAdder(inputA, inputB):

    g1 = XOrGate("G1")
    g1.setPinA(inputA)
    g1.setPinB(inputB)
    g2 = AndGate("G2")
    g2.setPinA(inputA)
    g2.setPinB(inputB)
    return (g1.getOutput(), g2.getOutput())


# 12) Now extend that circuit and implement an 8 bit full-adder.
def FullAdder(inputC, inputA, inputB):
    (sum1, carry1) = HalfAdder(inputA, inputB)
    (sum2, carry2) = HalfAdder(inputC, sum1)
    g1 = OrGate('G1')
    g1.setPinA(carry2)
    g1.setPinB(carry1)
    return (sum2, g1.getOutput())
    # print("Full Adder Input: C = %d, A = %d, B = %d \nFull Adder Output: sum = %d, carry = %d" %(inputC, inputA, inputB, sum2, g1.getOutput()))
    # print("Full Adder Input: C = {}, A = {}, B = {}\nFull Adder Output: sum = {}, carry = {}").format(inputC, inputA, inputB, sum2, g1.getOutput())


# 13) The circuit simulation shown in this chapter works in a backward direction. In other words, given a circuit,
#     the output is produced by working back through the input values, which in turn cause other outputs to be queried.
#     This continues until external input lines are found, at which point the user is asked for values.
#     Modify the implementation so that the action is in the forward direction;
#     upon receiving inputs the circuit produces an output.
def ForwardChapterSim(inputA1, inputB1, inputA2, inputB2):

    A1 = inputA1
    B1 = inputB1
    A2 = inputA2
    B2 = inputB2

    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")

    g1.setPinA(A1)
    g1.setPinB(B1)
    g2.setPinA(A2)
    g2.setPinB(B2)
    g3_A = g1.getOutput()
    g3_B = g2.getOutput()

    g3.setPinA(g3_A)
    g3.setPinB(g3_B)
    g4_A = g3.getOutput()

    g4.setPin(g4_A)
    output = g4.getOutput()
    return output
    # print("G4 Output = " + str(output))


def main():

    print("Additional Programming Exercise")
    print(HalfAdder(0, 1))
    print(FullAdder(1, 0, 0))
    print(ForwardChapterSim(1, 1, 1, 0))


if __name__ == '__main__':
    main()