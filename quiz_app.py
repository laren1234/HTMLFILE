import tkinter as tk
from tkinter import messagebox
questions = [
    {
        "question": "What is the unit of force?",
        "options": ["Newton", "Joule", "Watt", "Pascal"],
        "answer": "Newton"
    },
    {
        "question": "What planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "Which gas is most abundant in Earth's atmosphere?",
        "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer": "Nitrogen"
    },
    {
        "question": "What is the speed of light in vacuum?",
        "options": ["3x10^8 m/s", "3x10^6 m/s", "1.5x10^8 m/s", "1x10^6 m/s"],
        "answer": "3x10^8 m/s"
    },
    {
        "question": "Who proposed the laws of motion?",
        "options": ["Einstein", "Galileo", "Newton", "Tesla"],
        "answer": "Newton"
    },
    {
        "question": "Which part of the atom has a negative charge?",
        "options": ["Proton", "Neutron", "Electron", "Nucleus"],
        "answer": "Electron"
    },
    {
        "question": "What is the boiling point of water at sea level?",
        "options": ["90°C", "100°C", "80°C", "110°C"],
        "answer": "100°C"
    },
    {
        "question": "Which energy transformation happens in photosynthesis?",
        "options": ["Kinetic to Potential", "Light to Chemical", "Sound to Electrical", "Heat to Mechanical"],
        "answer": "Light to Chemical"
    },
    {
        "question": "What device is used to measure atmospheric pressure?",
        "options": ["Thermometer", "Barometer", "Hygrometer", "Altimeter"],
        "answer": "Barometer"
    },
    {
        "question": "Which of these is not a renewable energy source?",
        "options": ["Wind", "Solar", "Coal", "Hydro"],
        "answer": "Coal"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Science & Physics Quiz")
        self.root.geometry("600x400")
        self.root.config(bg="#f0f4f7")

        self.q_index = 0
        self.score = 0

        self.header = tk.Label(root, text="🧪 Science & Physics Quiz", font=("Helvetica", 20, "bold"),
                               bg="#4a90e2", fg="white", pady=10)
        self.header.pack(fill=tk.X)

        self.question_frame = tk.Frame(root, bg="#f0f4f7")
        self.question_frame.pack(pady=30)

        self.question_label = tk.Label(self.question_frame, text="", font=("Helvetica", 14), bg="#f0f4f7", wraplength=500)
        self.question_label.pack(pady=10)

        self.var = tk.StringVar()
        self.options = []
        for i in range(4):
            rb = tk.Radiobutton(self.question_frame, text="", variable=self.var, value="", font=("Helvetica", 12),
                                bg="#f0f4f7", anchor="w", padx=10, pady=5, activebackground="#d1e0ff")
            rb.pack(fill="x", padx=50, pady=2)
            self.options.append(rb)

        self.submit_button = tk.Button(root, text="Next Question", command=self.check_answer,
                                       font=("Helvetica", 12), bg="#4a90e2", fg="white", padx=10, pady=5)
        self.submit_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        current_q = questions[self.q_index]
        self.question_label.config(text=f"Q{self.q_index + 1}: {current_q['question']}")
        self.var.set(None)  
        for i, opt in enumerate(current_q["options"]):
            self.options[i].config(text=opt, value=opt)

    def check_answer(self):
        selected = self.var.get()
        if not selected:
            messagebox.showwarning("No Selection", "Please select an answer!")
            return
        if selected == questions[self.q_index]["answer"]:
            self.score += 1

        self.q_index += 1
        if self.q_index < len(questions):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"✅ Your Score: {self.score} / {len(questions)}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
