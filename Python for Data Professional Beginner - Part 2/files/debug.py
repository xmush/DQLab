lod = [{'tanah': '70', 'bangunan': '50', 'jarak_ke_pusat': '15', 'harga': '500'}, {'tanah': '70', 'bangunan': '60', 'jarak_ke_pusat': '30', 'harga': '400'}, {'tanah': '70', 'bangunan': '60', 'jarak_ke_pusat': '55', 'harga': '300'}, {'tanah': '100', 'bangunan': '50', 'jarak_ke_pusat': '30', 'harga': '700'}, {'tanah': '100', 'bangunan': '70', 'jarak_ke_pusat': '25', 'harga': '1000'}, {'tanah': '100', 'bangunan': '70', 'jarak_ke_pusat': '50', 'harga': '650'}, {'tanah': '120', 'bangunan': '100', 'jarak_ke_pusat': '20', 'harga': '2000'}, {'tanah': '120', 'bangunan': '80', 'jarak_ke_pusat': '50', 'harga': '1200'}, {'tanah': '150', 'bangunan': '100', 'jarak_ke_pusat': '50', 'harga': '1800'}, {'tanah': '150', 'bangunan': '90', 'jarak_ke_pusat': '15', 'harga': '3000'}]

def min_value(list_attributes):
    min_attribute = 9999
    for attr in list_attributes :
        if int(attr) < min_attribute:
            min_attribute = attr
    return min_attribute

d = min_value(['70', '70', '70', '100', '100', '100', '120', '120', '150', '150'])
print(d)
