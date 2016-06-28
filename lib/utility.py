'''
Created on June 28, 2016

@summary: some utilities in the system.
@author: Jay <smile665@gmail.com>
'''
security_key = 'hello'


def save_file(src_f, dest_f_path):
    ''' save file to a destination file path. '''
    with open(dest_f_path, 'wb') as f:
        for chunk in src_f.chunks():
            f.write(chunk)
    return dest_f_path


def key_validation(key):
    ''' validate the key used by the clients. '''
    ret = False
    if key.lower() == security_key:
        ret = True
    else:
        ret = False
    return ret


if __name__ == '__main__':
    print key_validation('haha')
    print key_validation(security_key)
