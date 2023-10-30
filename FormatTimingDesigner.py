

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#用于填充数据
# init_value: 初始状态：low/high/valid/z等
# cycle     : 周期(既然说是填充了，说明是有规律的，这个规律就是间隔周期)
# start     : 初始值
# end       : 结束值
# str_ref   : 参考格式(因为数据填充成多少位是有一定格式的，这个参考格式就是用来对齐用的)
#----------------------------------------------------------------------------------------
def PatternPad(init_value:str, cycle:float, start:float, end:float, str_ref="12345.000"):
    STR_REF = str_ref.split('.')

    while(start < end):
        str_start = (str(start)).split('.')
        line = "( " + ' ' * (7 - len(init_value)) + init_value + ', '
        str_num = ' ' * (len(STR_REF[0]) - len(str_start[0])) + str_start[0] + '.' + str_start[1]
        str_num = str_num + '0' * (len(STR_REF[1]) - len(str_start[1]))
        line = line + str_num + ', ' + str_num + "),"
        print(line)
        start += cycle
        if (init_value == "low"):
            init_value = 'high'
        elif(init_value == 'high'):
            init_value = 'low'
        elif(init_value == 'valid'):
            init_value = 'z'
        elif(init_value == 'z'):
            init_value = 'valid'

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#用于格式化数据：TimingDesigner自动生成的数据是不对齐的，这里将括号、逗号、数据等对齐
# string_timing: 字符串数据，例如：
#                                #test = '''(valid,0.000,0.000,L), 
#                                    #(z,41000.000,41000.000), 
#                                    #(valid,128000.000,128000.000), 
#                                    #(z,166000.000,166000.000), 
#                                    #(valid,278000.000,278000.000), 
#                                    #(z,332000.000,332000.000), 
#                                    #(valid,399000.000,399000.000), 
#                                    #(invalid,436000.000,436000.000), 
#                                    #(valid,454000.000,454000.000), 
#                                    #(blank,456135.104,456135.104)) '''
#                                    #print(FormatTiming(test))
# str_ref   : 参考格式(因为数据填充成多少位是有一定格式的，这个参考格式就是用来对齐用的)
#----------------------------------------------------------------------------------------
def FormatTiming(str_timing:str, str_ref="123456.000"):
    STR_REF   = str_ref.split('.')
    lines     = str_timing.split("\n")
    out_lines = ""
    for line in lines:
        if(line != ''):
            line = line.split(')')[0]
            line = line.split('(')[1]
            line = line.split(',')
            line[0] = ' ' * (7-len(line[0])) + line[0]
            tmp     = line[1].split('.')
            line[1] = ' ' * (len(STR_REF[0]) - len(tmp[0])) + tmp[0] + '.'
            line[1]+= tmp[1] + '0' * (len(STR_REF[1]) - len(tmp[1]))

            tmp     = line[2].split('.')
            line[2] = ' ' * (len(STR_REF[0]) - len(tmp[0])) + tmp[0] + '.'
            line[2]+= tmp[1] + '0' * (len(STR_REF[1]) - len(tmp[1]))
            out_line = ""
            for i in line:
                out_line += i + ", "
            out_line = out_line[:-2]
            out_line = '\t(' + out_line + '),'
            out_lines += out_line + "\n"
    return out_lines

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#用于四舍五入：在TimingDesigner中，用鼠标点的波形，可能与时钟沿没有对齐，为了与最近的时钟沿对齐
# string_timing: 字符串数据，例如：
#                                #test = '''(valid,0.000,0.000,L), 
#                                    #(z,41000.000,41000.000), 
#                                    #(valid,128000.000,128000.000), 
#                                    #(z,166000.000,166000.000), 
#                                    #(valid,278000.000,278000.000), 
#                                    #(z,332000.000,332000.000), 
#                                    #(valid,399000.000,399000.000), 
#                                    #(invalid,436000.000,436000.000), 
#                                    #(valid,454000.000,454000.000), 
#                                    #(blank,456135.104,456135.104)) '''
#                                    #print(FormatTiming(test))
# cycle     : 周期(既然说是填充了，说明是有规律的，这个规律就是间隔周期)
# start     : 初始值
# str_ref   : 参考格式(因为数据填充成多少位是有一定格式的，这个参考格式就是用来对齐用的)
#----------------------------------------------------------------------------------------
def RoundTiming(str_timing:str, cycle:float, start:float, str_ref="12345.000"):
    lines = str_timing.split('\n')
    STR_REF   = str_ref.split('.')
    lines     = str_timing.split("\n")
    out_lines = ""
    for line in lines:
        if(line != ''):
            line = line.split(')')[0]
            line = line.split(',')
            #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            tmp  = eval(line[1])
            num  = int( (tmp-start) / cycle)
            if( ((tmp-start) - num*cycle) > cycle/2):
                num += 1
            tmp  = str(start + num*cycle + 0.0001)#0.0001 is just for format
            tmp  = tmp[:-1]
            line[1] = tmp
            #-----------------------------------------------------------------
            #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            tmp  = eval(line[2])
            num  = int( (tmp-start) / cycle)
            if( ((tmp-start) - num*cycle) > cycle/2):
                num += 1
            tmp  = str(start + num*cycle + 0.0001)#0.0001 is just for format
            tmp  = tmp[:-1]
            line[2] = tmp
            #-----------------------------------------------------------------
            out_line = ""
            for i in line:
                out_line += i + ", "
            out_line = out_line[:-2]
            out_line = '\t' + out_line + '),'
            out_lines += out_line + "\n"
    return out_lines


if __name__ == "__main__":
    VALUE = ['low', 'high', 'z', 'valid', 'blank']

    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #######: PatternPad(init_value:str, cycle:float, start:float, end:float, str_ref="12345.000")
    #PatternPad('z', 84000.080, 0.0, 453150, str_ref="123045.000")
    ##------------------------------------------------------------------------------------------

    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #test = '''(valid,0.000,0.000,L), 
    #(z,41000.000,41000.000), 
    #(valid,128000.000,128000.000), 
    #(z,166000.000,166000.000), 
    #(valid,278000.000,278000.000), 
    #(z,332000.000,332000.000), 
    #(valid,399000.000,399000.000), 
    #(invalid,436000.000,436000.000), 
    #(valid,454000.000,454000.000), 
    #(blank,456135.104,456135.104)) '''
    #print(FormatTiming(test))
    ##------------------------------------------------------------------------------------------


    ##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #test = '''(valid,0.000,0.000,L), 
    #(z,41000.000,41000.000), 
    #(valid,128000.000,128000.000), 
    #(z,166000.000,166000.000), 
    #(valid,278000.000,278000.000), 
    #(z,332000.000,332000.000), 
    #(valid,399000.000,399000.000), 
    #(invalid,436000.000,436000.000), 
    #(valid,454000.000,454000.000), 
    #(blank,456135.104,456135.104)) '''
    #lines = RoundTiming(FormatTiming(test), 41000, 0, str_ref="12345.000")
    #print(lines)
    ##------------------------------------------------------------------------------------------


    

