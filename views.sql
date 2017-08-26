\c news


CREATE VIEW topArticles AS
	SELECT a.title as title, count(l.id) as views
	FROM articles as a LEFT JOIN log as l
	ON a.slug = split_part(l.path, '/', 3)
	GROUP BY title 
	ORDER BY views DESC
	LIMIT 3;


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


CREATE VIEW badDays AS
	SELECT date, errpercent
	FROM
	(
		SELECT time::date as date, ( 100 * count(
			CASE WHEN status != '200 OK' THEN 1 END) / count(id) ) as errpercent
		FROM log
		GROUP BY time::date
	) data
	WHERE errpercent >= 1;