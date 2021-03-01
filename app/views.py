from django.shortcuts import render
from . import logic 

# Create your views here.

def index(request):

    balls = {"Red": (1, "Take a day off!"), "Orange": (2, "Watch a movie/play games (3 hours)"),"Blue": (7, "Watch YouTube (1 hour)"), "Green": (90, "Keep being productive")}
    colors = logic.extract_colors(balls)
    ball_counts = logic.extract_ball_counts(balls)
    descriptions = logic.extract_descriptions(balls)
    total = logic.total_balls(balls)
    ranges = logic.generate_range(balls)
    r_num = logic.generate_random_number(total)
    result, reward = logic.calculate_reward(balls, ranges, r_num)

    return render(request, "app/index.html", {
        "result": result,
        "reward": reward,
        "num": r_num,
        "balls": balls,
        "colors": colors,
        "cols": len(colors),
        "ball_counts": ball_counts,
        "descriptions": descriptions
    })