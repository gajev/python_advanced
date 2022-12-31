from collections import deque
words = deque(input().split())
primary_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}
collected_colors = []

while words:
    left = words.popleft()
    right = words.pop() if words else ""
    result = left + right
    if result in primary_colors or result in secondary_colors:
        collected_colors.append(result)
        continue
    result = right + left
    if result in primary_colors or result in secondary_colors:
        collected_colors.append(result)
        continue
    left = left[:-1]
    right = right[:-1]
    if left:
        words.insert(len(words) // 2, left)
    if right:
        words.insert(len(words) // 2, right)
final_colors = []
for current_color in collected_colors:
    if current_color in primary_colors:
        final_colors.append(current_color)
    else:
        if current_color == "orange":
            if "red" in collected_colors and "yellow" in collected_colors:
                final_colors.append(current_color)
        if current_color == "purple":
            if "red" in collected_colors and "blue" in collected_colors:
                final_colors.append(current_color)
        if current_color == "green":
            if "blue" in collected_colors and "yellow" in collected_colors:
                final_colors.append(current_color)
print(final_colors)

