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
instructionSet = ['>', '<', '+', '-', '.'] # '[', ']'


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


instructions = seperateInstructions(instructions)
instructions = removeNull(instructions)

#define a tape 256 bits
tapeLength = 256
tape = [0] * tapeLength

def printValue(pos):
  print(chr(tape[pos]))

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
    

while(len(instructions) != 0):
  currentOperation = instructions.pop(0) #remove first instruction
  pos = 1 #bit pointer

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
    case _:
        print("not implemented")
     
  



