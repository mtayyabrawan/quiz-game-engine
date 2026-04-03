# Quiz Game Engine

A comprehensive Python-based quiz game engine that supports multiple question types, timed responses, and automated result tracking.

## 📋 Features

- **Three Question Types**:
  - **Simple Q&A**: Open-ended text-based questions
  - **Multiple Choice Questions (MCQ)**: Single-select from 4 options
  - **True/False Questions**: Boolean-based questions

- **Time-Based Quiz**: 30-second timer for each question (configurable)
- **Student Tracking**: Captures student name and roll number
- **Automated Scoring**: 5 marks per correct answer
- **Result Persistence**: Saves results to CSV file with detailed statistics
- **Type-Safe Data Loading**: Uses JSON Schema validation for question data
- **Multi-threaded Implementation**: Uses threading for timeout management

## 🗂️ Project Structure

```
quiz-game-engine/
├── main.py                 # Main entry point and quiz orchestration
├── schema.json            # JSON Schema for validating questions.json
├── questions.json         # Quiz questions data (supports qa, mcq, tfq) (not git tracked)
├── result.csv            # Auto-generated results file (not git tracked)
├── src/
│   ├── load.py          # Question loader with TypedDict definitions
│   └── questions.py     # Question class hierarchy and implementations
└── README.md            # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- No external dependencies required (uses only standard library)

### Installation

1. Clone or download the repository:
   ```bash
   cd quiz-game-engine
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

### Running the Quiz

Execute the main script:
```bash
python main.py
```

You'll be prompted to:
1. Enter your name
2. Enter your roll number
3. Answer all quiz questions

## 📖 Usage Guide

### Starting a Quiz Session

```sh
python main.py
```

### Features During Quiz

- **30-Second Timer**: Each question has a 30-second timeout
- **Answer Input**: Enter your answer and press Enter to submit
- **Question Types Display**:
  - Simple questions require typing the answer
  - MCQ questions show 4 options (enter 1-4)
  - True/False questions accept "True" or "False"

### Example Quiz Flow

```
Dear student! Enter your name: Muhammad Tayyab
Enter your Roll No: 2024001
You have 30 seconds to answer for each question

Simple Questions

Question 1: What is your name?

Enter answer: Muhammad Tayyab
...
```

### Results

After completing the quiz, you'll see:
- Total marks scored
- Total questions
- Correct answers count
- Wrong answers count

Results are automatically saved to `result.csv` with the format:
```
Roll No,Name,Marks,Total Questions,Correct Answers,Wrong Answers
2024001,Muhammad Tayyab,15/15,3,3,0
```

## 🔧 Question Data Format

### JSON Structure (questions.json)

```json
{
  "$schema": "./schema.json",
  "qa": [
    {
      "question": "Simple question text?",
      "answer": "Expected answer"
    }
  ],
  "mcq": [
    {
      "question": "Question text?",
      "answer": "Correct option",
      "choices": ["Option 1", "Option 2", "Option 3", "Option 4"]
    }
  ],
  "tfq": [
    {
      "question": "Is this true?",
      "answer": "True"
    }
  ]
}
```

### Adding Your Own Questions

1. Edit `questions.json` and add your questions to the appropriate array (qa, mcq, or tfq)
2. Ensure answers match exactly (case-insensitive for simple Q&A)
3. MCQ answers must match one of the choices exactly
4. True/False answers must be "True" or "False"

## 🎯 Scoring System

- **Points per Question**: 5 marks
- **Correct Answer**: Marks awarded
- **Wrong Answer**: No marks awarded
- **Timeout**: Treated as wrong answer
- **Total Marks**: Number of questions × 5

### Scoring Formula
```
Final Score = (Correct Answers × 5) / (Total Questions × 5)
```

## 📊 Result CSV Format

The `result.csv` file contains:
- **Roll No**: Student's roll number
- **Name**: Student's name
- **Marks**: Format: `[earned]/[total]`
- **Total Questions**: Number of questions in quiz
- **Correct Answers**: Count of correct responses
- **Wrong Answers**: Count of incorrect/timeout responses

## 🔍 Core Components

### main.py
- `Student` class: Manages student information and result generation
- `generate_questions()`: Creates question objects from loaded data
- `init_student()`: Takes student input with validation
- `main()`: Orchestrates quiz flow

### questions.py
- `Question`: Base class with timer implementation
- `MCQQuestion`: Inherits from Question, handles MCQ logic
- `TrueFalseQuestion`: Inherits from Question, validates boolean input
- `__input_with_timer__()`: Threading-based timeout mechanism

### load.py
- Type definitions using `TypedDict`
- `load_questions()`: Safe JSON loading with error handling
- Schema validation definitions

## ⚙️ Configuration

### Timer Duration
To change the question timeout (default: 30 seconds), modify in `src/questions.py`:
```python
class Question:
    seconds = 30  # Change this value
```

### Scoring
To change marks per question, modify in `main.py`:
```python
marks += 5 if qa.ask() else 0  # Change 5 to your desired value
```

## 🐛 Error Handling

- **Invalid Student Input**: Application exits if name or roll number is empty
- **Missing questions.json**: Displays "No questions found" message
- **JSON Parse Error**: Catches exceptions and notifies user
- **Invalid MCQ Input**: Only accepts numbers 1-4
- **Question Timeout**: Automatically marked as wrong

## 📝 Input Validation

- Student name must be non-empty and alphabetic
- Roll number must be non-empty
- MCQ answers must be 1-4
- True/False answers are case-insensitive

## 🎓 Example Questions

### Q&A Question
```json
{
  "question": "What is the capital of France?",
  "answer": "Paris"
}
```

### MCQ Question
```json
{
  "question": "Which programming language is this project written in?",
  "answer": "Python",
  "choices": ["JavaScript", "Python", "Java", "C++"]
}
```

### True/False Question
```json
{
  "question": "Python is a dynamically typed language?",
  "answer": "True"
}
```

## 👨‍💻 Author

Created by [Muhammad Tayyab](mailto:tayyabraza1918@gmail.com)

## ❓ Troubleshooting

| Issue | Solution |
|-------|----------|
| "No questions found" | Ensure `questions.json` exists and is properly formatted |
| Script won't start | Verify Python 3.7+ is installed |
| Timeout not working | Check if threading is enabled on your system |
