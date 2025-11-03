# condition statement

scores = int(input("Enter your score: "))

if scores >= 80 and scores <= 100:
    print("You got an A")
elif scores >= 70 and scores < 80:
    print("You got a B")
elif scores >= 60 and scores < 70:
    print("You got a C")
elif scores >= 50 and scores < 60:
    print("You got a D")
else:
    print("You got an F")

# matching condition
match scores:
    case scores if scores >= 80 and scores <= 100:
        print("You got an A")
    case scores if scores >= 70 and scores < 80:
        print("You got a B")
    case scores if scores >= 60 and scores < 70:
        print("You got a C")
    case scores if scores >= 50 and scores < 60:
        print("You got a D")
    case _:
        print("You got an F or Fail the exam")

# Expression statement
status = 404
match status:
    case 200:
        print("OK")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown Status")
