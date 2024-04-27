def calculate_score(answers: list, correct_answers: list) -> float:
    correct = sum(1 for answer, correct in zip(answers, correct_answers) if answer == correct)
    return (correct / len(correct_answers)) * 100
