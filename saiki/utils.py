import hashlib

COLOR_LIST = [
    ('#A13D63', 'white', '#ffffff', '#ced4da'),
    ('#34113F', 'white', '#ffffff', '#ced4da'),
    ('#AD8A64', 'white', '#ffffff', '#ced4da'),
    ('#FDFDFF', 'default', '#212529', '#50566c'),
    ('#86E7B8', 'default', '#212529', '#50566c'),
    ('#9E2A2B', 'white', '#ffffff', '#ced4da'),
    ('#335C67', 'white', '#ffffff', '#ced4da'),
    ('#011936', 'white', '#ffffff', '#ced4da'),
    ('#9FC490', 'default', '#ffffff', '#e7efe9'),
    ('#B0413E', 'white', '#ffffff', '#ced4da'),
    ('#FBD87F', 'default', '#212529', '#50566c'),
    ('#424651', 'white', '#ffffff', '#ced4da'),
    ('#457B9D', 'white', '#ffffff', '#ced4da'),
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