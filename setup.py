#!/usr/bin/env python


#* part of git-tracker project
#* git-tracker - updates local cloned git repos
#* Copyright (C) 2009 Ivan Zorin <ivan.a.zorin@gmail.com>
#* see README for more information


"""simple auto updater for local cloned git repositories""";


from distutils.core import setup;
from distutils.command.install_data import install_data;


class InstallData(install_data):
	def run(self):
		install_data.run(self);


setup(
	name = "git-tracker",
	version = "0.1",
	maintainer = "Ivan Zorin",
	maintainer_email = "ivan.a.zorin@gmail.com",
	description = "auto updater for local cloned git repos",
	license = "GNU GPL v3",
	scripts = ['git-tracker'],
	url = "http://github.com/ia/git-tracker/tree/master",
	package_dir = {
		"gitlib": ".",
	},
	packages = [
		"gitlib",
	],
	data_files=[('share/git-tracker/icons', ['icons/git-icon-32.png',
				'icons/git-icon-48.png',
				'icons/git-icon-64.png',
				'icons/git-icon-upd-64.png']),
		('share/applications', ['git-tracker.desktop']),
		('share/pixmaps', ['icons/git-tracker-logo.png']),
	],
	cmdclass={'install_data': InstallData}
)



