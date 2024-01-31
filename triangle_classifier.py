def classify_triangle(a,b,c):
  if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    return "Invalid triangle (side lengths must be positive and satisfy triangle inequality)"

  # Check for equilateral triangle
  if a == b == c:
    return "Equilateral triangle"

  # Check for isosceles triangle
  if a == b or a == c or b == c:
    # Check if it's also a right triangle
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
      return "Isosceles right triangle"
    else:
      return "Isosceles triangle"

  if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    return "Right triangle"
  return "Scalene triangle"

# Example usage
triangle_type = classify_triangle(3, 4, 5)
print(triangle_type)