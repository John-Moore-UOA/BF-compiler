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
pos = 1


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


def removeNullSet(instructions):
  # remove new line characters / could rather just ignore any chars and call them strings
  out = list(filter(('\n').__ne__, instructions))
  out = list(filter((' ').__ne__, out))
  return out

def testRemove(instruction):
  out = [x for x in instruction if x  in instructionSet]
  # out = set(instructions) - set(instructionSet)
  return out

def printValue():
  print(tape[pos])

def incrementValue():
  tape[pos] += 1

def decrementValue():
  tape[pos] -= 1

def moveRight():
  if pos < tapeLength:
    runTimeError("error: out of tape bounds")
    exit()
  else:
    pos += 1

def moveLeft():
  if pos > 0:
    pos -= 1
  else:
    runTimeError("error: can't move left")

instructions = seperateInstructions(instructions)
instructions = testRemove(instructions)
print(instructions)

#define a tape 256 bits
tapeLength = 256
tape = [0] * tapeLength

while(instructions):
  currentOperation = instructions.pop(0) #remove first instruction
  match currentOperation:
    case '>':
      moveRight()
      break
    case '<':
      moveLeft()
      break
    case '+':
      incrementValue()
      break
    case '-':
      decrementValue()
      break
    case '.':
      printValue()
      break
   

print("end")


