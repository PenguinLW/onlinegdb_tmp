def datetime_predict(days=32771):
    from datetime import datetime, timedelta;

    now_time = datetime.now(); #datetime.today();

    day_delta = timedelta(days=days);

    past_time = now_time - day_delta;
    future_time = now_time + day_delta;

    print("{0:n} дней назад была дата: {1:}.\nСпустя {0:n} дней наступит дата: {2:}.".format(days, past_time, future_time));

# def tmp_dt_pr():
#     from datetime import datetime
#     past_time = list();
#     # print(str(datetime.now()).split());
#     ps_time = "";
#     past_time.append(datetime.now().year);
#     past_time.append(datetime.now().month);
#     past_time.append(datetime.now().day);
#     past_time.append(datetime.now().hour);
#     past_time.append(datetime.now().minute);
#     past_time.append(datetime.now().second);
#     past_time.append(datetime.now().microsecond);
#     for el in past_time:
#         ps_time += " {:n}".format(el);
#     print(ps_time);
#
#     predict_time = list();
#     pr_time = "";
#     predict_time.append(2056);  # year
#     predict_time.append(4);  # mounth
#     predict_time.append(22);  # day
#     predict_time.append(5);  # hour
#     predict_time.append(0);  # minute
#     predict_time.append(0);  # second
#     predict_time.append(0);  # microsecond
#     for el in predict_time:
#         pr_time += " {:n}".format(el);
#     print(pr_time);
#
#     res_time = "Вот сколько времени пройдёт до указанной даты: ";
#     for i in range(0, len(predict_time), ):
#         res_time += " {:n}".format(predict_time[i] - past_time[i]);
#     print(res_time);
#
#     res_time = "Вот какая дата наступит через указанное количество времени: ";
#     for i in range(0, len(predict_time), ):
#         res_time += " {:n}".format(predict_time[i] + past_time[i]);
#     print(res_time);