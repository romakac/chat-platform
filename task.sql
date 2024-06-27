-- a
SELECT DISTINCT ticket_client
FROM tickets t
WHERE t.csat < 3;

-- b
SELECT ticket_id
FROM tickets
WHERE text LIKE '%отлично%'
ORDER BY csat DESC;
