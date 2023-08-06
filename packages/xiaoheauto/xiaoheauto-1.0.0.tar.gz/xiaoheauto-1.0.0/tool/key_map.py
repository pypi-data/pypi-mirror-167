from tool.jsonpath_tool import json_excutor, get_var, set_var, assert_contains, assert_json
from tool.key_tools import random_str, random_int, phone

key_mps={
    "RANDOM_STR": random_str,
    "RANDOM_INT": random_int,
    "PHONE": phone,
    "JSON_EXCUTOR": json_excutor,
    "GET_VAR": get_var,
    "SET_VAR": set_var,
    "ASSERT_CONTAINS": assert_contains,
    "ASSERT_JSON": assert_json,
}