-- Link: https://leetcode.com/problems/second-highest-salary/submissions/

/*
SUBMISSION LOGS - 

Runtime: 167 ms, faster than 92.47% of MySQL online submissions for Second Highest Salary.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Second Highest Salary.

*/

--MYSQL Solution : 

select 
IFNULL(
(select distinct Salary  from Employee
order by Salary desc
limit 1 offset 1),
    NULL) as SecondHighestSalary;