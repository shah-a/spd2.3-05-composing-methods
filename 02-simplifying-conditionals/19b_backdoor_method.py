"""Exercise 19 (part 2): Remove control flag"""

# Reference: https://searchcode.com/file/92870153/frameworkconsole/framework.py/


def backdoor_srcmethod():
    while True:
        print("Puts the Android Agent inside an Android App APK. The application runs normally, with extra functionality.")
        input_file = input('APK to Backdoor: ').strip()
        if input_file == '':
            break
        print('doing other stuff.')


backdoor_srcmethod()
