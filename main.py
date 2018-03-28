# -*- coding: utf-8-*-
from jira import JIRA

jira = JIRA(server='http://jira.lanzhu.xin', basic_auth=('tenstone', ''))
projects = jira.projects()
print(projects.encode('utf8'))