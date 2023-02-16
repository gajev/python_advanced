from collections import deque

eggs_size = deque(int(x) for x in input().split(", "))
paper_size = [int(x) for x in input().split(", ")]
box_size = 50
box_filled = 0
while eggs_size and paper_size:
    current_egg = eggs_size.popleft()
    current_paper = paper_size.pop()
    if current_egg <= 0:
        paper_size.append(current_paper)
        continue
    if current_egg == 13:
        paper_size.append(paper_size[0])
        paper_size[0] = current_paper
        continue
    if current_egg + current_paper <= box_size:
        box_filled += 1
if box_filled > 0:
    print(f"Great! You filled {box_filled} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs_size:
    print(f"Eggs left: {', '.join(str(x) for x in eggs_size)}")
if paper_size:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper_size)}")
