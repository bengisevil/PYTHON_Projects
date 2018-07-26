#!/usr/bin/env python3
import sys
import requests
from flask import Flask, render_template, request, redirect

'''
1. When the user enters the classes they wish to take during the specified semester,
   one or more possible schedules are generated with their corresponding CRNs.

2. Based on the class input, the in-state and out-of-state tuition is calculated for
   the relevant semester.

3. The user can retrieve a checksheet of classes they need to take before graduation
   based on their major (ECE only).

4. Based on system time, upcoming course-request and drop/add deadlines are displayed
   on the app.
'''

COURSE_BLANK = {
	'crn': 0,
	'course': '',
	'title': '',
	'credits': 0,
	'days': (0,0,0,0,0),
	'times': (0,0),
	'location': '',
	'ad_days': (0,0,0,0,0),
	'ad_times': (0,0),
	'ad_location': ''
}
