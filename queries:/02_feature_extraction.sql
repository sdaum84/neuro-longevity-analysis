-- Select your database first
USE neuro_longevity;

-- Drop view if it already exists
DROP VIEW IF EXISTS vw_brain_volumetric_features;

-- Create view to calculate normalized brain volume ratios
CREATE VIEW vw_brain_volumetric_features AS
SELECT 
    s.subject_id,
    s.chronological_age,
    s.sex,
    s.cognitive_status,
    s.mmse_score,
    m.scan_id,
    m.scan_date,
    
    -- Raw Volumes (mm³)
    m.total_intracranial_vol,
    m.total_gray_matter_vol,
    m.cortical_white_matter_vol,
    (m.left_hippocampus_vol + m.right_hippocampus_vol) AS total_hippocampus_vol,
    m.ventricles_lateral_vol,
    m.mean_cortical_thickness_mm,
    
    -- Normalized Biomarkers (% of Head Size / eTIV)
    ROUND(((m.left_hippocampus_vol + m.right_hippocampus_vol) / m.total_intracranial_vol) * 100, 4) AS hippocampal_ratio_pct,
    ROUND((m.ventricles_lateral_vol / m.total_intracranial_vol) * 100, 4) AS ventricular_ratio_pct,
    ROUND((m.total_gray_matter_vol / m.total_intracranial_vol) * 100, 4) AS gray_matter_ratio_pct,
    
    -- Hippocampal-to-Ventricle Ratio (HVR Index)
    ROUND((m.left_hippocampus_vol + m.right_hippocampus_vol) / NULLIF(m.ventricles_lateral_vol, 0), 4) AS HVR_index

FROM subjects s
JOIN mri_volumetric_data m ON s.subject_id = m.subject_id;