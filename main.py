# language compiler
# author John Moore
# date 12/07/2023

# language
# bit wise manipulation
# > < to shift the bit pointer
# + - to increment or decrement the value at the bit pointer
# . to print the value at the bit pointer


with open('code.txt') as f:
    lines = f.readlines()
    
#initalize instruction set
instructions = [] 
instructionSet = ['>', '<', '+', '-', '.', '[', ']']


#seperate instructions into list
def seperateInstructions(instructions):
    # for each line
  for line in lines:
      # for each line
      for operation in line:
          # for each operation
          instructions.append(operation)
    # return list
  return instructions


def runTimeError(msg):
  if msg:
    print(msg)
  exit()


def removeNull(instruction):
  out = [x for x in instruction if x  in instructionSet]
  # out = set(instructions) - set(instructionSet)
  return out

def checkBalancedBrackets(instruction):
  openBrackets = 0
  closeBrackets = 0

  for operation in instruction:
    if operation == '[':
      openBrackets = openBrackets + 1
    elif operation == ']':
      closeBrackets = closeBrackets + 1


  if openBrackets != closeBrackets:
    runTimeError("error: brackets are not balanced")
    exit()

instructions = seperateInstructions(instructions) # seperate instructions into list
instructions = removeNull(instructions) # remove characters that are out of instruction set
checkBalancedBrackets(instructions) #check if brackets are balanced

#define a tape 256 bits
tapeLength = 256
tape = [0] * tapeLength



def printValue(pos):
  print(chr(tape[pos]), end="")
  # print(tape[: 8])

def incrementValue(pos):
  tape[pos] += 1

def decrementValue(pos):
  tape[pos] -= 1


def moveRight(pos):
  if pos > tapeLength:
    runTimeError("error: out of tape bounds")
    exit()
  else:
    return pos + 1 

def moveLeft(pos):
  if pos < 1:
    runTimeError("error: can't move left")
    exit()
  else:
    return pos - 1
  
  currentValue = tape[pos] # when current value is 0, exit loop, pick up instruction set until end of loop
def loopInstructions(innerInstructions, pos, currentValue):
  # loop through instructions until tape[pos] == 0
  loopPos = pos
  wolf = 0
  while(tape[loopPos] != 0):
    

    for currentOperation in innerInstructions:
      pos = activeInstruction(currentOperation, pos)
      # print(tape[: 8])

      wolf = wolf + 1
      if wolf == 100000:
        runTimeError("error: infinite loop?")
        exit()

def activeInstruction(currentOperation, pos):

  match currentOperation:
    case '>':
      pos = moveRight(pos)
    case '<':
      pos = moveLeft(pos)
    case '+':
      incrementValue(pos)
    case '-':
      decrementValue(pos)
    case '.':
      printValue(pos)
    case '[':
        innerInstructions = []
        currentOperation = instructions.pop(0)
        while(currentOperation != ']'):
          innerInstructions.append(currentOperation)
          currentOperation = instructions.pop(0)
        loopInstructions(innerInstructions, pos, tape[pos]) 
  
  return pos  
      
pos = 0 #bit pointer

while(len(instructions) != 0):
  currentOperation = instructions.pop(0) #remove first instruction
  pos = activeInstruction(currentOperation, pos)


     
  



