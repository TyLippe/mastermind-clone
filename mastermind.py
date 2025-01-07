import random


def generate_pattern():
    return [random.randint(1, 6) for _ in range(4)]


def get_feedback(pattern, guess):
    correct_position = sum([1 for i in range(4) if pattern[i] == guess[i]])
    return correct_position


def main():
    pattern = generate_pattern()
    attempts = 10

    print("Welcome to Mastermind!")
    print("Guess the 4-digit pattern. Each digit is between 1 and 6.")
    print("You have 10 attempts to guess the pattern correctly.")

    for attempt in range(1, attempts + 1):
        guess = input(f"Attempt {attempt}: ")
        guess = [int(digit) for digit in guess]

        if len(guess) != 4 or any(digit < 1 or digit > 6 for digit in guess):
            print("Invalid input. Please enter 4 digits between 1 and 6.")
            continue

        correct_position = get_feedback(pattern, guess)
        feedback = []
        for i in range(4):
            if guess[i] == pattern[i]:
                feedback.append(
                    f"\033[92m{guess[i]}\033[0m"
                )  # Green for correct position
            elif guess[i] in pattern:
                feedback.append(
                    f"\033[93m{guess[i]}\033[0m"
                )  # Yellow for correct number, wrong position
            else:
                feedback.append(f"\033[91m{guess[i]}\033[0m")  # Red for wrong number

        print("Feedback: " + " ".join(feedback))

        if correct_position == 4:
            print("Congratulations! You've guessed the pattern correctly.")
            break
    else:
        print(f"Sorry, you've used all your attempts. The pattern was: {pattern}")


if __name__ == "__main__":
    main()
