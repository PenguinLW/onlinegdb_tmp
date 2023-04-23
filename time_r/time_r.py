# https://wikihandbk.com/wiki/Python:Рецепты/Определить_дату,_которая_наступит_через_N_дней_от_текущей_даты
# https://pythoner.name/datetime-qty

# from tmp_time_r import *
# time_use();
# datetime_use();

from datetime_count import datetime_count
datetime_count(
    [2056, 1, 1], [1995, 10, 11]
);

from datetime_predict import datetime_predict
datetime_predict(days=2056);