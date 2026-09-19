from slug import slugify

def test_slugify_lowercase_letters():
    assert slugify("Hello World") == "hello-world"

def test_slugify_strip_whitespace():
    assert slugify("   Hello World   ") == "hello-world"

def test_slugify_replace_spaces():
    assert slugify("Hello World") == "hello-world"