def read_file(filename):
    lines = []
    with open(filename,'r',encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None
    allen_word = 0
    viki_word  = 0
    a_skr = 0
    v_skr = 0
    a_pic = 0
    v_pic = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                a_skr += 1
            for msg in s[2:]:
                allen_word += len(msg)
                if msg =='圖片':
                    a_pic += 1
        elif name == 'Viki':
            if s[2] == '貼圖':
                v_skr += 1
            for msg in s[2:]:
                viki_word += len(msg)
                if msg == '圖片':
                    v_pic += 1
    print('allen:',allen_word)
    print('viki:',viki_word)
    print('allen_skr:',a_skr)
    print('viki_skr:',v_skr)
    print('allen_pic:',a_pic)
    print('viki_pic:',v_pic)

def write_file(filename,lines):
    with open(filename,'w',encoding='utf-8-sig')as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
    #write_file('output.txt',lines)

main()