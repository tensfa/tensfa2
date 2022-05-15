import pandas as pd
from pprint import pprint
import json
import numpy as np


def merge_time():
    time1 = json.load(open('time_dict_icse.json', 'r', encoding='utf-8'))
    time2 = json.load(open('time_dict_so.json', 'r', encoding='utf-8'))
    for k,  v in time2.items():
        if k in time1:
            time1[k].extend(time2[k])
        else:
            time1[k] = time2[k]
    tf_mean_time, keras_mean_time = {}, {}
    for k, v in time1.items():
        if k.startswith('tf'):
            tf_mean_time[k] = sum(v)/len(v)
        else:
            keras_mean_time[k] = sum(v)/len(v)

    tf_mean_time = sorted(tf_mean_time.items(), key=lambda x: -x[1])
    keras_mean_time = sorted(keras_mean_time.items(), key=lambda x: -x[1])

    pprint(tf_mean_time)
    pprint(keras_mean_time)


def sort_patterns():
    random_means, ascending_means, descending_means, time_freq_means = [], [], [], []
    random_sum, ascending_sum, descending_sum, time_freq_sum = [], [], [], []
    for i in range(1, 11):
        icse_random = pd.read_excel(f'time{i}/ICSE2020RandomOrderTime.xlsx')
        so_random = pd.read_excel(f'time{i}/StackOverflowRandomOrderTime.xlsx')
        random = pd.concat([icse_random, so_random], axis=0)

        icse_ascending = pd.read_excel(
            f'time{i}/ICSE2020AscendingOrderTime.xlsx')
        so_ascending = pd.read_excel(
            f'time{i}/StackOverflowAscendingOrderTime.xlsx')
        ascending = pd.concat([icse_ascending, so_ascending], axis=0)

        icse_descending = pd.read_excel(
            f'time{i}/ICSE2020DescendingOrderTime.xlsx')
        so_descending = pd.read_excel(
            f'time{i}/StackOverflowDescendingOrderTime.xlsx')
        descending = pd.concat([icse_descending, so_descending], axis=0)

        icse_time_freq = pd.read_excel(
            f'time{i}/ICSE2020TimeFreqOrderTime.xlsx')
        so_time_freq = pd.read_excel(
            f'time{i}/StackOverflowTimeFreqOrderTime.xlsx')
        time_freq = pd.concat([icse_time_freq, so_time_freq], axis=0)

        random_means.append(sum(random['time'])/len(random['time']))
        ascending_means.append(sum(ascending['time'])/len(ascending['time']))
        descending_means.append(
            sum(descending['time'])/len(descending['time']))
        time_freq_means.append(sum(time_freq['time'])/len(time_freq['time']))

        random_sum.append(sum(random['time']))
        ascending_sum.append(sum(ascending['time']))
        descending_sum.append(sum(descending['time']))
        time_freq_sum.append(sum(time_freq['time']))

    pprint(random_means)
    pprint(ascending_means)
    pprint(descending_means)
    pprint(time_freq_means)

    print(sum(random_means)/len(random_means))
    print(sum(ascending_means)/len(ascending_means))
    print(sum(descending_means)/len(descending_means))
    print(sum(time_freq_means)/len(time_freq_means))
    print('===========================================')

    print(np.std(random_means))
    print(np.std(ascending_means))
    print(np.std(ascending_means))
    print(np.std(ascending_means))
    print('===========================================')

    print(sum(random_sum)/len(random_sum))
    print(sum(ascending_sum)/len(ascending_sum))
    print(sum(descending_sum)/len(descending_sum))
    print(sum(time_freq_sum)/len(time_freq_sum))
    print('===========================================')

    print(np.std(random_sum))
    print(np.std(ascending_sum))
    print(np.std(descending_sum))
    print(np.std(time_freq_sum))


if __name__ == '__main__':
    sort_patterns()
