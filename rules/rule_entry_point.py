from mpp import Result 
def runRule(mpp): 
    res = Result()       
    try:
        maxSalary = 0
        for applicant in mpp.application.applicant :
            maxSalary = max(maxSalary, applicant.salary)
        if maxSalary > 100000:
            res.rate = 0.05
        else :
            res.rate = 0.06
        res.reference = "success"
        return res
    except Exception as e:
        res.reference = "error"
        return res


