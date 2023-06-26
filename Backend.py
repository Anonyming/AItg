from gpt4free import usesless

import Frontend


class Dialog():
    def __init__(self):
        self.message_id = ''
        self.request = None

    async def getAnswer(self, prompt, iteration):
        try:
            try:
                self.request = usesless.Completion.create(prompt=prompt, parentMessageId=self.message_id)
            except:
                err = "server request error"
                print(err)
                raise err
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
                iteration = iteration + 1
                return self.getAnswer(iteration=iteration-1, prompt=prompt)
            else:
                print("Finally crash in Backend")
                raise Exception
