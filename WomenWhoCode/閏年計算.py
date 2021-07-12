# 閏年

try:
    year = int(input("年份: "))
    if year < 1800:
        print("Please input year above 1800 !")
    else: # input > 1800
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print(f"{year}年 是閏年")  # % 400 == 0
                else:
                    print(f"{year}年 不是閏年") # % 100 == 0
            else:
                print(f"{year}年 是閏年")       #  %4 == 0
        else:
            print(f"{year}年 不是閏年")
except: # input is not a number
    print("Not a vaild year !")