var timemap = [ -1,
   800, 805, 810, 815, 820, 825, 830, 835, 840, 845, 850, 855,
   900, 905, 910, 915, 920, 925, 930, 935, 940, 945, 950, 955,
  1000,1005,1010,1015,1020,1025,1030,1035,1040,1045,1050,1055,
  1100,1105,1110,1115,1120,1125,1130,1135,1140,1145,1150,1155,
  1200,1205,1210,1215,1220,1225,1230,1235,1240,1245,1250,1255,
  1300,1305,1310,1315,1320,1325,1330,1335,1340,1345,1350,1355,
  1400,1405,1410,1415,1420,1425,1430,1435,1440,1445,1450,1455,
  1500,1505,1510,1515,1520,1525,1530,1535,1540,1545,1550,1555,
  1600,1605,1610,1615,1620,1625,1630,1635,1640,1645,1650,1655,
  1700,1705,1710,1715,1720,1725,1730,1735,1740,1745,1750,1755,
  1800,1805,1810,1815,1820,1825,1830,1835,1840,1845,1850,1855,
  1900,1905,1910,1915,1920,1925,1930,1935,1940,1945,1950,1955
]

var colourmap = [
  "Tomato","Orange","DodgerBlue","MediumSeaGreen","Violet","SlateBlue","Gray"
]

var daymap = ["", "M", "T", "W", "R", "F"]

function gen_schedule(obj) {
  var data = JSON.parse(obj);
  var table = document.getElementById("schedule");

  // print a colour-coded list of courses
  for (var course in data) {
    c = data[course]
    var item = document.createElement("li");

    var text = document.createTextNode(
      " (" + c.data.crn + ") " + c.course + ": " + c.data.days + " @ " + c.data.start + "-" + c.data.end + " in " + c.data.location
    );

    var ad_text = document.createTextNode(
      " (plus " + c.data.ad_days + " @ " + c.data.ad_start + "-" + c.data.ad_end + " in " + c.data.ad_location + ")"
    );

    item.appendChild(text);
    if (c.data.ad_days) item.appendChild(ad_text);

    item.style.color = colourmap[course];
    item.style.fontWeight = 900;
    document.getElementById("courses").appendChild(item);
  }

  // create schedule base
  for (i = 0; i < 144; i++) {
    bgcol = "#ffffff";

    var row = table.insertRow(-1);

    var time = row.insertCell(0);
    var mon = row.insertCell(1);
    var tue = row.insertCell(2);
    var wed = row.insertCell(3);
    var thu = row.insertCell(4);
    var fri = row.insertCell(5);

    mon.style.backgroundColor = bgcol;
    tue.style.backgroundColor = bgcol;
    wed.style.backgroundColor = bgcol;
    thu.style.backgroundColor = bgcol;
    fri.style.backgroundColor = bgcol;
  }

  // create schedule
  for (day = 1; day < 6; day++) {
    for (time = 1; time < 145; time++) {
      for (var course in data) {
        // generate colour-coded days
        if (data[course].data.days.search(daymap[day]) > -1) {
          if ( (timemap[time] >= data[course].data.start) && (timemap[time] < data[course].data.end) ) {
            table.rows[time].cells[day].style.backgroundColor = colourmap[course];
          }
        }

        // generate colour-coded ad_days
        if (data[course].data.ad_days) {
          if (data[course].data.ad_days.search(daymap[day]) > -1) {
            if ( (timemap[time] >= data[course].data.ad_start) && (timemap[time] < data[course].data.ad_end) ) {
              table.rows[time].cells[day].style.backgroundColor = colourmap[course];
            }
          }
        }
      }
    }
  }

  // clear column for times
  for (i = 1; i < 145; i++) {
    table.rows[i].deleteCell(0);
  }

  // create times column
  time = 800;
  for (i = 1; i < 145; i+=12) {
    row = table.rows[i];

    timecell = row.insertCell(0);
    timecell.rowSpan = 12;
    timecell.innerHTML = time;
    timecell.style.textAlign = 'right';
    timecell.style.verticalAlign = 'top';
    timecell.style.border = "1px solid #000";

    row.style.borderTop = "1px solid #000";

    time += 100;
  }
}
