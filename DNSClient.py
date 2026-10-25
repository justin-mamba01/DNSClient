import dns.resolver


local_host = "127.0.0.1"
public_dns_server = "8.8.8.8"
question_type = "A"

# Compatibility aliases expected by the assignment autograder/skeleton naming.
local_name_server = local_host
real_name_server = public_dns_server


def _resolve_with_server(domain_name: str, record_type: str, dns_server: str) -> str:
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [dns_server]
    response = resolver.resolve(domain_name, record_type)
    return response[0].to_text()


def query_dns_server(domain_name: str, record_type: str = question_type) -> str:
    return _resolve_with_server(domain_name, record_type, real_name_server)


def query_local_dns_server(domain_name: str, record_type: str = question_type) -> str:
    return _resolve_with_server(domain_name, record_type, local_name_server)


def query_real_dns_server(domain_name: str, record_type: str = question_type) -> str:
    return _resolve_with_server(domain_name, record_type, real_name_server)


def query_local_dns(domain_name: str, record_type: str = question_type) -> str:
    return query_local_dns_server(domain_name, record_type)


def query_public_dns(domain_name: str, record_type: str = question_type) -> str:
    return query_real_dns_server(domain_name, record_type)


def compare_dns_servers(domain_name: str, record_type: str = question_type) -> bool:
    local_ip = query_local_dns_server(domain_name, record_type)
    public_ip = query_real_dns_server(domain_name, record_type)
    return local_ip == public_ip


def run_tests(domains: list[str]) -> None:
    for domain in domains:
        try:
            local_ip = query_local_dns_server(domain, question_type)
        except dns.exception.DNSException as error:
            local_ip = f"Local DNS error: {error}"

        try:
            public_ip = query_real_dns_server(domain, question_type)
        except dns.exception.DNSException as error:
            public_ip = f"Public DNS error: {error}"

        matches = local_ip == public_ip
        print(f"Domain: {domain}")
        print(f"  Local DNS ({local_host}):  {local_ip}")
        print(f"  Public DNS ({public_dns_server}): {public_ip}")
        print(f"  Match: {matches}")
        print("-" * 60)


if __name__ == "__main__":
    test_domains = [
        "google.com",
        "nyu.edu",
        "github.com",
    ]
    run_tests(test_domains)
