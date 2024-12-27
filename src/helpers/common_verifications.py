def verification_by_status_code(response_data, expected_data):
    assert response_data == expected_data


def verification_json_key_notnull(key):
    assert key != 0, "Failed - Key should not be empty" + key
    assert key > 0, "Failed - Key should be greater than zero"

def verify_key_is_not_none(key):
    assert key is not None
