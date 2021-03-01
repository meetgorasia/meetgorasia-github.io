import random

def extract_colors(balls):
    colors = []
    for color in balls:
        colors.append(color)
    return colors

def extract_ball_counts(balls):
    ball_counts = []
    for color in balls:
        ball_counts.append(balls[color][0])
    return ball_counts

def extract_descriptions(balls):
    descriptions = []
    for color in balls:
        descriptions.append(balls[color][1])
    return descriptions

def total_balls(balls):
    total = 0
    for color in balls:
        num = balls[color][0]
        total = total + num
    return total

def generate_range(balls):
    ranges = {}
    b = 0
    for color in balls:
        a = b + 1
        b = balls[color][0] + a - 1
        r = (a,b)
        ranges[color] = r
    return ranges

def generate_random_number(total):
    r = random.randint(1,total)
    return r

def calculate_reward(balls, ranges, r_num):
    for color in ranges:
        for i in range(ranges[color][0],ranges[color][1]+1):
            if i == r_num:
                result = color
                reward = balls[color][1]
    return result, reward