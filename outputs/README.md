# Analytics Outputs Folder Structure

```
outputs/
├── README.md
├── figures/
│   ├── exploratory/
│   │   ├── distribution_plots/
│   │   ├── correlation_matrices/
│   │   └── time_series/
│   ├── final/
│   │   ├── executive_summary/
│   │   ├── detailed_analysis/
│   │   └── appendix/
│   └── archive/
│       └── YYYY-MM-DD_analysis_name/
├── reports/
│   ├── automated/
│   │   ├── daily/
│   │   ├── weekly/
│   │   └── monthly/
│   ├── ad-hoc/
│   │   ├── YYYY-MM-DD_report_name.pdf
│   │   └── YYYY-MM-DD_report_name.html
│   ├── executive/
│   │   └── executive_summary_YYYY-MM-DD.pdf
│   └── templates/
│       ├── standard_report_template.html
│       └── executive_summary_template.pptx
├── dashboards/
│   ├── specs/
│   │   ├── dashboard_requirements.md
│   │   └── metric_definitions.yaml
│   ├── screenshots/
│   │   └── dashboard_v1_YYYY-MM-DD.png
│   └── exports/
│       ├── dashboard_data_YYYY-MM-DD.csv
│       └── dashboard_config.json
├── presentations/
│   ├── stakeholder_meetings/
│   │   ├── YYYY-MM-DD_quarterly_review.pptx
│   │   └── YYYY-MM-DD_findings_presentation.pdf
│   ├── team_share/
│   │   └── methodology_walkthrough.pptx
│   └── templates/
│       └── company_template.pptx
├── exports/
│   ├── data/
│   │   ├── cleaned_datasets/
│   │   ├── aggregated_metrics/
│   │   └── segmentation_results/
│   ├── tables/
│   │   ├── summary_statistics.csv
│   │   ├── key_metrics.xlsx
│   │   └── comparison_tables.csv
│   └── for_stakeholders/
│       └── YYYY-MM-DD_data_package/
└── archive/
    ├── 2024/
    │   ├── Q1/
    │   ├── Q2/
    │   ├── Q3/
    │   └── Q4/
    └── 2025/
        ├── Q1/
        └── Q2/
```

## Folder Purposes

### `figures/`

- **exploratory/**: Charts created during analysis (not for final presentation)
- **final/**: Publication-ready visualizations organized by audience
- **archive/**: Historical versions of figures with date-stamped folders

### `reports/`

- **automated/**: Scheduled reports (daily/weekly/monthly metrics)
- **ad-hoc/**: One-time analysis reports with clear date stamps
- **executive/**: High-level summaries for leadership
- **templates/**: Reusable report formats (HTML, PowerPoint, etc.)

### `dashboards/`

- **specs/**: Requirements and metric definitions for dashboard development
- **screenshots/**: Visual documentation of dashboard versions
- **exports/**: Data extracts and configuration files for dashboard tools

### `presentations/`

- **stakeholder_meetings/**: Formal presentations for decision-makers
- **team_share/**: Internal knowledge sharing and methodology documentation
- **templates/**: Company-branded presentation templates

### `exports/`

- **data/**: Processed datasets ready for external use or sharing
- **tables/**: Summary tables and metrics in spreadsheet format
- **for_stakeholders/**: Complete data packages with documentation

### `archive/`

- Organized by year and quarter for long-term storage
- Prevents clutter in active folders
- Maintains audit trail of historical analyses

## Best Practices

1. **Date Stamping**: Use `YYYY-MM-DD` format for all dated files
2. **Naming Convention**: `YYYY-MM-DD_descriptive_name.ext`
3. **Version Control**: For iterative work, use `_v1`, `_v2`, or date stamps
4. **README Files**: Add README.md in key folders explaining contents
5. **Regular Archiving**: Move completed projects to archive quarterly
6. **Stakeholder-Ready**: Keep `for_stakeholders/` folders clean and documented

## Example File Names

```
outputs/figures/final/executive_summary/2025-10-06_revenue_trends.png
outputs/reports/ad-hoc/2025-10-06_customer_churn_analysis.pdf
outputs/presentations/stakeholder_meetings/2025-10-06_Q3_business_review.pptx
outputs/exports/for_stakeholders/2025-10-06_sales_data_package/
    ├── data.csv
    ├── data_dictionary.md
    └── analysis_summary.pdf
```
