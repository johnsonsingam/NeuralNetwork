#Question 3
def getHeightUsingLoop(heights_inches):
    heights_centimeters = []
    for height in heights_inches:
        centimeters = height * 2.54
        heights_centimeters.append(round(centimeters, 2))
    return heights_centimeters

def main():
    # Input heights in inches from the user.
    heights_inches = list(map(float, input("Enter the list numbers separated by comma: ").strip().split(",")))
    print("Input List in Inches: ", heights_inches)

    # Interactive loop for converting height into centimeters.
    heights_cm_nested = getHeightUsingLoop(heights_inches)

    # List comprehension for converting height into centimeters.
    heights_cm_comprehension= [round(height * 2.54, 2) for height in heights_inches]

    # Printing the results.
    print("Heights using Nested Loop:", heights_cm_nested)
    print("Heights using List Comprehension:", heights_cm_comprehension)

if __name__ == "__main__":
    main()
