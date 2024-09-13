

def bold(string):
    string = str(string)
    string = "\33[1m" + string + "\33[m"
    return string

def italic(string):
    string = str(string)
    string = "\33[3m" + string + "\33[m"
    return string

def underline(string):
    string = str(string)
    string = "\33[4m" + string + "\33[m"
    return string

def strikethrough(string):
    string = str(string)
    string = "\33[9m" + string + "\33[m"
    return string

def invisible(string):
    string = str(string)
    string = "\33[8m" + string + "\33[m"
    return string

def overline(string):
    string = str(string)
    string = "\33[53m" + string + "\33[m"
    return string

def double_underline(string):
    string = str(string)
    string = "\33[21m" + string + "\33[m"
    return string

def no_formatting(string):
    string = str(string)
    string = "\33[0m" + string + "\33[m"
    return string

def blink(string):
    string = str(string)
    string = "\33[5m" + string + "\33[m"
    return string

def rapid_blink(string):
    string = str(string)
    string = "\33[6m" + string + "\33[m"
    return string

def reverse_video(string):
    string = str(string)
    string = "\33[7m" + string + "\33[m"
    return string


def concealed(string):
    string = str(string)
    string = "\33[8m" + string + "\33[m"
    return string

def crossed_out(string):
    string = str(string)
    string = "\33[9m" + string + "\33[m"
    return string

def doubly_underlined(string):
    string = str(string)
    string = "\33[21m" + string + "\33[m"
    return string

def framed(string):
    string = str(string)
    string = "\33[51m" + string + "\33[m"
    return string

def encircled(string):
    string = str(string)
    string = "\33[52m" + string + "\33[m"
    return string

def overlined(string):
    string = str(string)
    string = "\33[53m" + string + "\33[m"
    return string

def hidden(string):
    string = str(string)
    string = "\33[8m" + string + "\33[m"
    return string

def ideogram_underline(string):
    string = str(string)
    string = "\33[60m" + string + "\33[m"
    return string

def ideogram_double_underline(string):
    string = str(string)
    string = "\33[61m" + string + "\33[m"
    return string

def ideogram_overline(string):
    string = str(string)
    string = "\33[62m" + string + "\33[m"
    return string

def ideogram_strikethrough(string):
    string = str(string)
    string = "\33[63m" + string + "\33[m"
    return string

def superscript(string):
    string = str(string)
    string = "\33[73m" + string + "\33[m"
    return string

def subscript(string):
    string = str(string)
    string = "\33[74m" + string + "\33[m"
    return string
