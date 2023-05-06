from gpt4free import you

class Chat():
    history = []
    # def __init__ (self):
    #     self.history = []

    def getAnswer (self, question):
        prompt = question
        response = you.Completion.create(
            prompt=prompt,
            chat=self.history,
            detailed=True
        )

        self.history.append({"question": prompt, "answer": response.text})
        return response.text
