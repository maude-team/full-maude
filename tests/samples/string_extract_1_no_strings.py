#  We look for outputs of the form "104"
#  We are having problems with strings, for themoment we look for @104@

import re


def select_text(s):
    p = re.compile("@(.*)@")  # result:  "\"(.*)\""
    result = p.search(s)
    if result:
        return result.group(1)
    else:
        # return "not found"
        raise Exception("not found")


print(select_text("rewrites: 11 in 0ms cpu (2ms real) (13750 rewrites/second)\nresult Configuration: <> signaledProcess(me, process(32943)) < me : User |\n    state: 6,process: process(32943),result: @104@ > exited(me, process(32943),\n    terminatedBySignal(\"SIGTERM\"))\n"))
