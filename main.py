import Frontend
import decorators

@decorators.debug(name='main')
async def main():
    await print("main func started OK")
    Frontend.Frontend()
    print("Frontend func stopped")


if __name__ == "__main__":
    print("starting main ...")
    main(iteration=1)
