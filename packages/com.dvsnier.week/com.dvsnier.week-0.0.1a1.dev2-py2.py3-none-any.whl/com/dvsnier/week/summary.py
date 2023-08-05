# -*- coding:utf-8 -*-

import json
import os
import pickle
import re
import time

from com.dvsnier.config.cfg.configuration import Configuration
from com.dvsnier.config.journal.compat_logging import logging
from com.dvsnier.directory.base_file import BaseFile
from com.dvsnier.email.email import Email
from com.dvsnier.git.git import Git
from com.dvsnier.process.execute import execute
from com.dvsnier.week.util.dvs_logging import LOGGING
from com.dvsnier.week.util.utils import calculate_complex_date, detransfer, find_git_repository
from datetime import date
from deprecated import deprecated


class Summary(object):
    '''the summary class'''

    basis_local_git_command = 'git branch --list --sort=-committerdate --format="%(objectname:short)|%(refname:short)|%(committerdate:format:%Y-%m-%d_%H:%M:%S)|%(subject)"'
    basis_remotes_git_command = 'git branch --list --remotes --sort=-committerdate --format="%(objectname:short)|%(refname:short)|%(committerdate:format:%Y-%m-%d_%H:%M:%S)|%(subject)"'
    cfg = None
    flags = True
    msgs = {}

    def __init__(self, flags=True, no_logging=True):
        super(Summary, self).__init__()
        self.flags = flags
        #
        # the config menu:
        #
        #   1. the configure log
        #   2. the configure directory
        #   3. the configure git log output
        #
        if not no_logging:
            LOGGING.set_logging(dvs_file_name='summary', dvs_logging_name='log')

        self.directory = BaseFile(True)
        self.git = Git()
        # self.git.config(output_dir_name='summary')

    def config(self, config):
        'the resolve local configuration list'
        parsing_configuration_start = time.time()
        self.cfg = Configuration().obtain_config(config)
        logging.debug('the current config is {}'.format(json.dumps(self.cfg, indent=4, ensure_ascii=False)))
        parsing_configuration_end = time.time()
        logging.info('the parsing configuration file complete, that total time consumed {:.3f} seconds '.format(
            parsing_configuration_end - parsing_configuration_start))
        return self.cfg

    def query(self, config=None, _on_callback=None, cli=False):
        'the Query git recently submitted list branch'
        if _on_callback:
            if config:
                self.cfg = _on_callback(config)
            else:
                self.cfg = _on_callback()
        else:
            if config:
                if isinstance(config, dict):
                    self.cfg = config
                elif isinstance(config, str):
                    self.cfg = self.config(config)
                elif cli:
                    pass
                else:
                    raise ValueError('the current {} is an illegal parameter.'.format('config'))
            elif cli:
                pass
            else:
                raise ValueError('the current {} is an illegal parameter.'.format('config'))
        if not self.cfg:
            raise ValueError('the current {} is an illegal parameter.'.format('cfg'))
        self.directory.set_work_region_space(self.cfg.get('project-prefix'))
        if self.cfg['dest-project']:
            dest_project = self.cfg['dest-project']
            if dest_project and os.path.exists(dest_project):
                self.directory.set_executed_region_space(dest_project)
                logging.warning('the current destination directory that is {} '.format(dest_project))
                os.chdir(dest_project)
                # Determine the current branch status and whether it is necessary to temporarily store the branch
                since_date, until_date = self.get_format_integrate_isodate()
                self.cfg['since_date'] = since_date
                self.cfg['until_date'] = until_date
                self.write_original_and_stash_git_branch()
                if self.flags:  # the remote nodes
                    logging.info('the start remote node data synchronization to local...')
                    remote_start = time.time()
                    self.query_remote_nodes()
                    remote_end = time.time()
                    logging.info(
                        'The remote data node synchronizes to the local data, and the task completion time is {:.3f} seconds'
                        .format((remote_end - remote_start)))
                else:  # the local nodes only
                    logging.info('the start executing local node data...')
                    local_start = time.time()
                    self.query_local_nodes()
                    local_end = time.time()
                    logging.info('The local node data, and the task completion time is {:.3f} seconds '.format(
                        (local_end - local_start)))
        else:
            raise ValueError('the current configuration dest-project parameter({}) dest project is invalid'.format(
                self.cfg['dest-project']))
        return self

    def query_remote_nodes(self):
        'the query remote nodes'
        execute(['git status -z -u'])
        execute(['git stash'])
        response_with_pull = execute(['git pull'])
        if response_with_pull and self.cfg:
            local_branch_list = self.get_local_branch_list()  # at the moment
            current_branch_queue = self.get_remotes_or_local_branch_list(
                **{
                    'since': self.cfg.get('since'),
                    'until': self.cfg.get('until'),
                    'latest_month': self.cfg.get('latest_month'),
                    'latest_week': self.cfg.get('latest_week'),
                    'flags': self.cfg.get('flags'),
                })
            if current_branch_queue:
                for index, branch_list_object in enumerate(current_branch_queue):
                    if branch_list_object and branch_list_object[1]:
                        branch_name = None
                        if branch_list_object[1].find('origin/') >= 0:  # the ref/origin/*
                            branch_list_object_with_split = branch_list_object[1].split('/', 1)
                            branch_name = branch_list_object_with_split[1]
                            if branch_name == 'HEAD':
                                continue
                            if branch_list_object_with_split and local_branch_list and local_branch_list.count(
                                    branch_name) > 0:
                                execute(['git checkout {}'.format(branch_name)])
                                execute(['git branch -u origin/{} {}'.format(branch_name, branch_name)])
                                execute(['git stash'])
                                logging.debug(
                                    'the current remote branch({}) to be switched already exists locally.'.format(
                                        branch_name))
                            else:
                                execute([
                                    'git checkout -b {} {}'.format(branch_list_object_with_split[1],
                                                                   branch_list_object[1])
                                ])
                                logging.debug(
                                    'the current switch to remote branch({}) and perform remote branch association operation.'
                                    .format(branch_list_object_with_split[1]))
                            execute(['git pull'])
                        else:  # the local branch
                            branch_name = branch_list_object[1]
                            execute(['git checkout {}'.format(branch_list_object[1])])
                            execute(['git stash'])
                            logging.warning('the current checkout locally branch name is {}'.format(
                                branch_list_object[1]))
                            execute(['git pull'])
                        if branch_name:
                            if branch_name in self.msgs:
                                logging.warning(
                                    'The current branch name({}) is already in the object being counted, this skip.'.
                                    format(branch_name))
                            else:
                                self.msgs[branch_name] = {}
                            # self.msgs[branch_name][self.cfg['author']] = self.get_current_branch_msg_queue_with_special_author(
                            #     self.cfg['author'])[1]
                            original_msg_queue = self.get_current_branch_original_msg_queue()
                            if original_msg_queue:
                                for msg_with_tuple in original_msg_queue:
                                    author = msg_with_tuple[0]
                                    msg = msg_with_tuple[1]
                                    if author in self.msgs[branch_name]:
                                        self.msgs[branch_name][author].append(msg)
                                    else:
                                        self.msgs[branch_name][author] = []
                                        self.msgs[branch_name][author].append(msg)
        return self.msgs

    def query_local_nodes(self):
        'the query local nodes'
        current_branch_queue = self.get_current_branch_list()
        if current_branch_queue and self.cfg:
            for index, branch_name in enumerate(current_branch_queue):
                execute(['git stash'])  # optional
                execute(['git branch -u origin/{} {}'.format(branch_name, branch_name)])
                response_with_pull = execute(['git pull'])
                if response_with_pull:
                    logging.warning('the current checkout locally branch name is {}'.format(branch_name))
                    execute(['git checkout {}'.format(branch_name)])
                    execute(['git pull'])
                    # There is no reliable pull merge conflict here
                    if branch_name in self.msgs:
                        logging.warning(
                            'The current branch name({}) is already in the object being counted, this skip.'.format(
                                branch_name))
                    else:
                        self.msgs[branch_name] = {}
                    # self.msgs[branch_name][self.cfg['author']] = self.get_current_branch_msg_queue_with_special_author(
                    #     self.cfg['author'])[1]
                    original_msg_queue = self.get_current_branch_original_msg_queue()
                    if original_msg_queue:
                        for msg_with_tuple in original_msg_queue:
                            author = msg_with_tuple[0]
                            msg = msg_with_tuple[1]
                            if author in self.msgs[branch_name]:
                                self.msgs[branch_name][author].append(msg)
                            else:
                                self.msgs[branch_name][author] = []
                                self.msgs[branch_name][author].append(msg)
        return self.msgs

    def get_remotes_or_local_branch_list(self, **kwargs):
        '''
            the current branch list

            - kwargs is dict {
                'since' : 2021-07-01,
                'until' : 2021-07-31,
                'latest_month' : [1-12],
                'latest_week' : [1-4],
                'flags' : [0|1|3]
              }

            the please notice:

            - The kwargs{since, until} and kwargs{latest_month, latest_week} are mutually exclusive options;
        '''
        since = None
        until = None
        latest_month = None
        latest_week = None
        branch_queue = []
        if kwargs:
            since = kwargs.get('since')
            until = kwargs.get('until')
            latest_month = kwargs.get('latest_month')
            latest_week = kwargs.get('latest_week')
            flags = kwargs.get('flags', 0)
            if since and until and latest_month and '0' != latest_month and latest_week and '0' != latest_week:
                raise NotImplementedError('This method is not supported at present, please choose one or two.')
            else:
                if latest_month and '0' != latest_month or latest_week and '0' != latest_week:
                    since_date, until_date = calculate_complex_date(latest_month, latest_week)
                    if since_date and since_date < until_date:
                        if isinstance(self.cfg, dict):
                            self.cfg['since'] = since_date
                            self.cfg['until'] = until_date
                        branch_queue = self.__get_branch_queue_with_origin(since_date, until_date, flags)
                    else:
                        raise ValueError('the since date cannot be greater than or equal to until date')
                elif since and until:
                    since_date = date.fromisoformat(since)
                    until_date = date.fromisoformat(until)
                    if since_date < until_date:
                        branch_queue = self.__get_branch_queue_with_origin(since_date, until_date, flags)
                    else:
                        raise ValueError('the since date cannot be greater than or equal to until date')
                else:
                    raise ValueError(
                        'The parameter set is invalid, please select the specified key(since, until, latest_month, latest_week).'
                    )
        if branch_queue and len(branch_queue) == 0:
            for i in range(3):
                logging.error(
                    'The branch queue currently retrieved is empty({}), that in the future, there is no need for business processes such as data collation and e-mail sending, Please readjust your configuration data items(since or until).'
                    .format(branch_queue))
        elif kwargs and kwargs.get('flags', 0) == 3:
            logging.debug('The branch queue currently retrieved is {}'.format(
                json.dumps(branch_queue, indent=4, ensure_ascii=False)))
            sub_branch_queue = []
            for item in branch_queue:
                sub_branch_queue.append(item[1])
            branch_queue = sub_branch_queue
        else:
            logging.debug('The branch queue currently retrieved is {}'.format(
                json.dumps(branch_queue, indent=4, ensure_ascii=False)))
        return branch_queue

    def __get_branch_queue_with_origin(self, since_date, until_date, flags):
        branch_queue = []
        branch_queue_with_origin = []
        branch_list_strs_with_many_equivocal = []
        if flags is None or flags == 0 or flags == 3:
            branch_list_strs_with_many_equivocal = execute([self.basis_remotes_git_command])
        else:
            branch_list_strs_with_many_equivocal = execute([self.basis_local_git_command])
        if branch_list_strs_with_many_equivocal:
            branch_list_strs_with_more_regular = branch_list_strs_with_many_equivocal.split('\n')
            if branch_list_strs_with_more_regular:
                # the branches information per line
                for branch_item_qualified_describe in branch_list_strs_with_more_regular:
                    elements_qualified_describe = branch_item_qualified_describe.split('|', maxsplit=3)
                    if elements_qualified_describe:
                        # ['b78cd7ad8', 'origin/dream_Test', '2019-12-11_17:08:43', '修改版本号']
                        # objectname
                        # refname
                        # committerdate
                        # subject
                        # logging.debug(elements_qualified_describe)
                        branch_queue_with_origin.append(elements_qualified_describe)
        if len(branch_queue_with_origin):
            for branch_queue_item in branch_queue_with_origin:
                timestamp_with_origin = branch_queue_item[2]
                if timestamp_with_origin:
                    timestamp_with_split = timestamp_with_origin.split('_', 1)
                    if timestamp_with_split:
                        branch_latest_date = date.fromisoformat(timestamp_with_split[0])
                        if flags == 3:  # Specific interval range
                            if branch_latest_date and since_date <= branch_latest_date and branch_latest_date <= until_date:
                                branch_queue.append(branch_queue_item)
                            else:
                                continue
                        else:
                            if branch_latest_date and since_date <= branch_latest_date:  # There is no need to enable strict mode
                                branch_queue.append(branch_queue_item)
                            else:
                                continue
                else:
                    continue
        return branch_queue

    def get_current_branch_list(self):
        'the current branch list'
        branch_queue = []
        branch_list_strs = execute(['git branch --list']).strip()
        if branch_list_strs:
            branch_list = branch_list_strs.split('\n')
            if branch_list:
                for branch in branch_list:
                    branch_element = branch.split(' ')
                    if branch_element:
                        branch_queue.append(branch_element[-1])
        return branch_queue

    @deprecated(version='0.0.1.dev1', reason="this method has been marked as deprecated.")
    def get_local_branch_list(self):
        branch_list = self.get_current_branch_list()
        logging.info(
            'At present, it is found that the existing branch list of the current project is {}'.format(branch_list))
        return branch_list

    def get_current_branch_original_msg_queue(self):
        'the current branch msg original msg queue'
        msgs = []
        if self.cfg:
            since, until = self.get_format_integrate_isodate()
            cmds = 'git log --oneline --pretty=format:"%an|%s" --since="{}" --until="{}" "HEAD"'.format(since, until)
            queue = execute([cmds])
            if queue:
                qs = queue.split('\n')
                for index, author_and_conntent in enumerate(qs):
                    author_and_conntent_split = author_and_conntent.split('|', 1)
                    if author_and_conntent_split:
                        value = (author_and_conntent_split[0], author_and_conntent_split[1])
                        logging.debug(value)
                        msgs.append(value)
        return msgs

    def get_current_branch_msg_queue_with_special_author(self, author):
        'the current branch msg queue with special author'
        msgs = []
        if self.cfg and author:
            since, until = self.get_format_integrate_isodate()
            cmds = 'git log --oneline --pretty=format:"%s" --since="{}" --until="{}" --author="{}" "HEAD"'.format(
                since, until, author)
            queue = execute([cmds])
            if queue:
                qs = queue.split('\n')
                for index, msg in enumerate(qs):
                    value = '{}'.format(str(index + 1) + '. ' + msg)
                    logging.debug(value)
                    msgs.append(value)
        else:
            raise ValueError('the currently given author({}) parameter is illegal.'.format(author))
        return (author, msgs)

    def get_summary_current_branch_msg_queue_with_basic_data_structure(self):
        '''
            the summarize the basic data structure under the current specified branch name

            the data structure:

            {
                'author_a': ['1. xyz', '2. xyz', ...'n. xyz'],
                'author_b': ['1. xyz', '2. xyz', ...'n. xyz'],
                    ...
                'author_n': ['1. xyz', '2. xyz', ...'n. xyz'],
            }

        '''
        data_structure = {}
        if self.cfg:
            authors = self.cfg.get('authors')
            if authors:
                for author in authors:
                    since, until = self.get_format_integrate_isodate()
                    cmds = 'git log --oneline --pretty=format:"%s" --since="{}" --until="{}" --author="{}" "HEAD"'.format(
                        since, until, author)
                    queue = execute([cmds])
                    msgs = []
                    if queue:
                        qs = queue.split('\n')
                        for index, msg in enumerate(qs):
                            value = '{}'.format(str(index + 1) + '. ' + msg)
                            logging.debug(value)
                            msgs.append(value)
                    data_structure[author] = msgs
            else:
                for i in range(3):
                    logging.warning(
                        'please note {}: the current authors list is not configured, skipping retrieval summary.'.
                        format(i + 1))
        return data_structure

    def get_summary_author_list(self):
        'get summary author list'
        authors = []
        if self.msgs:
            for branch_name in self.msgs:
                for author in self.msgs[branch_name]:
                    if author in authors:
                        continue
                    else:
                        authors.append(author)
        return authors

    def __exist_with_content_list(self, content_list, str_part_no_item):
        if content_list and str_part_no_item:
            for item in content_list:
                content_split = re.split(r'\s', item, 1)
                if content_split:
                    if content_split[1].find(str_part_no_item) > -1:
                        return True
        return False

    def get_format_integrate_isodate(self):
        'the get format integrate iso date()'
        since_date = None
        until_date = None
        if self.cfg:
            since_date = self.cfg.get('since')
            until_date = self.cfg.get('until')
            latest_month = self.cfg.get('latest_month')
            latest_week = self.cfg.get('latest_week')
            if latest_month and '0' != latest_month or latest_week and '0' != latest_week:
                since_date, until_date = calculate_complex_date(latest_month, latest_week)
        return (since_date, until_date)

    def get_report_format_ac_list(self):
        '''
            get report author-content with index list

            the format is described below:

                一. xxx:
                    1. ...
                    2. ...
                    3. ...
                    .
                    .
                    .
                    n. ...

                二. yyy
                    1. ...
                    2. ...
                    3. ...
                    .
                    .
                    .
                    n. ...

                三. ...
                .
                .
                .
        '''
        msgs = ''
        original_msgs = {}
        format_start = time.time()
        if self.msgs:
            logging.info('the start formatting tool output...')
            for index_with_branch, branch_name in enumerate(self.msgs):
                if branch_name:
                    for index, author in enumerate(self.msgs[branch_name]):
                        original_content_list = self.msgs[branch_name][author]
                        if original_content_list:
                            if author in original_msgs:
                                if original_msgs[author]['content']:
                                    for index_sustain, item in enumerate(original_content_list):
                                        if not self.__exist_with_content_list(original_msgs[author]['content'], item):
                                            value = '{}. '.format(int(len(original_msgs[author]['content']) + 1)) + item
                                            original_msgs[author]['content'].append(value)
                                else:
                                    # if msgs[author]['index'] != index_with_branch:
                                    #     msgs[author]['index'] = index_with_branch
                                    original_msgs[author]['index'] = len(original_msgs.keys()) - 1
                                    original_msgs[author]['count'] = len(original_content_list)
                                    original_msgs[author]['content'] = []
                                    for index_content, item in enumerate(original_content_list):
                                        if not self.__exist_with_content_list(original_msgs[author]['content'], item):
                                            value = '{}. '.format(int(len(original_msgs[author]['content']) + 1)) + item
                                            original_msgs[author]['content'].append(value)
                                original_msgs[author]['count'] = len(original_msgs[author]['content'])
                                continue
                            else:
                                original_msgs[author] = {}
                                original_msgs[author]['index'] = len(original_msgs.keys()) - 1
                                # msgs[author]['count'] = len(original_content_list)
                                original_msgs[author]['content'] = []
                                for index_content, item in enumerate(original_content_list):
                                    if not self.__exist_with_content_list(original_msgs[author]['content'], item):
                                        value = '{}. '.format(int(len(original_msgs[author]['content']) + 1)) + item
                                        original_msgs[author]['content'].append(value)
                                original_msgs[author]['count'] = len(original_msgs[author]['content'])
                                continue
                        else:
                            raise ValueError('Illegal data structure with author({}).'.format(author))
                else:
                    raise ValueError('Illegal data structure with branch_name({}).'.format(branch_name))
        if original_msgs:
            logging.debug('the current msgs strcture that is {}'.format(
                json.dumps(original_msgs, indent=4, ensure_ascii=False)))
            # msgs += '\n'
            for index, author in enumerate(original_msgs):
                if author:
                    item_with_author = original_msgs.get(author)
                    if item_with_author:
                        msgs += detransfer(item_with_author.get('index') + 1) + '. ' + author + ':\n'
                        contents = item_with_author.get('content')
                        if contents:
                            for content in contents:
                                msgs += '    ' + content + '\n'
        format_end = time.time()
        logging.info('It takes {:.3f} seconds to complete the output task of the format tool'.format(
            (format_end - format_start)))
        self.update_or_synchronization_original_git_branch()
        return msgs

    def recent_specific_range_branch_list(self, cfg='conf/email_ssl_config.cfg', **kwargs):
        ''' the recent specific range branch list '''
        if self.cfg:
            self.directory.set_work_region_space(self.cfg.get('project-prefix'))
            self.directory.set_executed_region_space(self.cfg['dest-project'])
            os.chdir(self.cfg['dest-project'])
            if kwargs:
                pass
            else:
                kwargs = {
                    'since': self.cfg.get('since'),
                    'until': self.cfg.get('until'),
                    'latest_month': self.cfg.get('latest_month'),
                    'latest_week': self.cfg.get('latest_week'),
                    'flags': self.cfg.get('flags'),
                }
            current_branch_queue = self.get_remotes_or_local_branch_list(**kwargs)
            value = json.dumps(current_branch_queue, indent=4, ensure_ascii=False)
            # logging.info(value)
            dest_project = self.cfg.get('dest-project')
            if dest_project:
                subject = '{} 项目: {} - {} 过期, 分支列表'.format(os.path.basename(dest_project), self.cfg.get('since'),
                                                           self.cfg.get('until'))
                # self.sendContent(subject, value, cfg, debug=True)
                self.sendContent(subject, value, cfg)

    def send_email(self, msgs, cfg):
        'the send mail'
        if msgs and self.cfg:
            os.chdir(self.cfg['current-project'])
            logging.warning('the current destination directory that is {}'.format(self.cfg['current-project']))
            email = Email()
            email.config_file(cfg).init(True)
            subject = self.cfg['subject']
            if subject:
                if re.findall(r'\{\w*\}', subject):
                    since_date = self.cfg['since_date']
                    until_date = self.cfg['until_date']
                    subject = subject.format(since_date, until_date)
                dest_project = self.cfg.get('dest-project')
                if dest_project and os.path.basename(dest_project):
                    subject = '{}: {}'.format(os.path.basename(dest_project), subject)
            logging.info('the current subject is [\'{}\']'.format(subject))
            email.builderText(subject, msgs)
            logging.debug('the current plain text data to be sent is \n{}'.format(msgs))
            email.sendmail().quit()

    def send(self, cfg='conf/email_ssl_config.cfg'):
        'the send default format data'
        if self.msgs and len(self.msgs) > 0:
            content = self.get_report_format_ac_list()
            if content:
                email_start = time.time()
                logging.info('the start mail sending task...')
                self.send_email(content, cfg)
                email_end = time.time()
                logging.info('The task of sending mail is completed, which takes {:.3f} seconds'.format(
                    (email_end - email_start)))

    def sendContent(self, subject, content, cfg='conf/email_ssl_config.cfg', debug=False):
        'the send custom data'
        if subject and content and self.cfg:
            email_start = time.time()
            logging.info('the start mail sending task...')
            os.chdir(self.cfg['current-project'])
            logging.warning('the current destination directory that is {}'.format(self.cfg['current-project']))
            if debug:
                logging.info('the current subject is [\'{}\']'.format(subject))
                logging.debug('the current plain text data to be sent is \n{}'.format(content))
            else:
                email = Email()
                email.config_file(cfg).init(True)
                email.builderText(subject, content)
                email.sendmail().quit()
            email_end = time.time()
            logging.info('The task of sending mail is completed, which takes {:.3f} seconds'.format(
                (email_end - email_start)))

    def update_or_synchronization_original_git_branch(self):
        '''
            Update or synchronize the original branch list,\
            so as to avoid the situation that a large number of local and remote branches are associated with each statistical data
        '''
        wrs = self.directory.get_work_region_space()
        if wrs and isinstance(wrs, str):
            pgs_file_name = os.path.join(wrs, 'out/python_git_statistics.pkl')
            original_branch_queue = pickle.load(open(pgs_file_name, 'rb'))
            logging.info('the currently load file directory is {} that load local branch list is {}'.format(
                pgs_file_name, original_branch_queue))
            current_branch_queue = self.get_current_branch_list()
            if current_branch_queue and original_branch_queue:
                execute(['git checkout {}'.format(original_branch_queue[0])])
                for branch_name in current_branch_queue:
                    if branch_name in original_branch_queue:
                        continue
                    else:
                        result = execute(['git branch -d {}'.format(branch_name)])
                        if result:
                            logging.warning('{}'.format(result))
                            logging.debug(
                                'the currently, the local branch {} associated with remote has been deleted'.format(
                                    branch_name))
            os.remove(pgs_file_name)

    def update_or_synchronization_local_git_repository(self, is_associate_remote=False):
        '''
            the update or synchronization local git repository

            the Notice:

                1. the only absolute path fields are supported

                target_absolute_list = ['/User/.../xxx', '/User/.../yyy', '/User/.../zzz']

                2. the custom exclusion lists are currently supported

                exclude_list = ['...', '...']
        '''
        update_or_synchronization_start = time.time()
        if not self.cfg:
            raise KeyError('the please set the profile information, that is currently an invalid configuration.')
        self.directory.set_work_region_space(self.cfg.get('project-prefix'))
        wrs = self.directory.get_work_region_space()
        if wrs and isinstance(wrs, str):
            target_absolute_list = self.cfg.get('target_absolute_list')
            exclude_list = self.cfg.get('exclude_list')
            if target_absolute_list and len(target_absolute_list) > 0:  # absolute path queue
                if not exclude_list:
                    exclude_list = []
                logging.debug('the current target absolute list that is {}'.format(target_absolute_list))
                logging.debug('the current exclude list that is {}'.format(exclude_list))
                local_git_repository_queue_with_absolute_path = find_git_repository(target_absolute_list, exclude_list)
                logging.info('the current git repository queue that is {}'.format(
                    json.dumps(local_git_repository_queue_with_absolute_path, ensure_ascii=False, indent=4)))
                if local_git_repository_queue_with_absolute_path:
                    for git_repository_item in local_git_repository_queue_with_absolute_path:
                        if git_repository_item and os.path.exists(git_repository_item):
                            self.directory.set_executed_region_space(git_repository_item)
                            logging.warning('the current destination directory that is {} '.format(git_repository_item))
                            os.chdir(git_repository_item)  # switch to destination direcoty
                            prune_result = execute(['git remote prune origin'])
                            if prune_result:
                                logging.info('the current remote prune information that is {}'.format(prune_result))
                            current_branch_queue = self.get_current_branch_list()
                            if current_branch_queue:
                                for index, branch_name in enumerate(current_branch_queue):
                                    execute(['git stash'])  # optional
                                    if is_associate_remote:
                                        execute(['git branch -u origin/{} {}'.format(branch_name, branch_name)])
                                        logging.debug(
                                            'the currently, the local branch {} associated with remote has been successed'
                                            .format(branch_name))
                                    pull_result = execute(['git pull'])
                                    if pull_result:
                                        logging.info(
                                            'the current remote pull information that is {}'.format(pull_result))
                                    logging.debug(
                                        'the current git repository({}) that update or synchronization branch({}) that had success.'
                                        .format(git_repository_item, branch_name))
        update_or_synchronization_end = time.time()
        logging.info('the update or synchronization local git repository that total time is {:.3f}s'.format(
            update_or_synchronization_end - update_or_synchronization_start))

    def write_original_and_stash_git_branch(self):
        '''
            The staging branch is written to the specified file,\
            and it is restored to the state before statistics after the data has been made available for subsequent statistics
        '''
        original_branch_queue = self.get_current_branch_list()
        if original_branch_queue and self.directory:
            wrs = self.directory.get_work_region_space()
            if wrs and isinstance(wrs, str):
                pgs_file_name = os.path.join(wrs, 'out/python_git_statistics.pkl')
                with open(pgs_file_name, 'wb') as output:
                    pickle.dump(original_branch_queue, output, pickle.DEFAULT_PROTOCOL)
                    logging.info('the currently written file directory is {} that write local branch list is {}'.format(
                        pgs_file_name, original_branch_queue))
        else:
            logging.warning('the current local branch list is invaild, skipping the process of writing to file.')
