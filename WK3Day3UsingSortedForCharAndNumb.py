import re
array = ["Said,25","Majid,19","Salim,32","Ali,21","Sultan,28"]
print(sorted(array, key=lambda array: int(re.search(r'\d+', array).group())))