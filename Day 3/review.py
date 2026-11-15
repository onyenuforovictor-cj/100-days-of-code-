import random
print("welcome the adventure shop")
name = input("Enter your name: ").lower()
starting_coin = 0
inventory = []
challenge_questions = {
    "q1": {
        "prompt": "Which planet in our solar system has the most moons?",
        "choices": ["Jupiter", "Saturn", "Uranus", "Neptune"],
        "answer": "Saturn"
    },
    "q2": {
        "prompt": "What is the chemical symbol for gold?",
        "choices": ["Gd", "Go", "Ag", "Au"],
        "answer": "Au"
    },
    "q3": {
        "prompt": "Which data structure uses the Last-In, First-Out (LIFO) principle?",
        "choices": ["Queue", "Stack", "Linked List", "Hash Table"],
        "answer": "Stack"
    },
    "q4": {
        "prompt": "In what year did the first human land on the Moon?",
        "choices": ["1965", "1969", "1971", "1975"],
        "answer": "1969"
    },
    "q5": {
        "prompt": "Which element has the atomic number 1?",
        "choices": ["Helium", "Oxygen", "Hydrogen", "Carbon"],
        "answer": "Hydrogen"
    },
}
print(type(challenge_questions.items))
print(challenge_questions.keys())
print(challenge_questions.values())
#user_choice = input (f"welcome {name }, press 'y' to continue or 'n' to exit")

