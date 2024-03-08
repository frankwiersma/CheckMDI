# PyDefenderIdentityChecker - Microsoft Defender for Identity Instance Checker (Python Port)

This repository contains the Python port of the original PowerShell script "Microsoft Defender for Identity Instance Checker" developed by R. Roethof (Thalpius). The original PowerShell script is designed to check if there is a Microsoft Defender for Identity instance created by getting all accepted domains in Microsoft 365 using autodiscover, getting the tenant name, and checking if there is a Microsoft Defender for Identity instance. This Python port aims to provide the same functionality for users who prefer Python or need to integrate this check into a Python-based environment.

## Credits

All credit for the original concept, logic, and PowerShell script implementation goes to R. Roethof (Thalpius). The original PowerShell script can be found at the following link:

- [Original PowerShell Script by Thalpius](https://github.com/thalpius/Microsoft-Defender-for-Identity-Check-Instance/tree/main)

Special thanks to Thalpius for the development of the initial script and for the idea behind this tool.

## Python Port

This Python port was developed to provide an alternative for those who prefer Python or are working in environments where Python is the primary scripting language. While the core logic and functionality remain the same, certain adaptations were made to accommodate differences between PowerShell and Python.

## Usage

To use this Python port, you need Python 3 installed on your system. You can then run the script in a terminal or command prompt:

```bash
python3 PyDefenderIdentityChecker.py
```

You will be prompted to enter a domain name, and the script will perform the necessary checks to determine if a Microsoft Defender for Identity instance is running.

## Dependencies
This script requires the requests library to perform HTTP requests. You can install it using pip:

```bash
pip install requests
```

## Disclaimer
This script is provided "as is" without any warranties or guarantees. Users should use this script at their own risk. The author of the Python port is not responsible for any direct or indirect damage caused by the use of this script.

## License
This Python port is released under the MIT License. See the LICENSE file for details.

## Contributions
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, feel free to submit a pull request or open an issue.
