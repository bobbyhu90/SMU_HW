-- 1 employee data with employee number, last name, first name, gender, and salary
SELECT e.emp_no, e.last_name, e.first_name, e.sex, s.salary FROM employees AS e
JOIN salaries AS s ON e.emp_no=s.emp_no
ORDER BY emp_no;

-- 2 employees hired in 1986
SELECT * FROM employees
WHERE EXTRACT(year FROM hire_date) = 1986
ORDER BY hire_date;

-- 3 manager data with  department number, department name, the manager's employee number,
-- last name, first name, and start and end employment dates

SELECT m.dept_no, d.dept_name, m.emp_no, e.last_name, e.first_name FROM dept_manager AS m
JOIN departments AS d ON m.dept_no=d.dept_no
JOIN employees AS e ON m.emp_no=e.emp_no
ORDER BY dept_no;

-- 4employee data with employee number, last name, first name, and department name
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name FROM employees AS e
JOIN dept_emp ON e.emp_no=dept_emp.emp_no
JOIN departments AS d ON dept_emp.dept_no=d.dept_no
ORDER BY emp_no;

-- 5 employees whose first name is "Hercules" and last names begin with "B"
SELECT * FROM employees
WHERE first_name='Hercules' AND last_name LIKE 'B%'
ORDER BY emp_no;

-- 6 employees in the Sales department with employee number, last name, first name, and department name
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name FROM employees AS e
JOIN dept_emp ON e.emp_no=dept_emp.emp_no
JOIN departments AS d ON dept_emp.dept_no=d.dept_no
WHERE dept_name='Sales'
ORDER BY emp_no;

-- 7 employees in the Sales and Development departments with employee number, last name, first name, and department name
SELECT e.emp_no, e.last_name, e.first_name, d.dept_name FROM employees AS e
JOIN dept_emp ON e.emp_no=dept_emp.emp_no
JOIN departments AS d ON dept_emp.dept_no=d.dept_no
WHERE dept_name='Sales' OR dept_name='Development'
ORDER BY emp_no;

-- 8 employees with same last name
SELECT last_name, count(last_name) AS num_occurance FROM employees
GROUP BY last_name
ORDER BY num_occurance DESC;
