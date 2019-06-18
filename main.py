import time
from multiprocessing import Pool

import parser

test_data = [
    ["https://www.auchan.ru/pokupki/eda/bakaleja/krupy-boby/goroh.html", {'88007005800'}],
    ["https://repetitors.info/", {'88005555676', '84955405676'}],
    ["https://hands.ru/company/about/", {'84951370720'}],
    ["https://dodopizza.ru/dmitrov/moskovskaya23a", {'88003020060'}],
    ["https://dm.pizzeriaantonio.ru/", {'89055673555', '89779475626'}],
    ["https://ipizza.ru/", {'84957907797'}],
    ["https://www.perekrestok.ru", {'84957975777', '88002009555'}],
    ["http://prosto-food.ru/", {'79623654365', '74962224333'}],
    ["https://www.delivery-club.ru/contacts/",
     {'88003336250', '84956637724', '84956637722', '88126779122', '88002220022', '84952522603', '84999558613',
      '84952522788', '88003336150', '88125021713', '84956467437'}]
]

HEADERS = {
    'accept': '*/*',
    'user-agent': "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36"
}
NUMBER_PROCESSES = 8


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

check_relevance_numbers(test_data)