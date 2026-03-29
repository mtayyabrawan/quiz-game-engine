from json import load
from typing import List, TypedDict

QA = TypedDict("QA", {"question": str, "answer": str})
MCQ = TypedDict("MCQ", {"question": str, "answer": str, "choices": List[str]})
TFQ = TypedDict("TFQ", {"question": str, "answer": str})
LoadedQuestions = TypedDict(
    "LoadedQuestions", {"qa": List[QA], "mcq": List[MCQ], "tfq": List[TFQ]}
)


def load_questions():
    try:
        with open("./questions.json") as loaded_file:
            loaded_questions: LoadedQuestions = load(loaded_file)
        return loaded_questions
    except Exception as e:
        print(e)
        return None
