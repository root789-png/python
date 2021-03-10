id1 = 1;
name1 = "短袖";
price1 = 50;
quality1 = "A+";
type1 = "上衣";
sales1 = 500;

id2 = 2;
name2 = "背心";
price2 = 100;
quality2 = "A+";
type2 = "上衣";
sales2 = 50;

id3 = 3;
name3 = "裙裤";
price3 = 300;
quality3 = "A+";
type3 = "上衣";
sales3 = 700;

id4 = 4;
name4 = "打底裤";
price4 = 89;
quality4 = "A+";
type4 = "上衣";
sales4 = 900;

print("---------------------------------------")
print("__          欢迎来到水果商城            --")
print("---------------------------------------")
print("编号    衣服名称   价格    品质     类型    销量")
print(id1, "     ", name1, "    ", price1, "   ", quality1, "    ", type1, "  ", sales1)
print(id2, "     ", name2, "    ", price2, "  ", quality2, "    ", type2, "  ", sales2)
print(id3, "     ", name3, "    ", price3, "  ", quality3, "    ", type3, "  ", sales3)
print(id4, "    ", name4, "    ", price4, "  ", quality4, "    ", type4, "  ", sales4)
print("--------------------------------------")
print("总金额：", (price1 * sales1 + price2 * sales2 + price3 * sales3 + price4 * sales4), "￥")
