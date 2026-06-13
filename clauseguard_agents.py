import os
from dotenv import load_dotenv
from azure.ai.projects import AIProjectClient
from azure.core.credentials import AzureKeyCredential

load_dotenv()

endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT")
api_key = os.getenv("AZURE_AI_API_KEY")
model = os.getenv("AZURE_AI_MODEL_DEPLOYMENT")

client = AIProjectClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(api_key)
)

def clause_extraction_agent(contract_text):
    print("\n🔍 AGENT 1: Extracting clauses...")
    response = client.agents.run_thread(
        agent_name="ClauseExtractor",
        messages=[{
            "role": "user",
            "content": f"""You are a contract clause extraction specialist.
            Extract ALL important clauses from this contract:
            - Auto-renewal clauses
            - Notice periods
            - Penalties and fees
            - Payment terms
            - Termination conditions
            
            Contract: {contract_text}
            
            Return extracted clauses in a structured format."""
        }],
        model=model
    )
    return response

def risk_detection_agent(clauses):
    print("\n⚠️ AGENT 2: Detecting risks...")
    response = client.agents.run_thread(
        agent_name="RiskDetector", 
        messages=[{
            "role": "user",
            "content": f"""You are a contract risk detection specialist.
            Analyze these clauses and identify ALL risks:
            - Upcoming auto-renewals
            - Missed notice deadlines
            - Penalty exposure
            - Unfavorable terms
            
            Clauses: {clauses}
            
            Rate each risk as HIGH, MEDIUM, or LOW."""
        }],
        model=model
    )
    return response

def financial_impact_agent(risks):
    print("\n💰 AGENT 3: Calculating financial impact...")
    response = client.agents.run_thread(
        agent_name="FinancialAnalyst",
        messages=[{
            "role": "user", 
            "content": f"""You are a financial impact specialist.
            Calculate the financial exposure from these risks:
            - Total money at risk
            - Cost of inaction
            - Potential savings if acted upon
            
            Risks: {risks}
            
            Provide specific dollar amounts."""
        }],
        model=model
    )
    return response

def recommendation_agent(financial_impact):
    print("\n✅ AGENT 4: Generating recommendations...")
    response = client.agents.run_thread(
        agent_name="Recommender",
        messages=[{
            "role": "user",
            "content": f"""You are a contract action specialist.
            Based on this financial analysis, provide:
            - Immediate actions required
            - Deadlines to act by
            - Priority ranking (Critical/High/Medium)
            - Specific next steps
            
            Analysis: {financial_impact}
            
            Format as an executive action report."""
        }],
        model=model
    )
    return response

if __name__ == "__main__":
    print("🛡️ ClauseGuard - Contract Risk Navigator")
    print("=" * 50)
    
    # Read sample contract
    with open("contracts/SaaS_Software_Agreement.txt", "r") as f:
        contract = f.read()
    
    # Run 4-agent pipeline
    clauses = clause_extraction_agent(contract)
    risks = risk_detection_agent(clauses)
    impact = financial_impact_agent(risks)
    recommendations = recommendation_agent(impact)
    
    print("\n" + "=" * 50)
    print("✅ ClauseGuard Analysis Complete!")
    print(recommendations)