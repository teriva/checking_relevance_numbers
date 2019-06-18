import time
from multiprocessing import Pool

import parser



HEADERS = {
    'accept': '*/*',
    'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36"
}
NUMBER_PROCESSES = 10


def check(input_data):
    url = input_data[0]
    expectation = input_data[1]
    parse = parser.parse(url, HEADERS)
    if len(parse) != 0 and parse[0] == expectation:
        print("test", url, "result=OK time=" + parse[1])
    else:
        print("test", url, "result=NUMBERS DON'T MATCH!!!")


def check_relevance_numbers(input_data):
    time_start_test = time.time()
    with Pool(NUMBER_PROCESSES) as pool:
        pool.map(check, input_data)
    print("total time spent: ", time.time() - time_start_test)

def get_numbers(url):
    parse = parser.parse(url, HEADERS)
    if len(parse) != 0:
        print("test", url, "result=OK time=" + parse[1], "numbers:")
        for number in parse[0]:
            print(number)
    else:
        print("test", url, "result=NUMBERS DON'T MATCH!!!")


def get_all_numbers(urls):
    time_start_test = time.time()
    with Pool(NUMBER_PROCESSES) as pool:
        pool.map(get_numbers, urls)
    print("total time spent: ", time.time() - time_start_test)
