\c news


-- What are the three most popular articles of all time?

CREATE VIEW topNews AS
	SELECT a.title as title, count(l.id) as views
	FROM articles as a LEFT JOIN log as l
	ON a.slug = split_part(l.path, '/', 3)
	GROUP BY title 
	ORDER BY views DESC
	LIMIT 3;

-- What are the three most popular authors of all time?

CREATE VIEW topAuthors AS
	SELECT authors.name as author, count(log.id) as views
	FROM authors
	RIGHT JOIN articles
	ON authors.id = articles.author
	LEFT JOIN log
	ON articles.slug = split_part(log.path, '/', 3)
	GROUP BY authors.name
	ORDER BY views DESC
	LIMIT 3;

-- List of days by number of requests

CREATE VIEW requestsByDate AS
	SELECT time::date as date, count(id) as requests
	FROM log
	GROUP BY date
	ORDER BY requests DESC;

-- List of days by number of failures

CREATE VIEW failuresByDate AS
	SELECT time::date as date, count(id) as failures
	FROM log
	WHERE status != '200 OK'
	GROUP BY date
	ORDER BY failures DESC;

-- List of days where bad request are >= 1%

CREATE VIEW badDays AS
	SELECT f.date, (100*f.failures/r.requests) as errpercent
	FROM failuresByDate as f RIGHT JOIN requestsByDate as r
	ON f.date = r.date
	WHERE (100*f.failures/r.requests) >= 1;