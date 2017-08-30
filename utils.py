def prefix_format(code):
    instr, *args = code
    if instr == 'assign':
        return f'{args[1]}: {prefix_format(args[0])}'
    elif instr == 'call':
        _args = ', '.join(map(prefix_format, args[1]))
        return f'{prefix_format(args[0])}({_args})'
    elif instr == 'literal':
        if type(args[0]) in (list, set):
            _args = ', '.join(map(prefix_format, args[0]))
            _sep = {
                list: '[]',
                set: '{}',
            }[type(args[0])]
            return f'{_sep[0]}{_args}{_sep[1]}'
        return f'{args[0]}'
    elif instr == 'name':
        return args[0]
    # elif instr == 'conditional':
    #     for condition, expression in zip(args[0], args[1]):
    #         if eval_bytecode(condition):
    #             return eval_bytecode(expression)