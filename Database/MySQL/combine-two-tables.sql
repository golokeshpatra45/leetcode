-- LINK : https://leetcode.com/problems/combine-two-tables/
/*

SUBMISSION LOGS - 

Runtime: 392 ms, faster than 22.63% of MySQL online submissions for Combine Two Tables.
Memory Usage: 0B, less than 100.00% of MySQL online submissions for Combine Two Tables.

*/

-- MYSQL SOLUTION :

select a.FirstName,a.LastName,b.City,b.State
from Person a
left join Address b on a.PersonId = b.PersonId