class PriorityAnalyzer:
    def __init__(self):
        # Critical symptoms that require immediate attention
        self.critical_symptoms = {
            'chest pain', 'difficulty breathing', 'severe bleeding',
            'unconscious', 'stroke', 'heart attack', 'seizure',
            'severe trauma', 'head injury', 'severe allergic reaction',
            'anaphylaxis', 'overdose', 'poisoning'
        }

        # High priority symptoms
        self.high_priority_symptoms = {
            'high fever', 'broken bone', 'severe pain',
            'severe vomiting', 'severe dehydration', 'diabetic emergency',
            'asthma attack', 'severe infection'
        }

    def analyze_symptoms(self, symptoms):
        """
        Analyze patient symptoms to determine if they should be tagged as critical.
        
        Args:
            symptoms (str): String containing patient symptoms
            
        Returns:
            tuple: (is_critical (bool), priority_level (str), reason (str))
        """
        symptoms_lower = symptoms.lower()
        
        # Check for critical symptoms
        for symptom in self.critical_symptoms:
            if symptom in symptoms_lower:
                return True, "Critical", f"Critical symptom detected: {symptom}"

        # Check for high priority symptoms
        for symptom in self.high_priority_symptoms:
            if symptom in symptoms_lower:
                return True, "High Priority", f"High priority symptom detected: {symptom}"

        # Count the number of symptoms
        symptom_count = len([s for s in symptoms_lower.split() if len(s) > 3])
        
        # If patient has multiple symptoms, mark as medium priority
        if symptom_count >= 3:
            return False, "Medium Priority", "Multiple symptoms reported"
            
        return False, "Normal", "No critical symptoms detected"

    def get_recommendation(self, priority_level):
        """
        Get recommended actions based on priority level.
        
        Args:
            priority_level (str): The priority level determined by analyze_symptoms
            
        Returns:
            str: Recommended actions for medical staff
        """
        recommendations = {
            "Critical": "Immediate medical attention required. Alert emergency team.",
            "High Priority": "Expedited care needed. Monitor closely.",
            "Medium Priority": "Regular monitoring required. Check vitals periodically.",
            "Normal": "Standard care protocols apply."
        }
        
        return recommendations.get(priority_level, "Standard care protocols apply.")
