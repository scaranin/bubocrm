from datetime import datetime, date, time

def log(text):
    """
    Добавление лога
    """
    f = open('D:/LOG.LOG', 'a')
    text = datetime.now().strftime("%d.%m.%Y %H:%M:%S") + ' ' + text + '\n'
    f.write(text)
    f.close()
