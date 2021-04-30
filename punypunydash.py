import weechat
import re


def _puny_to_utf8(match: re.Match):
    return match.group(0).encode('utf8').decode('idna')


def puny_decode(data, modifier, modifier_data, string):
    return re.sub(r'xn--[a-zA-Z0-9-]+', _puny_to_utf8, string)


if __name__ == '__main__':
    weechat.register('punypunydash', 'tokoyami', '1', 'MIT',
                     'Decodes punycode-encoded strings', '', '')
    hook = weechat.hook_modifier('9999|weechat_print', 'puny_decode', '')
