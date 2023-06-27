from Frontend import ERROR

def debug(func, name):
    async def new_func(iteration):
        try:
            func()
        except:
            print(f'{name} func crashed, error: "{Exception}"')
            if iteration <= 3:
                print("restarting main func")
                print(f'{iteration}/3')
                iteration = iteration + 1
                result = new_func(iteration=iteration-1)
                return result
            else:
                print(f'Finally crash: {Exception}')
                print("trying to set error mode")
                await ERROR(Exception=Exception)
                raise Exception