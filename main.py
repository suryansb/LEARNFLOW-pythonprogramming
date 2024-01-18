from tkinter import *

technology_questions = {
    "What is the main purpose of an SSL certificate in web security?": ["Secure Socket Layer", "Secure Server Link",
                                                                     "Secure Sockets Language", "Secure System Login"],
    "Which programming language is commonly used for building mobile applications?": ["Java", "Swift", "Python", "C#"],
    "What does the acronym 'URL' stand for in the context of the internet?": ["Universal Resource Locator",
                                                                             "Uniform Resource Locator",
                                                                             "Universal Resource Link", "Uniform Resource Link"],
    "What is the purpose of a version control system like Git?": ["Document Editing", "Code Collaboration and Versioning",
                                                                "File Compression", "Data Encryption"]
}
technology_answers = ['Secure Socket Layer', 'Swift', 'Uniform Resource Locator', 'Code Collaboration and Versioning']

science_questions = {
    "What is the chemical symbol for water?": ["H2O", "CO2", "O2", "NaCl"],
    "Which planet is known as the 'Blue Planet'?": ["Mars", "Earth", "Jupiter", "Venus"],
    "What is the process by which plants make their own food?": ["Photosynthesis", "Respiration", "Transpiration",
                                                              "Fermentation"],
    "What is the speed of light?": ["299,792 kilometers per second", "150,000 kilometers per second",
                                   "450,000 kilometers per second", "200,000 kilometers per second"],
}
science_answers = ['H2O', 'Earth', 'Photosynthesis', '299,792 kilometers per second']

history_questions = {
    "Who was the first President of the United States?": ["Thomas Jefferson", "George Washington", "John Adams",
                                                         "Abraham Lincoln"],
    "In which year did World War II end?": ["1945", "1939", "1941", "1943"],
    "Which ancient civilization built the pyramids of Giza?": ["Greek", "Roman", "Egyptian", "Mayan"],
    "Who wrote 'Romeo and Juliet'?": ["William Shakespeare", "Jane Austen", "Charles Dickens", "Leo Tolstoy"],
}
history_answers = ['George Washington', '1945', 'Egyptian', 'William Shakespeare']

general_knowledge_questions = {
    "What is the currency of Japan?": ["Yuan", "Won", "Yen", "Ringgit"],
    "Which ocean is the largest?": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
    "Who wrote 'To Kill a Mockingbird'?": ["Harper Lee", "J.K. Rowling", "Ernest Hemingway", "George Orwell"],
    "What is the capital of Australia?": ["Sydney", "Melbourne", "Canberra", "Brisbane"]
}
general_knowledge_answers = ['Yen', 'Pacific Ocean', 'Harper Lee', 'Canberra']

question = {}
ans = []
current_question = 0
domain_name = ["Technology", "Science", "History", "General_knowledge"]


def start_quiz():
    start_button.pack_forget()
    next_button.pack()
    next_question()


def next_question():
    global current_question
    if current_question < len(question):
        check_ans()
        user_ans.set('None')
        c_question = list(question.keys())[current_question]
        clear_frame()
        Label(root, text="Quiz App", font="calibre 40 bold",
              relief=SUNKEN, background="green", padx=12, pady=9).pack()
        
        Label(root, text=f"Question : {c_question}", padx=15, font="calibre 12 normal").pack(anchor=NW)
        for option in question[c_question]:
            Radiobutton(root, text=option, variable=user_ans, value=option, padx=28).pack(anchor=NW)
        current_question += 1
        next_button.pack(side=BOTTOM,pady=200) # Move the Next Question button to the bottom
    else:
        next_button.pack_forget()
        check_ans()
        clear_frame()
        Label(root, text="", font="calibre 10 bold").pack()
        Label(root, text="", font="calibre 10 bold").pack()
        Label(root, text="", font="calibre 10 bold").pack()
        Label(root, text="", font="calibre 10 bold").pack()
        output = f"Your Score is {user_score.get()} out of {len(question)}"
        Label(root, text=output, font="calibre 25 bold").pack()
        Label(root, text="Thanks for Participating",
              font="calibre 18 bold").pack()


def check_ans():
    temp_ans = user_ans.get()
    if temp_ans != 'None' and temp_ans == ans[(current_question - 1)]:
        user_score.set(user_score.get() + 1)


def clear_frame():
    for widget in root.winfo_children():
        if widget not in [start_button, next_button]:
            widget.destroy()


def select_domain():
    global question, ans
    domain_name = user_.get()
    if domain_name == "Technology":
        question = technology_questions
        ans = technology_answers
    elif domain_name == "Science":
        question = science_questions
        ans = science_answers
    elif domain_name == "History":
        question = history_questions
        ans = history_answers
    else:
        question = general_knowledge_questions
        ans = general_knowledge_answers

    domain_frame.pack_forget()  # Hide domain selection frame
    start_button.pack()  # Show the start quiz button


if __name__ == "__main__":
    root = Tk()
    root.title("SURYANS QUIZ")
    root.geometry("1000x650")
    root.minsize(800, 400)

    user_ans = StringVar()
    user_ans.set('None')
    user_score = IntVar()
    user_score.set(0)
    user_ = StringVar()
    user_.set("None")

    Label(root, text="Quiz App",
          font="calibre 40 bold",
          relief=SUNKEN, background="green", padx=12, pady=9).pack()
    Label(root, text="", font="calibre 10 bold").pack()
    Label(root, text="", font="calibre 10 bold").pack()
    Label(root, text="", font="calibre 10 bold").pack()
    Label(root, text="", font="calibre 10 bold").pack()

    domain_frame = Frame(root)
    domain_frame.pack(side=TOP, fill=X)
    Label(domain_frame, text="Choose the domain: ", font="calibre 14 bold", padx=50).pack(anchor=NW)
    for option in domain_name:
        Radiobutton(domain_frame, text=option, variable=user_, value=option, padx=78).pack(anchor=NW)
    Button(domain_frame, text="Select Domain", command=select_domain, font="calibre 17 bold").pack(anchor=NW)

    start_button = Button(root,
                          text="Start Quiz",
                          command=start_quiz,
                          font="calibre 17 bold")

    next_button = Button(root, text="Next Question", background="blue",
                         command=next_question,
                         font="calibre 17 bold")

    root.mainloop()
