from threading import Thread
from typing import List, Union


class Question:
    seconds = 30

    def __init__(self, quest_no: int, question: str, answer: str):
        self.quest_no: int = quest_no
        self.question: str = question
        self.answer: str = answer

    def __input_with_timer__(self, question: str) -> Union[str, None]:
        print(f"\nQuestion {self.quest_no}: {self.question}\n")
        user_input = []

        def get_input():
            user_input.append(input(question))

        thread = Thread(target=get_input)
        thread.daemon = True
        thread.start()
        thread.join(timeout=self.seconds)
        if thread.is_alive():
            print("Time out!")
            return None
        else:
            return user_input[0]

    def ask(self) -> bool:
        user_answer = self.__input_with_timer__("Enter answer: ")
        if user_answer == None:
            return False
        if user_answer.lower().strip() == self.answer.lower().strip():
            return True
        else:
            return False


class MCQQuestion(Question):
    def __init__(self, quest_no, question: str, answer: str, choices: List[str]):
        super().__init__(quest_no, question, answer)
        self.choices = choices

    def ask(self):
        user_answer = self.__input_with_timer__(
            f"[1] {self.choices[0]}\n[2] {self.choices[1]}\n[3] {self.choices[2]}\n[4] {self.choices[3]}\n\nEnter answer: "
        )
        try:
            if user_answer == None:
                return False
            parsed_answer = self.choices[int(user_answer.strip()) - 1]
            if parsed_answer == self.answer:
                return True
            else:
                return False
        except ValueError:
            print("Invlaid input you can only enter numbers from 1 to 4")
            return False
        except IndexError:
            print("Invlaid input you can only enter numbers from 1 to 4")
            return False


class TrueFalseQuestion(Question):
    def __init__(self, quest_no, question: str, answer: str):
        super().__init__(quest_no, question, answer)

    def ask(self):
        user_answer = self.__input_with_timer__(f"[True / False]\n\nEnter answer: ")
        if user_answer == None:
            return False
        parsed_answer = user_answer.strip().capitalize()
        if parsed_answer == str(self.answer):
            return True
        else:
            print("Invlaid input you can only enter [True / False]")
            return False
