from gpt4free import usesless

class Dialog():
    def __init__(self):
        self.message_id = ''
        self.request = None

    async def getAnswer(self, prompt, iteration):
        try:
            self.request = usesless.Completion.create(prompt=prompt, parentMessageId=self.message_id)
            self.message_id = self.request["id"]
            answer = self.request['text']
            return answer
        except:
            print(f'Backend crashed, error: "{Exception}"')
            if iteration <= 3:
                print("cleaning Dialog object")
                await self.__init__()
                print("restarting getAnswer func")
                print(f'{iteration}/3')
                returned = self.getAnswer(iteration)
                iteration = iteration + 1
                return returned
            else:
                print("Finally crash in Backend")
                raise Exception
