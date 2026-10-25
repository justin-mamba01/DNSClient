import dns.resolver

# Define configuration variables as instructed in the assignment
local_host = "127.0.0.1"      # IP address reserved for local server on local machine
public_dns_server = "8.8.8.8" # Public DNS Server IP (Google Public DNS)
question_type = "A"            # Standard IPv4 address query record type


def query_local_dns(domain_name):
    """
    Queries the local DNS server running on local_host (127.0.0.1)
    for the IP address associated with the provided domain_name.
    
    Parameters:
        domain_name (str): The domain name to query (e.g. 'google.com')
        
    Returns:
        str: The IP address returned by the local DNS server
    """
    # Create an instance of dns.resolver.Resolver
    resolver = dns.resolver.Resolver()
    
    # Set the nameservers attribute to the local DNS server address
    resolver.nameservers = [local_host]
    
    # Perform the DNS lookup for the given domain name and question_type
    answer = resolver.resolve(domain_name, question_type)
    
    # Extract and return the IP address using to_text() on the first answer record
    return answer[0].to_text()


def query_public_dns(domain_name):
    """
    Queries the designated public DNS server (e.g. 8.8.8.8)
    for the IP address associated with the provided domain_name.
    
    Parameters:
        domain_name (str): The domain name to query (e.g. 'google.com')
        
    Returns:
        str: The IP address returned by the public DNS server
    """
    # Create an instance of dns.resolver.Resolver
    resolver = dns.resolver.Resolver()
    
    # Set the nameservers attribute to the public DNS server address
    resolver.nameservers = [public_dns_server]
    
    # Perform the DNS lookup for the given domain name and question_type
    answer = resolver.resolve(domain_name, question_type)
    
    # Extract and return the IP address using to_text() on the first answer record
    return answer[0].to_text()


def compare_dns_servers(domain_name):
    """
    Compares the DNS query results from both local and public DNS servers.
    
    Parameters:
        domain_name (str): The domain name to check across servers
        
    Returns:
        bool: True if both DNS servers return matching IP addresses, False otherwise
    """
    try:
        local_result = query_local_dns(domain_name)
        public_result = query_public_dns(domain_name)
        return local_result == public_result
    except Exception as e:
        print(f"Error during DNS query comparison for {domain_name}: {e}")
        return False


if __name__ == '__main__':
    test_domain = "google.com"
    print(f"Querying Public DNS ({public_dns_server}) for {test_domain}:")
    try:
        pub_ip = query_public_dns(test_domain)
        print(f"Public DNS Result: {pub_ip}")
    except Exception as e:
        print(f"Public DNS lookup failed: {e}")