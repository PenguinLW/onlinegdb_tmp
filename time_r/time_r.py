def time_use():
    from time import time, ctime;
    #time() - time in seconds since the epoch; ctime() - local time.
    ta = ctime(time())

    #
    input("ДА! Вот просто стою - и просто жду. Это ТЫ ничего не понимаешь!");

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
def datetime_count():
    from datetime import datetime
    past_time = list();
    past_time.append(datetime.now().hour);
    past_time.append(datetime.now().minute);
    past_time.append(datetime.now().second);

    input("ДА! Вот просто стою - и просто жду. Это ТЫ ничего не понимаешь!");

    if datetime.now().hour >= past_time[0]:
        past_time[0] = datetime.now().hour - past_time[0];
    else:
        past_time[0] = past_time[0] + 12;

    if datetime.now().minute >= past_time[1]:
        past_time[1] = datetime.now().minute - past_time[1];

    if datetime.now().second >= past_time[2]:
        past_time[2] = datetime.now().second - past_time[2];

    return past_time;

print(datetime_count());

time_use()

datetime_use()