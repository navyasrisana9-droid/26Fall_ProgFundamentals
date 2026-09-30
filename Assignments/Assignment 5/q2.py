# Question 2: Rectangle Calculator Function

def rectangle_stats(length, width):
    area = length * width
    perimeter = 2 * (length + width)

    return area, perimeter

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

area, perimeter = rectangle_stats(length, width)

print(f"Area: {area:.2f}")
print(f"Perimeter: {perimeter:.2f}")
