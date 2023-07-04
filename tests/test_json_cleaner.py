from src.json_cleaner import JSONCleaner


def test_json_cleaner_should_return_clean_json_if_correct_input_provided():
    # Given
    dirty_json = '{"name": "John Doe", "email": "john.doe@example.com"}'
    regular_expressions = {
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b': '[REDACTED EMAIL]'
    }

    # When
    json_cleaner = JSONCleaner(dirty_json, regular_expressions)

    # Then
    expected_result = '{"name": "John Doe", "email": "[REDACTED EMAIL]"}'
    assert json_cleaner.clean_json() == expected_result
