def main():
    mark = getValue("Enter marks: ")
    grade = getGrade(mark)
    print(f"Your grade is {grade}")

def getValue(prompt):
    while True:
        value = float(input(prompt))
        if value >= 0:
            return value
        print("Invalid value!")
def getGrade(marks):
    if marks<50:
        return 'F'
    else:
        return 'A'
main()