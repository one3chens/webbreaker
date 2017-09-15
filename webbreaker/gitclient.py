#!/usr/bin/env python
# -*- coding: utf-8 -*-

from webbreaker.gitapi import GitApi
import requests
import requests.exceptions
import requests.packages.urllib3
import os
try:
    import ConfigParser as configparser
except ImportError: #Python3
    import configparser
try:  # Python 2
    config = configparser.SafeConfigParser()
except NameError:  # Python 3
    config = configparser.ConfigParser()

class GitClient(object):
    def __init__(self, host):
        self.host = host
        self.token = self.get_token()

    def get_user_email(self, login):
        gitapi = GitApi(host=self.host, token=self.token, verify_ssl=False)
        response = gitapi.get_user(login)
        if response.success:
            return response.data['email']
        else:
            print(response.message)
            return None

    def get_contributors(self, owner, repo):
        gitapi = GitApi(host=self.host, token=self.token, verify_ssl=False)
        response = gitapi.get_contributors(owner, repo)
        if response.success:
            contributors = []
            for contributor in response.data:
                contributors.append(contributor['login'])
            return contributors
        else:
            print(response.message)
            return None

    def get_all_emails(self, owner, repo):
        emails = []
        logins = self.get_contributors(owner, repo)
        if logins:
            for login in logins:
                email = self.get_user_email(login)
                if email:
                    emails.append(email)
        return emails

    def get_token(self):
        config_file = os.path.abspath(os.path.join('webbreaker', 'etc', 'webbreaker.ini'))
        config.read(config_file)
        return config.get("git", "token")


class UploadLog(object):
    def __init__(self, log_file):
        # Accept a file, set values
        self.log_file = log_file

class GitUploader(object):
    def __init__(self, agent_url=None):
        # set file here
        self.upload_log = UploadLog(None)
        self.agent_url = agent_url
        if not agent_url:
            self.agent_url = self.read_ini()


    def read_ini(self):
        return None


    def upload(self):
        data = {}
        data['fortify_pv_url'] = self.upload_log.fortify_pv_url
        data['fortify_build_id'] = self.upload_log.fortify_build_id
        data['git_emails'] = self.upload_log.git_emails
        response = requests.put(self.agent_url, data=data, verify_ssl=False)


