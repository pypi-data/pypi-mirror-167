# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2022-present Ramiro Gómez <code@ramiro.org>
# SPDX-License-Identifier: MIT
import httpx


def check(url):
    result = {'url': url}

    try:
        resp = httpx.head(url)
    except Exception as err:
        result['exception'] = err
        return result

    result['status'] = resp.status_code
    if resp.is_redirect:
        result['redirect'] = resp.headers['location']

    return result
