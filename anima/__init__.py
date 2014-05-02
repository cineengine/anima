# -*- coding: utf-8 -*-
# Copyright (c) 2012-2014, Anima Istanbul
#
# This module is part of anima-tools and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause


__version__ = "0.1.7"


import logging
logging.basicConfig()
logging_level = logging.DEBUG

stalker_server_address = 'http://192.168.0.64:6543'
local_cache_folder = '~/.cache/anima/'
recent_file_name = 'recent_files'
avid_media_file_path_storage = 'avid_media_file_path'

normal_users_group_names = ['Normal Users']
power_users_group_names = ['Power Users', 'admins']
