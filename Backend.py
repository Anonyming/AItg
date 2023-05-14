from gpt4free import usesless

class Dialog():
    message_id = ''

    def getAnswer(self, prompt):
        request = usesless.Completion.create(prompt=prompt, parentMessageId=self.message_id)
        self.message_id = request["id"]
        answer = request['text']
        return answer
