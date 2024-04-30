
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
![2-1_create database](https://github.com/angelc1997/bootcamp/assets/162414402/f13bea99-518d-4447-8b28-f4b287dd4520)


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
![2-2_create table](https://github.com/angelc1997/bootcamp/assets/162414402/9f3ad80d-14a7-4ced-8bfc-f9e36f85af3e)




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
![3-1_add data](https://github.com/angelc1997/bootcamp/assets/162414402/41b805f4-9657-47e3-b5ae-2311cbba5710)


➡️ Select all rows from member table

```
   SELECT * FROM member;
```
![3-2_select all](https://github.com/angelc1997/bootcamp/assets/162414402/a8c6d2f6-a48b-4999-aa33-8562aef2a8b7)


➡️ Select all rows in descending order of time

```
SELECT * FROM member ORDER BY time DESC;
```
![3-3 select all in desc](https://github.com/angelc1997/bootcamp/assets/162414402/31173c86-5146-41c3-b777-4db17cf87093)

➡️ Select 2 to 4 rows in descending order of time

```
SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
```
![3-4_select 2-4](https://github.com/angelc1997/bootcamp/assets/162414402/9ca55a2d-bada-4436-aa05-f2198d49f064)

➡️ Select username equals to test

```
SELECT * FROM member WHERE username = 'test';
```
![3-5_test username](https://github.com/angelc1997/bootcamp/assets/162414402/6f68d628-8b83-478b-a328-ad9d9dc82f19)

➡️ Select name includes "es" word

```
SELECT * FROM member WHERE name LIKE '%es%';
```
![3-6_name including es](https://github.com/angelc1997/bootcamp/assets/162414402/b500d11f-769b-4e18-9ada-a8c280e76568)


➡️ Select username and password euqal to test

```
SELECT * FROM member WHERE username = 'test' and password = 'test';
```
![3-7_username and password](https://github.com/angelc1997/bootcamp/assets/162414402/92f4839a-0748-45ba-8d11-dbcb616aecdc)


➡️ Update username which equals to test to 'test2';

```
UPDATE member SET name = 'test2' WHERE username = 'test';
```
![3-8_update name](https://github.com/angelc1997/bootcamp/assets/162414402/357ce9da-d94d-4969-840d-3ac796e299e0)


## 🚀 Write aggregation function statements

➡️ Count rows

```
SELECT COUNT(*) FROM member;
```
![4-1_count rows](https://github.com/angelc1997/bootcamp/assets/162414402/f0e3601d-1d0a-4240-8626-cca6647bc4a9)


➡️ Sum all follow_count 

```
SELECT SUM(follower_count) FROM member;
```
![4-2_sum  all](https://github.com/angelc1997/bootcamp/assets/162414402/b80921b1-eae5-4c7e-95ee-6c0bd644a9d6)


➡️ Average all follower_count

```
SELECT AVG(follower_count) FROM member;
```
![4-3_ average all](https://github.com/angelc1997/bootcamp/assets/162414402/93327962-48d8-4ceb-a288-ab93abea1ed3)


➡️ Average 2 first follower_count which in descending order

```
SELECT AVG(follower_count) AS avg_follower 
FROM (SELECT follower_count FROM member ORDER BY follower_count DESC LIMIT 2) AS subquery;
```
![4-4_average first 2](https://github.com/angelc1997/bootcamp/assets/162414402/3605085f-c313-486c-ad03-ec8b7bbb901f)


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
![5-1 create table](https://github.com/angelc1997/bootcamp/assets/162414402/b13048ba-a02a-4fab-bec7-30633c33d78c)


➡️ Select messages, including sender names

```
SELECT message.*, member.name AS sender
FROM message
INNER JOIN member ON messsage.member_id = member.id;
```
![5-2_select all](https://github.com/angelc1997/bootcamp/assets/162414402/7de3b4bd-7d5f-4edc-85e1-3865c2984490)


➡️ Select messages, including sender names, where username is 'test'

```
SELECT message.*, member.name AS sender
FROM message
INNER JOIN member ON message.member_id = member.id WHERE member.username = 'test';
```
![5-3_select test username](https://github.com/angelc1997/bootcamp/assets/162414402/b5882acd-537a-41a7-9f31-2096440a6951)


➡️ Select messages and get average like count where sender is 'test'

```
SELECT username, AVG(sub.like_count) AS avg_likecount
FROM (SELECT message.*, member.username FROM message
INNER JOIN member ON message.member_id = member.id
WHERE member.username = 'test') AS sub
```
![5-4_average like count](https://github.com/angelc1997/bootcamp/assets/162414402/caccf494-c08d-463f-9dae-cd5a0b46b696)


➡️ Get average like count GROUP BY sender username

```
SELECT username, AVG(sub.like_count) AS avg_likecount
FROM (SELECT message.*, member.username FROM message
INNER JOIN member ON message.member_id = member.id)
AS sub GROUP BY sub.username;
```
![5-5_group by username](https://github.com/angelc1997/bootcamp/assets/162414402/aa8de1ee-af7d-4136-9943-31c46b1e3d49)


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
