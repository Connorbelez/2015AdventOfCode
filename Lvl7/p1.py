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

# cache = {}

# circuit = {"dummyWire": ["NOT","dummyWire2"], "dummyWire2": ["123"]}  


#wire is the target wire, it is the key in the dictionary, the value is the command and inputs
def findValue(wire,circuit,cache):
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
        cache[wire] = findValue(inputs[0], circuit,cache)
        return cache[wire]
    elif command == "NOT":
        cache[wire] = ~findValue(inputs[0], circuit,cache)
        return cache[wire]
    elif command == "AND":
        cache[wire] = findValue(inputs[0], circuit,cache) & findValue(inputs[1], circuit,cache)
        return cache[wire]
    elif command == "OR":
        cache[wire] = findValue(inputs[0], circuit,cache) | findValue(inputs[1], circuit,cache)
        return cache[wire]
    elif command == "LSHIFT":
        cache[wire] = findValue(inputs[0], circuit,cache) << findValue(inputs[1], circuit,cache)
        return cache[wire]
    elif command == "RSHIFT":
        cache[wire] = findValue(inputs[0], circuit,cache) >> findValue(inputs[1], circuit,cache)
        return cache[wire]
    

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
    cache = {}
    circuit = {}
    with open("/Users/connorbeleznay/Projects/Personal/AdventOfCode/2015/Lvl7/data7p1.txt", "r") as f:
        for line in f:

            command, inputs = getCommand(line)
            target = inputs.pop()
            for i,inp in enumerate(inputs):
                if inp.isnumeric():
                    inputs[i] = int(inp)
            
            circuit[target] = [command] + inputs
    print(circuit['b'])
    # a = findValue('a', circuit)
    z = findValue('a', circuit,cache)
    print("z: ",z)
    a = 16076
    cache['b'] = a 
    circuit['b'] = ['->',a]
    
    vala = findValue("a", circuit,cache)
    print(vala)
    # cache = {}
    