# 🛡️ ClauseGuard — Intelligent Contract Risk Navigator

> **Microsoft Agents League Hackathon 2026 | Reasoning Agents Track**
> Built with Microsoft Azure AI Foundry + Foundry IQ

---

## 🎯 The Problem

Every year, companies lose millions from missed contract deadlines:
- Auto-renewals they didn't want — locked in for another year
- Missed cancellation notice windows — paying penalties they could have avoided
- Hidden clauses discovered too late
- Manual contract review taking 3+ hours per document

**One missed deadline can cost $60,000–$180,000+**

---

## 💡 The Solution

**ClauseGuard** is an AI-powered contract risk intelligence agent that:
1. **Extracts** all critical clauses automatically from your knowledge base
2. **Detects** risks and rates them 🔴 HIGH / 🟡 MEDIUM / 🟢 LOW
3. **Calculates** exact financial exposure in dollars
4. **Recommends** specific actions with exact deadlines

---

## 🏗️ Architecture

```
User asks a question
        ↓
ClauseGuard Agent (grok-4.3 on Azure AI Foundry)
        ↓
Foundry IQ (Azure AI Search knowledge base)
Retrieves grounded contract context with citations
        ↓
4-Step Reasoning Chain:
    Step 1: Clause Extraction
    Step 2: Risk Detection
    Step 3: Financial Impact Analysis
    Step 4: Recommended Actions
        ↓
Structured Risk Report — grounded in actual contract text
```

---

## 🧠 Microsoft IQ Integration

| IQ Layer | Usage |
|----------|-------|
| **Foundry IQ** | Contract documents stored as a grounded knowledge base. Agent retrieves and cites actual contract text — no hallucinations, answers grounded in real clauses |

---

## 🔧 Technical Stack

| Component | Technology |
|-----------|------------|
| Agent Platform | Microsoft Azure AI Foundry |
| Model | grok-4.3 (Global Standard deployment) |
| Knowledge Base | Foundry IQ (Azure AI Search — cg-search-isha-2026) |
| Knowledge Source | File upload (3 synthetic contracts) |
| Code | Python 3.11 + Azure AI Projects SDK |
| Version Control | GitHub |

---

## 📁 Repository Structure

```
clauseguard/
├── clauseguard_agents.py      # Multi-agent Python implementation
├── clauseguard_contracts.py   # Synthetic contract generator
├── contracts/                 # Synthetic demo contracts
│   ├── SaaS_Software_Agreement.txt
│   ├── Office_Lease_Agreement.txt
│   └── Marketing_Services_Contract.txt
├── .env                       # Environment variables (not committed)
├── .gitignore
└── README.md
```

---

## 🚀 How to Run

### Prerequisites
- Python 3.10+
- Azure AI Foundry account
- Azure subscription

### Setup
```bash
git clone https://github.com/ISHA301/clauseguard
cd clauseguard
python -m venv .venv
.venv\Scripts\activate
pip install azure-ai-projects azure-identity openai python-dotenv
```

### Configure
Create `.env` file:
```
AZURE_AI_PROJECT_ENDPOINT=your-endpoint-here
AZURE_AI_MODEL_DEPLOYMENT=grok-4.3
AZURE_AI_API_KEY=your-api-key-here
```

### Run
```bash
python clauseguard_agents.py
```

---

## 📊 Live Demo Results

ClauseGuard analyzed 3 synthetic contracts via Foundry IQ and answered real questions:

**Q: "Am I in trouble with any of these contracts?"**
> "Yes, you are exposed to significant ongoing commitments. The high-risk auto-renewal clause has already materialized — because no written notice was provided by the October 3, 2024 deadline, the agreement automatically renewed, locking you into at least two additional $120,000 annual payments unless you exercise early termination at the estimated $60,000 penalty cost."

**Q: "What's my most urgent deadline across all contracts?"**
> "The most urgent deadline is the written non-renewal notice due by approximately October 2–3, 2026, to avoid another auto-renewal on January 1, 2027. This is 90 days before the December 31, 2026 term end."

**Q: "When do I need to cancel to avoid auto-renewal?"**
> "You must provide written notice no less than 90 days prior to the end of the current term. Based on today's date of June 14, 2026, the next deadline is approximately October 2–3, 2026 to prevent renewal on January 1, 2027."

**Q: "What's the worst case financially if I do nothing?"**
> Total exposure: $180,000
> - Early termination penalty: $60,000
> - Auto-renewed annual commitment (2027): $120,000
> - Potential late fees: $1,800/month

| Contract | Risk Level | Financial Exposure | Action Deadline |
|----------|-----------|-------------------|-----------------|
| SaaS Agreement | 🔴 HIGH | $180,000 total | October 3, 2026 |
| Office Lease | 🔴 HIGH | $150,000 penalty | August 31, 2026 |
| Marketing Contract | 🔴 HIGH | $180,000 auto-renewal | October 31, 2026 |

**Total exposure detected across all contracts: $390,000+**

---

## 🎯 Business Impact

- ⏱️ Contract review time: **3 hours → 30 seconds (99% reduction)**
- 💰 Financial exposure identified: **$390,000+**
- 🎯 Multi-step reasoning: **4-step grounded analysis**
- 🏢 Target users: Legal teams, Finance, Procurement
- 📚 Market context: AI reduces contract review time by 75-85% (LegalOn 2026 report)

---

## 💬 Intelligent Response Modes

ClauseGuard adapts its response based on what you actually need:

| Question Type | Response |
|---------------|----------|
| Full contract analysis | Complete 4-step structured report |
| Specific question | Direct 2-4 sentence answer |
| Summary request | 3-5 bullet points under 100 words |
| What should I do? | Numbered action list with deadlines |
| Financial question | Dollar breakdown with risk ratings |

---

## 🔮 Future Roadmap

- 📅 Automated deadline alerts (90/60/30 day notifications via email/Teams)
- 📄 PDF and Word document direct upload support
- 📊 Contract portfolio risk dashboard
- 🔗 SharePoint and OneDrive integration via Foundry IQ
- 🤖 Multi-contract batch analysis

---

## ⚠️ Disclaimer

All contracts in this repository are **completely synthetic** and created for demonstration purposes only. No real customer data, PII, or confidential information is included. ClauseGuard analysis is AI-generated for informational purposes only — consult a legal professional for binding contract decisions.

---

## 👩‍💻 Built By

**Isha Singh** | BI & Data Analyst | Austin, TX
- LinkedIn: [linkedin.com/in/ishasingh-ak](https://linkedin.com/in/ishasingh-ak)

*Built for Microsoft Agents League Hackathon @ AI Skills Fest 2026*
*Reasoning Agents Track — Microsoft Azure AI Foundry + Foundry IQ*
