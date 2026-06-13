# ClauseGuard - Synthetic Contract Documents Generator
# These are FAKE contracts for demo purposes only

contracts = [
    {
        "name": "SaaS_Software_Agreement.txt",
        "content": """SOFTWARE AS A SERVICE AGREEMENT (SYNTHETIC - DEMO ONLY)

Contract ID: CG-2024-001
Vendor: TechCorp Solutions Inc.
Client: Acme Business Ltd.
Effective Date: January 1, 2024

1. TERM AND RENEWAL
This Agreement shall commence on January 1, 2024 and continue for 12 months.
AUTO-RENEWAL CLAUSE: This contract will automatically renew for successive 
one-year terms unless written notice of termination is provided by either 
party no less than 90 days prior to the end of the current term.
Next renewal date: January 1, 2025.
Notice deadline: October 3, 2024.

2. PAYMENT TERMS
Annual fee: $120,000 USD payable in advance.
Late payment penalty: 1.5% per month on outstanding balances.

3. PENALTIES AND TERMINATION
Early termination penalty: 6 months remaining contract value.
Estimated early exit cost: $60,000 USD.

4. VENDOR OBLIGATIONS
Vendor must maintain 99.9% uptime SLA.
Breach of SLA results in service credits of 10% monthly fee per incident.

5. DATA SECURITY
Vendor must comply with SOC2 Type II standards.
Data breach notification required within 72 hours."""
    },
    {
        "name": "Office_Lease_Agreement.txt", 
        "content": """COMMERCIAL OFFICE LEASE AGREEMENT (SYNTHETIC - DEMO ONLY)

Contract ID: CG-2024-002
Landlord: Premier Properties LLC
Tenant: Acme Business Ltd.
Property: Suite 500, 123 Business Ave, Chicago IL

1. LEASE TERM
Start Date: March 1, 2024
End Date: February 28, 2027
Total Term: 36 months

2. AUTO-RENEWAL
This lease will automatically renew for 12 months unless tenant provides
written notice of non-renewal at least 180 days before expiration.
Notice deadline: August 31, 2026.
Failure to notify results in automatic renewal at 5% increased rent.

3. MONTHLY RENT
Base rent: $25,000 per month
Annual increase: 3% per year
Year 2 rent: $25,750
Year 3 rent: $26,522

4. EARLY TERMINATION
Early exit penalty: 6 months base rent = $150,000 USD
Requires 90 days written notice before early exit.

5. TENANT OBLIGATIONS
Tenant responsible for all interior maintenance.
Must carry $2M general liability insurance at all times."""
    },
    {
        "name": "Marketing_Services_Contract.txt",
        "content": """MARKETING SERVICES AGREEMENT (SYNTHETIC - DEMO ONLY)

Contract ID: CG-2024-003
Agency: BrandBoost Marketing Agency
Client: Acme Business Ltd.
Date: June 1, 2024

1. CONTRACT DURATION
Initial term: 6 months (June 1, 2024 - November 30, 2024)

2. AUTO-RENEWAL WARNING
CONTRACT WILL AUTO-RENEW FOR 12 MONTHS unless cancelled in writing
with minimum 30 days notice before November 30, 2024.
CRITICAL NOTICE DEADLINE: October 31, 2024.
Auto-renewal value: $180,000 USD for additional year.

3. MONTHLY RETAINER
Fee: $15,000 per month
Total contract value: $90,000

4. PERFORMANCE PENALTIES
If agreed KPIs not met for 2 consecutive months:
Client may terminate with 30 days notice, NO early exit penalty.

5. INTELLECTUAL PROPERTY
All creative work belongs to client upon full payment.
Agency retains portfolio rights for award submissions only.

6. CONFIDENTIALITY
Both parties agree to 2-year non-disclosure period post-contract."""
    }
]

# Create contract files
import os

os.makedirs("contracts", exist_ok=True)

for contract in contracts:
    filepath = os.path.join("contracts", contract["name"])
    with open(filepath, "w") as f:
        f.write(contract["content"])
    print(f"Created: {filepath}")

print("\nAll synthetic contracts created successfully!")
print("These are FAKE documents for hackathon demo purposes only.")