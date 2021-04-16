# program = "line"
# flag_rules = ["-s STRINGS", "-n NUMBERS", "-e NULL"]
# commands = ["line -n 100 102 -s hi -e", "line -n id pwd -n 100"]
program = "trip"
flag_rules = ["-days NUMBERS", "-dest STRING"]
commands = ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]


def solution(program, flag_rules, commands):
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

                if ' ' in flag:
                    if len(flag) > 1:
                        fla = flag.split(' ')[0]
                        args = flag.split(' ')[1:]

                        if diction[f'-{fla}'] in ['STRING', 'NUMBER'] and len(args) > 1:
                            check = False
                            break

                        for arg in args:
                            if diction[f'-{fla}'] in ['STRING', 'STRINGS'] and not arg.isalpha():
                                check = False
                                break
                            elif diction[f'-{fla}'] in ['NUMBER', 'NUMBERS'] and not arg.isdigit():
                                check = False
                                break
                            elif diction[f'-{fla}'] == "NULL" and arg:
                                check = False
                                break

                else:
                    if f'-{flag}' in diction.keys() and diction[f'-{flag}'] == 'NULL':
                        pass
                    else:
                        check = False

            check_list.append(check)

    return check_list


print(solution(program, flag_rules, commands))