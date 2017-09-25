#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Linkindle - Linky energy consumption curves on a Kindle display.
# Copyright (C) 2016 Baptiste Candellier
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import linky
import os

username = os.environ['LINKY_USERNAME']
password = os.environ['LINKY_PASSWORD']

try:
    print("logging in as " + username + "...")
    token = linky.login(username, password)
    print("logged in successfully")
    res = linky.get_data_per_day(token, '27/10/2016', '30/10/2016')
    print(res)
except linky.LinkyLoginException as e:
    print(e)
