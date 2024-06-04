from smartphone import Smartphone
iPhone = Smartphone('iPhone', 'XR', '89001000001')
Xiaomi = Smartphone('Xiaomi', 'redmi 9C', '89001000002')
Huawei = Smartphone('Huawei', 'One', '89001000003')
Poco = Smartphone('Poco', 'X3', '89001000004')
Oppo = Smartphone('Oppo', 'x5 NFC', '89001000005') 

catalog = [iPhone, Xiaomi, Huawei, Poco, Oppo]

for i in range(0,len(catalog)):
    print(catalog[i].mark, '-', catalog[i].model, '.', catalog[i].number)