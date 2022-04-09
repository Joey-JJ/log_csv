from datetime import datetime
import csv
import time # Only necessary for example


class log_message(object):
    def __init__(self, message: str) -> None:
        self.message = message
        self.date = datetime.today().date()
        self.time = str(datetime.now().time())[:-7]


def log(msg: str='Program executed', file_name: str='log.csv') -> None:
    msg = log_message(msg)
    with open(file_name, 'a') as file:
        if file.tell() == 0:
            file.write('Date,Time,Message\n')
        csv_file = csv.writer(file)
        csv_file.writerow([msg.date, msg.time, msg.message])


def Main() -> None:
    # Example:
    for _ in range(10):
        log(msg='test message', file_name='test.csv')
        time.sleep(1)


if __name__ == '__main__':
    Main()
