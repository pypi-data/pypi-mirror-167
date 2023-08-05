# -*- coding:utf-8 -*-

import json
import math
import os
import re
import time

from com.dvsnier.config.journal.compat_logging import logging
from datetime import date


def entransfer(num_with_str):
    'Only support conversion within 100, not including the number of 100.'
    num = -1
    if not num_with_str:
        raise ValueError('Illegal parameter exception.')
    elif num_with_str.find('百') > 0:
        raise ValueError('Only support conversion within 100, not including the number of 100.')
    else:
        pass
    str_to_num_dict = {"一": "1", "二": "2", "三": "3", "四": "4", "五": "5", "六": "6", "七": "7", "八": "8", "九": "9", "十": "0"}
    # [一, 一百)
    if len(num_with_str) == 1:  # (0, 10]
        if num_with_str == '十':
            num = int(str(str_to_num_dict['一'] + str_to_num_dict[num_with_str]))
        else:
            num = int(str_to_num_dict[num_with_str])
    else:
        if len(num_with_str) == 2:
            if num_with_str[1] == '十':  # [20, 30, 40, 50, 60, 70, 80, 90]
                num = int(str(str_to_num_dict[num_with_str[0]] + str_to_num_dict[num_with_str[1]]))
            else:  # (10, 20)
                num = int(str(str_to_num_dict['一'] + str_to_num_dict[num_with_str[1]]))
        elif len(num_with_str) == 3:
            num = int(str(str_to_num_dict[num_with_str[0]] + str_to_num_dict[num_with_str[2]]))
        else:
            raise ValueError('Only support conversion within 100, not including the number of 100.')
    return num


def detransfer(num):
    'Only support conversion within 100, not including the number of 100.'
    str_num = ""
    if 0 >= num or num >= 100:
        raise ValueError('Only support conversion within 100, not including the number of 100.')
    else:
        pass
    num_to_str_dict = {"1": "一", "2": "二", "3": "三", "4": "四", "5": "五", "6": "六", "7": "七", "8": "八", "9": "九", "0": "十"}
    # [1, 100)
    if num > 9:
        if str(num)[0] == '0':  # (0, 10)
            str_num = num_to_str_dict[str(num)[1]]
        elif str(num)[0] == '1':  # [10, 19)
            if str(num)[1] == '0':
                str_num = num_to_str_dict['0']
            else:
                str_num = num_to_str_dict['0'] + num_to_str_dict[str(num)[1]]
        elif str(num)[1] == '0':  # [20, 100)
            str_num = num_to_str_dict[str(num)[0]] + num_to_str_dict['0']
            pass
        else:
            str_num = num_to_str_dict[str(num)[0]] + num_to_str_dict['0'] + num_to_str_dict[str(num)[1]]
    else:  # (0, 10)
        str_num = num_to_str_dict['{}'.format(num)]
    return str_num


def calculate_complex_date(latest_month, latest_week):
    'Calculate complex date, only provide natural month and natural week, and calculate according to calendar mode.'
    nearest_month = 0
    nearest_week = 0
    if isinstance(latest_month, str) and latest_month.isdigit():
        nearest_month = int(latest_month)
    elif isinstance(latest_month, int):
        nearest_month = latest_month
    else:
        logging.warning('the current latest_month is illegal parameter that value is {}.'.format(latest_month))
    if isinstance(latest_week, str) and latest_week.isdigit():
        nearest_week = int(latest_week)
    elif isinstance(latest_week, int):
        nearest_week = latest_week
    else:
        logging.warning('the current latest_week is illegal parameter that value is {}.'.format(latest_week))
    now = date.today()
    since_date = None
    until_date = date.fromisoformat(now.isoformat())
    now_year = now.year
    now_month = now.month
    now_day = now.day
    now_calendar_tuple = now.isocalendar()
    if nearest_month:
        if math.fabs(nearest_month) > 0:
            delta_month = now_month - nearest_month
            if delta_month > 0:  # Refers to the current year query
                since_date = date(now_year, delta_month, now_day)
            elif delta_month == 0:  # Just in the current year query
                since_date = date(now_year, delta_month + 1, 1)
            else:  # Last year to this year
                if math.fabs(delta_month) < 12:
                    since_date = date(now_year - 1, delta_month + 12, 1)
                else:
                    raise ValueError(
                        'Data date assignment with months greater than the last two years is not supported now. Please specify directly (since_date and until_date) ways.'
                    )
    elif nearest_week:
        if math.fabs(nearest_week) > 0:
            delta_week = now_calendar_tuple[1] - nearest_week
            if delta_week > 0:  # Refers to the current year query
                # since_date = date(now_year, delta_week, 1)
                since_date = date.fromisocalendar(now_year, delta_week, 1)
                pass
            elif delta_week == 0:  # Just in the current year query
                since_date = date.fromisocalendar(now_year, delta_week + 1, 1)
                pass
            else:  # Last year to this year
                if date(now_year - 1, 12, 31).isocalendar()[1] > math.fabs(delta_week):
                    since_date = date.fromisocalendar(now_year - 1, delta_week + 1 + date(now_year - 1, 12, 31).isocalendar()[1], 1)
                else:
                    raise ValueError(
                        'Data date assignment with weeks greater than the last two years is not supported now. Please specify directly (since_date and until_date) ways.'
                    )
    else:
        raise ValueError('The parameter set is invalid, please select the specified key(since, until, latest_month, latest_week).')
    return (since_date, until_date)


def find_git_repository(absolute_dir_list, exclude_list=[]):
    'the find git repository'
    git_repository_queue = []
    find_start = time.time()
    if absolute_dir_list and len(absolute_dir_list) > 0:
        for absolute_dir in absolute_dir_list:
            if absolute_dir and os.path.exists(absolute_dir):
                git_repository_queue.extend(__find_special_directory(absolute_dir, exclude_list))
    find_end = time.time()
    logging.info('the find git repository that total time is {:.3f}s'.format(find_end - find_start))
    return git_repository_queue


def __find_special_directory(dir, exclude_list=[]):
    git_repository_queue = []
    # logging.debug('the current directory or file is {}'.format(dir))
    if os.path.isdir(dir):
        directory = os.listdir(dir)
        directory.sort()
        # logging.debug('the currently retrieved list information is {}'.format(directory))
        for file in directory:
            if exclude_list and len(exclude_list) > 0 and file in exclude_list:
                # logging.warning('the current directory or file is {} and ignore retrieval, skip check for {}'.format(file, file))
                continue
            # logging.info('the current retrieved file or directory that is {}'.format(file))
            if os.path.isdir(os.path.join(os.path.realpath(dir), file)):  # it is directory
                if file == '.git':
                    git_directory = os.path.dirname(os.path.join(os.path.realpath(dir), file))
                    # logging.warning('The current project directory is git project, ready to add {} to the queue.'.forma(git_directory))
                    git_repository_queue.append(git_directory)
                else:  # the recursive execute
                    sub_git_repository_queue = __find_special_directory(os.path.join(dir, file), exclude_list)
                    # logging.warning('Start a recursive call to find the subdirectory {}'.format(os.path.join(dir, file)))
                    if sub_git_repository_queue and len(sub_git_repository_queue) > 0:
                        git_repository_queue.extend(sub_git_repository_queue)
            else:
                # logging.debug('the current file is {} that is maybe skipped.'.format(file))
                continue
    # if git_repository_queue and len(git_repository_queue) > 0:
    #     logging.info('the current list of returned child git items is {}'.format(git_repository_queue))
    return git_repository_queue


def generator_vscode_workspace(absolute_git_repository_list, ws_name):
    '''
        the generator vscode workspace

        Now let's define the workspace concept as follows:

            1. work_sapce_xxx and worksapce and worksapces: the standard worksapce region;
            2. xxx_repository and xxx_repositories: the standard type repository region;
            3. vscode ws is generated in both of the above;

        absolute_git_repository_list: list string type
        ws_name: vscode worksapce name
        flag: 0: the default no merge repository; 1: the merge brother directory repository; the current no support it;
    '''
    if absolute_git_repository_list and len(absolute_git_repository_list) > 0:
        vsc_ws_region = dict()
        vsc_ws_folders = []
        KEY_NAME = 'name'
        KEY_PATH = 'path'
        KEY_FOLDERS = 'folders'
        KEY_SETTINGS = 'settings'
        for index, git_repository_path in enumerate(absolute_git_repository_list):
            vsc_ws_item = dict()
            project_name = os.path.basename(git_repository_path)
            project_directory_path = os.path.dirname(git_repository_path)
            split_list = project_directory_path.split(os.path.sep)
            if split_list and len(split_list) > 0:
                split_list.reverse()
                for split_item in split_list:
                    match = re.search(r'(work_space[\w]*_\w+)|(WorkSpace[\w]*_\w+)|(\w*workspace\w*)|(\w+_repositor\w+)',
                                      split_item,
                                      flags=re.I)
                    if match:
                        prefix = re.sub(r'(work_space[\w]*_)|(WorkSpace[\w]*_)|(workspace[\w]*)|(_repositor[\w]*)',
                                        '',
                                        match.string,
                                        flags=re.I)
                        pattern = re.compile('{}'.format(prefix), flags=re.I)
                        if prefix and re.match(pattern, project_name):
                            if KEY_NAME not in vsc_ws_item.keys():
                                vsc_ws_item.update({KEY_NAME: project_name})
                        else:
                            if KEY_NAME not in vsc_ws_item.keys():
                                vsc_ws_item.update({KEY_NAME: '{}-{}'.format(prefix, project_name)})
                                # logging.debug('the current project space is replace character that is {} -> {}'.format(
                                #     match.string, prefix))
                    else:
                        if KEY_NAME not in vsc_ws_item.keys():
                            vsc_ws_item.update({KEY_NAME: project_name})
            else:
                vsc_ws_item.update({KEY_NAME: project_name})
            vsc_ws_item.update({KEY_PATH: git_repository_path})
            vsc_ws_folders.append(vsc_ws_item)
        vsc_ws_region.update({KEY_FOLDERS: vsc_ws_folders})
        vsc_ws_settings = dict()
        vsc_ws_region.update({KEY_SETTINGS: vsc_ws_settings})
        if ws_name:
            with open(ws_name, 'w') as file:
                file.write(json.dumps(vsc_ws_region, ensure_ascii=False, indent=4))
        else:
            raise ValueError('the current ws_name is an illegal parameter.')
    else:
        logging.error('the current absolute path is an illegal parameter and then skipping it.')
