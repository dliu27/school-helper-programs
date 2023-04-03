
def main():
    """
    main loops through an econ.txt file generated from econ_looper.py and starts a flashcard quiz.
    """
    
    with open("econ.txt", "r") as f:
        lines = f.readlines()
        flashcards = {}
        question = ""
        answer = ""
        isquestion = False
        isanswer = False
        start = False
        startChapter = 2
        endChapter = 3
        for line in lines:
            if line.startswith(f"Chapter {startChapter}"):
                start = True
            if (not start):
                continue
            if line.startswith(f"Chapter {endChapter}"):
                break
            
            if (line.startswith("Diff:")):
                isanswer = False
                flashcards[question] = answer
                isquestion = False
                question = ""
                answer = ""
                continue
            # if (isquestion):
            #     question += "\n"
            # if (isanswer):
            #     answer += "\n"
            if (line.startswith("Answer:") or isanswer):
                isquestion = False
                isanswer = True
                answer += line
            if ((line[0].isdigit() and line[1] == ")") or (line[0].isdigit() and line[1].isdigit() and line[2] == ")") or isquestion):
                isquestion = True
                question += line
            
    # print(flashcards.items())
    for question, answer in flashcards.items():
        print(f"Question: {question}")
        ans = input("Your answer: ")
        if (ans == answer[-1]):
            continue
        else:
            print(f"Actual {answer}")


if __name__ == "__main__":
    main()
