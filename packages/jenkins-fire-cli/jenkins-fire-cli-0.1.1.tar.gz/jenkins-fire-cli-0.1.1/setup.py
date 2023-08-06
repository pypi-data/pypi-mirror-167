# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jenkins_fire_cli']

package_data = \
{'': ['*']}

install_requires = \
['fire>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['jenkins-fire-cli = jenkins_fire_cli.main:main']}

setup_kwargs = {
    'name': 'jenkins-fire-cli',
    'version': '0.1.1',
    'description': '',
    'long_description': '# jenkins-fire-cli\nA Jenkins command line tool built with python-fire that wraps the jenkins-cli and job-dsl-core.\n\n## Prerequisite \nYou need to ensure `Java` and `Python>=3.8` are in the PATH to use this tool. \n\n## Install\nIt can be installed by the following command.\n```bash\npip install jenkins-fire-cli\n```\n\n## Get Started\n\n### Provision\nYou need to set Jenkins site url and user credential for the first time\n\n```bash\njenkins-fire-cli config set jenkins.url http://your-jenkins-site\njenkins-fire-cli config set user.name john.doe\n\n# user.token is optional, but you will be asked to type it when it is missing\n# either api token or user\'s password will be OK, but it\'s recommneded to use token for the sake of security\njenkins-fire-cli config set user.token passw0rd \n```\n\nBefore you start to run Jenkins commands, don\'t forget to run the `init` command for the first time, which will download `jenkins-cli.jar` and `job-dsl-core-standalone.jar` automatically.\n\n```bash\njenkins-fire-cli init\n```\n\n### Run jenkins-cli commnads\nAs `jenkins-fire-cli` is a wrapper of `jenkins-cli` and `job-dsl-core` to make them easier to use, \nyou can find the document of `jenkins-cli` in your Jenkins site or run the following command to open in browser.\n\n```bash\njenkins-fire-cli doc --open\n```\n\nYou can use the `run` sub-command to execute `jenkins-cli` command, for example\n\n```bash\njenkins-fire-cli run list-jobs  \n# It is equivalent to "java -jar jenkins-cli.jar -s http://localhost:9090/ -webSocket list-jobs"\n\n# For command with multiple arguments you need to quote them with ""\njenkins-fire-cli run "get-job my-job"  \n```\n\n### Run job-dsl commands\n\nYou can also run the `job-dsl` command. For example you have a `job-dsl` script with the following content.\n\n```groovy\n// file: /tmp/sample.dsl\npipelineJob(\'job-dsl-plugin\') {\n  definition {\n    cpsScm {\n      scm {\n        git {\n          remote {\n            url(\'https://github.com/jenkinsci/job-dsl-plugin.git\')\n          }\n          branch(\'*/master\')\n        }\n      }\n      lightweight()\n    }\n  }\n}\n```\n\nThen you can run the following command to generate the job XML configuration.\n\n```bash\njenkins-fire-cli dsl /tmp/sample-dsl.groovy\n```\n\nThen you will find a file named `job-dsl-plugin.xml` is generated. \nNow you can run anthor command to create this job in jenkins:\n\n```bash\njenkins-file-cli run \'create-job job-dsl-plugin\' < job-dsl-plugin.xml\n```\n\nThen you will find a new job named `job-dsl-plugin` has been created in jenkins.\n\n### Environment Variables\n\nIf you want to use this tool in CI system, you may use the following environment variable instead of global setting.\n\n* `JENKINS_USER_ID`: equivalent to `user.name`\n* `JENKINS_API_TOKEN`: equvalent to `user.token`\n* `JENKINS_URL`: equvalent to `jenkins.url`\n* `JENKINS_JOB_DSL_PATH`: path to the job-dsl jar package, you may skip `init` when this is set \n* `JNEKINS_CLI_PATH`: path to the jenkins-cli jar package, you may skip `init` when this is set \n',
    'author': 'weihong.xu',
    'author_email': 'xuweihong.cn@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
