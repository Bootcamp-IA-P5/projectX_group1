"""
Módulo de evaluación y métricas.

Funciones:
- get_metrics: Calcula métricas de clasificación
- compare_train_test: Compara métricas y detecta overfitting
- print_classification_report: Imprime reporte formateado
"""

import pandas as pd
from sklearn.metrics import (
    accuracy_score, 
    precision_score, 
    recall_score, 
    f1_score, 
    classification_report
)
from typing import Dict, Any


def get_metrics(y_true, y_pred) -> Dict[str, float]:
    """
    Calcula métricas de clasificación binaria.
    
    Args:
        y_true: Etiquetas reales
        y_pred: Etiquetas predichas
        
    Returns:
        Dict con accuracy, precision, recall, f1
    """
    return {
        'accuracy': accuracy_score(y_true, y_pred),
        'precision': precision_score(y_true, y_pred, zero_division=0),
        'recall': recall_score(y_true, y_pred, zero_division=0),
        'f1': f1_score(y_true, y_pred, zero_division=0)
    }


def compare_train_test(
    y_train_true, y_train_pred,
    y_test_true, y_test_pred,
    gap_threshold: float = 0.05
) -> Dict[str, Any]:
    """
    Compara métricas de train y test para detectar overfitting.
    
    Args:
        y_train_true, y_train_pred: Datos de entrenamiento
        y_test_true, y_test_pred: Datos de test
        gap_threshold: Umbral de gap F1 para considerar overfitting (default: 0.05)
        
    Returns:
        Dict con métricas, gap y diagnóstico
    """
    metrics_train = get_metrics(y_train_true, y_train_pred)
    metrics_test = get_metrics(y_test_true, y_test_pred)
    
    # Calcular gaps
    gap = {k: metrics_train[k] - metrics_test[k] for k in metrics_train}
    
    # Diagnóstico
    has_overfitting = gap['f1'] > gap_threshold
    
    return {
        'train': metrics_train,
        'test': metrics_test,
        'gap': gap,
        'has_overfitting': has_overfitting,
        'gap_f1': gap['f1']
    }


def display_comparison(comparison: Dict[str, Any]) -> pd.DataFrame:
    """
    Muestra comparación de métricas en formato tabla.
    
    Args:
        comparison: Resultado de compare_train_test()
        
    Returns:
        DataFrame con la comparación
    """
    df = pd.DataFrame([
        comparison['train'],
        comparison['test'],
        comparison['gap']
    ], index=['Train', 'Test', 'Gap (Train-Test)'])
    
    return df


def print_overfitting_analysis(comparison: Dict[str, Any]) -> None:
    """
    Imprime análisis de overfitting.
    
    Args:
        comparison: Resultado de compare_train_test()
    """
    gap_f1 = comparison['gap_f1']
    
    print('\n🎯 Análisis de Overfitting:')
    if comparison['has_overfitting']:
        print(f"⚠️ Gap F1 = {gap_f1:.3f} (>5%) - Posible overfitting")
    else:
        print(f"✅ Gap F1 = {gap_f1:.3f} (<5%) - No hay overfitting significativo")


def print_report(y_true, y_pred, title: str = "Reporte de Clasificación") -> None:
    """
    Imprime reporte de clasificación formateado.
    
    Args:
        y_true: Etiquetas reales
        y_pred: Etiquetas predichas
        title: Título del reporte
    """
    print(f'\n--- {title} ---')
    print(classification_report(y_true, y_pred, zero_division=0))
