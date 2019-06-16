card_list = list()


def card_menu():
    print("*" * 50)
    print("欢迎使用【名片管理系统】v1.0")
    print()
    print()
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("0.退出系统")
    print()
    print("*" * 50)


def new_card():
    print("功能：新建名片")
    name = input("请输入姓名:")
    phone = input("请输入电话:")
    QQ = input("请输入QQ:")
    email = input("请输入email:")
    dict_card = dict()
    dict_card["name"] = name
    dict_card["phone"] = phone
    dict_card["QQ"] = QQ
    dict_card["email"] = email
    card_list.append(dict_card)

    print("添加成功%s的名片" % dict_card["name"])


# 显示所有名片
def show_all():
    print("*" * 50)

    print("功能：显示全部")
    if card_list == 0:
        print("提示：没有任何名片记录")
        return
    print("-" * 50)

    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    print()
    print("-" * 50)
    for dict_card in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (dict_card["name"], dict_card["phone"], dict_card["QQ"], dict_card["email"]))
        print("-" * 50)


# 查询名片
def search_card():
    print("功能：查询名片")

    for dict_card in card_list:
        while True:
            a = input("请输入要查询的姓名：")
            if dict_card["name"] == a:
                print("-" * 50)
                print("%s\t\t%s\t\t%s\t\t%s" % ("姓名", "电话", "QQ", "邮箱"))
                print("-" * 50)

                print("%s\t\t%s\t\t%s\t\t%s" % (dict_card["name"], dict_card["phone"], dict_card["QQ"], dict_card["email"]))
                print("-" * 50)
                return a

            else:
                print("没有找到%s" % a)
                continue


# 修改名片
def doing_card(username):
    while True:

        print("1.修改")
        print("2.删除")
        print("0.返回上一级")
        b = input("请输入选项：")
        if b == "1":
            print("修改")
            name = input("请重新输入姓名：")
            phone = input("请重新输入电话：")
            QQ = input("请重新输入QQ：")
            email = input("请重新输入邮箱：")
            for i in card_list:
                if i['name'] == username:
                    i['name'] = name
                    i['phone'] = phone
                    i['QQ'] = QQ
                    i['email'] = email
            print("%s的名片已经修改成功" % (name))
            break

        elif b == "2":
            print("删除")

            break

        elif b == "0":
            print("返回上一级")
            break
        else:
            print("输入有误")
