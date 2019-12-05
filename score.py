def calc():
    with open('score.csv','r',encoding= 'utf-8') as fo:
        str_info = ''
        statistic = '统计,语文,数学,英语\n'
        yuwen,math,English = 0,0,0
        yuwen_max,math_max,English_max = 0,0,0
        yuwen_min,math_min,English_min = 100,100,100
        n = -1
        for i in fo.readlines():
            line = i.strip('\n').split(',')
            sum = 0
            n += 1
            if len(str_info) == 0:
                str_info += i.strip('\n') + ',' + '总分\n'
            else:
                for a in line[1:]:
                    sum += eval(a)
                str_info += i.strip('\n') + ',' + str(sum) + '\n'
                yuwen_max = eval(line[1]) if yuwen_max < eval(line[1]) else yuwen_max
                math_max = eval(line[2]) if math_max < eval(line[2]) else math_max
                English_max = eval(line[3]) if English_max < eval(line[3]) else English_max
                yuwen_min = eval(line[1]) if yuwen_min > eval(line[1]) else yuwen_min
                math_min = eval(line[2]) if math_min > eval(line[2]) else math_min
                English_min = eval(line[3]) if English_min > eval(line[3]) else English_min
                yuwen += eval(line[1])
                math += eval(line[2])
                English += eval(line[3])
        statistic += '最高分' + ',' + str(yuwen_max) + ',' + str(math_max) + ',' + str(English_max) + '\n'
        statistic += '最低分' + ',' + str(yuwen_min) + ',' + str(math_min) + ',' + str(English_min) + '\n'
        statistic += '平均分' + ',' + '{:.2f}'.format(yuwen/n) + ',' + '{:.2f}'.format(math/n) + ',' + '{:.2f}'.format(English/n) + '\n'
    return str_info,statistic
        
info = calc()
print(info[1])
fo = open('score.csv','w',encoding= 'utf-8')
fo.write(info[0])
fo.close()
