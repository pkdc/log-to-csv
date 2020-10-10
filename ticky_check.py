#!/usr/bin/env python3
import re
#import sys
import csv


def extract_from_log(log):

    extracted_error = []
    extracted_usage_log_type = []
    extracted_usage_username = []

    with open(log, mode="r", encoding="UTF-8") as f:
        for line in f:
            r_usage = re.search(r"(ERROR|INFO).+\(([\w. -]+)\)", line)
            assert r_usage is not None, "There is no match ERROR or INFO in this log"
            #assert type(r_usage) != None
            extracted_usage_log_type.append(r_usage.group(1))
            extracted_usage_username.append(r_usage.group(2))
            # extracted_usage_log_type.append(r_usage[1])
            # extracted_usage_username.append(r_usage[2])

            # filter out irrelevant lines increases efficency
            if "ERROR" in line:
                r_error = re.search(r"\bERROR\b\s([\w. -]*) ", line)
                assert r_error is not None, "There is no match for ERROR in this log"
                extracted_error.append(r_error.group(1))
                # extracted_error.append(r_error[1])
    return extracted_error, extracted_usage_log_type, extracted_usage_username


def construct_error_dict(extracted_error):

    # construct the error error_dictionary
    error_dict = {}

    for error in extracted_error:
        # if there is a key in the dict, then increment it, if not then put the key in the dict, with value = 0, then + 1
        error_dict[error] = error_dict.get(error, 0) + 1

    # check if the dict is empty
    if error_dict == {}:
        raise ValueError("Dictionary is empty")

    # error_dict.items() returns a list of (key, value), see https://www.geeksforgeeks.org/dictionary-methods-in-python-set-1-cmp-len-items/
    # eg [(key1, value1), (key2, value2), (key3, value3)]
    # sorted(iterable, key=key, reverse=reverse), from W3Schools
    # iterable  Required. The sequence to sort, list, dictionary, tuple etc here it's a list
    # key   Optional. A Function to execute to decide the order. Default is None, Must be a lambda function!
    error_dict = {k: v for k, v in sorted(
        error_dict.items(), key=lambda tuple: tuple[1], reverse=True)}
    print(error_dict)
    return(error_dict)


def contruct_user_stats_dict(extracted_usage_log_type, extracted_usage_username):

    # construct the user stats Dictionary
    user_stats_dict = {}
    assert len(extracted_usage_log_type) > 0, "No log type recorded"
    assert len(extracted_usage_username) > 0, "No user recorded"
    assert len(extracted_usage_log_type) == len(
        extracted_usage_username), "Different no. of users and corresponding log type"
    # for index in range(len(list_of_lists[1])):  # can also use list_of_lists[2]
    #
    #     uname = list_of_lists[2][index]  # username
    #     log_type = list_of_lists[1][index]  # INFO / ERROR

    # zip function returns tuples consists of the elements from the lists
    for uname, log_type in zip(extracted_usage_username, extracted_usage_log_type):

        if uname not in user_stats_dict:  # new entry
            if log_type == "INFO":
                user_stats_dict[uname] = [1, 0]
            elif log_type == "ERROR":
                user_stats_dict[uname] = [0, 1]
            else:
                raise ValueError("Wrong log_type")

        else:  # entry already exist
            if log_type == "INFO":
                user_stats_dict[uname][0] = user_stats_dict.get(uname)[0] + 1
            elif log_type == "ERROR":
                user_stats_dict[uname][1] = user_stats_dict.get(uname)[1] + 1
            else:
                raise ValueError("Wrong log_type")

    # # experimenting with sorting the user_stat_dict with freq of logged uses per users
    # user_stats_dict = {k: v for k, v in sorted(
    #     user_stats_dict.items(), key=lambda tuple: tuple[1][0] + tuple[1][1], reverse=True)}
    # print(user_stats_dict)

    # sorting alphabetically by username
    user_stats_dict = {k: v for k, v in sorted(user_stats_dict.items(), key=lambda tuple: tuple[0])}

    print(user_stats_dict)
    return user_stats_dict


def error_dict_to_csv(error_dict):

    # write dictionaries to csv
    # write the error dict to error.csv
    err_key = ["error", "frequency"]

    with open("error_message.csv", "w", newline='') as f:
        err_writer = csv.writer(f)
        err_writer.writerow(err_key)
        for k, v in error_dict.items():
            err_writer.writerow([k, v])


def user_stats_dict_to_csv(user_stats_dict):

    # write the user stats dict to user_stats.csv
    u_stats_key = ["user", "INFO", "ERROR"]

    with open("user_statistics.csv", "w") as f:
        stats_writer = csv.writer(f)
        stats_writer.writerow(u_stats_key)
        for k, [v1, v2] in user_stats_dict.items():
            stats_writer.writerow([k, v1, v2])


def main():
    m_extracted_error, m_extracted_usage_log_type, m_extracted_usage_username = extract_from_log(
        "syslog.log")
    #m_extracted_error, m_extracted_usage_log_type, m_extracted_usage_username = extract_from_log(sys.argv[1])
    m_error_dict = construct_error_dict(m_extracted_error)
    m_stats_dict = contruct_user_stats_dict(m_extracted_usage_log_type, m_extracted_usage_username)
    error_dict_to_csv(m_error_dict)
    user_stats_dict_to_csv(m_stats_dict)


if __name__ == "__main__":
    main()
