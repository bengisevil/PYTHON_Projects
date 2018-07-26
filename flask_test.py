#!/usr/bin/env python3
import datetime
import results_test # TODO: remove
import urllib.parse
import urllib.request
from random import randrange
from flask import Flask, request, render_template, redirect, json, url_for

last_results = None
selections = []

results_test = {
	'major': '',
	'gradyear': '',
	'checksheet': 'https://registrar.vt.edu/content/dam/registrar_vt_edu/documents/Updates/coe/COE_cpe_18.pdf',
	'term': '',
	'results': []
}

app = Flask(__name__)
app.config['DEBUG'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def home():
	return render_template('home.html')
# end home

@app.route("/process", methods=['POST'])
def process():
	global last_results
	last_results = {}

	major_requested = request.form['major']
	gradyear_requested = request.form['gradyear']
	term_requested = request.form['term']
	courses_requested = []

	if request.form['course_1']: courses_requested.append(request.form['course_1'])
	if request.form['course_2']: courses_requested.append(request.form['course_2'])
	if request.form['course_3']: courses_requested.append(request.form['course_3'])
	if request.form['course_4']: courses_requested.append(request.form['course_4'])
	if request.form['course_5']: courses_requested.append(request.form['course_5'])
	if request.form['course_6']: courses_requested.append(request.form['course_6'])
	if request.form['course_7']: courses_requested.append(request.form['course_7'])

	# TODO: this is where courses are sent to the timetable, each page is received,
	# parsed, and a list of python dictionaries containing class data is created;
	# some json conversion might have to happen to pass the results between flask pages.
	# An example result from test_set.py is being used for now.

	# account for newer checksheet links requiring slightly different format
	append_year = ''
	append_college = '/COE_'
	if gradyear_requested == '19':
		append_year = '/2019'
		append_college = '/coe_'
	if gradyear_requested == '20':
		append_year = '/2020'
		append_college = '/coe_'

	checksheet_url = (
		'https://registrar.vt.edu/content/dam/registrar_vt_edu/documents/Updates/coe'
		+ append_year + append_college + major_requested + '_' + gradyear_requested + '.pdf'
	)

	if requests.get(checksheet_url).status_code == 404:
		checksheet_url = 'https://registrar.vt.edu/graduation-multi-brief/checksheets/college/index.html'

	# run timetable request loop
	for course in courses_requested:
		TERMYEAR = term_requested
		subj_code = course.split('-')[0].lower()
		CRSE_NUMBER = course.split('-')[1]

		url = 'https://banweb.banner.vt.edu/ssb/prod/HZSKVTSC.P_ProcRequest'

		data = (
			'CAMPUS=0' +
			'&TERMYEAR=' + term_requested +
			'&CORE_CODE=AR%25' +
			'&subj_code=' + course.split('-')[0].lower() +
			'&SCHDTYPE=%25' +
			'&CRSE_NUMBER=' + course.split('-')[1] +
			'&crn=' +
			'&open_only=' +
			'&disp_comments_in=N' +
			'&BTN_PRESSED=FIND+class+sections' +
			'&inst_name='
		).encode('utf-8')

		#Timetable parsing		
		#Append major, gradyear and term to result_test object

		results_test['major'] = str(major_requested)
		results_test['gradyear'] = str(gradyear_requested)
		results_test['term'] = str(term_requested)

		#Create and append course objects to the result of result_test
		course_a = {
			'course': '',
			'title': '',
			'credits': '',
			'slots': [
				{
					'crn': '',
					'days': '',
					'start': '',
					'end': '',
					'location': '',
					'ad_days': None,
					'ad_start': None,
					'ad_end': None,
					'ad_location': None
				}
			]
		}

		req = urllib.request.Request(url, data=data)
		response = urllib.request.urlopen(req)
		page = response.read()
		
		#Parse with beautiful soup to get class results
		soup = bs.BeautifulSoup(page, 'html.parser')	
		table = soup.find('table', attrs={'summary':'This table displays the Time Table of Classes'})
		rows = table.find_all('tr')[1::]
		first_sec = rows[0]
		course = first_sec.find_all('td')[1].text
		title =  first_sec.find_all('td')[2].text 
		credits =  first_sec.find_all('td')[4].text

		course_a['course'] = course
		course_a['title'] = title
		course_a['credits'] = credits

		newslot = {
					'crn': '',
					'days': '',
					'start': '',
					'end': '',
					'location': '',
					'ad_days': None,
					'ad_start': None,
					'ad_end': None,
					'ad_location': None
				}
		for row in rows:
			elm = row.find_all('td')
			crn = elm[0].text
			days = elm[7].text
			start = elm[8].text
			start = start.replace(':', '')
			start = start[:-2]
			end = elm[9].text
			end = end.replace(':', '')
			end = end[:-2]
			location= elm[10].text 

			newslot['crn'] = crn
			newslot['days'] = crn
			newslot['start'] = crn
			newslot['end'] = crn
			newslot['location'] = crn
			course_a['slots'].append(newslot)
			
		#add course to the results
		results_test['results'].append(course_a)
	# end timetable

	# end timetable

	print('major_requested:\t' + str(major_requested))
	print('gradyear_requested:\t' + str(gradyear_requested))
	print('term_requested:\t\t' + str(term_requested))
	print('courses_requested:\t' + str(courses_requested))
	print('checksheet_url:\t' + str(checksheet_url))

	last_results = results_test.results_test # TODO: replace with actual results

	return redirect('/results')
# end process

@app.route("/results")
def results():
	global last_results

	if last_results is None: return "No results stored. Please try again."

	return render_template('results.html', data=last_results)
# end results

@app.route("/schedule")
def schedule():
	global last_results

	if last_results is None: return "No results stored. Please try again."

	results = last_results['results']
	selections = []

	# try no more than 1000 times to generate something valid
	for attempt in range(1000):
		valid = True
		selections.clear()

		# pick a random selection from the results
		for i in range(len(results)):
			result = results[i]
			selection = randrange(len(result['slots']))
			selections.append({'course': result['course'], 'data': result['slots'][selection]})

		# check for conflicts; set not valid if one exists
		for i in range(len(selections)):
			for j in range(len(selections)):
				if i == j: continue

				# get data for courses i and j
				ci = selections[i]['data']
				cj = selections[j]['data']

				# get start and end times of courses i and j
				si, ei = ci['start'], ci['end']
				sj, ej = cj['start'], cj['end']

				# get ad_start and ad_end times of courses i and j
				asi, aei = ci['ad_start'], ci['ad_end']
				asj, aej = cj['ad_start'], cj['ad_end']

				# get days of courses i and j
				di = ci['days']
				dj = cj['days']

				# get ad_days of courses i and j
				adi = ci['ad_days']
				adj = cj['ad_days']

				if adi is None: adi = ''
				if adj is None: adj = ''

				# compare all days and times to make sure there are no conflicts
				for day in ['M','T','W','R','F']:
					if (di.find(day) > -1) and (dj.find(day) > -1):
						if (sj <= si <= ej) or (sj <= ei <= ej):
							valid = False

					if (adi.find(day) > -1) and (dj.find(day) > -1):
						if asi and aei:
							if (sj <= asi <= ej) or (sj <= aei <= ej):
								valid = False

					if (di.find(day) > -1) and (adj.find(day) > -1):
						if asj and aej:
							if (asj <= si <= aej) or (asj <= ei <= aej):
								valid = False

					if (adi.find(day) > -1) and (adj.find(day) > -1):
						if asi and aei and asj and aej:
							if (asj <= asi <= aej) or (asj <= aei <= aej):
								valid = False
				# end for day
			# end for j
		# end for i
		if valid: break
	# end for attempt

	if not valid: return "Error occurred. Please try again."

	# print(str(selections))

	return render_template('schedule.html', data=json.dumps(selections))
# end schedule

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)
# end if
