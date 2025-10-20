#!/usr/bin/env python3
"""
Script to classify prompts by topic based on filename patterns and keywords
"""

import os
import json
from collections import defaultdict

# Define topic categories and their associated keywords
CATEGORIES = {
    "AI & Technology": [
        "ai_", "ai ", "chatbot", "automation", "machine_learning", "ml_",
        "chatgpt", "claude", "llm", "neural", "deep_learning"
    ],
    "Business Strategy & Development": [
        "business_strategy", "business_plan", "business_development", "startup",
        "entrepreneur", "business_opportunities", "business_improvement",
        "business_incubation", "comprehensive_business", "franchise"
    ],
    "Marketing & Social Media": [
        "marketing", "social_media", "instagram", "tiktok", "facebook", "linkedin",
        "twitter", "content_strategy", "seo", "viral", "engagement", "branding",
        "brand_", "pinterest", "youtube_", "advertisement", "ad_strategy"
    ],
    "Cybersecurity & IT": [
        "cybersecurity", "malware", "threat", "security", "sigma_rules", "nuclei",
        "semgrep", "audit_guide", "incident", "breach", "gdpr", "nist", "iso_27001",
        "stride", "hackerone", "vulnerability"
    ],
    "Content Creation & Writing": [
        "write_", "create_content", "video_script", "copywriting", "blog_",
        "article", "newsletter", "podcast", "faceless", "video_prompts",
        "ugc", "screenplay", "documentary", "storytelling"
    ],
    "Career & Professional Development": [
        "career_", "resume", "cv_", "job_", "interview", "professional_development",
        "networking", "job_search", "job_application", "hiring", "recruitment",
        "salary_negotiation", "cover_letter"
    ],
    "Education & Training": [
        "course_", "study_", "lesson_plan", "curriculum", "training", "learning",
        "education", "teach", "academic", "school", "university", "student",
        "exam", "test_", "quiz", "masterclass", "workshop", "nclex", "gre_"
    ],
    "Analysis & Data": [
        "analyze_", "extract_", "summarize", "data_analysis", "insights",
        "evaluate", "assess", "review_", "rate_", "survey", "research_"
    ],
    "Health & Wellness": [
        "health", "wellness", "fitness", "nutrition", "meal_plan", "diet",
        "mental_health", "therapy", "medical", "nursing", "patient", "cognitive_health",
        "bodybuilding", "workout"
    ],
    "Creative & Entertainment": [
        "coloring_book", "storybook", "creative_writing", "story_", "folk_tale",
        "fantasy", "comic", "game_", "npc_", "character", "dialogue", "fiction"
    ],
    "Finance & Investment": [
        "investment", "finance", "financial", "trading", "stock", "options",
        "forex", "cryptocurrency", "crypto_", "banking", "tax_", "mortgage",
        "credit_card", "budgeting", "wealth"
    ],
    "Real Estate": [
        "real_estate", "property", "listing", "tenant", "housing", "home_improvement",
        "construction", "architect"
    ],
    "E-commerce & Digital Products": [
        "ecommerce", "e-commerce", "dropshipping", "digital_product", "shopify",
        "alibaba", "supplier", "kdp", "amazon", "etsy", "online_store"
    ],
    "Sales & Lead Generation": [
        "sales_", "lead_generation", "funnel", "conversion", "prospect",
        "pitch_deck", "proposal", "rfp_", "client_acquisition", "crm"
    ],
    "Personal Development": [
        "personal_development", "self_improvement", "self_help", "goal_setting",
        "productivity", "time_management", "motivation", "confidence", "adhd",
        "autism", "dream_life", "ikigai"
    ],
    "Prompt Engineering & Meta": [
        "prompt_engineering", "improve_prompt", "create_prompt", "prompt_library",
        "midjourney_prompts", "art_prompt", "combine_prompts"
    ],
    "Legal & Compliance": [
        "legal", "compliance", "contract", "terms_and_conditions", "privacy_policy",
        "agreement", "constitution", "petition", "appeal", "case_document"
    ],
    "Project Management": [
        "project_management", "project_charter", "project_closure", "agile", "scrum",
        "gantt", "roadmap", "workflow", "process"
    ],
    "Nonprofit & Social Impact": [
        "nonprofit", "non_profit", "grant", "funding", "charity", "community",
        "social_impact", "ngo", "sponsorship", "donation"
    ],
    "Human Resources": [
        "hr_", "human_resource", "employee", "recruitment", "hiring", "onboarding",
        "performance_review", "job_description", "workforce"
    ],
}

def classify_file(filename):
    """Classify a file based on its name"""
    filename_lower = filename.lower()

    # Store matching categories and their match counts
    matches = defaultdict(int)

    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in filename_lower:
                matches[category] += 1

    # Return the category with most matches, or "Miscellaneous" if no matches
    if matches:
        return max(matches.items(), key=lambda x: x[1])[0]
    return "Miscellaneous"

def main():
    # Get all .md files except README and this script
    files = [f for f in os.listdir('.') if f.endswith('.md') and f != 'README.md']

    # Classify files
    classified = defaultdict(list)
    for file in sorted(files):
        category = classify_file(file)
        classified[category].append(file)

    # Print results
    print(f"\n{'='*80}")
    print(f"PROMPT CLASSIFICATION SUMMARY")
    print(f"{'='*80}\n")
    print(f"Total files analyzed: {len(files)}\n")

    # Sort categories by number of files (descending)
    sorted_categories = sorted(classified.items(), key=lambda x: len(x[1]), reverse=True)

    for category, file_list in sorted_categories:
        print(f"\n{category} ({len(file_list)} files)")
        print("-" * 80)
        for file in file_list[:10]:  # Show first 10 files
            print(f"  • {file}")
        if len(file_list) > 10:
            print(f"  ... and {len(file_list) - 10} more")

    # Save detailed classification to JSON
    output = {
        "total_files": len(files),
        "categories": {cat: files for cat, files in sorted_categories}
    }

    with open('classification_results.json', 'w') as f:
        json.dump(output, f, indent=2)

    print(f"\n{'='*80}")
    print(f"Detailed results saved to: classification_results.json")
    print(f"{'='*80}\n")

if __name__ == "__main__":
    main()
