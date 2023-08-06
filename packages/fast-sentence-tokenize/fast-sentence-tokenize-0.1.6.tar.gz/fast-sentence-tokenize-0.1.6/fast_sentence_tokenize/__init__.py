from .bp import *
from .svc import *
from .dmo import *


from baseblock import Enforcer
from .bp.tokenizer import Tokenizer

__tok = Tokenizer().input_text


def tokenize_text(input_text: str) -> list:

    Enforcer.is_str(input_text)

    tokens = __tok(input_text)

    Enforcer.is_list_of_str(tokens)

    return tokens
