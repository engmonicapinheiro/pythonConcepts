'''In this assignment you will read through
and parse a file with text and numbers.
You will extract all the numbers in the file
and compute the sum of the numbers.'''

import re

#actual file to use
handler = open('regex_sum_1501726.txt')
#handler = open('regex_sum_42.txt')

reading = handler.read()
sum = 0

code = re.findall('[0-9]+', reading)

for line in code:
    sum +=int(line)

print(sum)


# for line in handler:
#     line = line.rstrip()
#   #  print(line)
#     code = re.findall('[0-9]+', line)
#    # print(code)
#     if len(code) != 1 : continue
#     numbers = int(code[0])
#     print(numbers)
#     summing = summing + numbers
#     print(summing)
# #     numlist.append(numbers)
# #
# # sum = SumListItems(numlist, len(numlist))
# # print(sum)