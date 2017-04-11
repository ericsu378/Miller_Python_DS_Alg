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

# Self Check
# Create a two new gate classes, one called NorGate the other called NandGate.
# NandGates work like AndGates that have a Not attached to the output.
# NorGates work lake OrGates that have a Not attached to the output.

# Create a series of gates that prove the following equality
# NOT (( A and B) or (C and D)) is that same as NOT( A and B ) and NOT (C and D).
# Make sure to use some of your new gates in the simulation.

# Additional Programming Exercises [1.17]
# 10) Research other types of gates that exist (such as NAND, NOR, and XOR). Add them to the circuit hierarchy.
#     How much additional coding did you need to do?
# 11) The most simple arithmetic circuit is known as the half-adder. Research the simple half-adder circuit.
#     Implement this circuit.
# 12) Now extend that circuit and implement an 8 bit full-adder.
# 13) The circuit simulation shown in this chapter works in a backward direction.
#     In other words, given a circuit, the output is produced by working back through the input values,
#     which in turn cause other outputs to be queried. This continues until external input lines are found,
#     at which point the user is asked for values. Modify the implementation so that the action is in the
#     forward direction; upon receiving inputs the circuit produces an output.

class LogicGate:

    def __init__(self, n):
        self.label = n # name
        self.output = None # output

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


# Each gate input can be either external (user) or from output of a connected gate
class BinaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self,n) # init parent class constructors
        # init own distinguished data
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
        # elif self.pinA == 1 or self.pinA == 0:
        #     return self.pinA
        # # # Redundant Maybe?
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))
        # elif self.pinB == 1 or self.pinB == 0:
        #     return self.pinB
        # # Redundanct Maybe?
        else:
            return self.pinB.getFrom().getOutput()

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

    def __init__(self, n):
        LogicGate.__init__(self, n)
        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate " + self.getLabel() + "-->"))
        # elif self.pin == 1 or self.pin == 0:
        #     return self.pin
        # # Redundant Maybe?
        else:
            return self.pin.getFrom().getOutput()

    def setPin(self, value):
        self.pin = int(value)

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Cannot Connect: NO EMPTY PINS on this gate")


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
        if self.getPin():
            return 0
        else:
            return 1


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

# 10) Research other types of gates that exist (such as NAND, NOR, and XOR). Add them to the circuit hierarchy.
#     How much additional coding did you need to do?
#     Answer: Not much. Just need to implement XOR (if a==b, return 0, else return 1), XNOR (reverse XOR)

class XOrGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==b:
            return 0
        else:
            return 1


class XNorGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==b:
            return 1
        else:
            return 0


# 11) The most simple arithmetic circuit is known as the half-adder. Research the simple half-adder circuit.
#     Implement this circuit.
#     2 gates, XOR and AND gate.

class HalfAdder(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        # Sum Logic [XOR]
        if a==b:
            Sum =  0
        else:
            Sum =  1

        # Carry Logic [AND]
        if a==1 and b==1:
            Carry =  1
        else:
            Carry =  0

        return Sum, Carry


# def HalfAdder():
#
#     g1 = BinaryGate("G1")
#     g2 = XOrGate("G2")
#     # g1.setPinA(inputA)
#     # g1.setPinB(inputB)
#     g3 = AndGate("G3")
#     # g2.setPinA(inputA)
#     # g2.setPinB(inputB)
#     c1 = Connector(g1, g2)
#     c2 = Connector(g1, g3)
#     print(g2.getOutput())
#     print(g3.getOutput())


# 12) Now extend that circuit and implement an 8 bit full-adder.
class HalfAdder(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        # Sum Logic [XOR]
        if a==b:
            Sum =  0
        else:
            Sum =  1

        # Carry Logic [AND]
        if a==1 and b==1:
            Carry =  1
        else:
            Carry =  0

        return Sum, Carry



def FullAdder(inputC, inputA, inputB):
    (sum1, carry1) = HalfAdder(inputA, inputB)
    (sum2, carry2) = HalfAdder(inputC, sum1)
    g1 = OrGate('G1')
    g1.setPinA(carry2)
    g1.setPinB(carry1)
    print("Full Adder Input: C = %d, A = %d, B = %d \nFull Adder Output: sum = %d, carry = %d" %(inputC, inputA, inputB, sum2, g1.getOutput()))
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
    print("G4 Output = " + str(output))


def main():

    # # Chapter Simulation
    # g1 = AndGate("G1")
    # g2 = AndGate("G2")
    # g3 = OrGate("G3")
    # g4 = NotGate("G4")
    # c1 = Connector(g1,g3)
    # c2 = Connector(g2,g3)
    # c3 = Connector(g3,g4)
    # print(g4.getOutput())

    # # NOT (( A and B) or (C and D))
    # g5 = AndGate("G5")
    # g6 = AndGate("G6")
    # g7 = NorGate("G7")
    # c4 = Connector(g5, g7)
    # c5 = Connector(g6, g7)
    # print(g7.getOutput())

    # # NOT( A and B ) and NOT (C and D)
    # g8 = NandGate("G8")
    # g9 = NandGate("G9")
    # g10 = AndGate("G10")
    # c6 = Connector(g8, g10)
    # c7 = Connector(g9, g10)
    # print(g10.getOutput())

    print("Additional Programming Exercise")
    h1 = HalfAdder("H1")
    print(h1.getOutput())
    # FullAdder(1, 0, 0)
    # ForwardChapterSim(1, 1, 1, 0)


if __name__ == '__main__':
    main()