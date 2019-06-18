checking_relevance_numbers
=====================
**To check the correctness of the rooms on the website is necessary in the method check_relevance_numbers to pass a two dimensional array, the numbers are transferred in a set. Array format [[url, {number, number}], [url, {number, number}]]**

**code usage example:**
    
```
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

main.check_relevance_numbers(test_data)
```
