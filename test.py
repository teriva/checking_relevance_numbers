import re
import time


def test1(input_str):
    return "".join(re.findall('\d', input_str))

def test2(input_str):
    return re.sub('\D', '', input_str)

def test3(string):
    number = ''
    for i in string:
        if i.isdigit():
            number += i
    return number

x = "dfahsdfa777sdfasdфавыажфырн234dfsg;dfgjls;kdfjgs;443442324334433244333423dfasdfjalsdknlkfh;fambeq;ewkbalsdkjfhlasdkhfalkhsdlfkjadslhasdjkhflasdjhflasdjhfafaыывафывафываф23423ывафвыафвафывавфвафыва342ывфафывоафдывлаофывдалфывлорадфвыолрафылвафывафыва34234фывавыsda97afsdfasld;fhlfas8dsdfadsfalsbdfalhh7869asdfsjlhdfagks,dbfkahgsdfba,msndgfalhjsdbhfa;hkjsldhgklf;abgsd;fahjbsljdf77aslkdbflaks"


time_start = time.time()
(test1(x))
print(time.time() - time_start)

time_start = time.time()
(test2(x))
print(time.time() - time_start)

time_start = time.time()
(test3(x))
print(time.time() - time_start)


