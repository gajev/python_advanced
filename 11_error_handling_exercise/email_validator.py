import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


pattern = r"(?P<name>[\w]+?\.?\w+)(?P<at>@)(?P<host>[\w]+)(?P<domain>.\w+)"
email = input()
domain_list = [".com", ".bg", ".org", ".net"]
while email != "End":
    matches = re.finditer(pattern, email)
    for match in matches:
        name = match.group("name")
        domain = match.group("domain")
    if "@" not in email:
        raise MustContainAtSymbolError('Email must contain @"')
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    elif domain not in domain_list:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(domain_list)}")
    print("Email is valid")
    email = input()



