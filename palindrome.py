s = "lolita"

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str


print ("The original string  is : ",s)

print ("The reversed string(using loops) is : ",reverse(s)) 

if(s==reverse(s)):
    print("gvn string is a palindrome")
print("gvn string is not a palindrome")  
