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
def datetime_count():
    from datetime import datetime
    past_time = list();
    past_time.append(datetime.now().hour);
    past_time.append(datetime.now().minute);
    past_time.append(datetime.now().second);

    input("{:s} ДА! Вот просто стою - и просто жду. Это ТЫ ничего не понимаешь!".format(
            str(datetime.now())
    ));

    if datetime.now().hour >= past_time[0]:
        past_time[0] = datetime.now().hour - past_time[0];
    else:
        past_time[0] = past_time[0] + 12;

    if datetime.now().minute >= past_time[1]:
        past_time[1] = datetime.now().minute - past_time[1];

    if datetime.now().second >= past_time[2]:
        past_time[2] = datetime.now().second - past_time[2];

    return past_time;

def datetime_predict():
    from datetime import datetime
    past_time = list();
    # print(str(datetime.now()).split());
    ps_time = "";
    past_time.append(datetime.now().year);
    past_time.append(datetime.now().month);
    past_time.append(datetime.now().day);
    past_time.append(datetime.now().hour);
    past_time.append(datetime.now().minute);
    past_time.append(datetime.now().second);
    past_time.append(datetime.now().microsecond);
    for el in past_time:
        ps_time += " {:n}".format(el);
    print(ps_time);
    
    predict_time = list();
    pr_time = "";
    predict_time.append(2056); #year
    predict_time.append(4); #mounth
    predict_time.append(22); #day
    predict_time.append(5); #hour
    predict_time.append(0); #minute
    predict_time.append(0); #second
    predict_time.append(0); #microsecond
    for el in predict_time:
        pr_time += " {:n}".format(el);
    print(pr_time);

    res_time = "Вот сколько времени пройдёт до указанной даты: ";
    for i in range(0, len(predict_time),):
        res_time += " {:n}".format(predict_time[i] - past_time[i]);
    print(res_time);

    res_time = "Вот какая дата наступит через указанное количество времени: ";
    for i in range(0, len(predict_time),):
        res_time += " {:n}".format(predict_time[i] + past_time[i]);
    print(res_time);

datetime_predict();
# print(datetime_count());
#
# time_use();
#
# datetime_use();