while True:
    ent = input("是否继续(y/n):")
    if ent == "n":
        break
    else:
        input_string = input("请输入一个用逗号分隔的列表:")
        strs = input_string.split(',')

        st = ""
        min_len = min(len(s) for s in strs)
        # for i in range(len(strs)):
        for i in range(min_len):
            char = strs[0][i]
            # s = [char[:i+1] for char in strs]
            #if len(set(s)) == 1:
            if all(s[i] == char for s in strs):
                st += char
            else:
                break
        print(st)