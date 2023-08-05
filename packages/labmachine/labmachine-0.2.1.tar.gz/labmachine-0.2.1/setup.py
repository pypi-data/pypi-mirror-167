# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['labmachine',
 'labmachine.io',
 'labmachine.providers.cloudflare',
 'labmachine.providers.google',
 'labmachine.providers.local']

package_data = \
{'': ['*'], 'labmachine': ['files/*']}

install_requires = \
['apache-libcloud>=3.6.0,<4.0.0',
 'click>=8.1.3,<9.0.0',
 'cryptography>=37.0.4,<38.0.0',
 'nanoid>=2.0.0,<3.0.0',
 'pydantic>=1.9.2,<2.0.0',
 'rich>=12.5.1,<13.0.0',
 'tomli-w>=1.0.0,<2.0.0',
 'tomli>=2.0.1,<3.0.0']

extras_require = \
{'gcs': ['smart-open>=6.0.0,<7.0.0', 'google-cloud-storage>=1.31.0,<2.0.0']}

entry_points = \
{'console_scripts': ['jupctl = labmachine.cli:cli']}

setup_kwargs = {
    'name': 'labmachine',
    'version': '0.2.1',
    'description': 'A simple creator of machines with Jupyterlab',
    'long_description': '# labmachine\n\nThis a POC about creating a jupyter instance on demand and registering it into a dns provider and HTTPS. \n\nRight now only works for Google Cloud but should be easy expand to other providers. \n\n\nFor examples, see [examples](examples/)\nThere you can see `infra_[cpu|gpu].py` and `lab_[cpu|gpu].py`\n\ninfra files are raw implementacion of the cluster library. \nlab files are abstractions built over this library for jupyter lab provisioning. \n\n\nFor authentication the google app cred variable should be defined:\n```\n./scripts/gce_auth_key.sh <ACCOUNT>@<PROJECT_ID>.iam.gserviceaccount.com\nmv gce.json ${HOME}/.ssh/gce.json\nexport GOOGLE_APPLICATION_CREDENTIALS=${HOME}/.ssh/gce.json\n```\n\nRun `gcloud iam service-accounts list` to see SA available in your project. \n\n### Suggested approach:\n\nIf you don\'t have a SA already created, you can take this strategy to create one and asign permissions to it.\n\n```\ngcloud iam service-accounts create labcreator\n    --description="Jupyter lab creator" \\\n    --display-name="lab-creator"\n```\n\nThen add the following roles to the account:\n\n- `roles/compute.instanceAdmin.v1`\n- `roles/iam.serviceAccountUser`\n- `roles/dns.admin` check https://cloud.google.com/dns/docs/access-control\n- `roles/artifactregistry.reader` If artifacts is used for pulling containers\n\n\nDNS role is needed only if the google dns provider is used\n\n**Warning**: those roles can be too permissive, please check [this for more information](https://cloud.google.com/compute/docs/access/iam)\n\n```\nroles="roles/compute.instanceAdmin.v1 roles/iam.serviceAccountUser"\nfor $perm in `cat $roles`; do\n\tgcloud projects add-iam-policy-binding PROJECT_ID \\\n  \t  --member="serviceAccount:labcreator@PROJECT_ID.iam.gserviceaccount.com" \\\n    \t--role=$perm\ndone\n``` \n\n## Destroy lab\n\n```\npython3 examples/destroy_lab.py\n```\n\n## Next work\n\nSee https://trello.com/b/F2Smw3QO/labmachine\n\n',
    'author': 'nuxion',
    'author_email': 'nuxion@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/nuxion/labmachine',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
