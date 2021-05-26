-- Link: https://leetcode.com/problems/employees-earning-more-than-their-managers/submissions/

/*

SUBMISSION LOGS - 

Runtime: 288 ms, faster than 95.18% of MySQL online submissions for Employees Earning More Than Their Managers.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees Earning More Than Their Managers.

*/

-- SUBMISSION:

select a.name as Employee
from Employee a
inner join Employee b
on  a.ManagerId = b.Id 
and a.Salary > b.Salary