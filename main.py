from jira import JIRA

jira = JIRA(server='http://jira.lanzhu.xin',basic_auth=('tenstone', 'Tenstone@123'))

print(jira)