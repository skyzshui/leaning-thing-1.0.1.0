mmessage = input("Tell me something,and I will repeat it back to you:")
print(mmessage)
name = input("please enter your name:")
print(f"\nhello,{name}!")
prompt = "if you tell us who you are ,we can personalize the messages you see."
prompt += "\nWhat is your first name?"
name_0 = input (prompt)
print(f"\nHello,{name}!")


height = input("How tall are you in inches?")
height = int(height)
if height >= 48:
    print("\nYou're tall enought to ride.")
else:
    print("\nYou'll be able to ride when you're a little older.")


current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1;


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)


po = '\ntext'
po += '\ntext'
active = True
while active:
    ms = input(po)
    if ms == 'quit':
        active = False
    else:
        print(ms)



cur_num = 0
while cur_num <10:
    cur_num += 1
    if cur_num % 2 ==0:
        continue
    print(cur_num)

# 首先，创建一个待验证用户列表
 # 和一个用于存储已验证用户的空列表。
未完成 = ['alice', 'brian', 'candace']
已完成用户 = []
 # 验证每个用户，直到没有未验证用户为止。
 # 将每个经过验证的用户都移到已验证用户列表中。
while 未完成:
    current_user = 未完成.pop()
    print(f"Verifying user: {current_user.title()}")
    已完成用户.append(current_user)
 # 显示所有已验证的用户。
print("\nThe following users have been confirmed:")
for confirmed_user in 已完成用户:
    print(confirmed_user.title())

