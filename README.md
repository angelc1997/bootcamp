
# MySQL Data Storage

Here is WeHelp bootcamp task for Using Command Line to accomplish MySQL instructions.


## 🖥️ Install MySQL server

🔗 [MySQL Download Link](https://dev.mysql.com/downloads/mysql/)



## 🖥️ Connect to Local Server

Change directory to bin directory to find MySQL programs

```
  cd C:\Program Files\MySQL\MySQL Server 8.0\bin
```

Log in with user and password
```
  mysql -u root -p
```

Connect to MySQL server and get mysql command prompt

```
  mysql>
```

## 🚀 Create database and table

✅ Database name：website 

✅ Table name：member

| Column Name | Description | 
| :-------- | :------- | 
| `id` | Unique ID |
| `name` | User Fullname |
| `username` | User Nickname |
| `password` | User Password |
| `follower_count` | Follower Count |
| `time` | Signup time |



➡️ Create database
```
CREATE DATABASE website;
```

➡️ Create table
```
CREATE TABLE member(
    -> id bigint PRIMARY KEY AUTO_INCREMENT,
    -> name varchar(255) NOT NULL,
    -> username varchar(255) NOT NULL,
    -> password varchar(255) NOT NULL,
    -> follower_count int unsigned NOT NULL DEFAULT 0,
    -> time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP);
```




## 🚀 Write CRUD statements

➡️ Add 5 data in member table

```
  INSERT INTO member (name, username, password) VALUES ('test', 'test', 'test');
```
```
  INSERT INTO member (name, username, password) VALUES ('aimer', 'aimer', 'aimer12');
```
```
  INSERT INTO member (name, username, password) VALUES ('LEO','leo', 'lionleo');
```
```
  INSERT INTO member (name, username, password) VALUES ('Jacky', 'jacky', 'jack0941');
```
```
  INSERT INTO member (name, username, password) VALUES ('wendy', 'wendy', '09412345');
```


➡️ Select all rows from member table

```
   SELECT * FROM member;
```


➡️ Select all rows in descending order of time

```
SELECT * FROM member ORDER BY time DESC;
```

➡️ Select 2 to 4 rows in descending order of time

```
SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
```

➡️ Select username equals to test

```
SELECT * FROM member WHERE username = 'test';
```

➡️ Select name includes "es" word

```
SELECT * FROM member WHERE name LIKE '%es%';
```

➡️ Select username and password euqal to test

```
SELECT * FROM member WHERE username = 'test' and password = 'test';
```

➡️ Update username which equals to test to 'test2';

```
UPDATE member SET username = 'test2' WHERE id = 1;
```


## 🚀 Write aggregation function statements

➡️ Count rows

```
SELECT COUNT(*) FROM member;
```

➡️ Sum all follow_count 

```
SELECT SUM(follower_count) FROM member;
```

➡️ Average all follower_count

```
SELECT AVG(follower_count) FROM member;
```

➡️ Average 2 first follower_count which in descending order

```
SELECT AVG(follower_count) AS avg_follower 
FROM (SELECT follower_count FROM member ORDER BY follower_count DESC LIMIT 2) AS subquery;
```

## 🚀 Write joinable table statements

✅ Table name：message

| Column Name | Description | 
| :-------- | :------- | 
| `id` | Unique ID |
| `member_id` | Foreign key |
| `content` | Buyer Message |
| `like_count` | Rating |
| `time` | Publish time |


➡️ Create table

```
CREATE TABLE message(
  id bigint PRIMARY KEY AUTO_INCREMENT,
  member_id bigint NOT NULL,
  FOREIGN KEY (member_id) REFERENCES member(id),
  content varchar(255) NOT NULL,
  like_count int unsigned NOT NULL DEFAULT 0,
  time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP);
```

➡️ Select messages, including sender names

```
SELECT message.*, member.name AS sender
FROM message
INNER JOIN member ON messsage.member_id = member.id;
```

➡️ Select messages and get average like count where sender is 'test'

```
SELECT message.*, member.name AS sender
FROM message
INNER JOIN member ON message.member_id = member.id WHERE member.username = 'test';
```

➡️ Get average like count GROUP BY sender username

```
SELECT username, AVG(sub.like_count) AS avg_likecount
FROM (SELECT message.*, member.username FROM message INNER JOIN member ON message.member_id = member.id)
AS sub GROUP BY sub.username;
```

## 🚀 Export database

✅ Export file name：data.sql

Change directory to bin directory to find MySQL programs

```
  cd C:\Program Files\MySQL\MySQL Server 8.0\bin
```

Use mysqldump to export specific database

```
mysqldump -u root -p website member message > D:\F2E beginner project\WeHelp\data.sql
```
