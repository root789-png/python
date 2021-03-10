id1 = 1;
name1 = "苹果";
price1 = 3.6;
num1 = 500;
quality1 = "A+";
origin1 = "海南";

id2 = 2;
name2 = "香蕉";
price2 = 5.0;
num2 = 600;
quality2 = "B+";
origin2 = "泰国";

id3 = 3;
name3 = "凤梨";
price3 = 6.5;
num3 = 503;
quality3 = "A+";
origin3 = "台湾";

id4 = 4;
name4 = "榴莲 ";
price4 = 30;
num4 = 900;
quality4 = "C+";
origin4 = "泰国";


print("---------------------------------------")
print("__          欢迎来到水果商城            --")
print("---------------------------------------")
print("编号    名称   价格    数量     质量    产地")
print(id1, "    ", name1, "  ", price1, "  ", num1, "  ", quality1, "  ", origin1)
print(id2, "    ", name2, "  ", price2, "  ", num2, "  ", quality2, "  ", origin2)
print(id3, "    ", name3, "  ", price3, "  ", num3, "  ", quality3, "  ", origin3)
print(id4, "    ", name4, "  ", price4, "  ", num4, "  ", quality4, "  ", origin4)
print("--------------------------------------")
print("总金额：", (price1 * num1 + price2 * num2 + price3 * num3 + price4 * num4), "￥")
