import pytest # type: ignore
from string_processor import StringProcessor

@pytest.mark.parametrize( 'text_start, text_finish', [
    ('привет меня зовут серёга', 'Привет меня зовут серёга.'), 
    ('what are you doing now?', 'What are you doing now?.'), 
    ('its awesome', 'Its awesome.'), 
    ('Just test.', 'Just test.'),
    ('', '.'),
    ('    ', '    .'),
    (0, '.'),
    (None, '.'),
    ('1', '1.')
    ]
    )

def test_string_remake(text_start, text_finish):
    processor  = StringProcessor()
    assert processor.process(text_start) == text_finish