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

print(instructions)

def removeNullSet(instructions):
  # remove new line characters / could rather just ignore any chars and call them strings
  out = list(filter(('\n').__ne__, instructions))
  out = list(filter((' ').__ne__, out))
  return out

def testRemove(instruction):
  out = [x for x in instruction if x  in instructionSet]
  # out = set(instructions) - set(instructionSet)
  return out

instructions = seperateInstructions(instructions)
instructions = testRemove(instructions)
print(instructions)

#define a tape 256 bits
tapeLength = 256
tape = [0] * tapeLength

while(instructions):
   print(instructions)
   instructions.pop(0) #remove first instruction

print("end")