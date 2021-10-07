from sys import argv 

string = "OHz1jsc64Q0na2LLFOs1nKEeQN2Q76neuIfEGDSSBHlEYfby91ITvVRdZrTetraodarIUoVO8wbM6cjmebrubidaMtu5pZjC6rXZsIKQ1JOMSNXTIwEEzlQd5x8nzMzRrky4wk9WVdfZGsoqGfZXMGgYGaTzBgENm."
first = 58
second = 63
third = 82
fourth = 87 

firstSlice = string[first:second+1]
secondSlice = string[third:fourth+1]

print firstSlice 
print secondSlice