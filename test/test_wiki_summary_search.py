# test_wiki_summary_search.py
import sys
import wikipedia
from main import WikiSummarySearch

def test_format_error_response_PageError():
    wiki = WikiSummarySearch()
    ex_type = wikipedia.exceptions.PageError
    ex_response = "PageError: 'test_page' does not match any pages."
    result = wiki.format_error_response(ex_type, ex_response)
    assert result == {
        "Status": "NotFound",
        "Response": "PageError: 'test_page' does not match any pages."
    }

def test_format_error_response_DisambiguationError():
    wiki = WikiSummarySearch()
    ex_type = wikipedia.exceptions.DisambiguationError
    ex_response = "DisambiguationError: 'test_page' may refer to:\n- Test Page 1\n- Test Page 2\n- Test Page 3"
    result = wiki.format_error_response(ex_type, ex_response)
    assert result == {
        "Status": "NotFoundWithSuggestions",
        "Response": ["- Test Page 1", "- Test Page 2", "- Test Page 3"]
    }

def test_get_summary_empty_value():
    wiki = WikiSummarySearch()
    result = wiki.get_summary('')
    print(result)
    assert result == {
        "Status": "Error",
        "Response": "Please provide a search value"
    }

def test_get_summary_valid_value(mocker):
    wiki = WikiSummarySearch()

    mocker.patch.object(wiki.wiki, 'summary', return_value='Valid term summary.')
    result = wiki.get_summary('valid_term')
    assert result == {
        "Status": "Success",
        "Response": "Valid term summary."
    }

def test_get_summary_page_error(mocker):
    wiki = WikiSummarySearch()

    mocker.patch.object(wiki.wiki, 'summary', side_effect=wikipedia.exceptions.PageError('test_page'))
    result = wiki.get_summary('invalid_term')
    assert result == {
        "Status": "NotFound",
        "Response": "Term not found."
    }

def test_get_summary_disambiguation_error(mocker):
    wiki = WikiSummarySearch()

    mocker.patch.object(
        wiki.wiki,
        'summary',
        side_effect=wikipedia.exceptions.DisambiguationError(
            'test_page',
            ['Test Page 1', 'Test Page 2', 'Test Page 3']
        )
    )
    result = wiki.get_summary('ambiguous_term')
    assert result == {
        "Status": "NotFound",
        "Response": "Term not found."
    }
