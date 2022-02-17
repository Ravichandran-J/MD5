import hashlib
inp=input("enter the string that you want to encrypt in md5:")
result=hashlib.md5(inp.encode())
#result=hashlib.md5(b'{}'.format(inp))
print("The byte equivalent of hash is :",end=" ")
print(result.hexdigest())

x=result.hexdigest()

y=x+inp
print("y",y)

result1=hashlib.md5(y.encode())
print("md5_plain_md5:",result1.hexdigest())


result2=hashlib.sha256(inp.encode())
print("value:",end=" ")
print(result2.hexdigest())


z=result.hexdigest()

z1=z+inp
result3=hashlib.sha256(z1.encode())
print("value:",end=" ")
print("double sha56")
print(result3.hexdigest())
