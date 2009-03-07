#!/usr/bin/env python
# -*- coding: utf-8 -*-


#* part of git-tracker project
#* git-tracker - updates local cloned git repos
#* Copyright (C) 2009 Ivan Zorin <ivan.a.zorin@gmail.com>
#* see README for more information


import gtk;


def state(tray, icon):
	#changing tray icon;
	tray.set_from_file(icon);
	
	return 0;


def init(icon):
	#initialize git tray icon;
	#creating icon;
	tray = gtk.StatusIcon();
	#creating pop-up menu for tray icon;
	menu = gtk.Menu();
	#creating about menu item;
	menuItem = gtk.ImageMenuItem(gtk.STOCK_ABOUT);
	menuItem.connect('activate', info, icon);
	menu.append(menuItem);
	#creating quit menu item;
	menuItem = gtk.ImageMenuItem(gtk.STOCK_QUIT);
	menuItem.connect('activate', quit, tray);
	menu.append(menuItem);
	#setting up tray icon properties;
	tray.set_from_file(icon);
	tray.set_tooltip("git tracker");
	tray.connect('popup-menu', popup_menu, menu);
	#showing tray icon;
	tray.set_visible(True);
	#returning created tray icon object for using in other tray-related methods;
	return tray;


def quit(widget, data = None):
	#handling quit menu item;
	if data:
		data.set_visible(False);
	gtk.main_quit();
	
	return 0;


def popup_menu(widget, button, time, data = None):
	#handling pop-up menu of tray;
	if button == 3:
		if data:
			data.show_all();
			data.popup(None, None, None, 3, time);
	pass;
	
	return 0;


def info(widget, icon, data = None):
	#creating info message box about git tracker;
	msgBox = gtk.MessageDialog(parent = None, buttons = gtk.BUTTONS_OK, message_format = "Simple auto updater for local cloned git repositories\nCopyright (©) 2009 Ivan Zorin");
	msgBox.set_title("git tracker");
	msgBox.set_icon_from_file(icon);
	msgBox.run();
	msgBox.destroy();
	
	return 0;



