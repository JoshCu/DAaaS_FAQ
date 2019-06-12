
class QA():
    def __init__(self, question, q_link, answer, image):
        self.question = question
        self.q_link = q_link
        self.answer = answer
        self.image = image

    def __str__(self):
        output = f'<h2><a name="{self.q_link}" href="#{self.q_link}">{self.question}</a></h2>'
        output += '\n'
        output += f'<p>{self.answer}</p>'
        output += '\n'
        if (self.image != ""):
            output += f'<img src="Images/{self.image}" alt="{self.image}">'
            output += '\n'
        return output

class QAG():
    def __init__(self):
        self.questions = []

    def get_qa(self):
        question = input("What's the question?: ")
        q_link = input("What's the link/tag for this question?: ")
        answer = input("What's the answer to the question?: ")
        image = input("image file name or leave blank for no image: ")
        qa = QA(question,q_link,answer,image)
        self.questions.append(qa)
        return qa

if __name__ == "__main__":
    gen = QAG()
    while True:
        with open('Qs.html', "a") as file:
            file.write(str(gen.get_qa()))
        
