from command_parser.cd_parser import cd_parser
from command_parser.ls_parser import ls_parser
from command_parser.get_parser import get_parser
from command_parser.rsync_parser import rsync_parser
from command_parser.bash_parser import argsplit


def parser(unsplit_args):
    split = argsplit(unsplit_args)
    program = split[0]
    unparsed_args = split[1:]
    if program == 'ls':
        args = vars(ls_parser.parse_args(unparsed_args))
    elif program == 'cd':
        if len(unparsed_args) > 1:
            unparsed_args = [' '.join(unparsed_args)]
        args = vars(cd_parser.parse_args(unparsed_args))
    elif program == 'get':
        args = vars(get_parser.parse_args(unparsed_args))
    elif program == 'rsync':
        for var in unparsed_args:
            # Workaround to remove e. from functions
            if var[:1] == '-' and var[1:2] != '-':
                if 'e.' in var:
                    fixed_argument = var.replace('e.', '')
                    unparsed_args[unparsed_args.index(var)] = fixed_argument

        args = vars(rsync_parser.parse_args(unparsed_args))
    else:
        args = {}
    return (program, args)
