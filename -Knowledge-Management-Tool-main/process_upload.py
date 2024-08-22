class DecisionTree:
    def __init__(self):
        self.tree = {
            'Account Balances': {
                'Balance Inquiry Assistance': {
                    'Incorrect Balance Display': 'If you notice an incorrect balance, check for recent transactions or pending transactions. If the issue persists, contact customer support for further investigation.',
                    'Pending Transactions': 'Pending transactions may take some time to reflect in your balance. If the issue persists, please provide the details for us to assist you.',
                    'ATM Withdrawal Discrepancy': 'If you encounter issues with ATM withdrawals, please share the ATM location, date, and amount of withdrawal for us to investigate and resolve the discrepancy.'
                },
                'Discrepancy Resolution Services': {
                    'Unrecognized Transactions': 'Report any unrecognized transactions immediately. We will investigate and take appropriate action to secure your account.',
                    'Billing Errors': 'We apologize for billing errors. Kindly provide the relevant billing information, and we will review and rectify the error.',
                    'Disputed Transactions': 'If you have disputed a transaction, please share the details. We will conduct a thorough investigation and keep you updated on the resolution progress.',
                    'Failed or Reversed Transactions': 'We understand the frustration with failed or reversed transactions. Please provide transaction details, and we will look into the matter and provide a resolution.'
                }
            },
            'Transaction Inquiries': {
                'Transaction Verification Support': {
                    'Unauthorized Transactions': 'Report unauthorized transactions immediately. We take the security of your transactions seriously.',
                    'Transaction Details Clarification': 'If you need clarification on a transaction, please provide the details, and we will ensure you receive the necessary information.',
                    'Duplicate Transactions': 'We apologize for any duplication. Kindly share transaction details for us to investigate and rectify the issue.',
                    'Delayed Transaction Posting': 'Transactions may sometimes experience delays. If you have concerns, please provide details, and we\'ll look into it.'
                },
                'Payment Resolution Services': {
                    'Failed Payments': 'We apologize for any inconvenience. Please share payment details, and we\'ll investigate the issue and provide a resolution.',
                    'Refund Processing': 'If you are awaiting a refund, please provide relevant details, and we will check the status and provide assistance.',
                    'Payment Allocation Discrepancy': 'We understand the importance of accurate payment allocation. Please provide details, and we\'ll review and address the discrepancy.',
                    'Disputed Payments': 'If you have disputed a payment, please share the details, and we\'ll initiate an investigation and keep you informed.'
                }
            },
            'Card Issues': {
                'Lost/Stolen Card Reporting': {
                    'Unauthorized Transactions after Loss': 'Report any unauthorized transactions after losing your card. We will take immediate action to secure your account.',
                    'Emergency Card Replacement': 'Request emergency card replacement if your card is lost or stolen. We will expedite the replacement process.',
                    'Temporary Card Block Issues': 'If you need to temporarily block your card, please report the issue, and we will assist in resolving it.',
                    'Follow-up on Replacement Status': 'If you\'ve requested a replacement card, you can inquire about the status by providing your reference number.'
                },
                'Card Usage Troubleshooting': {
                    'Card Declined Issues': 'Troubleshoot card declined issues by checking the card status and transaction details. If issues persist, contact us for assistance.',
                    'ATM Withdrawal Problems': 'Address ATM withdrawal problems by verifying the ATM location and transaction details. Report the issue for further investigation.',
                    'International Usage Concerns': 'Resolve international usage concerns by checking your card\'s international settings. Contact us if issues persist.',
                    'Contactless Payment Issues': 'Address contactless payment issues by checking the card\'s contactless feature settings. Report any problems for assistance.'
                }
            },
            'Online Banking Assistance': {
                'Password Reset Services': {
                    'Forgotten Password': 'Initiate a password reset if you\'ve forgotten your password. Follow the online prompts or contact support for assistance.',
                    'Password Recovery Issues': 'Resolve password recovery issues by following the online prompts or contacting support for additional help.',
                    'Security Questions': 'Assist with security questions during the password reset process to enhance the security of your online account.'
                },
                'Online Account Access Support': {
                    'Login Problems': 'Resolve login problems by checking your credentials and ensuring your account is not locked. Contact us if issues persist.',
                    'Account Verification': 'Assist with account verification for added security. Follow the online prompts or contact support for assistance.',
                    'Two-Factor Authentication': 'Address two-factor authentication concerns by ensuring proper setup. Contact support for additional help if needed.'
                }
            },
            'Overdraft or Fees': {
                'Overdraft Fee Clarification': {
                    'Unaware of Overdraft Policies': 'Explain overdraft policies to address any confusion. Ensure you are aware of the policies to avoid unexpected fees.',
                    'Transaction Processing Questions': 'Clarify transaction processing questions to understand how fees are applied. Contact us for further explanation.',
                    'Multiple Fees Incurred': 'Investigate and address multiple fees by providing transaction details. We will review and assist in resolving any discrepancies.'
                },
                'Fee Dispute Resolution': {
                    'Disputed Transaction Charges': 'Report disputed charges promptly. We will investigate and provide updates on the resolution process.',
                    'Billing Errors': 'Address billing errors by providing relevant details. We will review and rectify any errors promptly.',
                    'Excessive or Incorrect Charges': 'Investigate and rectify excessive or incorrect charges. Provide details for a thorough review and resolution.'
                }
            },
            'Loan or Mortgage Questions': {
                'Mortgage Payment Schedule Inquiry': {
                    'Payment Due Date Confusion': 'Clarify payment due dates by providing your mortgage details. We will assist in explaining your payment schedule.',
                    'Change in Payment Amount': 'Address changes in payment amount by providing relevant details. We will review and assist with adjustments if necessary.',
                    'Payment Method Changes': 'Assist with changes in payment methods by providing details. We will guide you through the process and update your information.'
                },
                'Loan Information Request': {
                    'Interest Rate Inquiry': 'Provide interest rate details based on your loan. We will ensure you have the accurate information you need.',
                    'Loan Term Explanation': 'Explain loan terms to address any questions or concerns. Contact us for detailed explanations as needed.'
                }
            },
            'Fraud Concerns': {
                'Fraudulent Activity Investigation': {
                    'Unauthorized Transactions': 'Report any unauthorized transactions immediately. We will conduct a thorough investigation to secure your account.',
                    'Suspicious Activity on Statements': 'If you notice any suspicious activity on your statements, report it promptly. We will investigate and take appropriate action.',
                    'Unknown Charges': 'If you see unknown charges on your account, report them immediately. We will review and assist in resolving the issue.',
                    'Account Access Issues': 'If you experience difficulties accessing your account, report it immediately. We will investigate and ensure your account security.',
                    'Unauthorized Account Access Report': 'If you suspect unauthorized access to your account, change your password immediately and report the incident to our support team.',
                    'Identity Theft Concerns': 'If you believe you are a victim of identity theft, contact our support team for assistance in securing your account and preventing further harm.'
                },
                'Suspicious Email Verification': {
                    'Phishing Email Report': 'If you receive an email that appears to be phishing, do not click on any links. Forward the email to our support team for verification.',
                    'Identity Verification for Email Communication': 'To verify the authenticity of our emails, contact our support team directly using trusted contact information.',
                    'Email Content Clarification': 'If you are unsure about the content of an email from us, contact our support team for clarification and guidance.',
                    'Email Sender Authentication': 'Verify the sender\'s email address for authenticity. If in doubt, contact our support team before taking any action.',
                    'Suspicious Attachments or Links': 'Exercise caution with email attachments or links. If you receive unexpected attachments or links, contact our support team for guidance.'
                }
            },
            'General Account Information': {
                'Direct Deposit Setup Assistance': {
                    'Setting Up Direct Deposit': 'To set up direct deposit, provide your employer with our direct deposit details available in your account settings. For further assistance, contact our support team.',
                    'Direct Deposit Status Inquiry': 'If you\'ve set up direct deposit and want to check its status, contact our support team with your account details.',
                    'Changing Direct Deposit Information': 'If you need to update or change your direct deposit information, visit your account settings online or contact our support team for guidance.'
                },
                'New Account Requirements Information': {
                    'Account Opening Process': 'To open a new account, follow the account opening process on our website. Contact our customer support if you need assistance or have questions.',
                    'Document Requirements': 'Ensure you have the necessary documents (ID, proof of address, etc.) for opening a new account. Review our website or contact support for details on document requirements.',
                    'Eligibility Criteria': 'Check the eligibility criteria for opening a new account on our website or contact our customer support for clarification.',
                    'Types of Accounts Available': 'Explore the various types of accounts we offer by visiting our website or contacting our support team for detailed information.'
                }
            },
            'Mobile Banking Issues': {
                'Mobile App Troubleshooting': {
                    'App Login Issues': 'If you\'re experiencing issues logging into the mobile app, ensure you have the correct credentials. Contact support if the problem persists.',
                    'App Crashing': 'If the mobile app is crashing, try updating to the latest version. If the issue persists, contact our technical support team for assistance.',
                    'Error Messages': 'If you encounter error messages in the mobile app, note the details and contact our support team for troubleshooting.',
                    'Functionality Issues': 'For any issues with specific features or functionality, contact our support team with a detailed description for assistance.'
                },
                'Mobile Check Deposit Assistance': {
                    'Check Image Quality': 'Ensure the check image is clear and well-lit when depositing via the mobile app. Contact support if you encounter issues with image quality.',
                    'Deposit Status Inquiry': 'If you want to check the status of a mobile check deposit, contact our support team with the transaction details.',
                    'Deposit Limit Clarification': 'For information on mobile check deposit limits, refer to the app or contact our support team for clarification.',
                    'Failed Mobile Check Deposit': 'If a mobile check deposit fails, check your internet connection and ensure proper check endorsement. Contact support for further assistance.'
                }
            },
            'Interest Rates and Policies': {
                'Savings Account Interest Rate Inquiry': {
                    'Current Savings Account Interest Rate': 'To check the current interest rate for your savings account, visit our website or contact our support team for the latest information.',
                    'Interest Rate Comparison': 'If you\'re interested in comparing savings account interest rates, explore our website or contact our support team for detailed rate comparisons.',
                    'Variable Interest Rate Explanation': 'For an explanation of variable interest rates and how they may impact your savings, contact our support team for personalized assistance.'
                },
                'Account Terms and Conditions Explanation': {
                    'Terms and Conditions Overview': 'To get an overview of your account terms and conditions, review the documentation provided during account setup or contact our support team for clarification.',
                    'Specific Account Policies': 'If you have specific questions about account policies, fees, or terms, contact our support team for detailed information tailored to your account type.',
                }
            }
        }

    def get_user_input(self, options):
        """Get user input for decision tree traversal."""
        while True:
            print("Select one:")
            for idx, option in enumerate(options, 1):
                print(f"{idx}. {option}")
            try:
                choice = int(input("Enter the number: "))
                if 1 <= choice <= len(options):
                    return options[choice - 1]
                else:
                    print("Invalid choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def traverse_tree(self, tree):
        """Traverse the decision tree based on user input."""
        category = self.get_user_input(list(tree.keys()))
        subcategories = tree[category]

        if isinstance(subcategories, dict):
            subcategory = self.get_user_input(list(subcategories.keys()))
            subtopics = subcategories[subcategory]

            if isinstance(subtopics, dict):
                selected_subtopic = self.get_user_input(list(subtopics.keys()))
                print(f"Response: {subtopics[selected_subtopic]}")
            else:
                print(f"Response: {subtopics}")
        else:
            print(f"Response: {subcategories}")

    def start(self):
        """Start the decision tree interaction."""
        print("Welcome to the Customer Care Decision Tree!")

        while True:
            self.traverse_tree(self.tree)
            restart = input("Do you want to explore another branch? (yes/no): ").lower()
            if restart != 'yes':
                break

if __name__ == "__main__":
    decision_tree = DecisionTree()
    decision_tree.start()