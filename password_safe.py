import random
import string
FILE_PATH="pwd.txt"

def load_pwd():
    data={}
    try:
        with open(FILE_PATH,"r",encoding="utf-8") as f:
            for line in f:
                line=line.strip()
                if not line:
                    continue
                site,user,pwd=line.split("#")
                data[site]=[user,pwd]

    except FileNotFoundError:
        pass
    return data

def save_pwd(all_data):
    with open(FILE_PATH,"w",encoding="utf-8") as f:
        for site,info in all_data.items():
            username,password = info
            f.write(f"{site}#{username}#{password}\n")

def create_random_pwd(length):
    char_pool=string.ascii_letters + string.digits+"!@#$%^&*"
    res=random.sample(char_pool,length)
    return "".join(res)

def main():
    pwd_data=load_pwd()
    while True:
        print("\n=====密码保存工具箱=====")
        print("1,自动生成高难度密码")
        print("2,新赠网站账号密码")
        print("3,查找网站储存密码")
        print("4,修改账号或密码")
        print("5,删除网站记录")
        print("0.退出程序")
        try:
            opt=int(input("请输入功能序号："))
            if opt==1:
                i=int(input("请输入密码长度（建议8-16）："))
                if i<6:
                    print("密码长度不能小于6位")
                    continue
                new_pwd=create_random_pwd(i)
                print(f"生成密码:{new_pwd}")

            elif opt==2:
                site=input("输入网站/软件名称：").strip()
                if site=="":
                    print("网站/软件名不得为空")
                    continue
                if site in pwd_data:
                    print("该网站已存在，请勿重复使用！")
                    continue
                acc=input("输入账号：").strip()
                pw=input("输入密码（回车生成密码）：").strip()
                if pw=="":
                    i=int(input("请输入密码长度（建议8-16）："))
                    if i < 6:
                        print("密码长度不能小于6位")
                        continue
                    pw= create_random_pwd(i)
                    print(f"自动生成密码:{pw}")
                pwd_data[site]=[acc,pw]
                save_pwd(pwd_data)
                print("信息保存成功！")

            elif opt==3:
                search_site=input("输入要查询的网站名称：").strip()
                if search_site=="":
                    print("无此网站记录！")
                else:
                    u,p=pwd_data[search_site]
                    print(f"网站：{search_site}\n账号：{u}\n密码：{p}")

            elif opt==4:
                edit_site=input("请输入要修改的网站名称：").strip()
                if edit_site not in pwd_data:
                    print("没有该网站记录！")
                    continue
                new_acc=input("请输入新账号(不变直接按回车即可)：")
                new_pw=input("请输入新密码(不变直接回车即可)：")
                old_acc,old_pw=pwd_data[edit_site]
                if new_acc!="":
                    old_acc=new_acc
                if new_pw!="":
                    old_pw=new_pw
                pwd_data[edit_site]=[old_acc,old_pw]
                save_pwd(pwd_data)
                print("修改完成！")

            elif opt==5:
                del_site=input("输入要修改的网站名称：").strip()
                if del_site not in pwd_data:
                    print("无此网站记录！")
                    continue
                del pwd_data[del_site]
                save_pwd(pwd_data)
                print("记录已删除！")

            elif opt==0:
                print("数据已保存，程序结束")
                break
            else:
                print("请输入0-5的数字！")

        except ValueError:
            print("输入非法，请输入数字！")
if __name__=="__main__":
    main()





