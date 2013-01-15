from tests import ParserTestCase
from pijnu import makeParser

class RegexpTest(ParserTestCase):
    """Tests for custom transformation functions"""

    def test_choice_regex(self):
        """Make sure the Choice-optimize-as-Regexp works"""
        numbers_transform_grammar = """\
test_choice_regex
<toolset>
def to_int(node):
    node.value = int(node.value)
<definition>
    SEP            : ' '                        : drop
    digit          : [0..4] / [5..9]            : liftNode
    integer        : digit+                     : join
    number         : integer                    : to_int
    addedNumber    : SEP number                 : liftNode
    numbers        : number (addedNumber)*      : extract
"""
        make_parser = makeParser(numbers_transform_grammar)
        parser = make_parser()
        source = "12 3 5"
        result = "[number:'12'  number:'3'  number:'5']"
        self.assertEquals(unicode(parser.parseTest(source).value), result)

    def test_choice_regex2(self):
        """Make sure the Choice-optimize-as-Regexp works"""
        numbers_transform_grammar = """\
test_choice_regex
<toolset>
def to_int(node):
    node.value = int(node.value)
<definition>
    SEP            : ' '                        : drop
    digit          : [0..4] / [5..9]            : liftNode
    integer        : digit+                     : join
    number         : integer                    : to_int
    addedNumber    : SEP number                 : liftNode
    numbers        : number (addedNumber)*      : extract
"""
        make_parser = makeParser(numbers_transform_grammar)
        parser = make_parser()
        source = "129 3 5"
        result = "[number:'129'  number:'3'  number:'5']"
        self.assertEquals(unicode(parser.parseTest(source).value), result)
