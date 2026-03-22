# Decision-making using dictionary mapping

marks = int(input("Enter your marks: "))

grade = {
    range(90, 101): "A",
    range(75, 90): "B",
    range(50, 75): "C",
    range(0, 50): "Fail"
}

result = next(value for key, value in grade.items() if marks in key)

print("Grade:", result)