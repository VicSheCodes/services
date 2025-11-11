import pytest

path1 = "/home/user/Documents/../Pictures"
expected1 = "/home/user/Pictures"

path2 =  "/home//foo/"
expected2 = "/home/foo"

path3 = "/.../a/../b/c/../d/./"
expected = "/.../b/d"

@pytest.mark.parametrize("path, expected",
                         [(path1, expected1),
                          (path2, expected2),
                          (path3, expected)])
def test_simplify_path(path, expected):
    stack = []
    segments = path.split("/")

    for segment in segments:
        if segment == "..":
            if stack:
                stack.pop()
        elif segment == "." or segment =="":
            continue
        else:
            stack.append(segment)

    result = "/" + "/".join(stack)
    print(result)
    assert result == expected
