import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables for inputs and outputs
recipient_type = ctrl.Antecedent(np.arange(0, 11, 1), 'recipient_type')
occasion = ctrl.Antecedent(np.arange(0, 11, 1), 'occasion')
budget = ctrl.Antecedent(np.arange(0, 101, 1), 'budget')
gift_category = ctrl.Consequent(np.arange(0, 11, 1), 'gift_category')

# Define fuzzy sets for recipient type
recipient_type['family'] = fuzz.trimf(recipient_type.universe, [0, 2, 4])
recipient_type['friend'] = fuzz.trimf(recipient_type.universe, [3, 5, 7])
recipient_type['colleague'] = fuzz.trimf(recipient_type.universe, [6, 8, 10])

# Define fuzzy sets for occasion
occasion['birthday'] = fuzz.trimf(occasion.universe, [0, 2, 4])
occasion['anniversary'] = fuzz.trimf(occasion.universe, [3, 5, 7])
occasion['holiday'] = fuzz.trimf(occasion.universe, [6, 8, 10])

# Define fuzzy sets for budget
budget['low'] = fuzz.trimf(budget.universe, [0, 20, 40])
budget['medium'] = fuzz.trimf(budget.universe, [30, 50, 70])
budget['high'] = fuzz.trimf(budget.universe, [60, 80, 100])

# Define fuzzy sets for gift category (output)
gift_category = ctrl.Consequent(np.arange(0, 11, 1), 'gift_category')
gift_category['personalized'] = fuzz.trimf(gift_category.universe, [0, 2, 4])
gift_category['luxury'] = fuzz.trimf(gift_category.universe, [3, 6, 8])
gift_category['practical'] = fuzz.trimf(gift_category.universe, [7, 9, 10])

# Define fuzzy rules
rule1 = ctrl.Rule(recipient_type['family'] & occasion['birthday'] & budget['low'], gift_category['personalized'])
rule2 = ctrl.Rule(recipient_type['friend'] & occasion['holiday'] & budget['high'], gift_category['luxury'])
rule3 = ctrl.Rule(recipient_type['colleague'] & occasion['anniversary'] & budget['medium'], gift_category['practical'])

# Additional rules to ensure broader coverage
rule4 = ctrl.Rule(recipient_type['friend'] & occasion['birthday'] & budget['medium'], gift_category['personalized'])
rule5 = ctrl.Rule(recipient_type['family'] & occasion['holiday'] & budget['high'], gift_category['luxury'])

# Create and simulate fuzzy control system
gift_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
gift_suggestion = ctrl.ControlSystemSimulation(gift_ctrl)

# Function to get gift suggestions
def suggest_gift(recipient, occasion_input, budget_input):
    # Map string inputs to fuzzy values
    recipient_mapping = {'family': 2, 'friend': 5, 'colleague': 8}
    occasion_mapping = {'birthday': 2, 'anniversary': 5, 'holiday': 8}
    budget_mapping = {'low': 20, 'medium': 50, 'high': 80}
    
    # Convert the input strings to fuzzy values
    recipient_type_value = recipient_mapping.get(recipient.lower(), 5)  # Default to 'friend' if input is invalid
    occasion_value = occasion_mapping.get(occasion_input.lower(), 5)  # Default to 'anniversary'
    budget_value = budget_mapping.get(budget_input.lower(), 50)  # Default to 'medium'
    
    # Debugging logs to check input mapping
    print(f"Recipient Type Value: {recipient_type_value}, Occasion Value: {occasion_value}, Budget Value: {budget_value}")
    
    # Use the fuzzy logic system
    gift_suggestion.input['recipient_type'] = recipient_type_value
    gift_suggestion.input['occasion'] = occasion_value
    gift_suggestion.input['budget'] = budget_value
    gift_suggestion.compute()
    
    # Debugging log to check if output is available
    if 'gift_category' in gift_suggestion.output:
        print(f"Gift Category: {gift_suggestion.output['gift_category']}")
        return gift_suggestion.output['gift_category']
    else:
        print("No suggestion available.")
        return "No suggestion available. Please check your inputs."
