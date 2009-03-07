#!/usr/bin/env python


#* part of git-tracker project
#* git-tracker - updates local cloned git repos
#* Copyright (C) 2009 Ivan Zorin <ivan.a.zorin@gmail.com>
#* see README for more information


import sys;
import pynotify;


def update(git_repo, git_message, pull, notify_time, git_icon):
	#showing notify about available updates;
	#getting information for notify from log;
	hash_info = git_message[0];
	committer = git_message[1];
	message = git_message[2];
	date = git_message[3];
	#if pull updates by default is set, then make title green; if doesn't - red;
	if pull:
		title = "git tracker <span color = 'green'>updatable</span> info:";
	else:
		title = "git tracker <span color = 'red'>updatable</span> info:";
	#show update notification;
	git_notify = pynotify.Notification(title, git_repo + "\n" + hash_info + committer + message + date, git_icon);
	git_notify.set_timeout(notify_time * 1000);
	if not git_notify.show():
		print "Failed to send notification";
		sys.exit(1);
	
	return 0;


def pull(git_repo, git_message, notify_time, git_icon):
	#showing notify about commit information in updates;
	#getting information for notify from log;
	hash_info = git_message[0];
	committer = git_message[1];
	message = git_message[2];
	date = git_message[3];
	#show update notification;
	git_notify = pynotify.Notification("git tracker pulling info:", git_repo + "\n" + hash_info + committer + message + date, git_icon);
	git_notify.set_timeout(notify_time * 1000);
	if not git_notify.show():
		print "Failed to send notification";
		sys.exit(1);
	
	return 0;



