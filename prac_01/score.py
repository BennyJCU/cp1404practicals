"""
CP1404/CP5632 - Practical
Program to determine score status
"""
def main():
    score = float(input("Enter score: "))

    result = determines_score(score)
    print(f"User score {score} is {result}")


def determines_score(score: float):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result

main()