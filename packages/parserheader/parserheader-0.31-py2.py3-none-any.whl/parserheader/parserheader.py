#!/usr/bin/env python

import re
import click
from pprint import pprint
try:
    from pause import pause
except:
    def pause(*args, **kwargs):
        input("enter to continue")
try:
    from pydebugger.debug import debug
except:
    def debug(*args, **kwargs):
        return ''

if __name__ == '__main__':
    try:
        from pydebugger.debug import debug
    except:
        def debug(headers_dict=None):
            import os
            if os.getenv('DEBUG'):
                print("headers_dict =", headers_dict)
else:
    def debug(*args, **kwargs):
        return None

class parserheader(object):

    def __init__(self):
        super(parserheader, self)

    @classmethod
    def setCookies(self, cookies_str_or_dict, dont_format=False, **kwargs):
        cookie_dict = {}
        cookie_str = ''
        # if not cookies_str_or_dict:
        #     cookies_str_or_dict = "ym_uid=1532996994661863820; _ym_d=1532996994; _ym_isad=2; tr=2 4 6 8 9 10"
        if __name__ == '__main__':
            click.secho("Example Input string cookies:", fg='black', bg='cyan')
            print(cookies_str_or_dict)
        if isinstance(cookies_str_or_dict, str) or isinstance(cookies_str_or_dict, unicode):
            cookies_str_or_dict = re.split("; ", cookies_str_or_dict)
            for i in cookies_str_or_dict:
                if i.strip():
                    key,value = str(i).strip().split("=")
                    cookie_dict.update({key:value})
            debug(cookie_dict=cookie_dict)
        elif isinstance(cookies_str_or_dict, dict):
            for i in cookies_str_or_dict:
                cookie_str += str(i) + "=" + cookies_str_or_dict.get(i) + "; "
            cookie_str = cookie_str.strip()
            debug(cookie_str=cookie_str)
            if cookie_str:
                if cookie_str[-1] == ";":
                    cookie_str = cookie_str[:-1]
            cookie_dict = cookies_str_or_dict
        if not cookie_str:
            cookie_str = cookies_str_or_dict
        if __name__ == '__main__':
            click.secho("Example Output Dictionary cookies:", fg='black', bg='green')
            print(cookie_dict)
            print("-" * (click.get_terminal_size()[0] - 1))
            print("\n")
        if kwargs:
            for i in kwargs:
                if not dont_format:
                    key = str(i).replace("_","-")
                else:
                    key = str(i)
                value = kwargs.get(i)
                cookie_dict.update({key:value})
            return self.setCookies(cookie_dict)
        return cookie_dict, cookie_str

    @classmethod
    def parserHeader(self, string_headers = None, get_path='/', cookies_dict_str='', **kwargs):
        # cookies_dict_str example: _ym_uid=1532996994661863820; _ym_d=1532996994; _ym_isad=2;
        #
        string_headers_example = """
        Host: ''
        Connection: keep-alive
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
        Referer: ''
        Accept-Encoding: gzip, deflate
        Accept-Language: en-US,en;q=0.9
        Cookie: ''
        """
        headers_dict = {}
        if not string_headers:
            string_headers = string_headers_example
        
        if string_headers:
            # data = str(string_headers).replace("       ", "")
            # data = re.split("\n|\r", data)
            data = re.split("\n|\r", string_headers)
            debug(data = data)
            data = [i.strip() for i in data]
            debug(data = data)
            data = list(filter(None, data))
            debug(data = data)
            
            for i in data:
                debug(i = i)
                key, value = '', ''
                if ": " in i:
                    data_split = re.split(": ", i)
                    debug(data_split = data_split)
                    if len(data_split) == 2:
                        key, value = data_split
                        key = key.strip()
                        value = value.strip()
                        if value == "''" or value == '""': value = ''
                        headers_dict.update({key: value,})
                elif ":" in i:
                    data_split = re.split(":", i)
                    key, value = data_split[0], ":".join(data_split[1:])

            if kwargs:
                for i in kwargs:
                    key = str(i).replace("_","-").title()
                    value = kwargs.get(i)
                    headers_dict.update({key:value})
            debug(headers_dict = headers_dict)
            if cookies_dict_str:
                if isinstance(cookies_dict_str, str):
                    headers_dict.update({'Cookie':cookies_dict_str})
                    debug(headers_dict=headers_dict)
                elif isinstance(cookies_dict_str, dict):
                    cd, cs = self.setCookies(cookies_dict_str)
                    headers_dict.update({'Cookie':cs})
                    debug(headers_dict=headers_dict)
            debug(headers_dict = headers_dict, debug = 1)
        return headers_dict

    @classmethod
    def UserAgent(self, user_agent_string):
        '''Get User-Agent
        
        Get user agent string from header (parserHeader Object)
        
        Arguments:
            user_agent_string {string header get 'User-Agent' Object} -- parserHeader Object
        '''
        c = parserheader()
        if isinstance(user_agent_string, dict):
            user_agent = c.parserHeader(headers).get('User-Agent')
        else:
            user_agent = user_agent_string
        user_agent_split = re.split(' ', user_agent, 1)
        if __name__ == '__main__':
            click.secho("Example Output Get User-Agent:", fg='black', bg='yellow')
            print("user_agent =", user_agent)
            print("user_agent_split =", user_agent_split)
            print("-" * (click.get_terminal_size()[0] - 1))
            print("\n")
        return user_agent, user_agent_split

class parser(parserheader):

    headers = ""

    def __init__(self, headers = None):
        self.headers = headers

    @classmethod
    def parser(self, *args, **kwargs):
        if hasattr(self, 'headers'):
            return self.parserHeader(self.headers, *args, **kwargs)
        return self.parserHeader(*args, **kwargs)

if __name__ == '__main__':
    
    import sys
    if len(sys.argv) == 1:
        click.secho("Example Get Input Data headers string:", fg='black', bg='cyan')
        example_header = """
        Host: ''
        Connection: keep-alive
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
        Referer: ''
        Accept-Encoding: gzip, deflate
        Accept-Language: en-US,en;q=0.9
        Cookie: ''
    """
        click.secho("Example Output Dictionary Headers:", fg='white', bg='magenta')
        c = parserheader()
        print(c.parserHeader())
        c.setCookies(None)
        c.UserAgent(example_header)
        sys.exit(0)
    data = ''
    try:
        import clipboard
        data = clipboard.paste()
    except:
        try:
            data = sys.argv[1]
        except:
            pass
    try:
        data = sys.argv[1]
    except:
        pass
    
    headers = c.parserHeader(data)
    print(headers)
    import traceback
    try:
        clipboard.copy(str(headers))
    except:
        print(traceback.format_exc())