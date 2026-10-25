import dns.resolver

# ------------------------------------------------------------------
# Required Global Variables
# ------------------------------------------------------------------
local_host = "127.0.0.1"
real_name_server = "8.8.8.8"
question_type = "A"


# ------------------------------------------------------------------
# Core Query Function
# ------------------------------------------------------------------
def query_dns_server(domain_name, dns_server=real_name_server, qtype=question_type):
    """
    Queries a specified DNS server for a domain name and record type.
    """
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [dns_server]
    
    try:
        answers = resolver.resolve(domain_name, qtype)
        return answers[0].to_text()
    except Exception as e:
        return str(e)


# ------------------------------------------------------------------
# Dedicated Functions
# ------------------------------------------------------------------
def query_local_dns_server(domain_name, qtype=question_type):
    """
    Queries the local DNS server (127.0.0.1).
    """
    return query_dns_server(domain_name, dns_server=local_host, qtype=qtype)


def query_public_dns_server(domain_name, qtype=question_type):
    """
    Queries the public DNS server (real_name_server).
    """
    return query_dns_server(domain_name, dns_server=real_name_server, qtype=qtype)


def compare_dns_servers(domain_name, qtype=question_type):
    """
    Compares responses from the local DNS server and the public DNS server.
    """
    local_res = query_local_dns_server(domain_name, qtype)
    public_res = query_public_dns_server(domain_name, qtype)
    return local_res == public_res


if __name__ == "__main__":
    test_domain = "google.com"
    print("Local DNS Result:", query_local_dns_server(test_domain))
    print("Public DNS Result:", query_public_dns_server(test_domain))
