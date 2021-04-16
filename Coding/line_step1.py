program = "line"
flag_rules = ["-s STRING", "-n NUMBER", "-e NULL"]
# commands = ["line -n 100 -s hi -e", "lien -s Bye"]
commands = ["line -s 123 -n HI", "line fun"]
# commands = ["line -e -s 123 -n HI"]


def solution(program, flag_rules, commads):
    diction = {}
    for flag_rule in flag_rules:
        flag, rule = flag_rule.split(" ")
        diction[flag] = rule

    check_list = []
    for command in commands:
        pro = command.split(" ")[0]
        flags = command[len(pro):].strip().split(" -")

        if pro != program:
            check_list.append(False)
        else:
            check = True

            for flag in flags:
                flag = flag.replace("-", "")
                # "-n 100"
                if ' ' in flag:
                    if len(flag) > 1:
                        flag, types = flag.split(" ")
                        if diction[f'-{flag}'] == "STRING" and not types.isalpha():
                            check = False
                            break
                        elif diction[f'-{flag}'] == "NUMBER" and not types.isdigit():
                            check = False
                            break
                        elif diction[f'-{flag}'] == "NULL" and types:
                            check = False
                            break
                # "e"
                else:
                    # 순서 바꾸면 안됨
                    # if diction[f'-{flag}'] == "NULL" and f'-{flag}' in diction.keys():
                    #     pass
                    if f'-{flag}' in diction.keys() and diction[f'-{flag}'] == 'NULL':
                        pass
                    else:
                        check = False

            check_list.append(check)

    return check_list


print(solution(program, flag_rules, commands))