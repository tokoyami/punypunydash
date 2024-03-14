import weechat
import re


def _puny_to_utf8(match: re.Match) -> str:
    return match.group(0).encode('utf8').decode('idna')


def puny_decode(data: str) -> str:
    return re.sub(r'xn--[a-zA-Z0-9-]+', _puny_to_utf8, data)


def puny_decode_line_cb(data: str, line: dict[str, str]) -> dict[str, str]:
    result = dict()
    for key in ['prefix', 'message']:
        if key in line:
            result[key] = puny_decode(line[key])
    return result


if __name__ == '__main__':
    weechat.register('punypunydash', 'tokoyami', '1', 'MIT',
                     'Decodes punycode-encoded strings', '', '')
    weechat.hook_line('', '', '', 'puny_decode_line_cb', '')
