a={"Hello" :" namaskar",
"Bath":"Nahana",
"going":"aschi"}
b=input("Enter the word in english ")
if(b in a.keys()):
    print(a.get(b))