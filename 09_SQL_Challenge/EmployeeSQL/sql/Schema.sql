-- create tables and import data
CREATE TABLE departments (
	dept_no VARCHAR(10),
	dept_name VARCHAR(30)
);
--GO
--BULK INSERT departments
--FROM 

CREATE TABLE dept_emp (
	emp_no INT,
	dept_no VARCHAR(10)
);

CREATE TABLE dept_manager (
	dept_no VARCHAR(10),
	emp_no INT
);
CREATE TABLE employees (
	emp_no INT,
	emp_title_id VARCHAR(20),
	birth_date DATE,
	first_name VARCHAR(20),
	last_name VARCHAR(20),
	sex VARCHAR(10),
	hire_date DATE
);
CREATE TABLE salaries (
	emp_no INT,
	salary INT
);
CREATE TABLE titles (
	emp_no VARCHAR(20),
	title VARCHAR(30)
);