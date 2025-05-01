from {{ cookiecutter.project_slug }}.dummy import dump_func


def test_dump_func():
    a = dump_func(2)
    assert a == 2 + 2
