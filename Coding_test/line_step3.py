# program = "line"
# flag_rules = ["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"]
# commands = ["line -n 100 -s hi -e", "line -n 100 -e -n 150"]
program = "bank"
flag_rules = ["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"]
commands = ["bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"]


def solution(program, flag_rules, commands):
    diction = {}
    alias_dict = {}
    for flag_rule in flag_rules:
        if 'ALIAS' not in flag_rule:
            flag, rule = flag_rule.split(' ')
            diction[flag] = rule
        else:
            alias, _, flag = flag_rule.split(' ')
            alias_dict[alias] = flag

    check_list = []
    for command in commands:
        pro = command.split(" ")[0]
        flags = command[len(pro):].strip().split(" -")

        if pro != program:
            check_list.append(False)
        else:
            check = True

            list_flag = []
            for flag in flags:
                flag = flag.replace("-", "")

                if ' ' in flag:
                    if len(flag) > 1:
                        fla = flag.split(' ')[0]
                        args = flag.split(' ')[1:]

                        if f'-{fla}' not in diction.keys():
                            if f'-{fla}' in alias_dict.keys():
                                fla = alias_dict[f'-{fla}'][1:]

                        if fla in list_flag:
                            check = False
                            break
                        else:
                            list_flag.append(fla)

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