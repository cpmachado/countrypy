# See LICENSE for details
"""
    Define main program, which runs command based in cli args
"""
import argparse
import json
from countrypy.request import get_countries_base


def main() -> None:
    """
        Main countrypy program
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd', type=str, help="command")
    parser.add_argument('--arg', type=str, default="Portugal")
    args = parser.parse_args()
    list_of_cmds = [
        'all',
        'name',
        'fullname',
        'code',
        'codes',
        'currency',
        'language',
        'capital',
        'calling_code',
        'region',
        'region_bloc'
    ]

    if args.cmd not in list_of_cmds:
        print(f'{args.cmd} doesn\' exist')
        print(f'{list_of_cmds}')
        return

    if args.cmd == 'all':
        obj = get_countries_base()
    elif args.cmd == 'name':
        obj = get_countries_base(f'name/{args.arg}')
    elif args.cmd == 'fullname':
        obj = get_countries_base(f'name/{args.arg}?fullText=true')
    elif args.cmd == 'code':
        obj = get_countries_base(f'alpha/{args.arg}')
    elif args.cmd == 'codes':
        obj = get_countries_base(f'alpha?codes={args.arg}')
    elif args.cmd == 'currency':
        obj = get_countries_base(f'currency/{args.arg}')
    elif args.cmd == 'language':
        obj = get_countries_base(f'lang/{args.arg}')
    elif args.cmd == 'capital':
        obj = get_countries_base(f'capital/{args.arg}')
    elif args.cmd == 'calling_code':
        obj = get_countries_base(f'callingcode/{args.arg}')
    elif args.cmd == 'region':
        obj = get_countries_base(f'region/{args.arg}')
    elif args.cmd == 'region_bloc':
        obj = get_countries_base(f'regionalbloc/{args.arg}')




    print(json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False))

if __name__ == '__main__':
    main()
