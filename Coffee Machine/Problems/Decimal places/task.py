raw_num = float(input())
dec_place = int(input())
print("%.{}f".format(dec_place) % raw_num)
