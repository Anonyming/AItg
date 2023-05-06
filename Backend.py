from gpt4free import you

class Chat():
    def __init__ (self):
        self.history = []

    def getAnswer (self, question):
        prompt = question
        response = you.Completion.create(
            prompt=prompt,
            detailed=True,
            chat=self.history
        )

        self.history.append({"question": prompt, "answer": response.text})
        return response.text