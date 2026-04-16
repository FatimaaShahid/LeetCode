# Write your MySQL query statement below
select P.firstName,P.lastName,A.city ,A.state from
Person as P Left Join Address as A ON A.personId = P.personId;
