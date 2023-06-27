from gpt4free import usesless
import decorators

class Dialog():
    def __init__(self):
        self.message_id = ''
        self.request = None

    @decorators.debug(name='getAnswer')
    async def getAnswer(self, prompt, iteration):
        try:
            self.request = usesless.Completion.create(prompt=prompt, parentMessageId=self.message_id)
        except:
            err = "server request error"
            print(err)
            raise err
        self.message_id = self.request["id"]
        answer = self.request['text']
        return answer
