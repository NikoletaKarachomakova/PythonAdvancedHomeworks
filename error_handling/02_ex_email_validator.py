class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def validate_size(line):
    email = line.split("@")
    if len(email[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")


def if_at_exists(line):
    if "@" not in line:
        raise MustContainAtSymbolError("Email must contain @")


def validate_domain(line, domains):
    domain = line.split(".")[-1]
    if domain not in domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")


email = input()
while email != "End":
    valid_domains = ("com", "bg", "org", "net")
    validate_size(email)
    if_at_exists(email)
    validate_domain(email, valid_domains)
    print("Email is valid")
    email = input()

