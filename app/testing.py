import random

balls = {"red": (1, "Watch a movie"), "green": (90, "Productive life"), "blue": (9, "Watch YouTube")}
print(f"The dictionary of balls: {balls}")
print("")

def extract_colors(balls):
    colors = []
    for color in balls:
        colors.append(color)
    return colors

colors = extract_colors(balls)
print(f"The list of colors: {colors}")
print("")

def total_balls(balls):
    total = 0
    for color in balls:
        num = balls[color][0]
        total = total + num
    return total

total = total_balls(balls)
print(f"Total number of balls: {total}")
print("")

def generate_range(balls):
    ranges = {}
    b = 0
    for color in balls:
        a = b + 1
        b = balls[color][0] + a - 1
        r = (a,b)
        ranges[color] = r
    return ranges

ranges = generate_range(balls)
print(f"The dictionary showing ranges of different balls: {ranges}")
print("")

def generate_random_number(total):
    r = random.randint(1,total)
    return r

r_num = generate_random_number(total)
print(f"The generated random number: {r_num}")
print("")

def calculate_reward(balls, ranges, r_num):
    for color in ranges:
        for i in range(ranges[color][0],ranges[color][1]+1):
            if i == r_num:
                result = color
                reward = balls[color][1]
    print(f"The result color is: {result}")
    print(f"The reward is: {reward}")
    print("")    

calculate_reward(balls, ranges, r_num)


