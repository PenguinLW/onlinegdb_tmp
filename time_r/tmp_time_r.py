def time_use():
    from time import time, ctime;
    #time() - time in seconds since the epoch; ctime() - local time.
    ta = ctime(time())

    #
    input("Измерение начнётся после нажатия клавиши 'ввод'!");

    #
    tb = ctime(time());

    print(
        "Момент начала измерения:\t{:s}\nИзмерение завершено:\t{:s}".format(ta, tb, )
    );


def datetime_use():
    from datetime import datetime
    print(
        "{:s}\n{:s}\n{:s}\n{:s}\n{:s}".format(
            str(datetime.now()),
            str(datetime.now().hour),
            str(datetime.now().minute),
            str(datetime.now().second),
            str(datetime.now().microsecond)
    ));