from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

# Sample responses for legal Q&A
responses = {
    "What is a contract?": "A contract is a legally binding agreement between two or more parties. It outlines the terms and conditions under which the parties agree to act.",
    "What is the meaning of liability?": "Liability refers to the legal responsibility for something, especially in relation to legal claims or obligations. It can arise from contracts, torts, or statutory violations.",
    "What is a tort?": "A tort is a civil wrong or injury that causes harm or loss to an individual or entity. It can lead to legal liability if the harm was caused due to negligence, intentional misconduct, or strict liability.",
    "What is the difference between civil and criminal law?": "Civil law deals with disputes between individuals or organizations over rights, obligations, or compensation. Criminal law, on the other hand, deals with actions that are offenses against the state or society, which are punishable by law.",
    "What is intellectual property?": "Intellectual property (IP) refers to creations of the mind, such as inventions, literary works, designs, and symbols. Legal protections, like patents and copyrights, prevent others from using these without permission.",
    "What is a patent?": "A patent is a form of intellectual property that grants the patent holder the exclusive right to produce, use, and sell an invention for a specific period, typically 20 years.",
    "What is copyright?": "Copyright is a form of protection granted to the creators of original works of authorship, such as literature, music, and art. It allows the creator to control reproduction, distribution, and performance of their work.",
    "What is the statute of limitations?": "The statute of limitations is a law that sets the maximum time after an event within which legal proceedings can be initiated. It varies depending on the type of case and jurisdiction.",
    "What is a lease agreement?": "A lease agreement is a contract between a landlord and tenant that outlines the terms for renting property, including rental amount, duration, and responsibilities of both parties.",
    "What is the difference between a will and a trust?": "A will is a legal document that specifies how a person's assets will be distributed upon their death, while a trust is a legal arrangement where a trustee holds assets for the benefit of beneficiaries.",
    "What is bankruptcy?": "Bankruptcy is a legal process in which an individual or business declares an inability to pay their debts. It allows for a fresh start by liquidating assets or reorganizing finances under court supervision.",
    "What is a trademark?": "A trademark is a symbol, word, or other identifier used to distinguish goods or services of one company from those of others. It helps protect the brand identity of a company or product.",
    "What is defamation?": "Defamation is the act of making false statements about someone that harm their reputation. It can be either libel (written) or slander (spoken).",
    "What is a power of attorney?": "A power of attorney is a legal document that grants someone the authority to act on behalf of another person in private affairs, business, or legal matters.",
    "What is an NDA (Non-Disclosure Agreement)?": "An NDA is a legal contract where one or more parties agree to keep certain information confidential. It is commonly used to protect trade secrets, business strategies, or sensitive personal data.",
    "What is a breach of contract?": "A breach of contract occurs when one party fails to fulfill their obligations under a contract. The injured party may seek legal remedies, including damages or contract termination.",
    "What is an injunction?": "An injunction is a court order that requires a party to do or refrain from doing a specific act. It is often used to prevent harm or preserve the status quo.",
    "What is a shareholder agreement?": "A shareholder agreement is a contract between a company's shareholders that defines their rights and obligations, including the management of the company and how disputes will be resolved.",
    "What is wrongful termination?": "Wrongful termination occurs when an employee is dismissed from their job for illegal reasons, such as discrimination, retaliation, or breach of contract.",
    "What is workers' compensation?": "Workers' compensation is a form of insurance that provides financial benefits to employees who are injured or become ill as a result of their job. It typically covers medical expenses and lost wages.",
    "What is due process?": "Due process is the legal requirement that the state must respect all legal rights owed to a person. It ensures fair treatment through the normal judicial system, especially as it relates to the rights of the accused in criminal cases.",
    "What is an arrest warrant?": "An arrest warrant is a legal document issued by a judge or magistrate that authorizes law enforcement officers to arrest a person suspected of committing a crime.",
    "What is a class action lawsuit?": "A class action lawsuit is a legal action filed by a group of people who have suffered similar harm or damages from the same defendant. It allows them to sue as a group, rather than as individuals.",
    "What is an escrow account?": "An escrow account is a financial arrangement where a third party holds funds or assets on behalf of two other parties until specific conditions are met. It is commonly used in real estate transactions.",
    "What is the difference between mediation and arbitration?": "Mediation is a voluntary, non-binding process in which a neutral third party helps parties reach a resolution. Arbitration, on the other hand, is a more formal process in which an arbitrator makes a binding decision after hearing both sides.",
}

@app.route('/')
def home():
    return render_template('index.html')  # Serve the HTML file

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('question')  # Get the question from the request

    # Simulate some delay
    time.sleep(2)

    # Get the answer from the predefined responses
    answer = responses.get(user_input, "Sorry, I couldn't understand that question.")

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
