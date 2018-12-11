from utils import read_from_fifo


def process():
    with open("result.log", 'a') as output:
        data = read_from_fifo()
        if len(data) > 0:
            output.writelines(data)


if __name__ == "__main__":
    process()



