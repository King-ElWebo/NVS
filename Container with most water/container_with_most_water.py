def max_area(height):
    left = 0
    right = len(height) - 1
    max_love = 0

    while left < right:
        height_left = height[left]
        height_right = height[right]
        current_love = min(height_left, height_right) * (right - left)
        max_love = max(max_love, current_love)

        if height_left < height_right:
            left += 1
        else:
            right -= 1

    return max_love


input_str = input("Gib die Höhen ein (z. B. 1 8 6 2 5 4 8 3 7):\n")
heights = list(map(int, input_str.strip().split()))

print("Maximale Fläche:", max_area(heights))


# Benjamin Wilk
# Lösung: Die Lösung verwendet zwei Zeiger, die sich von außen nach innen bewegen.
# Dabei wird immer die kleinere Linie verschoben, um eine möglichst große Fläche zu finden.