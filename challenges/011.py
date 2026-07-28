width = float(input("Wall width(m): "))
height = float(input("Wall height(m): "))
area = width * height
paint_capacity = 2
total_paint = area // paint_capacity

print(f"Wall area(m²): {area}")
print(f"Paint needed: {total_paint + 1} buckets")
