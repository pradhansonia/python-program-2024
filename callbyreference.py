string = "Greeks"
def test(string):
    string = "GreeksforGreeks"
    print ("inside Functoin:", string)

test (id(string))
print("Outside Function:",string)