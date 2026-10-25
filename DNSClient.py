import dns.resolver


local_host = "127.0.0.1"
public_dns_server = "8.8.8.8"
question_type = "A"


def query_dns_server(domain_name: str, dns_server: str) -> str:
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [dns_server]
    response = resolver.resolve(domain_name, question_type)
    return response[0].to_text()


def query_local_dns(domain_name: str) -> str:
    return query_dns_server(domain_name, local_host)


def query_public_dns(domain_name: str) -> str:
    return query_dns_server(domain_name, public_dns_server)


def compare_dns_servers(domain_name: str) -> bool:
    local_ip = query_local_dns(domain_name)
    public_ip = query_public_dns(domain_name)
    return local_ip == public_ip


def run_tests(domains: list[str]) -> None:
    for domain in domains:
        try:
            local_ip = query_local_dns(domain)
        except dns.exception.DNSException as error:
            local_ip = f"Local DNS error: {error}"

        try:
            public_ip = query_public_dns(domain)
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
