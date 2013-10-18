import os
import random


from django.conf import settings


def get_randomized_file_name(filename):
    """ Return a randomized file name for
    storage in our system.
    """
    num1 = str(random.randint(0, 1000000))
    num2 = str(random.randint(1001, 9000000))

    ext = os.path.splitext(filename)[1]
    return str(num1 + num2) + ext


def convert_bytes(bytes):
    """ @todo - Add Comments
        """
    bytes = float(bytes)
    if bytes >= 1099511627776:
        terabytes = bytes / 1099511627776
        size = '%.2fT' % terabytes
    elif bytes >= 1073741824:
        gigabytes = bytes / 1073741824
        size = '%.2fG' % gigabytes
    elif bytes >= 1048576:
        megabytes = bytes / 1048576
        size = '%.2fM' % megabytes
    elif bytes >= 1024:
        kilobytes = bytes / 1024
        size = '%.2fK' % kilobytes
    else:
        size = '%.2fb' % bytes
    return size


def get_size(start_path = '%s/images' % settings.MEDIA_ROOT):
    """ @todo - Add Comments
        """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size