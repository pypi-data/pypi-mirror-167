def fwrite(path: str, text, encoding='cp949'):
    """
    It writes a text to a file
    
    :param path: The path to the file you want to write to
    :type path: str
    :param text: The text to be written
    :param encoding: The encoding of the file, defaults to cp949 (optional)
    """

    text = str(text)
    
    if not text:
        text += '\n'
    elif text[-1] != '\n':
        text += '\n'
    
    try:
        with open(path, 'a', encoding=encoding) as f:
            f.write(text)
    except UnicodeEncodeError:
        try:
            with open(path, 'a', encoding='cp949') as f:
                f.write(text)
        except UnicodeEncodeError:
            with open(path, 'a', encoding='utf-8') as f:
                f.write(text)


def distinct(myList: list):
    """
    It takes a list as an argument, converts it to a dictionary, and then returns the list of keys
    
    :param myList: list
    :type myList: list
    :return: A list of unique values from the list passed in.
    """
    return list(dict.fromkeys(myList))


def ip_change2():
    """Change IP.
    USB Tethering is Needed.

    Returns:
        bool: True if success, False otherwise.
    """
    import requests
    import subprocess
    
    result_flag = False
    
    try:
        old_ip = requests.get("https://api.myip.la", timeout=1).text
    except:
        for _ in range(30):
            try:
                old_ip = requests.get("https://api.myip.la", timeout=1).text
            except:
                pass
            else:
                break
        else:
            import socket
            if socket.gethostbyname(socket.gethostname()) == '127.0.0.1':
                print('네트워크가 연결되어있지 않습니다.')
            else:
                print('인터넷 속도가 불안정합니다.')
            return result_flag
    
    subprocess.run(['c:\\adb\\adb', 'shell', 'am', 'start', '-a', 'android.intent.action.MAIN', '-n', 'com.mmaster.mmaster/com.mmaster.mmaster.MainActivity'])
    
    for cnt in range(90):
        print('인터넷 접속대기중 - {}초'.format(cnt+1), end='\r')
        try:
            cur_ip = requests.get("https://api.myip.la", timeout=1).text
        except:
            pass
        else:
            if old_ip == cur_ip:
                print('\n아이피가 변경되지 않았습니다.')
                return result_flag
            else:
                print(f'\n{old_ip} -> {cur_ip} 변경 완료.')
                result_flag = True
                return result_flag
    print('\n아이피가 변경되지 않았습니다.')
    return result_flag


def http_remove(link: str):
    """
    It takes a string, removes the http:// or https:// from the beginning of the string, and then
    removes any trailing slashes
    
    :param link: str = The link you want to remove the http(s):// from
    :type link: str
    :return: The link without the http:// or https://
    """
    import re
    link = re.sub(r"https?://", '', link).strip('/')
    return link


def http_append(link: str):
    '''url에 https 추가'''
    return link if link.startswith('http') else "http://" + link


def get_code_from_image(img_path: str):
    """
    > The function takes an image path as an argument and returns the text in the image
    
    :param img_path: The path to the image file
    :type img_path: str
    :return: The return value is the text of the captcha.
    """
    import sys
    import datetime
    from python_anticaptcha import AnticaptchaClient, ImageToTextTask, AnticaptchaException
    
    ret_val = 'Failed'

    API_KEY = 'b336be7de932b65c877403893a382713'
    
    sys.stdout.write(f'> 보안코드 분석중 (이미지 기반) - {datetime.datetime.now().strftime("%H:%M:%S")}\n')

    try:
        img = open(img_path, 'rb')
    except:
        return ret_val
    
    client = AnticaptchaClient(API_KEY)
    task = ImageToTextTask(img)
    
    try:
        job = client.createTask(task)
        job.join()
    except AnticaptchaException:
        pass
    else:
        ret_val = job.get_captcha_text()
    
    return ret_val


def sound_alert(__msg: str='> 계속하려면 엔터를 입력하세요.\n> '):
    """
    > It plays a bell sound in a loop until the user presses the Enter key
    
    :param __msg: str='> 계속하려면 엔터를 입력하세요.\n> ', defaults to > 계속하려면 엔터를 입력하세요.\n> 
    :type __msg: str (optional)
    """
    import time
    import winsound
    import threading
    import pkgutil

    _pkg = '.'.join(__name__.split('.')[:-1])

    bell_data = pkgutil.get_data(_pkg, 'Bell.wav')

    class AlertThread(threading.Thread):
        
        def __init__(self):
            threading.Thread.__init__(self)
            self.flag = threading.Event()
        
        def run(self):

            while not self.flag.is_set():
                winsound.PlaySound(bell_data, winsound.SND_MEMORY)
                time.sleep(1)
    
    alert = AlertThread()

    alert.start()
    input(__msg)
    alert.flag.set()
    alert.join()


def sep_check(__input, __sep_cnt:int, __sep:str='\t') :
    """
    It check the line divied by param separater count 
    return : dictionary
    result = {
        'success' : boolean
        'error_data' : [ { 'line_no' : 'error_idx', 'sep_cnt' : 'error_line_sep_cnt }, { 'line_no' : 'error_idx', 'sep_cnt' : 'error_line_sep_cnt }, ...]
    }
    
    :param __input: The path to the file you want to read to or text list to splitlines()
    :type __input: str or list
    :param __sep_cnt: The separater count in input file text line
    :param __sep: the separate character
    """

    assert isinstance(__input,str) or isinstance(__input,list), "잘못된 인풋입니다."
    
    __result = {
        'success' : True,
        'error_data' : [],
        'sep' : repr(__sep)
    }

    islist = isinstance(__input,list)
    if islist:
        for __input_idx, __read_line in enumerate(__input, start=1):
            line_sep_cnt = __read_line.count(f'{__sep}')
            if __sep_cnt != line_sep_cnt:
                __result['success'] = False
                __result['error_data'].append({'line_no': str(__input_idx), 'sep_cnt': f'{line_sep_cnt}'})
    else:
        try:
            __input_list = open(f'{__input}','r').read().splitlines()
        except UnicodeDecodeError:
            __input_list = open(f'{__input}','r', encoding='utf-8').read().splitlines()
        for __input_idx, __read_line in enumerate(__input_list, start=1):
            line_sep_cnt = __read_line.count(f'{__sep}')
            if __sep_cnt != line_sep_cnt:
                __result['success'] = False
                __result['error_data'].append({'line_no': str(__input_idx), 'sep_cnt': f'{line_sep_cnt}'})
    return __result


def wait_until(__timestr: str=None):
    import re
    import sys
    import time
    from dateutil.parser import parse, ParserError
    from datetime import datetime

    loading_char_lst = [
        "     ",
        "•    ",
        "••   ",
        "•••  ",
        " ••• ",
        "  •••",
        "   ••",
        "    •",
        "     ",
    ]
    max_idx = len(loading_char_lst)

    if not __timestr:

        while True:
            sys.stdout.write('언제까지 대기할까요?\n')
            sys.stdout.write('ex)20220916 16:08\n')
            sys.stdout.write('ex)16:08\n')
            sys.stdout.write('＊ 형식에 맞게 입력해주세요\n')
            __timestr: str = input("> ")
            if re.match(r'\d{8} \d\d:\d\d', __timestr) or re.match(r'\d\d:\d\d', __timestr):
                break

    try:
        target_time = parse(__timestr)
    except ParserError:
        input("알 수 없는 시간 형식입니다.")
        sys.exit()

    sys.stdout.write(f'{target_time}까지 대기합니다.\n')

    for _ in range(round((target_time - datetime.now()).total_seconds()) * 6):
        time.sleep(1/6)
        sys.stdout.write(f'{loading_char_lst[_ % max_idx]}\r')
    else:
        sys.stdout.write('대기 완료.\n')