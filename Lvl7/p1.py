# --- Day 7: Some Assembly Required ---

# This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, 
# little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

# Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535).
# A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a
# signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

# The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

# For example:

# 123 -> x means that the signal 123 is provided to wire x.
# x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
# p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
# NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
# Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

# For example, here is a simple circuit:

# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i
# After it is run, these are the signals on the wires:

# d: 72
# e: 507
# f: 492
# g: 114
# h: 65412
# i: 65079
# x: 123
# y: 456

#In little Bobby's kit's instructions booklet (provided as your puzzle input),
# what signal is ultimately provided to wire a?

cache = {}
class Com:
    def __init__(self, command, inputs):
        self.command = command
        self.inputs = inputs
    def output(self):
        print(self.command)
        print(self.inputs)
        if self.command == "AND":
            return int(self.inputs[0]) & int(self.inputs[1])
        elif self.command == "OR":
            return int(self.inputs[0]) | int(self.inputs[1])
        elif self.command == "LSHIFT":
            return int(self.inputs[0]) << int(self.inputs[1])
        elif self.command == "RSHIFT":
            return int(self.inputs[0]) >> int(self.inputs[1])
        elif self.command == "NOT":
            return ~int(self.inputs[0])
        else:
            return int(inputs[0])

# circuit = {"dummyWire": ["NOT","dummyWire2"], "dummyWire2": ["123"]}  

circuit = {}
#wire is the target wire, it is the key in the dictionary, the value is the command and inputs
def findValue(wire,circuit):
    #we do this because we recursively search the input,
    #once we find an integer value we can return it
    if type(wire) == int:
        return wire
    
    if wire in cache:
        return cache[wire]
    
    print("Input To Wire: ", circuit[wire])
    
    inputs = circuit[wire]
    command = inputs.pop(0)

    for i,w in enumerate(inputs):
        if w in cache:
            inputs[i] = cache[w]

    if command == "->":
        cache[wire] = findValue(inputs[0], circuit)
        return cache[wire]
    elif command == "NOT":
        cache[wire] = ~findValue(inputs[0], circuit)
        return cache[wire]
    elif command == "AND":
        cache[wire] = findValue(inputs[0], circuit) & findValue(inputs[1], circuit)
        return cache[wire]
    elif command == "OR":
        cache[wire] = findValue(inputs[0], circuit) | findValue(inputs[1], circuit)
        return cache[wire]
    elif command == "LSHIFT":
        cache[wire] = findValue(inputs[0], circuit) << findValue(inputs[1], circuit)
        return cache[wire]
    elif command == "RSHIFT":
        cache[wire] = findValue(inputs[0], circuit) >> findValue(inputs[1], circuit)
        return cache[wire]
    
    
def get_value(wire, circuit):
    print("WIRE ",wire)
    if isinstance(wire, int):
        print("WIRE IS DIGIT: ",wire)
        return wire
    print(type(wire))
    if wire.isnumeric():
        print("Wire is numeric")
        return int(wire)
    
    print("Input to Wire: ",circuit[wire])
    wireVal = circuit[wire]
    if wire in cache:
        print("Cache hit: Wire: ", wire, " Value: ", cache[wire])
        return cache[wire]
    
    for i in range(len(wireVal)):
        if wireVal[i] in cache:
            wireVal[i] = cache[wireVal[i]]
        
    if wireVal[0] == "->":
        if wireVal[1].isnumeric():
            print("WireVal is numeric : ", wireVal[1])
            cache[wire] = int(wireVal[1])
            return int(wireVal[1])
        else :
            return get_value(wireVal[1], circuit)
        
    
    elif wireVal[0] == "NOT":
        print("NOT", "input1: ",wireVal[1]," output: ",wire)
        return ~(get_value(wireVal[1], circuit))
    elif wireVal[0] == "AND":
        print("AND", "input1: ",wireVal[1]," Input2: ", wireVal[2], " output: ",wire)
        
        if wireVal[1].isnumeric() and wireVal[2].isnumeric():
            print("Both inputs are numeric")
            cache[wire] = int(wireVal[1]) & int(wireVal[2])
            return int(wireVal[1]) & int(wireVal[2])
        
        return (get_value(wireVal[1], circuit) & get_value(wireVal[2], circuit))
    elif wireVal[0] == "OR":
        
        print("or", "input1: ",wireVal[1]," Input2: ", wireVal[2], " output: ",wire)
        return (get_value(wireVal[1], circuit) | get_value(wireVal[2], circuit))
    elif wireVal[0] == "LSHIFT":
        print("LSHIFT", "input1: ",wireVal[1]," output: ",wire)
        return (get_value(wireVal[1], circuit) << int(wireVal[2]))
    elif wireVal[0] == "RSHIFT":
        print("RSHIFT", "input1: ",wireVal[1]," output: ",wire)
        return (get_value(wireVal[1], circuit) >> int(wireVal[2]))


def getCommand(string):
    non_atomic = ['AND', 'OR', 'LSHIFT', 'RSHIFT']
    atomic = 'NOT'
    Command = "->"
    inputs = []
    lineProcessing = string.strip().split(" ")
    for command in non_atomic:
        if command in string:
            Command = command
            inputs.append(lineProcessing[0])
            inputs.append(lineProcessing[2])
            inputs.append(lineProcessing[4])
    if atomic in string:
        Command = atomic
        inputs.append(lineProcessing[1])
        inputs.append(lineProcessing[3])
    if Command == "->":
        inputs.append(lineProcessing[0])
        inputs.append(lineProcessing[2])
    
    return Command, inputs

if __name__ == "__main__":
    with open("/Users/connorbeleznay/Projects/Personal/AdventOfCode/2015/Lvl7/data7p1.txt", "r") as f:
        for line in f:

            command, inputs = getCommand(line)
            target = inputs.pop()
            for i,inp in enumerate(inputs):
                if inp.isnumeric():
                    inputs[i] = int(inp)
            
            circuit[target] = [command] + inputs

    # print(circuit)
    print(findValue("a", circuit))