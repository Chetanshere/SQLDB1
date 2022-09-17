def convert_string(value):
    new_value = str(value)
    return new_value
s = [1,34,33,67,7,21]
convert_string(s)
print(type(s))
l=[]
try:
    for i in s:
        l.append(i)

except Exception as e:
    print(e)

print(l)
print(type(l))




