import dns.resolver

# Define required global variables
local_host = "127.0.0.1"
real_name_server = "8.8.8.8"  # Public DNS server IP expected by GradeScope
question_type = "A"


def query_local_dns_server(domain_name, record_type=question_type):
    """
    Queries the local DNS server for a given domain and record type.
    """
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [local_host]
    try:
        answers = resolver.resolve(domain_name, record_type)
        return answers[0].to_text()
    except Exception as e:
        return str(e)


def query_public_dns_server(domain_name, record_type=question_type):
    """
    Queries a public DNS server for a given domain and record type.
    """
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [real_name_server]
    try:
        answers = resolver.resolve(domain_name, record_type)
        return answers[0].to_text()
    except Exception as e:
        return str(e)


def compare_dns_servers(domain_name, record_type=question_type):
    """
    Compares the responses from local and public DNS servers.
    """
    local_result = query_local_dns_server(domain_name, record_type)
    public_result = query_public_dns_server(domain_name, record_type)
    return local_result == public_result


if __name__ == "__main__":
    # Optional local test execution
    test_domain = "google.com"
    print(f"Local query result: {query_local_dns_server(test_domain)}")
    print(f"Public query result: {query_public_dns_server(test_domain)}")
