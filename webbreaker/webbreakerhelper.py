#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from webbreaker.webbreakerlogger import Logger


class WebBreakerHelper(object):
    @classmethod
    def check_run_env(cls):
        jenkins_home = os.getenv('JENKINS_HOME', '')
        if jenkins_home:
            return "jenkins"
        return None


    @classmethod
    def help_description(cls):
        return """
    SYNOPSIS:
    webbreaker [webinspect|fortify] [list|scan|download|upload] [OPTIONS]

    DESCRIPTION:
    WebBreaker is a light-weight, scalable, distributed, and automated dynamic security testing framework with a rich
    command set providing both high-level Product operations and Dynamic Application Security Test Orchestration (DASTO) on Products.

    COMMANDS:
    Webbreaker is separated into Upper ("Products") and Lower level ("Actions") commands with their respective options.

    UPPER-LEVEL COMMANDS:
    webbreaker-fortify
    Administer WebInspect scan results with Fortify Software Security Center (SSC).  Available `Actions` are
    add, list, and upload.

    webbreaker-webinspect
    Select WebInspect as your commercial scanner or Dynamic Application Security Test (DAST) product.  Available  `Actions` are
    scan, list and download.

    LOWER-LEVEL COMMANDS
    webbraker-list
    List current and past WebInspect scans.

    webbreaker-scan
    Create or launch a WebInspect scan from a fully licensed WebInspect server or host. Scan results are automatically
    downloaded in both XML and FPR formats.

    webbreaker-download
    Download or export a WebInspect scan locally.

    fortify-upload
    Upload a WebInspect scan to Fortify Software Security Center (SSC).

    WEBINSPECT SCAN OPTIONS:
      --settings            WebInspect scan configuration file, if no setting file is specified the ```Default``` file
                            shipped with WebInspect will be used.
      --scan_name           Used for the command 'webinspect scan' as both a scan instance variable and file name.  Default value is
                            _`WEBINSPECT-<random-5-alpha-numerics>`, or Jenkins global
                            environment variables may be declared, such as $BUILD_TAG.
      --scan_policy         Overrides the existing scan policy from the value in the setting file from `--settings`,
                            see `webinspect.ini` for built-in values.  Any custom policy must include only the GUID.
                            Do NOT include the `.policy` extension.
      --login_macro         Overrides the login macro declared in the original setting file from `--settings` and
                            uploads it to the WebInspect server.
      --workflow_macros     Workflow macros are located under webbreaker/etc/webinspect/webmacros, all webmacro files
                            end with a .webmacro extension, do NOT include the `webmacro` extension.
      --scan_mode           Acceptable values are `crawl`, `scan`, or `all`.
      --scan_scope          Acceptable values are `all`, `strict`, `children`, and `ancestors`.
      --scan_start          Acceptable values are `url` or `macro`.
      --start_urls          Enter a single url or multiple each with it's own --start_urls.
                            For example --start_urls http://test.example.com --start_urls http://test2.example.com
      --allowed_hosts       Hosts to scan, either a single host or a list of hosts separated by spaces. If not provided,
                            all values from `--start_urls` will be used.
      --size                WebInspect scan servers are managed with the `webinspect.ini` file, however a medium or large
                            size WebInspect server defined in the config can be explicitely declared with `--size medium`
                            or `--size large`.

      WEBINSPECT LIST OPTIONS:
      --server              Query a list of past and current scans from a specific WebInspect server or host.
      --scan_name           Limit query results to only those matching a given scan name
      --protocol            Specify which protocol should be used to contact the WebInspect server. Valid protocols
                            are 'https' and 'http'. If not provided, this option will default to 'https'

      WEBINSPECT DOWNLOAD OPTIONS:
      --scan_name           Specify the desired scan name to be downloaded from a specific WebInspect server or host.
      --server              Required option for downloading a specific WebInspect scan.  Server must be appended to all
                            WebInspect download Actions.
      --protocol            Specify which protocol should be used to contact the WebInspect server. Valid protocols
                            are 'https' and 'http'. If not provided, this option will default to 'https'

      FORTIFY LIST OPTIONS:
      --application         Provides a listing of Fortify SSC Version(s) within a specific Application or Project.
      --fortify_user        If provided WebBreaker authenticates to Fortify using these credentials. If not provided
        --fortify_password  WebBreaker attempts to use a secret for fortify.ini. If no secret is found our the secret is
                            no longer valid, you will be prompted for these credentials.

      FORTIFY UPLOAD OPTIONS:
      --fortify_user        If provided WebBreaker authenticates to Fortify using these credentials. If not provided
      --fortify_password    WebBreaker attempts to use a secret for fortify.ini. If no secret is found our the secret is
                            no longer valid, you will be prompted for these credentials.
      --application         If provided WebBreaker will look for version under this application name instead of the one
                            provided in fortify.ini
      --version             Used for the command 'fortify upload' this option specifies the application version name and
                            is used to both locate the file to be uploaded and the correct fortify application version
                            to upload the file to.
      --scan_name           If the scan file you wish to upload has a different name then --version, this option can
                            override which file WebBreaker uploads. Note: WebBreaker still assume the .fpr extension so
                            it should not be included here
        """


