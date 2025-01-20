from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Sorular listesi
questions = [
    {
        "question": "What does market entry refer to?",
        "choices": [
            "A) Introducing a product into domestic markets",
            "B) Entering new markets strategically",
            "C) Eliminating competition through alliances",
            "D) Focusing on a single revenue source"
        ],
        "answer": "B"
    },
    {
        "question": "What is the main benefit of entering multiple markets?",
        "choices": [
            "A) Reduced risk through diversification",
            "B) Easier regulatory requirements",
            "C) Lower operational costs",
            "D) Guaranteed first-mover advantage"
        ],
        "answer": "A"
    },
    # Diğer sorularınızı buraya ekleyin...
    {
    "question": "Which company used rapid delivery to expand internationally?",
    "choices": ["A) Turkish Airlines", "B) Simit Sarayı", "C) Getir", "D) BİM"],
    "answer": "C"
    },
    {
    "question": "What is a disadvantage of the first-mover strategy?",
    "choices": ["A) Lower initial costs", "B) Reduced brand recognition", "C) High market uncertainty", "D) Guaranteed customer loyalty"],
    "answer": "C"
    },
    {
    "question": "What is a key aspect of differentiation?",
    "choices": ["A) Low-cost operations", "B) Emotional branding", "C) Standardized products", "D) Broad focus on mass markets"],
    "answer": "B"
    },
    {
    "question": "What does cost leadership emphasize?",
    "choices": ["A) Premium pricing", "B) Minimizing operational costs", "C) Exclusive product features", "D) Broad market differentiation"],
    "answer": "B"
    },
    {
    "question": "What is a focus strategy?",
    "choices": ["A) Targeting niche markets with specialized products", "B) Reducing costs across all operations", "C) Leveraging economies of scale", "D) Broadly differentiating product offerings"],
    "answer": "A"
    },
    {
    "question": "Which strategy involves building new facilities in a target market?",
     "choices": ["A) Joint ventures", "B) Franchising", "C) Greenfield investments", "D) Acquisitions"],
    "answer": "C"
    },
    {
    "question": "What is an advantage of joint ventures?",
    "choices": ["A) Complete independence from local markets", "B) Gaining local market expertise", "C) Reducing all operational risks", "D) Eliminating partner dependency"],
    "answer": "B"
    },
    {
    "question": "What does franchising involve?",
     "choices": ["A) Acquiring local firms", "B) Licensing a business model to local operators", "C) Building infrastructure in foreign markets", "D) Focusing on premium pricing"],
    "answer": "B"
    },
    {
    "question": "What is a primary risk of acquisitions?",
     "choices": ["A) Dependency on partners", "B) High initial costs", "C) Lack of market Access", "D) Limited operational control"],
    "answer": "B"
    },
    {
    "question": "Which strategy focuses on emotional branding?",
     "choices": ["A) Cost leadership", "B) Differentiation", "C) Greenfield investments", "D) Franchising"],
    "answer": "B"
    },
    {
    "question": "What is a benefit of the first-mover strategy?",
     "choices": ["A) Lower entry costs", "B) Brand recognition", "C) Avoiding market competition", "D) Reduced marketing costs"],
    "answer": "B"
    },
    {
    "question": "Which strategy is best for reducing dependency on a single revenue source?",
    "choices": ["A) Differentiation", "B) Joint ventures", "C) Diversification", "D) Cost leadership"],
    "answer": "C"
    },
    {
    "question": "What does a cost-benefit analysis involve?",
    "choices": ["A) Understanding consumer preferences", "B) Weighing investment costs against potential returns", "C) Identifying new market opportunities", "D) Minimizing marketing efforts"],
    "answer": "B"
    },

    {
        "question": "What is a direct competitor?",
        "choices": ["A) A business that operates in a different industry",
                    "B) A business that sells the same product or service",
                    "C) A business that focuses on unrelated markets",
                    "D) A business that offers a complementary service"],
        "answer": "B"
    },
    {
        "question": "How do competitors encourage innovation?",
        "choices": ["A) By reducing prices", "B) By investing in unrelated industries",
                    "C) By forcing businesses to improve", "D) By avoiding market competition"],
        "answer": "C"
    },
    {
        "question": "What is an example of an indirect competitor?",
        "choices": ["A) Coca-Cola vs. Pepsi", "B) Uber vs. bike rental services", "C) Nike vs. Adidas",
                    "D) Eti vs. Ülker"],
        "answer": "B"
    },
    {
        "question": "What does a 'strategic midwife' do?",
        "choices": ["A) Prevents new businesses from entering the market", "B) Grows awareness of a product type",
                    "C) Creates distrust in the market", "D) Reduces competition through partnerships"],
        "answer": "B"
    },
    {
        "question": "What is a characteristic of a good competitor?",
        "choices": ["A) Misleading customers with false claims", "B) Avoiding innovation",
                    "C) Following fair competition rules", "D) Limiting market education"],
        "answer": "C"
    },
    {
        "question": "How do harmful competitors damage industries?",
        "choices": ["A) By promoting innovation", "B) By creating high-quality products",
                    "C) By using unethical practices", "D) By growing customer loyalty"],
        "answer": "C"
    },
    {
        "question": "What did Amazon’s global expansion achieve?",
        "choices": ["A) It limited local seller opportunities", "B) It grew awareness for e-commerce",
                    "C) It reduced shipping times for all industries", "D) It replaced all local retailers"],
        "answer": "B"
    },
    {
        "question": "What is the purpose of a competitor barometer?",
        "choices": ["A) To measure market opportunities", "B) To analyze competitors' impact on your business",
                    "C) To determine customer preferences", "D) To eliminate competition"],
        "answer": "B"
    },
    {
        "question": "What type of competitor is Pepsi to Coca-Cola?",
        "choices": ["A) Indirect", "B) Complementary", "C) Direct", "D) Strategic"],
        "answer": "C"
    },
    {
        "question": "How did Pegasus Airlines influence Turkish Airlines?",
        "choices": ["A) By reducing air travel demand", "B) By making air travel more affordable",
                    "C) By increasing luxury competition", "D) By focusing on international travel only"],
        "answer": "B"
    },
    {
        "question": "What defines a harmful competitor?",
        "choices": ["A) Respecting fair competition", "B) Using unethical practices", "C) Encouraging innovation",
                    "D) Building customer trust"],
        "answer": "B"
    },
    {
        "question": "What is an advantage of good competitors?",
        "choices": ["A) Limiting industry growth", "B) Misleading customers", "C) Improving industry standards",
                    "D) Avoiding competition"],
        "answer": "C"
    },
    {
        "question": "What does the competitor barometer evaluate?",
        "choices": ["A) Product pricing strategies", "B) Ethical practices and innovation",
                    "C) Regulatory requirements", "D) Customer loyalty only"],
        "answer": "B"
    },
    {
        "question": "What is the impact of patent wars in technology?",
        "choices": ["A) Encouraging more competition", "B) Slowing down innovation", "C) Building customer trust",
                    "D) Reducing operational costs"],
        "answer": "B"
    },
    {
        "question": "What can useful competitors teach customers?",
        "choices": ["A) The value of a product category", "B) How to avoid certain products",
                    "C) The benefits of low-quality goods", "D) Ways to mistrust brands"],
        "answer": "A"
    },
    {
        "question": "How do indirect competitors compete?",
        "choices": ["A) Selling identical products", "B) Solving the same problem with different products",
                    "C) Focusing on unrelated markets", "D) Avoiding customer overlap"],
        "answer": "B"
    },
    {
        "question": "How can competitors grow the market?",
        "choices": ["A) By reducing demand", "B) By educating customers about products", "C) By avoiding advertisement",
                    "D) By restricting access to new customers"],
        "answer": "B"
    },

    {
        "question": "What is a new market?",
        "choices": ["A) An industry with established rules and products",
                    "B) A place where products or services are just starting to develop",
                    "C) A market dominated by large corporations", "D) A region with low customer demand"],
        "answer": "B"
    },
    {
        "question": "Why are new markets challenging?",
        "choices": ["A) High competition", "B) Customers may not know they need the product", "C) Strict regulations",
                    "D) Limited technological Access"],
        "answer": "B"
    },
    {
        "question": "What is the main benefit of being one of the first businesses in a new market?",
        "choices": ["A) Avoiding customer education", "B) Reducing investment risks", "C) Leading the market",
                    "D) Avoiding regulatory scrutiny"],
        "answer": "C"
    },
    {
        "question": "What does adaptation mean in business?",
        "choices": ["A) Using untested methods in all markets", "B) Changing a successful product to fit a new market",
                    "C) Avoiding competition by targeting untapped regions", "D) Copying competitors’ products"],
        "answer": "B"
    },
    {
        "question": "How did Uber adapt its model for Turkey?",
        "choices": ["A) Allowed cash payments", "B) Introduced luxury rides only", "C) Focused on international routes",
                    "D) Lowered commission rates"],
        "answer": "A"
    },
    {
        "question": "What is the first step in experimentation?",
        "choices": ["A) Launching a full-scale product", "B) Expanding immediately to multiple markets",
                    "C) Avoiding customer feedback", "D) Testing a simple version with a small group"],
        "answer": "D"
    },
    {
        "question": "How did Starbucks combine ideas in Turkey?",
        "choices": ["A) Introduced global coffee models with local Turkish coffee offerings",
                    "B) Eliminated international coffee options", "C) Focused on mobile-only orders",
                    "D) Partnered with grocery stores"],
        "answer": "A"
    },
    {
        "question": "How can businesses teach customers about their products?",
        "choices": ["A) Avoid marketing efforts", "B) Focus on reducing prices", "C) Rely solely on word of mouth",
                    "D) Use education and advertising"],
        "answer": "D"
    },
    {
        "question": "What is the main advantage of partnering with others in a new market?",
        "choices": ["A) Reducing competition", "B) Controlling the entire market", "C) Avoiding customer demand",
                    "D) Sharing costs and resources"],
        "answer": "D"
    },
    {
        "question": "What is the goal of risk management in a new market?",
        "choices": ["A) To avoid taking any risks", "B) To minimize competitors’ actions",
                    "C) To identify and prepare for potential risks", "D) To focus only on short-term gains"],
        "answer": "C"
    },
    {
        "question": "What is an example of financial risk?",
        "choices": ["A) Spending too much money before making sales", "B) Overpricing products",
                    "C) Losing market share", "D) Creating ads that fail"],
        "answer": "A"
    },
    {
        "question": "How can businesses reduce customer risks?",
        "choices": ["A) By using clear advertising and product explanations", "B) By avoiding new customer segments",
                    "C) By focusing only on competitors", "D) By reducing product quality"],
        "answer": "A"
    },
    {
        "question": "What does a competitor barometer analyze?",
        "choices": ["A) Customer preferences", "B) Competitors' impact on your business", "C) Market trends only",
                    "D) Pricing strategies"],
        "answer": "B"
    },
    {
        "question": "Why are early adopters important in a new market?",
        "choices": ["A) They set market regulations", "B) They represent the majority of customers",
                    "C) They provide feedback and build trust", "D) They are easy to attract"],
        "answer": "C"
    },
    {
        "question": "How can crowdfunding reduce financial risks?",
        "choices": ["A) By lowering product costs", "B) By raising money before launching a product",
                    "C) By focusing on loans", "D) By avoiding small investors"],
        "answer": "B"
    },
    {
        "question": "Which method focuses on mixing proven ideas with new features?",
        "choices": ["A) Adaptation", "B) Experimentation", "C) Combination", "D) Risk reduction"],
        "answer": "C"
    },

    {
        "question": "What is the primary purpose of a business plan?",
        "choices": ["A) To secure immediate profits", "B) To provide clarity, direction, and confidence",
                    "C) To compete directly with larger companies", "D) To avoid market research"],
        "answer": "B"
    },
    {
        "question": "Why is market research important before writing a business plan?",
        "choices": [
            "A) To finalize product pricing",
            "B) To avoid customer feedback",
            "C) To create financial reports",
            "D) To understand the market and competition"
        ],
        "answer": "D"
    },
    {
        "question": "What is an example of identifying a problem for a business?",
        "choices": [
            "A) A meal delivery service solving the lack of cooking time",
            "B) Lowering product prices",
            "C) Advertising on social media",
            "D) Hiring additional staff"
        ],
        "answer": "A"
    },
    {
        "question": "What does a unique selling proposition (USP) highlight?",
        "choices": [
            "A) A company’s weaknesses",
            "B) Customer dissatisfaction",
            "C) What makes a product or service stand out",
            "D) General industry trends"
        ],
        "answer": "C"
    },
    {
        "question": "What is an example of a short-term business goal?",
        "choices": [
            "A) Expanding into international markets",
            "B) Selling 1,000 units in six months",
            "C) Becoming a global leader in the industry",
            "D) Reducing long-term operational costs"
        ],
        "answer": "B"
    },
    {
        "question": "What is the purpose of an executive summary?",
        "choices": [
            "A) To provide a detailed financial analysis",
            "B) To list all market competitors",
            "C) To explain customer demographics",
            "D) To offer a concise overview of the business"
        ],
        "answer": "D"
    },
    {
        "question": "What is the significance of the company’s origin story?",
        "choices": [
            "A) It explains the business’s mission and purpose",
            "B) It provides details about competitors",
            "C) It highlights product flaws",
            "D) It lists financial resources"
        ],
        "answer": "A"
    },
    {
        "question": "What is the legal structure of a business used for?",
        "choices": [
            "A) Determining marketing strategies",
            "B) Identifying customer preferences",
            "C) Simplifying liability management and tax planning",
            "D) Choosing product designs"
        ],
        "answer": "C"
    },
    {
        "question": "What are core values in a business plan?",
        "choices": [
            "A) The company’s marketing budget",
            "B) Industry benchmarks",
            "C) Annual financial goals",
            "D) Principles guiding the business"
        ],
        "answer": "D"
    },
    {
        "question": "Why should a business plan be updated regularly?",
        "choices": [
            "A) To align with changes in the business",
            "B) To attract more competitors",
            "C) To replace outdated customer data",
            "D) To avoid market expansion"
        ],
        "answer": "A"
    },
    {
        "question": "What should be the focus of a business plan’s executive summary?",
        "choices": [
            "A) Detailed team member roles",
            "B) Product, target market, and key advantage",
            "C) Competitor weaknesses",
            "D) Logistics and supply chain management"
        ],
        "answer": "B"
    },
    {
        "question": "What does market research involve?",
        "choices": [
            "A) Avoiding competitor analysis",
            "B) Reviewing outdated market reports",
            "C) Ignoring customer feedback",
            "D) Studying customer demographics and industry trends"
        ],
        "answer": "D"
    },
    {
        "question": "How can a strong company description build trust?",
        "choices": [
            "A) By listing competitors",
            "B) By showcasing the business’s purpose and structure",
            "C) By highlighting market gaps",
            "D) By providing customer testimonials"
        ],
        "answer": "B"
    },
    {
        "question": "Why is it important to identify resources before writing a business plan?",
        "choices": [
            "A) To determine what is needed to start the business",
            "B) To simplify competitor analysis",
            "C) To reduce marketing costs",
            "D) To finalize financial projections"
        ],
        "answer": "A"
    },
    {
        "question": "What is an example of a company’s competitive advantage?",
        "choices": [
            "A) Using outdated manufacturing methods",
            "B) A unique manufacturing process reducing costs",
            "C) Targeting a broad, undefined market",
            "D) Avoiding innovation"
        ],
        "answer": "B"
    },
    {
        "question": "What is an example of a long-term business goal?",
        "choices": [
            "A) Selling 1,000 units in the first six months",
            "B) Reducing short-term costs",
            "C) Expanding into European markets by year two",
            "D) Improving the company’s website"
        ],
        "answer": "C"
    },
    {
        "question": "What should a business focus on when writing a plan?",
        "choices": [
            "A) Avoiding customer preferences",
            "B) Increasing competitor dependence",
            "C) Expanding without research",
            "D) The target audience and their needs"
        ],
        "answer": "D"
    },
    {
        "question": "Why is clarity important in a business plan?",
        "choices": [
            "A) To ensure readers understand its goals and strategies",
            "B) To avoid unnecessary details",
            "C) To simplify competitor analysis",
            "D) To replace visuals and tables"
        ],
        "answer": "A"
    },
    {
        "question": "Why is market analysis important in a business plan?",
        "choices": ["A) To finalize pricing strategies", "B) To describe the organizational structure",
                    "C) To avoid unnecessary research",
                    "D) To understand customers, competitors, and market opportunities"],
        "answer": "D"
    },
    {
        "question": "What should be included in the target market section of business plan?",
        "choices": ["A) A list of all potential customers globally", "B) Specific ideal customer groups",
                    "C) Competitor weaknesses", "D) Revenue projections"],
        "answer": "B"
    },
    {
        "question": "What is an example of competitor analysis of business plan?",
        "choices": ["A) Ignoring competitors’ weaknesses", "B) Listing all competitors without analysis",
                    "C) Highlighting your competitors’ branding and gaps", "D) Showing financial projections"],
        "answer": "C"
    },
    {
        "question": "Why is the organization and management section of business plan important?",
        "choices": ["A) It shows investors the team’s qualifications and business structure",
                    "B) It focuses solely on the CEO's qualifications", "C) It emphasizes competitors' strategies",
                    "D) It replaces the financial projections"],
        "answer": "A"
    },
    {
        "question": "What should be included under key team members section of business plan?",
        "choices": ["A) Competitor revenue estimates", "B) Only the CEO’s details",
                    "C) Team members' experience and roles", "D) Product descriptions"],
        "answer": "C"
    },
    {
        "question": "What makes a product description effective in a business plan?",
        "choices": ["A) It avoids technical details", "B) It explains the product's features and benefits",
                    "C) It focuses only on competitors’ features", "D) It lists future revenue projections"],
        "answer": "B"
    },
    {
        "question": "Why are financial projections important in a business plan?",
        "choices": ["A) To describe competitors’ weaknesses", "B) To define product features",
                    "C) To avoid detailed cost analysis", "D) To show potential for profit and growth"],
        "answer": "D"
    },
    {
        "question": "What does a break-even analysis show?",
        "choices": ["A) When the business will cover its costs and become profitable",
                    "B) When customer feedback will be collected", "C) When competitors might overtake your business",
                    "D) When funding applications should be submitted"],
        "answer": "A"
    }
]

random.shuffle(questions)  # Soruları karıştır
current_question_index = 0
correct_count = 0

@app.route('/')
def home():
    """Ana sayfa: testi başlatır"""
    global current_question_index, correct_count
    current_question_index = 0
    correct_count = 0
    return redirect(url_for('quiz'))

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    """Soruları görüntüleme ve cevap kontrolü"""
    global current_question_index, correct_count

    if request.method == 'POST':
        user_answer = request.form.get('choice')
        correct_answer = questions[current_question_index]['answer']
        if user_answer == correct_answer:
            correct_count += 1
        current_question_index += 1

        if current_question_index >= len(questions):
            return redirect(url_for('result'))

    question = questions[current_question_index]
    return render_template('quiz.html', question=question, index=current_question_index + 1, total=len(questions))

@app.route('/result')
def result():
    """Sonuçları gösterir"""
    return render_template('result.html', correct_count=correct_count, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
