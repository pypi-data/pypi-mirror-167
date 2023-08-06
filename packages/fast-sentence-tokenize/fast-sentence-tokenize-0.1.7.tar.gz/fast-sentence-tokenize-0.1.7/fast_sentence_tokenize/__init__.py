from .bp import *
from .svc import *
from .dmo import *


from baseblock import Enforcer
from .bp.tokenizer import Tokenizer

__tok = Tokenizer().input_text


def tokenize_text(input_text: str,
                  eliminate_whitespace: bool = True) -> list:
    """ Tokenize Input Text

    Args:
        input_text (str): any input string of any length
        eliminate_whitespace (bool, optional): strip whitespace from tokens. Defaults to True.

    Returns:
        list: a list of tokens
    """

    Enforcer.is_str(input_text)

    tokens = __tok(input_text)

    Enforcer.is_list_of_str(tokens)

    if eliminate_whitespace:
        ## ---------------------------------------------------------- ##
        # Note:         Eliminate Trailing Whitespace for accurate dependency parsing
        # Reference:    https://github.com/craigtrim/fast-sentence-tokenize/issues/4#issuecomment-1236220669
        ## ---------------------------------------------------------- ##
        tokens = [x.strip() for x in tokens]
        tokens = [x for x in tokens if x and len(x)]

    return tokens
