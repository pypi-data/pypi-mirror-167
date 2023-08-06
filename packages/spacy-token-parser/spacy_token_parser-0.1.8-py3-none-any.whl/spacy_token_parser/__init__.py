from .dmo import *
from .svc import *
from .dto import *

from .svc.parse_input_tokens import ParseInputTokens

__parse = ParseInputTokens().process


def parse_tokens(tokens: list) -> tuple:
    return __parse(tokens)
