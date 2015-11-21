## New File or Directory

@given("/^the (.*) does not exist$/")
def step_implementation(arg1):
  pass

@when("/^`--init` option is invoked$/")
def step_implementation():
  pass

@then("/^the (.*) should be created$/")
def step_implementation(arg1):
  pass

@then("/^the message `(.*) created` should be displayed$/")
def step_implementation(arg1):
  pass

## Existing File or Directory

@given("/^the (.*) exist$/")
def step_implementation(arg1):
  pass

@then("/^the (.*) should not be created$/")
def step_implementation(arg1):
  pass

@then("/^the message `(.*) exists` should be displayed$/")
def step_implementation(arg1):
  pass
