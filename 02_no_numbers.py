name=input("Product Name:")

error="This cannot have numbers"
has_errors=""

for letter in name:
    if letter.isdigit()==True:
        print(error)
        has_errors="yes"
        break
if has_errors!="yes":
    print("Continue")
