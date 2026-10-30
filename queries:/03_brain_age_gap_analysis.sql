
USE neuro_longevity;

-- ============================================================================
-- Script: 03_brain_age_gap_analysis.sql (MySQL Version)
-- Description: Queries predicted biological brain age against actual chronological
--              age, ranks subjects by BAGI score, and correlates risk with 
--              cognitive scores (MMSE).
-- ============================================================================

-- Query 1: Rank subjects by accelerated brain aging (BAGI score)
SELECT 
    p.subject_id,
    p.chronological_age_at_scan AS chronological_age,
    p.predicted_brain_age,
    p.bagi_score,
    p.risk_category,
    s.cognitive_status,
    s.mmse_score,
    -- Rank highest BAGI score first (highest neurodegeneration risk)
    DENSE_RANK() OVER (ORDER BY p.bagi_score DESC) AS accelerated_aging_rank
FROM brain_age_predictions p
JOIN subjects s ON p.subject_id = s.subject_id
ORDER BY p.bagi_score DESC;

-- Query 2: Aggregate risk summary across cognitive status groups
SELECT 
    s.cognitive_status,
    COUNT(p.subject_id) AS total_subjects,
    ROUND(AVG(p.chronological_age_at_scan), 2) AS avg_chronological_age,
    ROUND(AVG(p.predicted_brain_age), 2) AS avg_predicted_brain_age,
    ROUND(AVG(p.bagi_score), 2) AS avg_bagi_score
FROM brain_age_predictions p
JOIN subjects s ON p.subject_id = s.subject_id
GROUP BY s.cognitive_status;