/* Welcome to the SQL mini project. For this project, you will use
Springboard' online SQL platform, which you can log into through the
following link:

https://sql.springboard.com/
Username: student
Password: learn_sql@springboard

The data you need is in the "country_club" database. This database
contains 3 tables:
    i) the "Bookings" table,
    ii) the "Facilities" table, and
    iii) the "Members" table.

Note that, if you need to, you can also download these tables locally.

In the mini project, you'll be asked a series of questions. You can
solve them using the platform, but for the final deliverable,
paste the code for each solution into this script, and upload it
to your GitHub.

Before starting with the questions, feel free to take your time,
exploring the data, and getting acquainted with the 3 tables. */

/* Q1: Some of the facilities charge a fee to members, but some do not.
Please list the names of the facilities that do. */
  
/* Query: */
SELECT name
FROM  `Facilities` 
WHERE  `membercost` >0
LIMIT 0 , 30

/* output:
name
Tennis Court 1
Tennis Court 2
Massage Room 1
Massage Room 2
Squash Court

*/


/* Q2: How many facilities do not charge a fee to members? */
/* Answer 2: Badminton Court, Table Tennis, Snooker Table, Pool Table. */

/* Query: */
SELECT name, membercost
FROM  `Facilities` 
WHERE  `membercost` =0
LIMIT 0 , 30

/* Output:

This table does not contain a unique column. Grid edit, checkbox, Edit, Copy and Delete features are not available.
Showing rows 0 - 3 (4 total, Query took 0.0003 sec) */

SELECT name, membercost
FROM  `Facilities` 
WHERE  `membercost` =0
LIMIT 0 , 30
 
/*
Output:
name		membercost
Badminton Court	0.0
Table Tennis	0.0
Snooker Table	0.0
Pool Table	0.0 */


/* Query: */
SELECT COUNT( name ) 
FROM  `Facilities` 
WHERE  `membercost` =0

/*
Output:
count(name)
4
*/

SELECT count(membercost)
FROM  `Facilities` 
WHERE  `membercost` =0

/*
Output:
count(membercost)
4 */


/* Q3: How can you produce a list of facilities that charge a fee to members,
where the fee is less than 20% of the facility's monthly maintenance cost?
Return the facid, facility name, member cost, and monthly maintenance of the
facilities in question. */

/* Query: */

SELECT  `name` ,  `membercost` ,  `monthlymaintenance` 
FROM  `Facilities` 
WHERE (
 `membercost` /  `monthlymaintenance`
) < 0.2
LIMIT 0 , 30

/*
Output:
name		membercost	monthlymaintenance
Tennis Court 1	5.0		200
Tennis Court 2	5.0		200
Badminton Court	0.0		50
Table Tennis	0.0		10
Massage Room 1	9.9		3000
Massage Room 2	9.9		3000
Squash Court	3.5		80
Snooker Table	0.0		15
Pool Table	0.0		15   */



/* Q4: How can you retrieve the details of facilities with ID 1 and 5?
Write the query without using the OR operator. */

/* Query: */
SELECT  * 
FROM  `Facilities` 
WHERE `facid` IN (1,5)

/*
Output:
	
name		membercost	guestcost	facid	initialoutlay	monthlymaintenance
Tennis Court 2	5.0		25.0		1	8000		200
Massage Room 2	9.9		80.0		5	4000		3000			*/


/* Q5: How can you produce a list of facilities, with each labelled as
'cheap' or 'expensive', depending on if their monthly maintenance cost is
more than $100? Return the name and monthly maintenance of the facilities
in question. */

/* Query: */
SELECT  `name`,  `monthlymaintenance`, 
	CASE 
		WHEN  `monthlymaintenance` >100
			THEN  'expensive'
			ELSE  'cheap'
	END AS cost
FROM  `Facilities` 

/*
Output:
name		monthlymaintenance	cost
Tennis Court 1	200			expensive
Tennis Court 2	200			expensive
Badminton Court	50			cheap
Table Tennis	10			cheap
Massage Room 1	3000			expensive
Massage Room 2	3000			expensive
Squash Court	80			cheap
Snooker Table	15			cheap
Pool Table	15			cheap   */


/* Q6: You'd like to get the first and last name of the last member(s)
who signed up. Do not use the LIMIT clause for your solution. */

Query:
SELECT memid, surname, firstname
FROM  `Members` 
WHERE  `memid` = 
	(
	SELECT MAX(`memid`) 
	FROM  `Members`
	)

/*
Output:
surname	firstname
Smith	Darren		*/



/* Q7: How can you produce a list of all members who have used a tennis court?
Include in your output the name of the court, and the name of the member
formatted as a single column. Ensure no duplicate data, and order by
the member name. */

SELECT DISTINCT 
	CASE 
		WHEN  b.facid = 0
			THEN  'Tennis Court 1'
			ELSE  'Tennis Court 2'
	END AS facid,
	CASE 
		WHEN  m.surname = 'GUEST'
			THEN  m.surname
			ELSE  CONCAT(m.surname, ", ", m.firstname)
	END AS member_name
FROM `Bookings` b
JOIN `Members` m
ON b.memid = m.memid
WHERE `facid` IN (0,1)
ORDER BY member_name, facid


/*

Output :

court_name	member_name
Tennis Court 1	Bader, Florence
Tennis Court 2	Bader, Florence
Tennis Court 1	Baker, Anne
Tennis Court 2	Baker, Anne
Tennis Court 1	Baker, Timothy
Tennis Court 2	Baker, Timothy
Tennis Court 1  Boothe, Tim
Tennis Court 2	Boothe, Tim
Tennis Court 1	Butters, Gerald
Tennis Court 2	Butters, Gerald
Tennis Court 1	Coplin, Joan
Tennis Court 1	Crumpet, Erica
Tennis Court 1	Dare, Nancy
Tennis Court 2	Dare, Nancy
Tennis Court 1	Farrell, David
Tennis Court 2	Farrell, David
Tennis Court 1	Farrell, Jemima
Tennis Court 2	Farrell, Jemima
Tennis Court 1	Genting, Matthew
Tennis Court 1	GUEST
Tennis Court 2	GUEST
Tennis Court 1	Hunt, John
Tennis Court 2	Hunt, John
Tennis Court 1	Jones, David
Tennis Court 2	Jones, David
Tennis Court 1	Jones, Douglas
Tennis Court 1	Joplette, Janice
Tennis Court 2	Joplette, Janice
Tennis Court 1	Owen, Charles
Tennis Court 2	Owen, Charles
*/

/* Q8: How can you produce a list of bookings on the day of 2012-09-14 which
will cost the member (or guest) more than $30? Remember that guests have
different costs to members (the listed costs are per half-hour 'slot'), and
the guest user's ID is always 0. Include in your output the name of the
facility, the name of the member formatted as a single column, and the cost.
Order by descending cost, and do not use any subqueries. */

SELECT f.name as facility_name, 
	CASE 
		WHEN  m.surname = 'GUEST'
			THEN  m.surname
			ELSE  CONCAT(m.surname, ", ", m.firstname)
	END AS member_name,
	CASE 
		WHEN  m.surname = 'GUEST'
			THEN  f.guestcost * b.slots
			ELSE  f.membercost * b.slots
	END AS cost
FROM `Bookings` b
INNER JOIN `Facilities` f
ON b.facid = f.facid
INNER JOIN `Members` m
ON b.memid = m.memid
WHERE b.starttime BETWEEN '2012-09-14' AND '2012-09-15'
HAVING cost > 30
ORDER BY cost DESC

/* Q9: This time, produce the same result as in Q8, but using a subquery. */

SELECT f.name as facility_name, 
	CASE 
		WHEN  m.surname = 'GUEST'
			THEN  m.surname
			ELSE  CONCAT(m.surname, ", ", m.firstname)
	END AS member_name,
	CASE 
		WHEN  m.surname = 'GUEST'
			THEN  f.guestcost * b.slots
			ELSE  f.membercost * b.slots
	END AS cost
FROM (
	 SELECT *
	 FROM `Bookings`
	 WHERE starttime BETWEEN '2012-09-14' AND '2012-09-15'
	 ) b
INNER JOIN `Facilities` f
ON b.facid = f.facid
INNER JOIN `Members` m
ON b.memid = m.memid
HAVING cost > 30
ORDER BY cost DESC

/* Q10: Produce a list of facilities with a total revenue less than 1000.
The output of facility name and total revenue, sorted by revenue. Remember
that there's a different cost for guests and members! */

SELECT f.name, 
		SUM(
			CASE 
				WHEN b.memid=0 
				THEN b.slots*f.guestcost 
				ELSE b.slots*f.membercost
			END
		) as total_revenue
FROM `Facilities` f
JOIN `Bookings` b
ON f.facid = b.facid
GROUP BY f.name
HAVING total_revenue < 1000

/*
Output:

name		total_revenue
Pool Table	270.0
Snooker Table	240.0
Table Tennis	180.0
*/


