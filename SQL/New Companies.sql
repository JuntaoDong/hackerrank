SELECT C.company_code, C.founder, COUNT(DISTINCT(LM.lead_manager_code)), COUNT(DISTINCT(SM.senior_manager_code)), COUNT(DISTINCT(M.manager_code)), COUNT(DISTINCT(E.employee_code))
FROM COMPANY C, LEAD_MANAGER LM, SENIOR_MANAGER SM, MANAGER M, EMPLOYEE E
WHERE C.company_code = LM.company_code AND LM.lead_manager_code = SM.lead_manager_code AND SM.senior_manager_code = M.senior_manager_code AND M.manager_code = E.manager_code
GROUP BY 1,2
ORDER BY 1;