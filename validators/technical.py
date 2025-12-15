def technical_validator(change_description):
    issues = []
    score = 80

    if "cloud" in change_description.lower():
        issues.append("Cloud provider not specified")
        score -= 20

    return {
        "summary": "Basic technical validation completed.",
        "score": score,
        "risk_level": "Medium" if score < 90 else "Low",
        "critical_issues": issues,
        "recommendations": [
            "Specify cloud provider",
            "Review backup and rollback strategy"
        ]
    }
