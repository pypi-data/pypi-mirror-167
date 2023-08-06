from .base import Config

FILE = '~/bar.json'
CFG = Config(FILE)
CFG.bar = CFG.get_bar()


def main():
    CFG.bar.run()

if __name__ == '__main__':
    main()

