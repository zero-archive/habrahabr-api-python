# -*- coding: utf-8 -*-


def accepts(*types):
    def check_accepts(f):
        # don't forget self
        assert 1 + len(types) == f.func_code.co_argcount

        def fn(*args, **kwargs):
            for (a, t) in zip(args[1:], types):
                assert isinstance(a, t), "Arg %r does not match %s" % (a, t)
            return f(*args, **kwargs)

        return fn

    return check_accepts
