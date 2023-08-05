#!/usr/bin/env python3

# BoBoBo

import yaml


def load_yaml(path):
    try:
        with open(path, mode='r') as cf:
            conf = yaml.load(cf, Loader=yaml.FullLoader)
    except Exception as ex:
        print('Failed to load conf for %s' % ex)
    else:
        return conf


def get_conf(conf_file, top_key=None):
    conf = load_yaml(conf_file)
    if not conf:
        print('Invalid configuration: %s' % conf)
        return None

    if not top_key:
        return conf

    if top_key not in conf:
        print('No %s in conf top_keys: %s' % (top_key, conf))
        return None
    return conf[top_key]
