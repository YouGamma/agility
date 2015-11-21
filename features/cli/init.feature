Feature: `--init` option

    Use `--init` option on the command line to generate conventional directories and files
    for an agility project. It generates the followings:

    Directories: `features` | `features/support` | `features/step_definitions` | `spec`
    Files: `.agility` | `spec/spec_helper.py` | `features/support/environment.py`

    Scenario: Generate Files and Directories

        Scenario Outline: New File or Directory
            Given the <file_or_directory> does not exist
            When `--init` option is invoked
            Then the <file_or_directory> should be created
            And the message `<file_or_directory> created` should be displayed

            Examples:
            | file_or_directory               |
            | features                        |
            | features/support                |
            | features/step_definitions       |
            | spec                            |
            | .agility                        |
            | spec/spec_helper.py             |
            | features/support/environment.py |

        Scenario Outline: Existing File or Directory
            Given the <file_or_directory> exists
            When `--init` option is invoked
            Then the <file_or_directory> should not be created
            And the message `<file_or_directory> exists` should be displayed

            Examples:
            | file_or_directory               |
            | features                        |
            | features/support                |
            | features/step_definitions       |
            | spec                            |
            | .agility                        |
            | spec/spec_helper.py             |
            | features/support/environment.py |
