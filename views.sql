\c news

CREATE VIEW viewsByPath AS
	SELECT path, count(*) AS views
	FROM log
	GROUP BY path;


CREATE VIEW topArticles AS
	SELECT a.title as title, v.views
	FROM articles as a 
	LEFT JOIN viewsByPath as v
	ON '/article/' || a.slug = v.path
	ORDER BY views DESC
	LIMIT 3;


CREATE VIEW topAuthors AS
	SELECT authors.name as author, v.views
	FROM authors
	RIGHT JOIN articles
	ON authors.id = articles.author
	LEFT JOIN viewsByPath as v
	ON '/article/' || articles.slug = v.path
	ORDER BY views DESC
	LIMIT 3;


CREATE VIEW badDays AS
	SELECT date, to_char(float8(percent), 'FM999999999.00') as errpercent
	FROM
	(
		SELECT time::date as date, 
		(CAST(100 * count(CASE WHEN status != '200 OK' THEN 1 END) AS float)
		/ CAST(count(id) AS float)) AS percent
		FROM log
		GROUP BY time::date
	) data
	WHERE percent >= 1;