# @Time    : 2020/3/29 14:30
# @Author  : LavÖz
# @File    : 京东.py
# @Software: PyCharm
import frida, sys, os
os.system("adb -s emulator-5554 forward tcp:27042 tcp:27042")
with open("./index.js", "r", encoding="utf8") as f:
    jscode = f.read()


def message(message, data):
    if message["type"] == "send":
        try:
            print("[*]", message["payload"])
        except:
            print("============")

            print(message)
            print("============")

    else:
        print(message)


if __name__ == '__main__':
    # 先打开app进程
    process = frida.get_remote_device().attach("com.jinanshenghuoribao")
    # process = frida.get_remote_device().attach("com.jingdong.app.mall")
    script = process.create_script(jscode)
    script.on("message", message)
    script.load()
    sys.stdin.read()
