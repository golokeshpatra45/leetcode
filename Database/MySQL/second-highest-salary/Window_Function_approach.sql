-- Link: https://leetcode.com/problems/second-highest-salary/submissions/

/*
SUBMISSION LOGS - 

Runtime: 183 ms, faster than 67.15% of MySQL online submissions for Second Highest Salary.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Second Highest Salary.

*/

--MYSQL Solution : 

select IFNULL(
         (select a.Salary from 
(
    select  b.Salary, 
    row_number() over (order by b.Salary desc) as rnk
    from (select distinct salary from Employee) b
)a where a.rnk = 2),
    NULL) as SecondHighestSalary;