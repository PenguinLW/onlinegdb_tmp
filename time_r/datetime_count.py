def datetime_count(date1, date2):
    from datetime import datetime, date;

    date1 = date(date1[0], date1[1], date1[2]);
    date2 = date(date2[0], date2[1], date2[2]);

    print(abs(date2 - date1));

# def tmp_dt_cnt():
#     from datetime import datetime
#     past_time = list();
#     past_time.append(datetime.now().hour);
#     past_time.append(datetime.now().minute);
#     past_time.append(datetime.now().second);
#
#     input("{:s} ДА! Вот просто стою - и просто жду. Это ТЫ ничего не понимаешь!".format(
#             str(datetime.now())
#     ));
#
#     if datetime.now().hour >= past_time[0]:
#         past_time[0] = datetime.now().hour - past_time[0];
#     else:
#         past_time[0] = past_time[0] + 12;
#
#     if datetime.now().minute >= past_time[1]:
#         past_time[1] = datetime.now().minute - past_time[1];
#
#     if datetime.now().second >= past_time[2]:
#         past_time[2] = datetime.now().second - past_time[2];
#
#     return past_time;