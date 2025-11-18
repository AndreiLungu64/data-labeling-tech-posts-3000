# Stack Exchange Data Labeling Project

This project demonstrates a complete data labeling workflow using Stack Exchange datasets. It includes data extraction, annotation with **Label Studio**, and creation of clean, annotated datasets suitable for machine learning tasks.

---

## Original Data Source

The raw XML files are available publicly from Stack Exchange:

- **Code Review:** [Stack Exchange Data Dump](https://archive.org/details/stackexchange)
- **Web Apps:** [Stack Exchange Data Dump](https://archive.org/details/stackexchange)
- **Workplace:** [Stack Exchange Data Dump](https://archive.org/details/stackexchange)

> The CSV files in this repository are extracted samples (first 1000 posts per site, filtered for text ≥50 characters) from the respective `Posts.xml` files.

---

## Project Structure

```
stackexchange-data-labeling/
│
├── data/
│   │
│   ├── processed/             # CSV samples produced by parse.py (first 1,000 posts per site, filtered for text ≥50 chars)
│   │   ├── codereview_processed.csv
│   │   ├── webapps_processed.csv
│   │   └── workplace_processed.csv
│   │
│   └── annotated/             # CSVs after Label Studio annotation
│       ├── codereview_classification_annotated.csv
│       ├── webapps_ner_annotated.csv
│       └── workplace_sentiment_annotated.csv
│
├── scripts/
│   └── parse.py               # XML-to-CSV extraction script
│
├── labeling_templates/        # Custom Label Studio templates
│   ├── text_classification.xml
│   └── ner_template.xml
│
└── README.md
```

---

## Workflow Overview

1. **Data Extraction**
   The `parse.py` script parses `Posts.xml` files, filters posts with ≥50 characters, and outputs the first 1000 entries per dataset as CSV files.

2. **Data Annotation**
   Custom Label Studio templates were created for the Text Classification and NER tasks, while the Sentiment Analysis task used Label Studio’s built-in “Text Classification” template.

   - Text Classification: `text_classification.xml`
   - Named Entity Recognition: `ner_template.xml`
   - Annotated datasets were exported as CSV for model training or analysis.

---

## Dataset Details

### 1. Text Classification — Code Review

- **Source:** `codereview.stackexchange.com`
- **Goal:** Classify posts by intent and various technical topics.
- **Labels:**

**Intent**

- **Optimization** — performance, efficiency, or memory improvements
- **BugFix** — resolving errors, failures, or unexpected behavior
- **Readability** — clarity, formatting, naming, or style issues
- **Design** — architectural, structural, or OOP-related concerns
- **LanguageHelp** — questions tied to a specific programming language feature or syntax

**Context**

- **WebDevelopment** — web apps, frontend, backend, APIs, or browser-related topics
- **DataAlgorithms** — data structures, algorithms, or computational logic
- **SystemCode** — system-level programming or environment-related issues
- **GeneralProgramming** — broadly applicable programming topics

**Programming Language**

- **Python** — explicitly Python-related content
- **JavaScript** — JS-related code or issues
- **C++** — C++-specific questions
- **Java** — Java-related content
- **C#** — C# or .NET topics
- **PHP** — PHP-based questions
- **Other** — any language outside the main list

**Tone**

- **Informative** — factual, explanatory tone
- **SeekingHelp** — the author requests guidance or solutions
- **Opinionated** — subjective views, preferences, or evaluations
- **Neutral** — unemotional, descriptive, or matter-of-fact statements

* **Dataset size:** 1000 posts
* **Annotated file:** `codereview_classification_annotated.csv`
* **Result:** Dataset suitable for training models to auto-categorize programming discussions.

---

### 2. Named Entity Recognition (NER) — Web Apps

- **Source:** `webapps.stackexchange.com`
- **Goal:** Identify software names, features, and UI elements.
  **Entity examples:**
- **APP** — Tools the user interacts with directly, typically client-side or installed apps. _Example:_ “Outlook”, “JWPlayer”, “Mafia Wars”.
- **SERVICE** — Online platforms or hosted systems delivering content or functionality. . _Example:_ “Gmail”, “YouTube”, “Dropbox”.
- **FEATURE** — Named functionality or capability inside a service or app. _Example:_ “auto-forward”, “Protect my Tweets”, “Content ID”.
- **FILE_TYPE** — Named file formats or programming file types. _Example:_ “PDF”, “.docx”, “spreadsheet”. Programming languages are only labeled if referring to actual files (e.g., “.php file”).
- **UI_ELEMENT** — Clickable or interactable interface components such as buttons, menus, checkboxes, tabs, or paths. _Example:_ “Settings → Protect my Tweets”, “Hide button” “Select all”.

**Workflow Clarifications:**

- Company names alone are not SERVICE unless the platform is explicitly referenced.
- Only canonical names were labeled; possessives or extra characters were ignored (e.g., “Amazon,” not “Amazon’s”).
- Each distinct UI_ELEMENT in navigation paths or menus was labeled separately; for example, in “Settings → Advanced → User,” each element (Settings, Advanced, User) was labeled individually. Separators like → or | were ignored.
- Actions or features mentioned by the user that are not confirmed to exist in the app (e.g., “delete my messages”) were not labeled as FEATURE. Only actual, existing features were categorized.
- Generic nouns or user actions were not labeled unless they corresponded to official feature names (e.g., “account,” “log in” were ignored ).
- UI status messages or descriptive text were left untagged and not categorised as UI_ELEMENT, System messages, status texts, or outcomes are **not** UI_ELEMENT even if they appear on screen.

- **Dataset size:** 1000 posts
- **Annotated file:** `webapps_ner_annotated.csv`
- **Result:** Dataset useful for training models on software and UI-related entity recognition.

---

### 3. Sentiment Analysis — Workplace

- **Source:** `workplace.stackexchange.com`
- **Goal:** Label emotional tone of posts.
- **Labels:**

- **Positive** — Expresses encouragement, helpful guidance, or success stories with an uplifting tone. Offers actionable advice or constructive ideas. _Example:_ “Here’s a method that worked for me to take a vacation without stress.”
- **Neutral** — Informational, factual, or procedural posts without strong emotional content. May mention issues but remains descriptive. _Example:_ “Ask the recruiter what the salary range is for the position.”
- **Negative** — Expresses frustration, complaints, or dissatisfaction without constructive guidance. Focuses on emotional struggle or venting. _Example:_ “I’m overwhelmed with work and can’t take a vacation.”

- **Dataset size:** 1000 posts
- **Annotated file:** `workplace_sentiment_annotated.csv`
- **Result:** Dataset for training models on professional sentiment and tone detection.

---

## Usage

1. Clone the repository.
2. Inspect the processed CSVs in `data/processed/`.
3. Explore annotated datasets in `data/annotated/`.
4. Use `parse.py` to reprocess XMLs if needed (requires original XML files from Stack Exchange).
5. Label Studio templates are in `labeling_templates/` for reproduction or further annotation.

---
