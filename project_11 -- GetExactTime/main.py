import datetime

def main():
    now = datetime.datetime.now()
    print(now.strftime("%I:%M:%S %p"))


if __name__ == "__main__":
    main()