DROP DATABASE IF EXISTS UniManagement;
CREATE DATABASE UniManagement;
use UniManagement;

create table dept(
    dept_id varchar(5),
    dname varchar(50),
    primary key(dept_id)
);

create table student(
    id varchar(13),
    fname varchar(20),
    mname varchar(20),
    lname varchar(20),
    dob date,
    gender enum('M','F','O'),
    email varchar(20),
    phone varchar(10),
    address varchar(50),
    tenth int,
    twelth int,
    qemarks int, 
    qeexam varchar(20),
    fee int,
    join_year year,
    did varchar(5),
    hos enum('Y','N'),
    unit_no int,
    room_no int,
    primary key(id),
    foreign key(did) references dept(dept_id)
);

create table guardian(
    gname varchar(30),
    rel varchar(20),
    gemail varchar(20),
    designation varchar(30),
    gphone varchar(10),
    gaddr varchar(50),
    age int, 
    gsrn varchar(13),
    alum enum('Y','N') ,
    ggender enum('M','F','O'),
    foreign key(gsrn) references student(id)
);

alter table guardian add constraint pk_g primary key(gsrn,gemail);

create table mentor(
    mid varchar(6),
    mname varchar(30),
    memail varchar(20),
    mphone varchar(10),
    mdid varchar(5),
    primary key(mid),
    foreign key(mdid) references dept(dept_id)
);

create table sgpa(
    sid varchar(13),
    sgpa1 float(4,2),
    sgpa2 float(4,2),
    sgpa3 float(4,2),
    sgpa4 float(4,2),
    sgpa5 float(4,2),
    sgpa6 float(4,2),
    sgpa7 float(4,2),
    sgpa8 float(4,2),
    cgpa float(4,2),
    scholarship varchar(5),
    foreign key(sid) references student(id)
);

alter table sgpa add constraint sg_pk primary key(sid);

create table fam(
    ssid varchar(13),
    mmid varchar(5),
    foreign key(ssid) references student(id), 
    foreign key(mmid) references mentor(mid)
);

alter table fam add constraint prim_key primary key(ssid,mmid);

create table register_w(
    email varchar(20),
    password varchar(8),
    role enum('Teacher','Student','Accounts')
);

-- values --
INSERT INTO dept VALUES('AI&ML','Artificial Intelligence and Machine Learning'),
                        ('CSE','Computer Science and Engineering'),
                        ('ECE','Electronics and Communication Engineering'),
                        ('EEE','Electrical Engineering'),
                        ('ME','Mechanical Engineering');

INSERT INTO student(id,fname,lname,dob,gender,email,phone,address,tenth,twelth,qemarks,qeexam,fee,join_year,did,hos,unit_no,room_no)
            VALUES('CS###','Nammi','C V','2003-09-26','F','nam@gmail.com','9874563210','mangalore',100,100,1,'CET',112573,2021,'CSE','Y','2','114');

INSERT INTO student(id,fname,lname,dob,gender,email,phone,address,tenth,twelth,qemarks,qeexam,fee,join_year,did,hos) VALUES
                    ('CS###','Harika','H','2002-04-26','F','haru@gmail.com','9845675210','Bangalore',99,98,698,'JESSAT',320000,2020,'CSE','N'),
                    ('CS###','Disha','M R','2003-04-29','F','disha@gmail.com','9874561214','fhgjh',99,98,1920,'CET',112573,2021,'CSE','N'),
                    ('CS###','N','Bayathri','2004-01-23','F','gayu@gmail.com','7777777777','Andhra',100,100,1,'CET',112573,2021,'CSE','N'),
                    ('EC###','Disha','R M','2003-04-17','F','drisha@gmail.com','8856236541','Bangalore',95,99,2205,'CET',112573,2021,'ECE','N'),
                    ('EC###','Parvathy','Remesh','2003-04-05','F','paru@gmail.com','9985632415','Bangalore',99,100,2000,'CET',112573,2021,'ECE','N'),
                    ('ME###','Deepashree','D','2003-05-26','F','deepu@gmail.com','7845123690','Bangalore',85,98,11100,'CET',112573,2021,'ME','N');

INSERT INTO guardian VALUES('Malathi','Mother','mal@gmail.com','Teacher','9978456321','Mangalore',45,'CS###','N','F'),
                            ('Kala','Mother','mkala@gmai.com','Merchandiser','9999093892','Bangalore',49,'CS###','N','F'),
                            ('K Rathnam','Mother','kasi@gmail.com','Teacher','7878787878','Andhra',40,'CS###','N','F'),
                            ('Ravi Kumar','Father','ravi@gmail.com','Professor','9999999992','Bangalore',55,'EC###','N','M'),
                            ('Remesh','Father','remes@gmail.com','Civil Engineer','9898989895','Bangalore',56,'EC###','Y','M'),
                            ('Dinesh','Father','dini@gmail.com','Contractor','8989898985','Bangalore',57,'ME###','Y','M');

INSERT INTO mentor VALUES('TAIML1','Rani','ranu@gmail.com','8756941230','AI&ML'),
                        ('TCS1','Farhana','farha@gmail.com','7896325410','CSE'),
                        ('TCS2','Manjula','mannju@gmail.com','7896541202','CSE'),
                        ('TEC12','Smriti','smriti@gmail.com','7889654123','ECE'),
                        ('TEC3','Shubha','sub@gmail.com','9874525361','ECE'),
                        ('TME1','Basavaraj','basu@gmail.com','9789789787','ME');

INSERT INTO sgpa (sid,sgpa1,sgpa2,sgpa3,sgpa4) VALUES
                ('CS###',9.08,9.08,9.52,9.63),
                ('CS###',9.00,7.20,8.30,7.60),
                ('CS###',9.32,9.82,9.41,9.82),
                ('CS###',10.00,10.00,10.00,10.00),
                ('EC###',9.00,9.80,9.80,9.90),
                ('EC###',9.63,9.64,9.50,9.82),
                ('ME###',9.53,8.60,8.30,8.00);

INSERT INTO fam VALUES('CS###','TCS1'),
                        ('CS###','TCS1'),
                        ('CS###','TCS2'),
                        ('EC###','TEC12'),
                        ('EC###','TEC3'),
                        ('ME###','TME1');

INSERT INTO register_w VALUES('admin@gmail.com','admin','Accounts'),
                            ('aruna@gmail.com','aruna','Accounts'),
                            ('bhavana@gmail.com','bhavana1','Teacher'),
                            ('deepu@gmail.com','deepa','Student'),
                            ('disha@gmail.com','disha','Student'),
                            ('drisha@gmail.com','drisha','Student'),
                            ('farha@gmail.com','farhana','Teacher'),
                            ('haru@gmail.com','harika','Student'),
                            ('mannju@gmail.com','manjul','Teacher'),
                            ('paru@gmail.com','parvat','Student'),
                            ('ranu@gmail.com','Rani','Teacher'),
                            ('smriti@gmail.com','smriti','Teacher'),
                            ('sub@gmail.com','subbi','Teacher');
                            
-- functions --

DELIMITER &&
CREATE TRIGGER before_student_insert
BEFORE INSERT ON student
FOR EACH ROW
BEGIN
  IF EXISTS (SELECT 1 FROM student WHERE id = NEW.id) THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Student with the same sid already exists';
  END IF;
END&&
DELIMITER ;

DELIMITER &&
CREATE DEFINER=`root`@`localhost` FUNCTION `GetNumberOfSids`(mid varchar(7)) RETURNS int
    DETERMINISTIC
BEGIN
    DECLARE NumberOfSids INT;
    SELECT COUNT(ssid) INTO NumberOfSids
    FROM fam
    WHERE mid = mmid;
    RETURN NumberOfSids;
END&&
DELIMITER ;

DELIMITER &&
CREATE DEFINER=`root`@`localhost` PROCEDURE calculate_average_grade(IN sgpa1 float(4,2),IN sgpa2 float(4,2),IN sgpa3 float(4,2),IN sgpa4 float(4,2),IN sgpa5 float(4,2),IN sgpa6 float(4,2),IN sgpa7 float(4,2),IN sgpa8 float(4,2), OUT grade DECIMAL(4,2),OUT scholarship varchar(5))
BEGIN
    DECLARE avg_sgpa DECIMAL(4,2);
    
    SET avg_sgpa=(
        COALESCE(sgpa1, 0) +
        COALESCE(sgpa2, 0) +
        COALESCE(sgpa3, 0) +
        COALESCE(sgpa4, 0) +
        COALESCE(sgpa5, 0) +
        COALESCE(sgpa6, 0) +
        COALESCE(sgpa7, 0) +
        COALESCE(sgpa8, 0)
    ) / 
    (
        CASE WHEN sgpa1 IS NOT NULL THEN 1 ELSE 0 END +
        CASE WHEN sgpa2 IS NOT NULL THEN 1 ELSE 0 END +
        CASE WHEN sgpa3 IS NOT NULL THEN 1 ELSE 0 END +
        CASE WHEN sgpa4 IS NOT NULL THEN 1 ELSE 0 END +
        CASE WHEN sgpa5 IS NOT NULL THEN 1 ELSE 0 END +
        CASE WHEN sgpa6 IS NOT NULL THEN 1 ELSE 0 END +
        CASE WHEN sgpa7 IS NOT NULL THEN 1 ELSE 0 END +
        CASE WHEN sgpa8 IS NOT NULL THEN 1 ELSE 0 END
    );

    SET grade=avg_sgpa;

    IF avg_sgpa > 9.5 THEN
        SET scholarship = 'C';
    ELSEIF avg_sgpa >= 9 AND avg_sgpa <= 9.5 THEN
        SET scholarship = 'D';
    ELSE
        SET scholarship = 'N/A';
    END IF;
END&&
DELIMITER ;


DELIMITER &&
CREATE DEFINER='root'@'localhost' TRIGGER sgpa_insert
    BEFORE INSERT ON UniManagement.sgpa
    FOR EACH ROW
BEGIN
    CALL calculate_average_grade(NEW.sgpa1,NEW.sgpa2,NEW.sgpa3,NEW.sgpa4,NEW.sgpa5,NEW.sgpa6,NEW.sgpa7,NEW.sgpa8,@avg_gpa,@scholarship);
    SET NEW.cgpa=@avg_gpa;
    SET NEW.scholarship=@scholarship;
END&&
DELIMITER ;

DELIMITER &&
CREATE DEFINER='root'@'localhost' TRIGGER sgpa_update
    BEFORE UPDATE ON UniManagement.sgpa
    FOR EACH ROW
BEGIN
    CALL calculate_average_grade(NEW.sgpa1,NEW.sgpa2,NEW.sgpa3,NEW.sgpa4,NEW.sgpa5,NEW.sgpa6,NEW.sgpa7,NEW.sgpa8,@avg_gpa,@scholarship);
    SET NEW.cgpa=@avg_gpa;
    SET NEW.scholarship=@scholarship;
END&&
DELIMITER ;


DELIMITER &&
CREATE DEFINER=`root`@`localhost` PROCEDURE `allocatef`(sid varchar(13))
BEGIN
 DECLARE vari VARCHAR(7);
    DECLARE c INT;
    DECLARE mid_found INT DEFAULT 0;
    
    -- Declare a cursor to fetch multiple rows from the SELECT statement
    DECLARE cur CURSOR FOR 
    SELECT mid, GetNumberOfSids(mid) AS c
    FROM mentor, student 
    WHERE student.did = mdid AND id = sid;
    
    -- Declare a handler for the cursor
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET mid_found = 1;
    
    -- Open the cursor
    OPEN cur;
    
    -- Loop to fetch and process rows
    fetch_loop: LOOP
        FETCH cur INTO vari, c;
        IF mid_found THEN
            LEAVE fetch_loop;  -- No suitable mid found, exit the loop
        END IF;
        
        IF c < 5 THEN
            -- Insert the found mid and sid into the fam table
            INSERT INTO fam (ssid, mmid) VALUES (sid, vari);
            LEAVE fetch_loop;  -- Exit the loop after the first successful insert
        END IF;
    END LOOP;
    
    -- Close the cursor
    CLOSE cur;
END&&
DELIMITER ;
