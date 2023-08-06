from json import dumps
from typing import List, Union
from yaml import safe_load
from jira import JIRA
from sys import exit

options  = {
  'help'   : ['-h', '--help'],
  'fetch'  : ['--fetch=', 'str'],
  'raw'    : ['-r', '--raw'],
}

# Utility: Print Issue Info
def printIssue(issue, new: bool, epic: bool, raw: bool):
  '''prints essential issue info'''
  if raw:
    print(dumps(issue.raw, sort_keys=True, indent=2))
  else:
    borderTailLength = 20
    if new:
      print(f"\n---NEW {issue.fields.issuetype.name.upper()}{'-'*(borderTailLength - len(issue.fields.issuetype.name))}")
    else:
      print(f"\n---EXISTING {issue.fields.issuetype.name.upper()}{'-'*(borderTailLength - len(issue.fields.issuetype.name) - 5)}")
    print(f"Key      | {issue.key}")
    print(f"Url      | {issue.self}")
    print(f"Type     | {issue.fields.issuetype.name}")
    print(f"Created  | {issue.fields.created}")
    print(f"Status   | {issue.fields.status}")
    print(f"Priority | {issue.fields.priority}")
    print(f"Branch   | git checkout -b [feature|bugfix]/{issue.key}_<name-of-feature>")
    print(f"MR       | git push origin [feature|bugfix]/{issue.key}_<name-of-feature> -o merge_request.create -o merge_request.target=<parent-branch>")
    if epic:
      print(f"Ticket created under parent: {issue.fields.parent.key}")
    print(f"\nOVERVIEW:\n{issue.fields.reporter} --> {issue.fields.assignee}")
    print(f"---Summary\n{issue.fields.summary}")
    print(f"---Description\n{issue.fields.description}\n")
  return

# Utility: Verify against all options
def verifyOption(args: List[str], options: dict) -> bool:
  '''Takes list of user arg strings and options dictionary.
Returns True if option flag exists and value matches required type, else False.'''
  res = []
  for arg in args:
    flag = False
    if '=' in arg:
      pretext = arg[:arg.index('=')+1]
      val = arg[arg.index('=')+1:]
      for optionTypeName in options:
        if options[optionTypeName][0] == pretext:
          if (options[optionTypeName][1] == 'int') and (val.isdigit()):
            flag = True
          elif (options[optionTypeName][1] == 'str') and (not val.isdigit()):
            flag = True
    else:
      for optionTypeName in options:
        for opFlag in options[optionTypeName]:
          if arg == opFlag:
            flag = True
    res.append(flag)
  return (False not in res)

# Utility: Check list overlap
def checkListOverlap(l1: List[str], l2: List[str]) -> bool:
  '''Takes 2 lists of strings.
Returns True if lists share elements, else False.'''
  return [i for i in l1 if i in l2] != []

# Utility : Get value from option input
def getOptionVal(args: List[str], key: List[str]) -> Union[str,int]:
  '''Takes list of user arg strings and list of option strings ([--myop=val,type]).
Returns val in it's intended type'''
  for arg in args:
    if key[0] in arg:
      val = arg[arg.index('=')+1:]
      if key[1].lower() == 'int':
        return int(val)
      elif key[1].lower() == 'str':
        return val
      else:
        return val

# Utility : Strip values from args
def stripOptionVals(args: List[str]) -> List[str]:
  '''Takes list of user arg strings.
Returns filtered list of all user args containing values, with said values stripped (equals sign is preserved).'''
  res = []
  for arg in args:
    if '=' in arg:
      res.append(arg[:arg.index('=')+1])
    else:
      res.append(arg)
  return res

# Worker: Fetch Specific Issue
def fetchIssue(agentPath: str, userArgs: List[str]):
  '''Takes user args and fetches issue data, accepts -r,--raw for full response dump'''
  with open(agentPath, 'r') as raw_agent:
    ### load config
    try:
      agent  = safe_load(raw_agent)
      domain   = agent['domain']
      userName = agent['userName']
      token    = agent['token']
      rawFlag  = checkListOverlap(userArgs, options['raw'])
    except Exception as e:
      print(f"Config error.\n{e}")
      exit(1)
    ### authenticate
    try:
      jira = JIRA(server=domain, basic_auth=(userName, token))
    except Exception as e:
      print(f"Authentication error.\n{e}")
      exit(1)
    ### parse user arg
    try:
      if checkListOverlap(stripOptionVals(userArgs), options['fetch']):
        val = getOptionVal(userArgs, options['fetch'])
    except Exception as e:
      print(f"Fetch value error.\n{e}")
      exit(1)
    issue = jira.issue(val)
    printIssue(issue=issue, new=False, epic=False, raw=rawFlag)
  return

# Worker: Create Issue
def createTicket(configPath: str, agentPath: str, summaryPath: str, descriptionPath: str, userArgs: List[str]):
  with open(summaryPath, 'r') as summary, open(descriptionPath, 'r') as description, open(configPath, 'r') as raw_config, open(agentPath, 'r') as raw_agent:
      ### load config
      try:
        summary     = summary.read()
        description = description.read()
        config      = safe_load(raw_config)
        project     = config['project']
        priority    = config['priority']
        epicKey     = config['epicKey']
        issueType   = config['issueType']
        reporter    = config['reporter']
        assignee    = config['assignee']
        agent       = safe_load(raw_agent)
        domain      = agent['domain']
        userName    = agent['userName']
        token       = agent['token']
        rawFlag     = checkListOverlap(userArgs, options['raw'])
        if (epicKey) and (issueType.lower() == 'epic'):
          print(f"Incompatible config values - can't attach epic to epic.")
          exit(1)
      except Exception as e:
        print(f"Config error.\n{e}")
        exit(1)
      ### authenticate
      try:
        jira = JIRA(server=domain, basic_auth=(userName, token))
      except Exception as e:
        print(f"Authentication error.\n{e}")
        exit(1)
      ### build ticket
      issue_blueprint_task = {
        'project'    : {'key': project},
        'summary'    : summary,
        'description': description,
        'issuetype'  : {'name': issueType},
        'priority'   : {'name': priority},
        'reporter'   : {'accountId': reporter},
        'assignee'   : {'accountId': assignee},
      }
      issue_blueprint_epic = {
        'project'    : {'key': project},
        'summary'    : summary,
        'description': description,
        'issuetype'  : {'name': issueType},
        'reporter'   : {'accountId': reporter},
        'assignee'   : {'accountId': assignee},
      }
      ### push ticket
      try:
        if issueType.lower() == 'task':
          if epicKey:
            issue_blueprint_task['parent'] = {'key': epicKey}
            newIssue = jira.create_issue(fields=issue_blueprint_task)
          else:
            newIssue = jira.create_issue(fields=issue_blueprint_task)
          printIssue(issue=newIssue, new=True, epic=False, raw=rawFlag)
          exit(0)
        elif issueType.lower() == 'epic':
          newIssue = jira.create_issue(fields=issue_blueprint_epic)
          printIssue(issue=newIssue, new=True, epic=True, raw=rawFlag)
          exit(0)
        else:
          print(f"issueType error - unsupported issue type.")
          exit(1)
      except Exception as e:
        print(f"Ticket publishing error.\n{e}")
  return
