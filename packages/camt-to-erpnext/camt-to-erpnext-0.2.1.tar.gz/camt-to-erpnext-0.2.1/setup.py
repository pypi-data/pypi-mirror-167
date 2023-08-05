# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['camt_to_erpnext']

package_data = \
{'': ['*']}

install_requires = \
['typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['camt-to-erpnext = camt_to_erpnext.main:app']}

setup_kwargs = {
    'name': 'camt-to-erpnext',
    'version': '0.2.1',
    'description': '',
    'long_description': 'This CLI can convert a CAMT CSV file (provided by your bank) into a normal CSV file that can be used for importing **Bank Transactions** into ERPNext.\n\nUsage:\n\n```\ncamt-to-erpnext convert IN_PATH OUT_PATH\n```\n\n### Input format\n\n- Delimiter: `;`\n- Quoting: all columns quoted\n- Date Format: `28.02.99`\n- Number Format: `-1234,56`\n- Encoding: `cp1252`\n- Columns:\n    - Auftragskonto\n    - Buchungstag\n    - Valutadatum\n    - Buchungstext\n    - Verwendungszweck\n    - Glaeubiger ID\n    - Mandatsreferenz\n    - Kundenreferenz (End-to-End)\n    - Sammlerreferenz\n    - Lastschrift Ursprungsbetrag\n    - Auslagenersatz Ruecklastschrift\n    - Beguenstigter/Zahlungspflichtiger\n    - Kontonummer/IBAN\n    - BIC (SWIFT-Code)\n    - Betrag\n    - Waehrung\n    - Info\n\n### Output format:\n\n- Delimiter: `,`\n- Quoting: where necessary\n- Date Format: `1999-02-28`\n- Number Format: `1234.56`\n- Encoding: `utf-8`\n- Columns:\n    - Date\n\n        "Buchungstag" of the input file, converted to ISO-format\n\n    - Deposit\n\n        "Betrag" of the input file (if > 0)\n\n    - Withdrawal\n\n        Absolute "Betrag" of the input file (if < 0)\n\n    - Description\n\n        The following columns of the input file: "Beguenstigter/Zahlungspflichtiger", "Verwendungszweck", "Kontonummer/IBAN", "BIC (SWIFT-Code)", "Glaeubiger ID", "Mandatsreferenz", "Kundenreferenz (End-to-End)", "Valutadatum"\n\n    - Reference Number\n\n        Hash of the following columns of the input file "Buchungstag", "Betrag", "Verwendungszweck", "Kontonummer/IBAN", "BIC (SWIFT-Code)".\n\n    - Bank Account\n\n        "Auftragskonto" of the input file\n\n    - Currency\n\n        "Waehrung" of the input file\n',
    'author': 'barredterra',
    'author_email': '14891507+barredterra@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
