import random

# List of programming jokes
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why do Python developers wear glasses? Because they don’t C#.",
    "How many programmers does it take to change a light bulb? None. It’s a hardware problem!",
    "Why did the programmer quit his job? Because he didn’t get arrays.",
    "Why do you think ladies like being around programmer? Becuase they know how to fork repo.",
    "Why do Java developers wear glasses? Because they can’t C#.",
    "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'",
    "Why did the developer go broke? Because he used up all his cache.",
    "There are 10 types of people in the world: those who understand binary and those who don’t.",
    "Knock knock.\nWho's there?\nProgram.\nProgram who?\nProgram crashes! Unexpected error occurred."
]

# Select a joke randomlly
def tellJoke():
    print("Here's a joke for you:\n")
    print(random.choice(jokes))

# invoke the joke function
tellJoke()
