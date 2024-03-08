import requests
from xml.etree import ElementTree
from termcolor import colored

def print_colored(message, color, attrs=[]):
    print(colored(message, color, attrs=attrs))

def get_accepted_domains(domain):
    print_colored("Start getting all accepted domains...", "yellow")
    body = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:exm="http://schemas.microsoft.com/exchange/services/2006/messages" 
        xmlns:ext="http://schemas.microsoft.com/exchange/services/2006/types" 
        xmlns:a="http://www.w3.org/2005/08/addressing" 
        xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" 
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap:Header>
        <a:RequestedServerVersion>Exchange2010</a:RequestedServerVersion>
        <a:MessageID>urn:uuid:6389558d-9e05-465e-ade9-aae14c4bcd10</a:MessageID>
        <a:Action soap:mustUnderstand="1">http://schemas.microsoft.com/exchange/2010/Autodiscover/Autodiscover/GetFederationInformation</a:Action>
        <a:To soap:mustUnderstand="1">https://autodiscover-s.outlook.com/autodiscover/autodiscover.svc</a:To>
        <a:ReplyTo>
            <a:Address>http://www.w3.org/2005/08/addressing/anonymous</a:Address>
        </a:ReplyTo>
    </soap:Header>
    <soap:Body>
        <GetFederationInformationRequestMessage xmlns="http://schemas.microsoft.com/exchange/2010/Autodiscover">
            <Request>
                <Domain>{domain}</Domain>
            </Request>
        </GetFederationInformationRequestMessage>
    </soap:Body>
</soap:Envelope>"""
    headers = {
        "Content-Type": "text/xml; charset=utf-8",
        "User-Agent": "AutodiscoverClient"
    }

    try:
        response = requests.post("https://autodiscover-s.outlook.com/autodiscover/autodiscover.svc", data=body, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print_colored(f"  Error: Cannot get all accepted domains. Are you sure the domain name is correct?\n  {e}", "red", attrs=['bold'])
        exit()

    namespaces = {
        'soap': 'http://schemas.xmlsoap.org/soap/envelope/',
        'a': 'http://schemas.microsoft.com/exchange/2010/Autodiscover'
    }
    
    try:
        tree = ElementTree.fromstring(response.content)
        domains = tree.findall('.//a:Domain', namespaces)
        return [domain.text for domain in domains]
    except ElementTree.ParseError as e:
        print_colored(f"  Error parsing XML: {e}", "red", attrs=['bold'])
        exit()

def get_tenant_name(domains):
    print_colored("Start getting instance name...", "yellow")
    for domain in domains:
        if domain.lower().endswith(".onmicrosoft.com"):
            tenant_name = domain.split('.')[0]
            print_colored(f"  {tenant_name}", "cyan")
            return tenant_name
    return None

def check_mdi_instance(tenant_name):
    print_colored("Check if instance exists...", "yellow")
    urls = [
        f"https://{tenant_name}.atp.azure.com",
        f"https://{tenant_name}-onmicrosoft-com.atp.azure.com"
    ]
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print_colored(f"[!] Looks like {tenant_name} is running an MDI instance on {url}", "red", attrs=['bold'])
            else:
                print_colored(":) No MDI instance is running on " + url, "green")
        except requests.RequestException as e:
            print_colored(":) No MDI instance is running on " + url, "green")

def main():
    domain = input("Enter a domain name: ")
    accepted_domains = get_accepted_domains(domain)
    tenant_name = get_tenant_name(accepted_domains)
    if tenant_name:
        check_mdi_instance(tenant_name)
    else:
        print_colored("No tenant name could be determined.", "magenta")

if __name__ == "__main__":
    main()
