
-- PART 1: DATABASE SETUP

CREATE TABLE IF NOT EXISTS user_activity (
    user_id INT,
    event_type VARCHAR(20),
    amount INT,
    event_time TIMESTAMP
);

INSERT INTO user_activity VALUES
(1, 'login', 0, '2024-01-01 10:00:00'),
(1, 'purchase', 200, '2024-01-01 11:00:00'),
(1, 'login', 0, '2024-01-02 09:00:00'),
(2, 'login', 0, '2024-01-01 10:30:00'),
(2, 'purchase', 500, '2024-01-03 12:00:00'),
(3, 'login', 0, '2024-01-02 14:00:00');

-- Display all records
SELECT * FROM user_activity;

-- Total rows
SELECT COUNT(*) AS total_rows FROM user_activity;



-- PART 2: SQL – WINDOW FUNCTIONS


-- Task 1: Count total events per user
SELECT user_id, COUNT(*) AS total_events
FROM user_activity
GROUP BY user_id;


-- Task 2: Ranking purchase transactions per user
SELECT *,
       RANK() OVER (PARTITION BY user_id ORDER BY amount DESC) AS rnk,
       DENSE_RANK() OVER (PARTITION BY user_id ORDER BY amount DESC) AS dense_rnk,
       ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY amount DESC) AS row_num
FROM user_activity
WHERE event_type = 'purchase';


-- Task 3: Latest activity per user
SELECT *
FROM (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY user_id
               ORDER BY event_time DESC
           ) AS LATEST
    FROM user_activity
) t
WHERE LATEST = 1;


-- Task 4: Analytical Functions

-- Previous purchase amount
SELECT user_id, event_time, amount,
       LAG(amount, 1, 0) OVER (
           PARTITION BY user_id
           ORDER BY event_time
       ) AS prev_amount
FROM user_activity;

-- Next event time
SELECT user_id, event_time,
       LEAD(event_time, 1) OVER (
           PARTITION BY user_id
           ORDER BY event_time
       ) AS next_event_time
FROM user_activity;


-- Task 5: CTE

WITH purchase_cte AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY user_id
               ORDER BY event_time DESC
           ) AS rn
    FROM user_activity
    WHERE event_type = 'purchase'
)
SELECT *
FROM purchase_cte;
