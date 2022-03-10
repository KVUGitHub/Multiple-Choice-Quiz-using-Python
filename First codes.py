class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "Where is Nigeria?\n (a) Africa\n (b) Asia\n (c) North America\n\n",
    "When was Nigeria independence?\n (a) 2005\n (b) 1950\n (c) 1960\n\n",
    "What color is in Nigerian flag?\n (a) Pink\n (b) Green\n (c) Blue\n\n",
    "How many states are in Nigeria?\n (a) 50\n (b) 41\n (c) 36\n\n",
    "What is the capital of Nigeria?\n (a) Abuja\n (b) Niger\n (c) Area\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)
