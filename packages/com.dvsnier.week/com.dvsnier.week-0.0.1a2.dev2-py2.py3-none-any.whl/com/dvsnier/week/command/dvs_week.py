# -*- coding:utf-8 -*-

import argparse
import copy
import json
import os
import sys

from com.dvsnier.config.journal.compat_logging import logging
from com.dvsnier.week import DEBUGGER, ENVIRONMENT_VARIABLE_CONFIGURATION, VERSIONS
from com.dvsnier.week.summary import Summary
from com.dvsnier.week.util.dvs_logging import LOGGING
# from datetime import datetime


def execute(args=None):
    '''
        the execute command

        it is that reference link:

            1. https://docs.python.org/zh-cn/3/library/argparse.html
            2. https://docs.python.org/zh-cn/2/library/argparse.html
    '''
    if args is None:
        args = sys.argv[1:]
    # LOGGING.set_logging()
    parser = argparse.ArgumentParser(
        prog='dvs-week',
        description="""
    this is a dvs week execution program.

        program one step: the update or synchronization local git repository

            the Notice:

                1. the only absolute path fields are supported

                    target_absolute_list = ['/User/.../xxx', '/User/.../yyy', '/User/.../zzz']

                2. the custom exclusion lists are currently supported

                    exclude_list = ['...', '...']

                3. the is associate remote are currently supported

                    iar = False

                4. the uslgr are currently supported

                    uslgr = True

        program two step: the recent specific range branch list

            the Notice:

                1. the dest-project are currently supported

                    dest-project = ...

                2. the dict are currently supported

                    - kwargs is dict {
                        'since' : '2021-07-01',
                        'until' : '2021-07-31',
                        'latest-month' : [1-12],
                        'latest-week' : [1-4],
                        'flags' : [0|1|2|3]
                      }

                    the please notice:

                        - The kwargs{since, until} and kwargs{latest_month, latest_week} are mutually exclusive options;
                        - since and until that both must exist at the same time
                        - (since, until) and latest_month and latest_week parameters,
                          All three are optional, but you must choose one of them.

                3. the email ssl config file are currently supported

                    email-ssl-config-file = ...

                4. the rsrbl are currently supported

                    rsrbl = True

        program three step: the statistical summary commit recorder information


                1. the destination project list are currently supported

                    dest-project-list = ['/User/.../xxx', '/User/.../yyy', '/User/.../zzz']

                2. the since are currently supported

                    since = '2021-07-01'

                3. the until are currently supported

                    until = '2021-07-31'

                4. the flags are currently supported

                    flags = [0|1|2|3]

                    the please notice:

                        - 0: remotes
                        - 1: locals
                        - 2: locals and specific range
                        - 3: remotes and specific range

                5. the email ssl config file are currently supported

                    email-ssl-config-file = ...

                6. the note-flavor are currently supported

                    note-flavor = [d, w, m, y]

                7. the s2 are currently supported

                    s2 = True
        """,
        epilog='the copyright belongs to DovSnier that reserve the right of final interpretation.\n',
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-V', '--version', action='version', version=VERSIONS, help='the show version and exit.')
    parser.add_argument(
        '-cp',
        '--current-project',
        action='store',
        nargs=1,
        default=os.getcwd(),
        type=str,
        metavar='current-project',
        # dest='current_project',
        help='the dvs current project property.')
    parser.add_argument(
        '-pp',
        '--project-prefix',
        action='store',
        nargs=1,
        default=os.getcwd(),
        type=str,
        metavar='project-prefix',
        # dest='project_prefix',
        help='the dvs project prefix property.')
    parser.add_argument(
        '-dp',
        '--dest-project',
        action='store',
        nargs='?',
        default=None,
        type=str,
        metavar='dest-project',
        # dest='dest_project',
        help='the dest project property.')
    parser.add_argument('-dpl',
                        '--dest-project-list',
                        action='store',
                        nargs='+',
                        default=None,
                        type=str,
                        metavar='dest-project-list',
                        dest='dest_project_list',
                        help='the dest project list property.')
    parser.add_argument('-pcl',
                        '--project-config-list',
                        action='store',
                        nargs='+',
                        default=None,
                        type=str,
                        metavar='project-config-list',
                        dest='project_config_list',
                        help='the project config list property.')
    parser.add_argument('-escf',
                        '--email-ssl-config-file',
                        action='store',
                        type=argparse.FileType('r'),
                        metavar='email-ssl-config-file',
                        dest='email_ssl_config_file',
                        help='the email ssl config file.')
    parser.add_argument('-nf',
                        '--note-flavor',
                        action='store',
                        default='w',
                        choices=[
                            'd',
                            'w',
                            'm',
                            'y',
                        ],
                        type=str,
                        metavar='note-flavor',
                        dest='note_flavor',
                        help='''
        The note flavor spatial range of the week can only be the following values:

        [d, w, m, y]

            and the default value is week.
        ''')
    parser.add_argument(
        '-s',
        '--since',
        action='store',
        # default=datetime.now().strftime('%Y-%m-%d'),
        default=None,
        type=str,
        metavar='since',
        # dest='since',
        help='the since property that is format with YY-mm-dd.')
    parser.add_argument(
        '-u',
        '--until',
        action='store',
        # default=datetime.now().strftime('%Y-%m-%d'),
        default=None,
        type=str,
        metavar='until',
        # dest='until',
        help='the until property that is format with YY-mm-dd.')
    parser.add_argument('-lm',
                        '--latest-month',
                        action='store',
                        nargs='?',
                        const='0',
                        default='0',
                        choices=[
                            '1',
                            '2',
                            '3',
                            '4',
                            '5',
                            '6',
                            '7',
                            '8',
                            '9',
                            '10',
                            '11',
                            '12',
                        ],
                        type=str,
                        metavar='latest-month',
                        dest='latest_month',
                        help='''
        The latest month spatial range of the week can only be the following values:

        [1, 12]

            and the default value is zero with no execute.
        ''')
    parser.add_argument('-lw',
                        '--latest-week',
                        action='store',
                        nargs='?',
                        const='0',
                        default='0',
                        choices=[
                            '1',
                            '2',
                            '3',
                            '4',
                        ],
                        type=str,
                        metavar='latest-week',
                        dest='latest_week',
                        help='''
        The latest week spatial range of the week can only be the following values:

        [1, 4]

            and the default value is zero with no execute.
        ''')
    parser.add_argument('-author',
                        '--author',
                        action='store',
                        nargs='?',
                        default=None,
                        type=str,
                        metavar='author',
                        dest='author',
                        help='the author property.')
    parser.add_argument('-authors',
                        '--authors',
                        action='store',
                        nargs='+',
                        default=None,
                        type=str,
                        metavar='authors',
                        dest='authors',
                        help='the authors property.')
    parser.add_argument(
        '-subject',
        '--subject',
        action='store',
        nargs=1,
        default=None,
        type=str,
        metavar='subject',
        # dest='subject',
        help='the subject property.')
    parser.add_argument('-f',
                        '--flags',
                        action='store',
                        default=0,
                        choices=[
                            0,
                            1,
                            2,
                            3,
                        ],
                        type=int,
                        metavar='flags',
                        dest='flags',
                        help='''
        The flags spatial range of the week can only be the following values:

        {0, 1, 2, 3} that is 0: remotes 1: locals 2: locals and specific range 3: remotes and specific range

            and the default value is zero.
        ''')
    parser.add_argument('-tal',
                        '--target-absolute-list',
                        action='store',
                        nargs='+',
                        default=None,
                        type=str,
                        metavar='target-absolute-list',
                        dest='target_absolute_list',
                        help='the target absolute list property.')
    parser.add_argument('-el',
                        '--exclude-list',
                        action='store',
                        nargs='*',
                        default=None,
                        type=str,
                        metavar='exclude-list',
                        dest='exclude_list',
                        help='the exclude list property.')
    parser.add_argument(
        '-iar',
        '--is-associate-remote',
        action='store_true',
        default=False,
        dest='iar',
        help='if iar == true, update or synchronization remote git repository, otherwise only local repository it.')
    parser.add_argument('-dr',
                        '--dry-run',
                        action='store_true',
                        default=False,
                        dest='dr',
                        help='if dr == true, the skip execute program, otherwise no it.')
    parser.add_argument('-uslgr',
                        '--update-or-synchronization-local-git-repository',
                        action='store_true',
                        default=False,
                        dest='uslgr',
                        help='if uslgr == true, update or synchronization local git repository, otherwise no it.')
    parser.add_argument('-rsrbl',
                        '--recent-specific-range-branch-list',
                        action='store_true',
                        default=False,
                        dest='rsrbl',
                        help='if rsrbl == true, recent specific range branch list, otherwise no it.')
    parser.add_argument('-s2',
                        '--statistical-summary',
                        action='store_true',
                        default=False,
                        dest='s2',
                        help='if s2 == true, do statistical summary data, otherwise no it.')
    args = parser.parse_args(args)
    run(args)


def run(args):
    ''' the run script command '''
    LOGGING.set_logging()
    if args:
        _cfg = {}
        if args.current_project:
            _cfg['current-project'] = args.current_project
        if args.project_prefix:
            _cfg['project-prefix'] = args.project_prefix
        if args.dest_project:
            _cfg['dest-project'] = args.dest_project
        if args.dest_project_list:
            _cfg['dest-project-list'] = args.dest_project_list
        if args.project_config_list:
            _cfg['project-config-list'] = args.project_config_list
        if args.since:
            _cfg['since'] = args.since
        if args.until:
            _cfg['until'] = args.until
        if args.latest_month:
            _cfg['latest_month'] = args.latest_month
        if args.latest_week:
            _cfg['latest_week'] = args.latest_week
        if args.author:
            _cfg['author'] = args.author
        if args.authors:
            _cfg['authors'] = args.authors
        if args.subject:
            _cfg['subject'] = args.subject
        if args.flags:
            _cfg['flags'] = args.flags
        if args.target_absolute_list:
            _cfg['target_absolute_list'] = args.target_absolute_list
        if args.exclude_list:
            _cfg['exclude_list'] = args.exclude_list
        if args.email_ssl_config_file:
            _cfg['email-ssl-config-file'] = args.email_ssl_config_file
        else:
            user = os.path.expanduser('~')
            dvs_rc = os.path.join(user, ENVIRONMENT_VARIABLE_CONFIGURATION)
            if os.path.exists(dvs_rc):
                args.email_ssl_config_file = dvs_rc
                _cfg['email-ssl-config-file'] = dvs_rc
                logging.info(
                    'the currently found user({}) environment variable definition configuration file.'.format(user))
        if args.note_flavor:
            _cfg['note-flavor'] = args.note_flavor
        if DEBUGGER:
            # print('vars(args): {}'.format(vars(args)))
            logging.warning('the current config(args): {}'.format(json.dumps(vars(args), indent=4)))
        summary = Summary(flags=(_cfg.get('flags', 0) == 0 or _cfg.get('flags', 0) == 3))  # type: Summary
        summary.cfg = _cfg
        if args.uslgr:
            _cfg['uslgr'] = args.uslgr
            if args.dr:
                pass
            else:
                summary.update_or_synchronization_local_git_repository(is_associate_remote=args.iar)
        if args.rsrbl:
            _cfg['rsrbl'] = args.rsrbl
            if args.dr:
                pass
            else:
                summary.recent_specific_range_branch_list(cfg=summary.cfg.get('email-ssl-config-file', ''))
        if args.s2:
            _cfg['s2'] = args.s2
            if args.dr:
                pass
            else:
                dpl = summary.cfg.get('dest-project-list', list())
                flags = summary.cfg.get('flags', 0)
                if dpl:
                    for index, dest_project in enumerate(dpl):
                        element_summary = Summary(flags=(flags == 0 or flags == 3))  # type: Summary
                        element_summary.cfg = copy.deepcopy(_cfg)
                        element_summary.cfg['index'] = index
                        element_summary.cfg['dest-project'] = dest_project
                        subject_flavor = ''
                        if 'd' == element_summary.cfg.get('note-flavor', 'w'):
                            subject_flavor = '工作日报'
                        elif 'm' == element_summary.cfg.get('note-flavor', 'w'):
                            subject_flavor = '工作月报'
                        elif 'y' == element_summary.cfg.get('note-flavor', 'w'):
                            subject_flavor = '工作年报'
                        else:
                            subject_flavor = '工作周报'
                        since_date = element_summary.cfg.get('since')
                        until_date = element_summary.cfg.get('until')
                        element_summary.cfg['subject'] = '{} -> {} {}'.format(since_date, until_date, subject_flavor)
                        element_summary.query(cli=True).send(cfg=element_summary.cfg.get('email-ssl-config-file', ''))


if __name__ == "__main__":
    '''the main function entry'''
    execute()
