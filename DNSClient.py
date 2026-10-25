import dns.resolver

# ------------------------------------------------------------------
# Global Variables (Required by Skeleton)
# ------------------------------------------------------------------
local_host = "127.0.0.1"[cite: 6]
real_name_server = "8.8.8.8"[cite: 6]
question_type = "A"[cite: 6]


# ------------------------------------------------------------------
# General DNS Query Function
# ------------------------------------------------------------------
def query_dns_server(domain_name, question_type=question_type, dns_server=real_name_server):
    """
    Queries a specified DNS server for a domain name and record type.
    """
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [dns_server][cite: 6]
    
    # Perform the query using resolve()
    answers = resolver.resolve(domain_name, question_type)[cite: 6]
    
    # Return the text representation of the first answer record
    return answers[0].to_text()[cite: 6]


# ------------------------------------------------------------------
# Helper Functions expected by GradeScope
# ------------------------------------------------------------------
def query_local_dns_server(domain_name, question_type=question_type):
    """
    Queries the local DNS server (127.0.0.1).
    """
    return query_dns_server(domain_name, question_type, dns_server=local_host)[cite: 6]


def query_public_dns_server(domain_name, question_type=question_type):
    """
    Queries the public DNS server (8.8.8.8).
    """
    return query_dns_server(domain_name, question_type, dns_server=real_name_server)[cite: 6]


def compare_dns_servers(domain_name, question_type=question_type):
    """
    Compares the responses from local and public DNS servers.
    """
    local_result = query_local_dns_server(domain_name, question_type)[cite: 7]
    public_result = query_public_dns_server(domain_name, question_type)[cite: 7]
    return local_result == public_result[cite: 7]


if __name__ == "__main__":
    test_domain = "google.com"
    print("Local DNS:", query_local_dns_server(test_domain))[cite: 7]
    print("Public DNS:", query_public_dns_server(test_domain))[cite: 7]
