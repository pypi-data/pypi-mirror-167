"""
Strip JSON comments while keeping the line/column positions of JSON text intact.

Author: Vlado Potisk
License: MIT
Project homepage: https://github.com/xitop/jsonstrip
"""

import enum

__all__ = ['strip']

State = enum.Enum('State',
    'JSON STRING ESCAPE SLASH SL_COMMENT ML_COMMENT ML_COMMENT_END')
Cmd = enum.Enum('Cmd',
    'FLUSH ECHO BLANK START')
DEFAULT = None  # anything but a valid char
NOOP = ()

TRANS = {
    State.JSON: {
        '/': (State.SLASH,),
        '"': (State.STRING,),
    },
    State.STRING: {
        '\\': (State.ESCAPE,),
        '"': (State.JSON,),
    },
    State.ESCAPE: {
        DEFAULT: (State.STRING,),
    },
    State.SLASH: {
        '/': (State.SL_COMMENT, Cmd.FLUSH),
        '*': (State.ML_COMMENT, Cmd.FLUSH),
        DEFAULT: (State.JSON,),
    },
    State.SL_COMMENT: {
        '\r': (State.JSON, Cmd.ECHO, Cmd.START),
        '\n': (State.JSON, Cmd.ECHO, Cmd.START),
    },
    State.ML_COMMENT: {
        '\r': (Cmd.ECHO, Cmd.START),
        '\n': (Cmd.ECHO, Cmd.START),
        '*': (State.ML_COMMENT_END,),
    },
    State.ML_COMMENT_END: {
        '/': (State.JSON, Cmd.BLANK, Cmd.START),
        '*': NOOP,
        DEFAULT: (State.ML_COMMENT,),
    },
}

def strip(json_str: str) -> str:
    """
    Remove /* multi-line comments */ and // single-line comments.

    Add whitespace where necessary to keep the text position
    (i.e. line/column numbers) unchanged.
    """
    result = []
    pos = 0
    state = State.JSON
    for i, ch in enumerate(json_str):
        trans = TRANS[state]
        try:
            new = trans[ch]
        except KeyError:
            new = trans.get(DEFAULT, NOOP)
        for n in new:
            if isinstance(n, State):
                state = n
            elif n is Cmd.ECHO:
                result.append(ch)
            elif n is Cmd.START:
                pos = i + 1
            elif n is Cmd.FLUSH:
                result.append(json_str[pos:i-1])
                pos = i - 1
            elif n is Cmd.BLANK:
                result.append(' ' * (i - pos + 1))
    if state not in {State.SL_COMMENT, State.ML_COMMENT, State.ML_COMMENT_END}:
        result.append(json_str[pos:])
    return "".join(result)


if __name__ == "__main__":
    import sys
    print(strip(sys.stdin.read()), end="")
