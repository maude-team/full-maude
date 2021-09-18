# from the Maude Manual
# by the Maude team
# the select_text function takes two arguments, a text and a regular expression
# to search occurrences of the given pattern in the text given as first argument


import re


def select_text(s, p):
    result = re.compile(p).search(s)
    if result:
        return result.group(1)
    else:
        raise Exception("not found")


#  print(select_text("rewrites: 11 in 0ms cpu (2ms real) (14030 rewrites/second)\nresult Configuration: <> signaledProcess(me, process(63900)) < me : User |\n    state: 6,process: process(63900),result: \"104\" > exited(me, process(63900),\n    terminatedBySignal(\"SIGTERM\"))\n"), "result: \"([^\"]*)\"")
