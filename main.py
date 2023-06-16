import Frontend

async def main(iteration):
    try:
        await print("main func started OK")
        Frontend.Frontend()
        print("Frontend func stopped")
    except:
        print(f'main content crashed, error: "{Exception}"')
        if iteration <= 3:
            print("restarting main func")
            print(f'{iteration}/3')
            await main(iteration)
            iteration = iteration + 1
            return None
        else:
            print("Finally crash")
            raise Exception



if __name__ == "__main__":
    print("starting main ...")
    iteration = 1
    main(iteration)
