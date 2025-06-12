class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            current_water = width * current_height
            max_water = max(max_water, current_water)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water


input_str = input("Gib die Höhen ein (z. B. 1 8 6 2 5 4 8 3 7):\n")
heights = list(map(int, input_str.strip().split()))

print("Maximale Fläche:", max_area(heights))


# Benjamin Wilk
# Lösung: Die Lösung verwendet zwei Zeiger, die sich von außen nach innen bewegen.
# Dabei wird immer die kleinere Linie verschoben, um eine möglichst große Fläche zu finden.