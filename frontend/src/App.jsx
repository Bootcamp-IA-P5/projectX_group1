import { useMemo, useState } from 'react'
import './App.css'
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from 'chart.js'
import { Doughnut, Bar } from 'react-chartjs-2'

ChartJS.register(ArcElement, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

function App() {
  const [text, setText] = useState('')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const API_URL = import.meta.env.VITE_API_URL || '/api'

  const handleSubmit = async (e) => {
    e.preventDefault()

    if (!text.trim()) {
      setError('Por favor, ingresa un texto para analizar')
      return
    }

    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const response = await fetch(`${API_URL}/predict`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      })

      if (!response.ok) {
        throw new Error(`Error: ${response.status} ${response.statusText}`)
      }

      const data = await response.json()

      // Transform backend response to match frontend expectations
      const transformedData = {
        prediction: data.label || data.prediction,
        confidence: data.score ?? data.confidence ?? 0,
        probabilities: data.probabilities || {
          [data.label || 'label']: data.score ?? 0,
          other: 1 - (data.score ?? 0),
        },
      }

      setResult(transformedData)
    } catch (err) {
      setError(err.message || 'Error al conectar con el servidor')
      console.error('Error:', err)
    } finally {
      setLoading(false)
    }
  }

  const handleClear = () => {
    setText('')
    setResult(null)
    setError(null)
  }

  const getResultColor = (prediction) => {
    if (!prediction) return 'neutral'
    return prediction === 'toxic' || prediction === 'hate_speech' ? 'toxic' : 'safe'
  }

  const probabilityChartData = useMemo(() => {
    if (!result?.probabilities) return null

    const labels = Object.keys(result.probabilities)
    const dataValues = labels.map((key) => {
      const val = Number(result.probabilities[key] ?? 0)
      return Number((val * 100).toFixed(2))
    })

    return {
      labels,
      datasets: [
        {
          label: 'Probabilidad (%)',
          data: dataValues,
          backgroundColor: labels.map((key) =>
            key === 'toxic' || key === 'hate_speech' ? '#ef4444' : '#10b981'
          ),
          borderRadius: 10,
          maxBarThickness: 48,
        },
      ],
    }
  }, [result?.probabilities])

  const confidenceDonutData = useMemo(() => {
    const confidencePct = Math.max(0, Math.min(100, (result?.confidence ?? 0) * 100))

    return {
      labels: ['Confianza', 'Resto'],
      datasets: [
        {
          data: [confidencePct, Math.max(0, 100 - confidencePct)],
          backgroundColor: ['#667eea', '#e5e7eb'],
          borderWidth: 0,
        },
      ],
    }
  }, [result?.confidence])

  return (
    <div className="app">
      <header className="app-header">
        <h1>🛡️ Detector de Lenguaje de Odio</h1>
        <p>Analiza textos para detectar contenido tóxico o lenguaje de odio</p>
      </header>

      <main className="app-main">
        <form onSubmit={handleSubmit} className="analysis-form">
          <div className="form-group">
            <label htmlFor="text-input">Texto a analizar:</label>
            <textarea
              id="text-input"
              value={text}
              onChange={(e) => setText(e.target.value)}
              placeholder="Escribe o pega el texto que deseas analizar..."
              rows={6}
              className="text-input"
              disabled={loading}
            />
            <div className="char-count">
              {text.length} caracteres
            </div>
          </div>

          <div className="button-group">
            <button
              type="submit"
              className="btn btn-primary"
              disabled={loading || !text.trim()}
            >
              {loading ? '🔄 Analizando...' : '🔍 Analizar Texto'}
            </button>
            <button
              type="button"
              onClick={handleClear}
              className="btn btn-secondary"
              disabled={loading}
            >
              🗑️ Limpiar
            </button>
          </div>
        </form>

        {error && (
          <div className="alert alert-error">
            <strong>❌ Error:</strong> {error}
          </div>
        )}

        {result && (
          <div className={`result-card ${getResultColor(result.prediction)}`}>
            <h2>📊 Resultado del Análisis</h2>
            <div className="result-content">
              <div className="result-grid">
                <div className="result-item">
                  <span className="label">Clasificación:</span>
                  <span className="value prediction">
                    {result.prediction === 'toxic' || result.prediction === 'hate_speech'
                      ? '⚠️ Contenido Tóxico'
                      : '✅ Contenido Seguro'}
                  </span>
                </div>

                <div className="result-item">
                  <span className="label">Confianza:</span>
                  <span className="value">{((result.confidence ?? 0) * 100).toFixed(2)}%</span>
                </div>
              </div>

              <div className="charts-grid">
                <div className="chart-card">
                  <div className="chart-header">
                    <span className="chart-title">Nivel de confianza</span>
                    <span className="badge">Doughnut</span>
                  </div>
                  <div className="chart-wrapper">
                    <Doughnut
                      data={confidenceDonutData}
                      options={{
                        cutout: '70%',
                        plugins: {
                          legend: { display: false },
                          tooltip: { callbacks: { label: (ctx) => `${ctx.parsed}%` } },
                        },
                        animation: { duration: 600 },
                        maintainAspectRatio: false,
                      }}
                    />
                    <div className="chart-center-text">
                      {((result.confidence ?? 0) * 100).toFixed(1)}%
                      <span>Confianza</span>
                    </div>
                  </div>
                </div>

                {probabilityChartData && (
                  <div className="chart-card">
                    <div className="chart-header">
                      <span className="chart-title">Distribución de probabilidades</span>
                      <span className="badge">Barras</span>
                    </div>
                    <div className="chart-wrapper bars">
                      <Bar
                        data={probabilityChartData}
                        options={{
                          plugins: {
                            legend: { display: false },
                            tooltip: {
                              callbacks: {
                                label: (ctx) => `${ctx.raw.toFixed(1)}%`,
                              },
                            },
                          },
                          responsive: true,
                          maintainAspectRatio: false,
                          scales: {
                            y: {
                              beginAtZero: true,
                              max: 100,
                              ticks: { callback: (value) => `${value}%` },
                              grid: { color: '#f3f4f6' },
                            },
                            x: {
                              grid: { display: false },
                            },
                          },
                        }}
                      />
                    </div>
                  </div>
                )}
              </div>

              {result.probabilities && (
                <div className="probabilities">
                  <h3>Probabilidades (detalle):</h3>
                  <div className="prob-bars">
                    {Object.entries(result.probabilities).map(([key, value]) => (
                      <div key={key} className="prob-item">
                        <span className="prob-label">{key}:</span>
                        <div className="prob-bar">
                          <div
                            className="prob-fill"
                            style={{ width: `${(value ?? 0) * 100}%` }}
                          />
                        </div>
                        <span className="prob-value">{((value ?? 0) * 100).toFixed(1)}%</span>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          </div>
        )}
      </main>

      <footer className="app-footer">
        <p>
          Project X - Group 1 | Bootcamp IA P5 |
          <a href="https://github.com/Bootcamp-IA-P5/projectX_group1" target="_blank" rel="noopener noreferrer">
            GitHub
          </a>
        </p>
      </footer>
    </div>
  )
}

export default App
