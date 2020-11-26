import hashlib

COLOR_LIST = [
    ('#A13D63', 'white', '#ffffff'),
    ('#34113F', 'white', '#ffffff'),
    ('#AD8A64', 'white', '#ffffff'),
    ('#FDFDFF', 'default', '#000000'),
    ('#86E7B8', 'default', '#000000'),
    ('#9E2A2B', 'white', '#ffffff'),
    ('#335C67', 'white', '#ffffff'),
    ('#011936', 'white', '#ffffff'),
    ('#9FC490', 'default', '#000000'),
    ('#B0413E', 'white', '#ffffff'),
    ('#FBD87F', 'default', '#000000'),
    ('#424651', 'white', '#ffffff'),
    ('#457B9D', 'white', '#ffffff'),
]


def get_site_title(title=None):
    if title:
        return f'{title} | Saiki'
    else:
        return 'Saiki'

def get_course_color(text):
    hex_hash = hashlib.sha1(text.encode('utf-8')).hexdigest()
    int_hash = int(hex_hash, 16)
    return COLOR_LIST[int_hash % len(COLOR_LIST)]