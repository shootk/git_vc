musician_list = ["Mr.Children","東京事変","aiko"]
musician_list

my_tuple = [(105.23,235.34),(291.23,34.25)]
my_tuple

my_info = {"身長":"175.8","色":"Blue","人":"R.K"}
my_info

key = input("Please input key:")
if key in my_info:
    print(my_info[key])
else:
    print("Fuck off")

fab_mu = {"Mr.Children":["and I love you","しるし",
                         "365日","NOT FOUND","CANDY","Heavenl Kiss"]}
key = input("input key")
if key in fab_mu:
    print(fab_mu[key])
else:
    print("fuck off")
