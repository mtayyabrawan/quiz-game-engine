from genericpath import exists
from src.load import LoadedQuestions, load_questions
from src.questions import MCQQuestion, Question, TrueFalseQuestion


class Student:
    def __init__(self, name: str, roll_no: str) -> None:
        self.name = name
        self.roll_no = roll_no

    def gen_result(
        self,
        total_marks: int,
        marks: int,
        total_questions: int,
        correct_count: int,
        wrong_count: int,
    ):
        if exists("result.csv"):
            with open("result.csv", "a") as result_file:
                result_file.write(
                    f"{self.roll_no},{self.name},{marks}/{total_marks},{total_questions},{correct_count},   {wrong_count}\n"
                )
        else:
            with open("result.csv", "w") as result_file:
                result_file.write(
                    "Roll No,Name,Marks,Total Questions,Correct Answers,Wrong Answers\n"
                )
                result_file.write(
                    f"{self.roll_no},{self.name},{marks}/{total_marks},{total_questions},{correct_count},   {wrong_count}\n"
                )


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
        student = init_student()
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
        total_marks = int(total_questions * 5)
        correct_count = int(marks / 5)
        wrong_count = total_questions - correct_count
        print(f"\nYou scored {marks} out of {total_marks} marks")
        print(
            f"Total Questions: {total_questions}\nCorrect Answers: {correct_count}\nWrong Answers: {wrong_count}"
        )
        student.gen_result(
            total_marks, marks, total_questions, correct_count, wrong_count
        )


def init_student():
    name = input("Dear student! Enter your name: ")
    roll_no = input("Enter your Roll No: ")

    if (len(name) == 0 and not name.isalpha()) or (len(roll_no) == 0):
        raise Exception("Please Enter valid Name or Roll No")
    return Student(name, roll_no)


if __name__ == "__main__":
    main()
