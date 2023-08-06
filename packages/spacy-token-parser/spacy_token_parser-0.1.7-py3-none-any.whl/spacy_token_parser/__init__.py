from .dmo import *
from .svc import *
from .dto import *

from .svc.parse_input_tokens import ParseInputTokens
from .svc.simplify_parse_result import SimplifyParseResult

__parse = ParseInputTokens().process
__simplify = SimplifyParseResult().process


def parse_tokens(tokens: list) -> tuple:
    return __parse(tokens)


def simplify_results(results: list) -> list:
    return __simplify(results)
