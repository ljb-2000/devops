#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import argparse
import json
import sys


def getHostList():
    inventory = dict()
    response = requests.get('http://127.0.0.1:8000/cmdb/groups/')
    groups = response.json()
    for group in groups:
        inventory[group['name']] = group['hosts']
    return json.dumps(inventory, indent=4)

def getHostDetail(hostname):
    vars = dict()
    response = requests.get('http://127.0.0.1:8000/cmdb/hosts/%s/' % hostname)
    host = response.json()
    vars = {
        "ansible_ssh_user": host['username'],
        "ansible_ssh_host": host['ipaddr'],
        'ansible_ssh_port': host['port'],
    }
    if host['login_type'] == 'password':
        vars.update({'ansible_ssh_pass': host['password']})
    else:
        vars.update({'ansible_ssh_private_key_file': host['private_key']})
    return json.dumps(vars, indent=4)

def main():
    # parser = argparse.ArgumentParser(description='Produce an Ansible Inventory file based on Cobbler')
    # parser.add_argument('--list', action='store_true', default=True, help='List instances (default: True)')
    # parser.add_argument('--host', action='store', help='Get all the variables about a specific instance')
    if len(sys.argv) == 2 and sys.argv[1] == '--list':
        print getHostList()
    elif len(sys.argv) == 3 and sys.argv[1] == '--host':
        print getHostDetail(sys.argv[2])
    else:
        print "Usage: %s --list or --host <hostname>" % sys.argv[0]
        sys.exit(1)

if __name__ == '__main__':
    main()
