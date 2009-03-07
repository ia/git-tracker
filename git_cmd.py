#!/usr/bin/env python


#* part of git-tracker project
#* git-tracker - updates local cloned git repos
#* Copyright (C) 2009 Ivan Zorin <ivan.a.zorin@gmail.com>
#* see README for more information


import os;


def check(git_repo):
	#checking available updates in repo for _master_ branch;
	#getting latest hash commit in local repo;
	local_repo = git_repo + "/.git/refs/heads/master";
	local_repo_file = open(local_repo, 'r');
	local_repo_hash = local_repo_file.read();
	local_repo_hash = local_repo_hash.strip();
	local_repo_file.close();
	#finding remote repo for local repo;
	remote_repo = os.popen("git --git-dir=" + git_repo + "/.git config remote.origin.url");
	remote_repo_url = remote_repo.read();
	remote_repo.close();
	remote_repo_url = remote_repo_url.strip();
	#getting latest hash commit in remote repo;
	remote_repo_file = os.popen("git ls-remote " + remote_repo_url + " | head -1 | awk \'{print $1}\'");
	remote_repo_hash = remote_repo_file.readline();
	remote_repo_hash = remote_repo_hash.strip();
	remote_repo_file.close();
	
	if (local_repo_hash == remote_repo_hash):
		#already updated;
		status = 0;
	else:
		#updates available;
		status = 1;
	
	return status;


def pull(git_repo):
	#silent pulling of updates in local repo;
	result = os.system("cd " + git_repo + " && git pull > /dev/null 2>&1");
	
	return 0;


def log(git_repo):
	#getting log information about last commit in updated repo;
	log = os.popen("git --git-dir=" + git_repo + "/.git log --pretty=format:'%H%n%an [%ce]%n%s%n%ai' -n 1");
	git_log_info = log.readlines();
	log.close();

	return git_log_info;



