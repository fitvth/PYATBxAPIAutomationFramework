# common verification

# HTTP status code
# headers
# data verification
# JSON schema

def verify_http_status_code(response_data,expected_data):
    assert response_data.statuscode==expected_data, "Failed to match status code"

def verify_key(key,expected_data):
    assert key == expected_data, "Failed to match key"

def verify_json_key_not_null(key):
    assert key!=0, "Failed key is null"

def verify_json_key_greater_than_zero(key):
    assert key>0, "Failed key is not >0"

