from src.load import LoadedQuestions, load_questions
from src.questions import MCQQuestion, Question, TrueFalseQuestion


def generate_questions(questions: LoadedQuestions):
    all_qa = [
        Question(idx + 1, qa["question"], qa["answer"])
        for (idx, qa) in enumerate(questions["qa"])
    ]
    all_mcq = [
        MCQQuestion(idx + 1, mcq["question"], mcq["answer"], mcq["choices"])
        for (idx, mcq) in enumerate(questions["mcq"])
    ]
    all_tfq = [
        TrueFalseQuestion(idx + 1, tfq["question"], tfq["answer"])
        for (idx, tfq) in enumerate(questions["tfq"])
    ]
    return {"all_qa": all_qa, "all_mcq": all_mcq, "all_tfq": all_tfq}


def main():
    all_questions = load_questions()
    if all_questions == None:
        print("Sorry! No questions found.")
    else:
        generated_questions = generate_questions(all_questions)
        print(f"You have {Question.seconds} seconds to answer for each question")
        marks = 0
        if len(generated_questions["all_qa"]) > 0:
            print("\nSimple Questions\n")
            for qa in generated_questions["all_qa"]:
                marks += 5 if qa.ask() else 0
        if len(generated_questions["all_mcq"]) > 0:
            print("\nMultiple Choice Questions\n")
            for mcq in generated_questions["all_mcq"]:
                marks += 5 if mcq.ask() else 0
        if len(generated_questions["all_tfq"]) > 0:
            print("\nTrue False Questions\n")
            for tfq in generated_questions["all_tfq"]:
                marks += 5 if tfq.ask() else 0
        total_questions = (
            len(generated_questions["all_qa"])
            + len(generated_questions["all_mcq"])
            + len(generated_questions["all_tfq"])
        )
        correct_count = int(marks / 5)
        print(f"\nYou scored {marks} out of {int(total_questions*5)} marks")
        print(
            f"Total Questions: {total_questions}\nCorrect Answers: {correct_count}\nWrong Answers: {total_questions-correct_count}"
        )


if __name__ == "__main__":
    main()
